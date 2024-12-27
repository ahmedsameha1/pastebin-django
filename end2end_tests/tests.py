from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_create_a_pastebin_then_visiting_it(self):
        self.browser.get(self.live_server_url)
        self.assertIn("Pastebin", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Pastebin", header_text)

        inputbox = self.browser.find_element(By.ID, "id_new_pastebin")
        self.assertEqual(inputbox.get_attribute("placeholder"),
                         "Enter a new pastebin")
        self.assertEqual(inputbox.text, "")
        inputbox.send_keys("This is a test pastebin")
        submit_button = self.browser.find_element(By.TAG_NAME, "button")
        self.assertEqual(submit_button.get_attribute("type"),
                         "submit")
        self.assertEqual(submit_button.text, "Submit")
        header_url = self.browser.find_element(By.ID, "id_url")
        self.assertEqual(header_url.text, "")
        submit_button.click()
        time.sleep(1)
        current_url = self.browser.current_url
        self.assertEqual(current_url,
                         self.live_server_url+"/6bde0a9108435670b29d23fd689a0e90")
        url_header = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(url_header, self.live_server_url +
                         "/6bde0a9108435670b29d23fd689a0e90")
        pastebin_text = self.browser.find_element(By.TAG_NAME, "p").text
        self.assertEqual(pastebin_text, "This is a test pastebin")
