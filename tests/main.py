import unittest
from selenium import webdriver
import page

PATH = "/home/vinicius/python-projects/web-scraper/chromedriver"
URL = "http://www.python.org"


class PythonOrgSearch(unittest.TestCase):
    
    # Start up. Called for every single test case
    def setUp(self):
        print("Setup")
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(URL)
    
    #Start with 'test' -> automaticly run
    # def test_example(self):
    #     print("Setup")
    #     assert True # assert the right part is true

    # def test_title(self):
    #     main_page = page.MainPage(self.driver)
    #     assert main_page.is_title_matches()

    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches() 
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    # Cleaning up
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()