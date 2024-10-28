import requests
from database.db import save_fetched_post

def fetch_tweets(api_key, query, user_id, limit=5):
    """Fetch tweets matching the query and save them to the database."""
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results={limit}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data.get('data', []):
            save_fetched_post(user_id, post['id'], post['text'], post['created_at'])
        return data
    else:
        print(f"Error fetching tweets: {response.status_code}")
        return None
