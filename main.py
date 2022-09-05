import unittest
from selenium import webdriver
import page
import warnings

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://Salesforce.com")
        warnings.simplefilter('ignore', ResourceWarning)

    def test_search_in_python_org2(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        # Load the main page. In this case the home page of Python.org.
        main_page2 = page.MainPage(self.driver)
        # Checks if the word "Python" is in title
        self.assertTrue(main_page2.is_title_matches(), "Salesforce.com title doesn't match.")
        # Sets the text of search textbox to "pycon"
     #   main_page2.search_text_element = "pycon"
        main_page2.enter_username()
        main_page2.enter_password()
        main_page2.click_go_button()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
