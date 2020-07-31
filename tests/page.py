from locator import MainPageLocator
from element import BasePageElement


class SearchTextElement(BasePageElement):
    locator = "q"


class GoButtonElement(BasePageElement):
    locator = "go"

    
class BasePage(object):
    # Constructor
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        # * Operator -> separates one object into two entities or more (splat or unpack)
        element = self.driver.find_element(*MainPageLocator.GO_BUTTON)
        element.click()


class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source