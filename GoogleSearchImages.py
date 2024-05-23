from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleImageSearch:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Initialize Chrome WebDriver

    def fetch_links_by_search(self, search_query):
        # Navigate to Google Images
        self.driver.get('https://www.google.com/imghp?hl=en')
        
        

        # Find the search bar and input the search query
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(search_query)
        search_box.submit()

        # Wait for search results to load (add any additional wait if required)
        self.driver.implicitly_wait(5)

        # Find all <a> elements with href containing "/imgres" (image result links)
        links = self.driver.find_elements(By.XPATH, "//a[contains(@href, '/imgres')]")

        # Extract and print the links
        for link in links:
            href_value = link.get_attribute('href')
            print(href_value)

        # Close the WebDriver
        self.driver.quit()

# Example usage: 
if __name__ == "__main__":
    search_query = "techsd" 
    google_image_search = GoogleImageSearch()
    google_image_search.fetch_links_by_search(search_query)