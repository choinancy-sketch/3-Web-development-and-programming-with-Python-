import requests

API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users():
    """Fetches user records from the public open API."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error fetching data from API: {error}")
        return []


def display_users(users):
    """Displays user records in a clean, formatted terminal layout."""
    if not users:
        print("No user records to display.")
        return

    print(f"{'Name':<25} | {'Username':<15} | {'Email':<30}")
    print("-" * 75)

    for user in users:
        name = user.get("name", "N/A")
        username = user.get("username", "N/A")
        email = user.get("email", "N/A")
        print(f"{name:<25} | {username:<15} | {email:<30}")


def main():
    """Main execution function."""
    print("Fetching fake user profiles from JSONPlaceholder...")
    users = fetch_users()
    display_users(users)


if __name__ == "__main__":
    main()