from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

driver_path = 'C:/Users/leeto/Desktop/chromedriver-win64/chromedriver.exe'
service = Service(driver_path)

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://myanimelist.net/topanime.php")

# Extract all anime links 
title_elements = driver.find_elements(By.XPATH, "//a[@class='hoverinfo_trigger']")
anime_links = [element.get_attribute('href') for element in title_elements]


for animeLink in anime_links:
    driver.get(animeLink)
    try:
        # Extract title and rating from the anime page
        animeTitle = driver.find_element(By.TAG_NAME, "strong").text
        animeRating = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animeRank = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animePopularity = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animeSyponosis = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animeEpisodes = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animeStatus = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animeAired = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animePremiered = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animeBroadcast = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animeProducer = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animeStudio = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        abuneGenre = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animeDemographic = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text
        animeType = driver.find_element(By.XPATH, "//div[contains(@class, 'score-label')]").text

        #click into reviews
        reviewLinkeElement = driver.find_element(By.XPATH, "//a[contains(text(), 'All reviews')]")
        reviewLink = reviewLinkeElement.get_attribute('href')
        driver.get(reviewLink)
        time.sleep(2)

        #get review

        #for review in review we add to csv
        print(f"Anime Title: {animeTitle}, Link: {animeLink}, Rating: {animeRating}")
    except Exception as e:
        print(f"Failed to retrieve data for {animeLink}: {e}")

driver.quit()
