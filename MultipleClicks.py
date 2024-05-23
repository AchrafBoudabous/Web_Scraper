from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Set up the Chrome driver service
service = Service(ChromeDriverManager().install())

# Initialize the Chrome webdriver with the service
browser = webdriver.Chrome(service=service)

# Define the URL to visit
url = "https://scorecount.com/click-counter/"  # URL of the website

# Open the URL
browser.get(url)

# Find the element to click
element_to_click = browser.find_element(By.CLASS_NAME, "overlay")  # Selector of the button

# Click the element 10 times
for i in range(10):
    # Click the element
    element_to_click.click()
    
    # Wait for some time before clicking again (optional)
    time.sleep(1)  # Adjust this as needed

# Close the browser
browser.close()
