import os
import unittest
from selenium import webdriver
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox(
            executable_path = BASE_DIR + "/geckodriver"
        )

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://0.0.0.0:8000")
        self.assertIn('Myblog', self.browser.title)

        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main()