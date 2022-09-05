from locators import MainPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Login | Salesforce" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def enter_username(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.Username)
        element.send_keys("a.aleem@curious-impala-gm3l5j.com")

    def enter_password(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.Password)
        element.send_keys("123password123")

# class SearchResultsPage(BasePage):
#   """Search results page action methods come here"""

#  def is_results_found(self):
# Probably should search for this text in the specific page
# element, but as for now it works fine
#     return "No results found." not in self.driver.page_source
