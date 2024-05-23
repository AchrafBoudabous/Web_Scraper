# Web Scraper Scripts

This repository contains several Python scripts for web scraping using Selenium. Below is a brief description of each script and its functionality.

## Requirements
* Python 3.x
* Selenium
* ChromeDriver
* WebDriver Manager

You can install the required packages using the following command: pip install selenium webdriver_manager

## Scripts
### GoogleSearchImages.py
This script automates the process of searching for images on Google and retrieving the image result links.

* Dependencies: selenium
* Key Features:
1) Initializes the Chrome WebDriver.
2) Searches for a query on Google Images.
3) Extracts and prints image result links.

### GoogleSearchLinks.py
This script performs a Google search for a given query and retrieves the titles and URLs of the first five search results.

* Dependencies: selenium, webdriver_manager
* Key Features:
1) Initializes the Chrome WebDriver using WebDriver Manager.
2) Performs a Google search for "Laptops".
3) Extracts and prints the titles and URLs of the top five search results.

### MultipleClicks.py
This script automates the process of clicking a specific element on a webpage multiple times.

* Dependencies: selenium, webdriver_manager
* Key Features:
1) Initializes the Chrome WebDriver using WebDriver Manager.
2) Navigates to a specified URL.
3) Clicks a specific element (button) on the page ten times with a delay between each click.

### Screenshot.py
This script takes a screenshot of a specified webpage.

* Dependencies: selenium
* Key Features:
1) Initializes the Chrome WebDriver.
2) Navigates to "https://google.com".
3) Saves a screenshot of the page as "google.png".

### SimpleWebScraping.py
This script demonstrates a simple web scraping task of navigating a website and interacting with elements.

* Dependencies: selenium, webdriver_manager
* Key Features:
1) Initializes the Chrome WebDriver using WebDriver Manager.
2) Navigates to "https://www.w3schools.com/".
3) Accepts cookies and clicks on the "Learn HTML" link.


## Notes
* Ensure that you have ChromeDriver installed and that it is compatible with your version of Google Chrome.
* These scripts are for educational purposes. Be mindful of the website's terms of service and use appropriate delays to avoid being blocked while scraping.
* Modify the scripts as needed to fit your specific use case.
* Feel free to contribute by opening issues or submitting pull requests for improvements or additional features. Happy scraping!