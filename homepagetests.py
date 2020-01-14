import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from parameterized import parameterized, parameterized_class


class HomePageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://demo.magentocommerce.com/")

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'fa-search'))

    @parameterized.expand([
        ("demo_button", "Get A Free Demo"),
        ("products_navigation", "Products"),
        ("solutions_navigation", "Solutions"),
        ("partners_navigation", "Partners"),
        # ("community_navigation", "Community"),
        ("resources_navigation", "Resources"),
        # ("blog_navigation", "Blog"),
    ])

    def test_page_links(self, name, link_text):
        self.assertTrue(self.is_element_present(By.LINK_TEXT, link_text.upper()))

    def is_element_present(self, how, what):
        """
        Utility method to check if an object is present on the page
        :param how: By locator type
        :param what: locator value
        """
        try:
            element = self.driver.find_element(how, what)
        except NoSuchElementException as e:
            return False
        return True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
