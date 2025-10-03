import json
from lumintu_scraper_client import LumintuScraperClient

client = LumintuScraperClient(api_key="YOUR_API_KEY")

# Step 1: Call actor
actor_resp = client.actor("shopee/scrape").call({
    "url": "https://shopee.co.id/Aerostreet-37-44-Hoops-Low-2.0-Gum-Hitam-Hitam-Sepatu-Sneakers-Casual-i.177400943.28618475570?xptdk=1c7a0e35-2e53-4740-a4ef-9de70312cb5d",
    "country": "ID"
})
print(actor_resp)

# Step 2: Wait for result
final = client.result().wait_for_result(actor_resp, interval=2, max_attempts=10)
print(
    json.dumps(final.result, indent=4, ensure_ascii=False)
)

with open("output/result_{}_shopee_id.json".format(actor_resp.get('request_id')), "w", encoding="utf-8") as f:
    json.dump(final.result, f, indent=4, ensure_ascii=False)
