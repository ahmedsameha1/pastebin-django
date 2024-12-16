import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_create_a_pastebin(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Pastebin", self.browser.title)
        self.fail("Finish the test!")

if __name__ == "__main__":
    unittest.main()