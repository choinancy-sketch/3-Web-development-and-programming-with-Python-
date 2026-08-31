import sys
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_posts():
    """Fetches post data from the API and prints post details."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)

    posts = response.json()

    print(f"{'ID':<5} | {'Title':<50}")
    print("-" * 58)

    for post in posts[:10]:  # Limit to first 10 for neat output
        post_id = str(post.get("id", "N/A"))
        title = post.get("title", "N/A")
        
        # Truncate long titles for clean table alignment
        if len(title) > 47:
            title = title[:44] + "..."
            
        print(f"{post_id:<5} | {title:<50}")


if __name__ == "__main__":
    fetch_posts()