from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def action_chains(driver):
    # Deal with loading pages (10 seconds)
    driver.implicitly_wait(5)
    cookie = driver.find_element_by_id("bigCookie")
    cookie_count = driver.find_element_by_id("cookies")
    # List compreesion, in reverse
    items = [driver.find_element_by_id("product" + str(i)) for i in range(1, -1, -1)]
    
    actions = ActionChains(driver)
    actions.click(cookie)

    for i in range(5000):
        actions.perform()
        count = int(cookie_count.text.split(" ")[0])
        for item in items:
            value = int(item.text)
            if value <= count:
                # Diferent items. We need to redefine the action chain
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()

                


def main():
    PATH = "/home/vinicius/python-projects/web-scraper/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    action_chains(driver)
main()

