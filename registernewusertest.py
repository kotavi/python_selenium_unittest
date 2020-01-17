import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

from selenium.webdriver.support.select import Select


class RegisterNewUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://magento.com/")

    def test_create_new_user(self):
        account_link = self.driver.find_element(By.CLASS_NAME, "fa-user")
        account_link.click()
        self.assertEqual(self.driver.title, "Customer Login")

        register_button = self.driver.find_element(By.XPATH, "//button[@type='button']")
        register_button.click()
        self.assertEqual(self.driver.title, "Create New Customer Account")
        first_name = self.driver.find_element_by_xpath("//input[@id='firstname']")
        first_name.send_keys("Sarah")
        last_name = self.driver.find_element_by_xpath("//input[@id='lastname']")
        last_name.send_keys('Connor')
        email_address = self.driver.find_element_by_xpath("//input[@id='email_address']")
        email_address.send_keys('Sarah.Connor@gmail.com')

        select_element = Select(self.driver.find_element_by_id("country"))
        for option in select_element.options:
            print(option.text)

        select_element.select_by_visible_text("United States")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

