from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():

    driver = webdriver.Firefox()  

    try:

        driver.get("http://the-internet.herokuapp.com/inputs")


        input_field = driver.find_element(By.TAG_NAME, "input")


        input_field.send_keys("Sky")


        input_field.clear()


        input_field.send_keys("Pro")


        time.sleep(2)

    finally:

        driver.quit()

if __name__ == "__main__":
    main()