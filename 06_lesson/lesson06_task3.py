from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )

    images = driver.find_elements(By.TAG_NAME, "img")

    if len(images) < 3:
        print("На странице меньше трех изображений!")
    else:
        third_image = images[2]
        src_value = third_image.get_attribute("src")

        print(src_value)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()