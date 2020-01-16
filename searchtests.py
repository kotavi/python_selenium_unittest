import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class SearchTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://demo.magentocommerce.com/")

        search_button = cls.driver.find_element_by_class_name('fa-search')
        search_button.click()

    def test_seach_text_field_max_length(self):
        search_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, "search-query")))
        self.assertEqual('255', search_field.get_attribute('maxlength'))

    def test_search_by_event(self):
        search_field = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "search-query")))
        search_field.send_keys("eTail West type:event")
        search_field.submit()
        search_result = self.driver.find_element_by_class_name("search-results.node-results")
        list_of_results = search_result.find_elements_by_tag_name('li')
        self.assertEqual(2, len(list_of_results))

    def test_search_by_blog_post(self):
        search_field = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "search-query")))
        search_field.send_keys("Cabinets type:blog_post")
        search_field.submit()
        search_results = self.driver.find_elements_by_xpath("//h3[@class='result-title']/a")
        self.assertEqual(2, len(search_results))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)