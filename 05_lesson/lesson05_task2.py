from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():

    driver = webdriver.Chrome()

    try:

        driver.get("http://uitestingplayground.com/dynamicid")


        blue_button = driver.find_element(By.LINK_TEXT, "Button with Dynamic ID")
        blue_button.click()


        time.sleep(2)

    finally:

        driver.quit()

if __name__ == "__main__":
    main()