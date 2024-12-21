import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_create_a_pastebin(self):
        self.browser.get("http://localhost:8000")
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
        self.assertEqual(inputbox.text, "")
        self.assertEqual(header_url.text,
                         "http://localhost:8000/4aa886a88005a7df")


if __name__ == "__main__":
    unittest.main()
