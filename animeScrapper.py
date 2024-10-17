from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver
def init_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service(executable_path=r"C:\Users\leeto\Desktop\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Fetch the page using Selenium
def fetch_page(url, driver):
    driver.get(url)
    time.sleep(3) 
    page_source = driver.page_source  
    return page_source


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def scraper():
    url = "https://myanimelist.net/topanime.php" 
    # Initialize WebDriver
    driver = init_driver()

    try:
        html = fetch_page(url, driver)
        soup = parse_html(html)
        title = soup.find('title').text
        print(f"Page Title: {title}")
    finally:
        driver.quit()

if __name__ == "__main__":
    scraper()
