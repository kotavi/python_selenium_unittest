import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://marketplace.magento.com/")

    def test_search_e_book(self):
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.send_keys("e-book")
        search_field.send_keys(Keys.ENTER)

        number_of_results = self.driver.find_element_by_css_selector("div.ais-body.ais-stats--body")
        self.assertEqual('11 Results', number_of_results.text)

        found_hits = self.driver.find_elements_by_css_selector('div.ais-hits div.result-content')
        self.assertEqual(11, len(found_hits))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)