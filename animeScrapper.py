import requests
from bs4 import BeautifulSoup
import csv
import sys
import io

# Set user-agent header
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
}

# URL of the review page
URL = "https://myanimelist.net/anime/52991/Sousou_no_Frieren/reviews?sort=suggested&filter_check=&filter_hide=&preliminary=on&spoiler=off&p=1"

# Get server response
request = requests.get(url=URL, headers=headers)

if request.status_code == 200:
    soup = BeautifulSoup(request.content, 'html5lib')

    # Get titles
    JpTitle = soup.find('strong').text
    EngTitle = soup.find('p', class_='title-english title-inherit').text

    # Get image
    animeImage = soup.find('img', itemprop='image')
    image_url = animeImage.get('data-src') or animeImage.get('src')

    # Get rating
    Rating = soup.find('span', itemprop='ratingValue', class_='score-label').text

    # Get User
    Reviewers = soup.find_all('a', {'data-ga-click-type': 'review-anime-reviewer'})

    # Get Review
    Reviews = soup.find_all('div', class_='text')

    # Get Reviewer Rating
    rating_div = soup.find_all('div', class_='rating mt20 mb20 js-hidden')

    reviewers_rating = []

    for rRating in rating_div:
        ReviewersRatingNumber = rRating.find('span', class_='num').text
        reviewers_rating.append(ReviewersRatingNumber)

    # Set encoding 
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Prepare dataset
    data = []

    # Clean text
    def clean_text(text):
        text = text.replace("...", "") 
        text = text.replace("â€“", "-").replace("â€œ", '"').replace("â€�", '"').replace("â€™", "'")
        return text.strip()

    # Add data
    for i in range(len(Reviewers)):
        clean_review = clean_text(Reviews[i].text)

        data.append((JpTitle, EngTitle, Rating, Reviewers[i].text.strip(), clean_review, reviewers_rating[i]))

    # Write to CSV 
    with open('review.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Japanese Title', 'English Title', 'Rating', 'Reviewer', 'Review', 'Reviewers Rating'])  # Column headers
        writer.writerows(data)

print("Scraping complete. Data saved to 'review.csv'.")
