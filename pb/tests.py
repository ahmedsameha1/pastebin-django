import hashlib
from django.test import TestCase
from django.http import HttpRequest
from pb.models import Pastebin
from pb.views import BASE_URL, home_page


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_that_a_POST_request_creates_then_saves_a_pastebin(self):
        hi_id = hashlib.md5("hi"
                         .encode("utf-8")).hexdigest()
        response = self.client.post("/", data={"pastebin_text": "hi"})
        self.assertEqual(Pastebin.objects.count(), 1)
        apastebin = Pastebin.objects.first()
        self.assertEqual(apastebin.text, "hi")
        self.assertEqual(apastebin.id, hi_id)

    def test_redirects_after_POST(self):
        hi_id = hashlib.md5("hi"
                         .encode("utf-8")).hexdigest()
        response = self.client.post("/", data={"pastebin_text": "hi"})
        self.assertRedirects(response, BASE_URL + hi_id)

class PastebinPageTest(TestCase):
    def test_pastebin_page_returns_correct_html(self):
        response = self.client.get("/78a")
        self.assertContains(response, "Invalid")
        self.assertTemplateUsed(response, "pastebin_invalid.html")
        Pastebin.objects.create(id="78a", text="hi")
        response = self.client.get("/78a")
        self.assertContains(response, "Delete")
        self.assertTemplateUsed(response, "pastebin.html")


    def test_pastebin_page_contains_the_correct_pastebin_data(self):
        Pastebin.objects.create(id="78a", text="hi")
        response = self.client.get("/78a")
        self.assertContains(response, "78a")
        self.assertContains(response, "hi")
    
    def test_delete_a_pastebin(self):
        Pastebin.objects.create(id="78a", text="hi")
        response = self.client.delete("/78a")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.content, b"")
        deletedPastebin = Pastebin.objects.filter(id="78a").first()
        self.assertIsNone(deletedPastebin)

    def test_delete_a_nonexistant_pastebin(self):
        response = self.client.delete("/78a")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content, b"")

class PastebinModelTest(TestCase):
    def test_saving_and_retrieving_pastebins(self):
        first_pastebin = Pastebin()
        first_pastebin.text = "one"
        first_pastebin.id = hashlib.md5("one"
                                        .encode("utf-8")).hexdigest()
        first_pastebin.save()

        second_pastebin = Pastebin()
        second_pastebin.text = "two"
        second_pastebin.id = hashlib.md5("two"
                                         .encode("utf-8")).hexdigest()
        second_pastebin.save()

        saved_items = Pastebin.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_pastebin = saved_items[0]
        second_saved_pastebin = saved_items[1]
        self.assertEqual(first_saved_pastebin.text, "one")
        self.assertEqual(first_saved_pastebin.id,
                         hashlib.md5("one"
                                     .encode("utf-8")).hexdigest())
        self.assertEqual(second_saved_pastebin.text, "two")
        self.assertEqual(second_saved_pastebin.id,
                         hashlib.md5("two"
                                     .encode("utf-8")).hexdigest())
