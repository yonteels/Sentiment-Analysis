import requests
import time
import csv

base_url = "https://api.jikan.moe/v4"

def get_all_anime_details_to_csv(file_name):
    current_page = 1 
    has_next_page = True
    
    with open(file_name, mode = 'w', newline='', encoding ='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['id','reaction','date','review','score','tags','is_spoiler', 'is_preliminary', 'episodes_watched', 'user'])


    #set anime to get review for need to do
    while has_next_page:
        url = f"{base_url}/reviews/anime?page={current_page}?preliminary=true?spoiler=true"
        response = requests.get(url)

        if response.status_code == 200:
            data= response.json()
            review_page = data.get('data', [])
            pagination = data.get('pagination', [])

            with open(file_name, mode = 'a', newline = '', encoding ='utf-8') as file:
                writer = csv.writer(file)

                for reviews in review_page:
                    mal_id = reviews.get('mal_id', 'N/A')
                    reaction = reviews.get('reaction', 'N/A')
                    date = reviews.get('date', 'N/A')
                    review = reviews.get('review', 'N/A')
                    score = review.get('score', 'N/A')
                    tags = review.get('tags', 'N/A')
                    is_spoiler =  review.get('is_spoiler', 'N/A')
                    is_preliminary = review.get('is_preliminary', 'N/A')
                    writer.writerow([])




csv_file_name = "animeReview.csv"
get_all_anime_details_to_csv(csv_file_name)
    