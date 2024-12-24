import hashlib
from django.test import TestCase
from django.http import HttpRequest
from pb.models import Pastebin
from pb.views import home_page


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_that_a_POST_request_shows_a_url(self):
        response = self.client.post("/", data={"pastebin_text": "hi"})
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response,
                            "http://localhost:8000/49f68a5c8493ec2c0bf489821c21fc3b")


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
