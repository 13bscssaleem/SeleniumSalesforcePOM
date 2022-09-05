from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'Login')
    Username = (By.ID, 'username')
    Password = (By.ID, 'password')
class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass
