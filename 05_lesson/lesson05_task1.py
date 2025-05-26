from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    driver = webdriver.Chrome()
    try:
        driver.get("http://uitestingplayground.com/classattr")
        blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")  # Ищем кнопку по CSS классу
        blue_button.click()

        time.sleep(2)
    finally:
        driver.quit()
if __name__ == "__main__":
    main()