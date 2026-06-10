from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by   import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, time

options = Options()
options.binary_location = "/opt/google/chrome/chrome"
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_experimental_option("detach", True)

service = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://ozh.github.io/cookieclicker/")

wait = WebDriverWait(driver, 10)

lang_select = wait.until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
lang_select.click()

sleep(2)

cookie = driver.find_element(by=By.ID, value="bigCookie")

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5

while True:
    cookie.click()

    if time() > timeout:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            if best_item:
                best_item.click()

        except (ValueError):
            print("Couldn't find cookie count or items")

        timeout = time() + wait_time


