from database.db import get_user_preferences, connect_db
from fetcher.twitter_fetcher import fetch_tweets
from summarizer.summarizer import summarize

def get_user_id(username):
    """Fetch the user ID from the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def main():
    username = 'user1'  # Manufactured user for now
    user_id = get_user_id(username)

    if not user_id:
        print(f"User '{username}' not found.")
        return

    preferences = get_user_preferences(username)
    query = " OR ".join(preferences)

    print(f"Fetching tweets for '{username}' with query: {query}")

    api_key = "YOUR_TWITTER_API_KEY"
    raw_data = fetch_tweets(api_key, query, user_id)

    if raw_data:
        posts = raw_data['data']
        summary = summarize(posts)
        print(f"\nSummary: {summary}")
    else:
        print("No tweets found.")

if __name__ == "__main__":
    main()
