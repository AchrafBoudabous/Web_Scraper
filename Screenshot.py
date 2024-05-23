from selenium import webdriver

driver = webdriver.Chrome()

url = "https://google.com"
driver.get(url)

driver.save_screenshot("google.png")

driver.quit()