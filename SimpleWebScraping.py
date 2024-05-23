from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver service
service = Service(ChromeDriverManager().install())

# Initialize the Chrome webdriver with the service
browser = webdriver.Chrome(service=service)

# Open the URL
browser.get('https://www.w3schools.com/')

# Wait for the "Accept all & visit the site" element to be clickable
accept_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'accept-choices')))

# Click the "Accept all & visit the site" button
accept_button.click()

# Wait for the page to load
time.sleep(5)

# Find and click the "Learn HTML" button
button = browser.find_element(By.LINK_TEXT, 'Learn HTML')
button.click()

# Wait for some time
time.sleep(3)

# Close the browser
browser.close()
