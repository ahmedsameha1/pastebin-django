from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser1 = webdriver.Chrome()
        self.browser2 = webdriver.Firefox()

    def tearDown(self):
        self.browser1.quit()
        self.browser2.quit()

    def test_can_create_a_pastebin_then_visiting_it_then_delete_it(self):
        self.browser1.get(self.live_server_url)
        self.assertIn("Pastebin", self.browser1.title)
        header_text = self.browser1.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Pastebin", header_text)

        inputbox = self.browser1.find_element(By.ID, "id_new_pastebin")
        self.assertEqual(inputbox.get_attribute("placeholder"),
                         "Enter a new pastebin")
        self.assertEqual(inputbox.text, "")
        inputbox.send_keys("This is a test pastebin")
        submit_button = self.browser1.find_element(By.TAG_NAME, "button")
        self.assertEqual(submit_button.get_attribute("type"),
                         "submit")
        self.assertEqual(submit_button.text, "Submit")
        header_url = self.browser1.find_element(By.ID, "id_url")
        self.assertEqual(header_url.text, "")
        submit_button.click()
        time.sleep(1)
        current_url = self.browser1.current_url
        self.assertEqual(current_url,
                         self.live_server_url+"/6bde0a9108435670b29d23fd689a0e90")
        self.browser2.get(self.live_server_url+"/6bde0a9108435670b29d23fd689a0e90")
        url_header = self.browser1.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(url_header, "6bde0a9108435670b29d23fd689a0e90")
        pastebin_text = self.browser1.find_element(By.TAG_NAME, "p").text
        self.assertEqual(pastebin_text, "This is a test pastebin")
        delete_button = self.browser1.find_element(By.ID, "deleteButton")
        self.assertEqual(delete_button.get_attribute("type"),
                         "submit")
        self.assertEqual(delete_button.text, "Delete")
        delete_button.click()
        time.sleep(1)
        confirmDialog = self.browser1.find_element(By.ID, "confirmDialog")
        message = confirmDialog.find_element(By.TAG_NAME, "p")
        self.assertEqual(message.text, "Delete?")
        confirmBtn = confirmDialog.find_element(By.ID, "confirmButton")
        confirmBtn.click()
        self.assertFalse(confirmDialog.is_displayed())
        time.sleep(1)
        infoDialog = self.browser1.find_element(By.ID, "infoDialog")
        info = infoDialog.find_element(By.TAG_NAME, "p")
        self.assertEqual(info.text, "Deleted")
        okBtn = infoDialog.find_element(By.ID, "okButton")
        okBtn.click()
        current_url = self.browser1.current_url
        self.assertEqual(current_url, self.live_server_url+"/?")
        delete_button2 = self.browser2.find_element(By.ID, "deleteButton")
        delete_button2.click()
        time.sleep(1)
        confirmDialog = self.browser2.find_element(By.ID, "confirmDialog")
        message = confirmDialog.find_element(By.TAG_NAME, "p")
        self.assertEqual(message.text, "Delete?")
        confirmBtn = confirmDialog.find_element(By.ID, "confirmButton")
        confirmBtn.click()
        alreadyDeletedDialog = self.browser2.find_element(By.ID, "alreadyDeletedDialog")
        message = alreadyDeletedDialog.find_element(By.TAG_NAME, "p")
        self.assertEqual(message.text, "Already deleted!")
        okBtn = alreadyDeletedDialog.find_element(By.ID, "okButton")
        okBtn.click()
        current_url = self.browser2.current_url
        self.assertEqual(current_url, self.live_server_url+"/?")
        self.browser1.get(self.live_server_url +
                         "/6bde0a9108435670b29d23fd689a0e90")
        time.sleep(1)
        infoDialog = self.browser1.find_element(By.ID, "infoDialog")
        info = infoDialog.find_element(By.TAG_NAME, "p")
        self.assertEqual(info.text, "Invalid id")
        okBtn = infoDialog.find_element(By.ID, "okButton")
        okBtn.click()
        time.sleep(1)
        current_url = self.browser1.current_url
        self.assertEqual(current_url, self.live_server_url+"/?")
