from lumintu_scraper_client import LumintuScraperClient, AuthenticationError

client = LumintuScraperClient(api_key="YOUR_API_KEY")

try:
    user_info = client.user().info(
        as_dict=True
    )
    print(user_info)
except AuthenticationError as e:
    print("Authentication failed:", e)
