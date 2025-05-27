from selenium import webdriver
from selenium.webdriver.common.by import By


def main():

    driver = webdriver.Chrome()

    try:

        driver.get("http://uitestingplayground.com/dynamicid")

        blue_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
        blue_button.click()

    finally:

        driver.quit()

if __name__ == "__main__":
    main()
