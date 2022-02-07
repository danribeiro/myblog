from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

import os
import time
import unittest


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
s =  Service("/Applications/Firefox.app/Contents/MacOS/firefox")


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox(
            service = s
        )

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://127.0.0.1:8000")
        self.assertIn('Myblog', self.browser.title)

        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main()