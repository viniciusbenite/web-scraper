from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def search(driver):
    search = driver.find_element_by_name("s")
    search.send_keys("test")
    search.send_keys(Keys.RETURN)

    # prevent exceptions (w8 for 10 seconds)
    try:
        main_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "main"))
        )
        articles = main_element.find_elements_by_tag_name("article")
        for article in articles:
            header = article.find_element_by_class_name("entry-summary")
            print(header.text)
    finally:
        print("Done!")
        driver.quit()

def clicking_buttons(driver):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Python Programming"))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
        )
        element.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sow-button-19310003"))
        )
        element.click()
        time.sleep(10)
        driver.back() # Back button on browser
        driver.back()
        driver.back()
        driver.forward() # Foward button on browser
        time.sleep(10)
    except:
        print("Done!")
        driver.quit()

def main():
    PATH = "/home/vinicius/python-projects/web-scraper/chromedriver"
    driver = webdriver.Chrome(PATH)
    # Seting up Selenium driver
    driver.get("https://techwithtim.net") # Execute
    print(driver.title) # Check title
    
    # search(driver)
    clicking_buttons(driver)

main()