import requests
import time
import csv

base_url = "https://api.jikan.moe/v4"

def get_all_anime_details_to_csv(file_name):
    current_page = 1
    has_next_page = True

    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['mal_id','Title', 'Picture', 'Score', 'Rank', 'Popularity', 'Synopsis', 'Episodes', 'Status', 'Aired', 'Genres'])
    
    while has_next_page:
        url = f"{base_url}/anime?page={current_page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            anime_page = data.get('data', [])
            pagination = data.get('pagination', {})

            with open(file_name, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                for anime in anime_page:
                    mal_id = anime.get('mal_id', 'N/A')
                    title = anime.get('title', 'N/A')
                    # Updated picture URL extraction
                    picture = anime.get('images', {}).get('jpg', {}).get('image_url', 'N/A')
                    score = anime.get('score', 'N/A')
                    rank = anime.get('rank', 'N/A')
                    popularity = anime.get('popularity', 'N/A')
                    synopsis = anime.get('synopsis', 'N/A')
                    episodes = anime.get('episodes', 'N/A')
                    status = anime.get('status', 'N/A')
                    aired = anime.get('aired', {}).get('string', 'N/A')
                    genres = anime.get('genres', [])
                    genre_names = ', '.join([genre.get('name', 'N/A') for genre in genres])
                    writer.writerow([mal_id,title, picture, score, rank, popularity, synopsis, episodes, status, aired, genre_names])

            has_next_page = pagination.get('has_next_page', False)
            print(f"Picture URL={picture}")
            current_page += 1
            time.sleep(1)
        else:
            has_next_page = False

csv_file_name = "animeData.csv"
get_all_anime_details_to_csv(csv_file_name)
