from selenium import webdriver
import unittest


class BasicTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_basic_site(self):
        self.browser.get('http://localhost:8000')
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Hello World!', body_text)

if __name__ == '__main__':
    unittest.main()
