from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)

browser.get("https://www.google.com/")
time.sleep(5)

try:
    accept_button = browser.find_element(By.CSS_SELECTOR, ".QS5gu.sy4vM")
    accept_button.click()
except:
    print("No pop-up found")

search_box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "q")))

search_box.send_keys("Laptops")
search_box.submit()

browser.implicitly_wait(5)

search_results = browser.find_elements(By.CSS_SELECTOR, "div.tF2Cxc")
for i, result in enumerate(search_results[:5], start=1):
    title = result.find_element(By.CSS_SELECTOR, "h3").text
    url = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
    print(f"{i}. {title} - {url}")

browser.close()