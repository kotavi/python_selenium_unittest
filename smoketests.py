from homepagetests import HomePageTests
from searchtests import SearchTests
import os
import HtmlTestRunner
import unittest

result_dir = os.getcwd()
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTests)

# create test suite
smoke_tests = unittest.TestSuite([search_tests, home_page_tests])

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))