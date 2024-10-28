from collections import Counter

def summarize(posts, top_n=3):
    """Generate a summary by extracting the most common words."""
    text = " ".join([post['text'] for post in posts])
    words = text.split()
    most_common = Counter(words).most_common(top_n)
    return " | ".join([word for word, _ in most_common])
