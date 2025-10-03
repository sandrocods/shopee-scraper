import json
from lumintu_scraper_client import LumintuScraperClient

client = LumintuScraperClient(api_key="YOUR_API_KEY")

# Step 1: Call actor
actor_resp = client.actor("shopee/scrape").call({
    "url": "https://shopee.co.th/%E0%B8%A3%E0%B9%88%E0%B8%A1%E0%B8%9E%E0%B8%B1%E0%B8%9A%E0%B8%AD%E0%B8%B1%E0%B8%95%E0%B9%82%E0%B8%99%E0%B8%A1%E0%B8%B1%E0%B8%95%E0%B8%B4-3-%E0%B8%95%E0%B8%AD%E0%B8%99-%E0%B8%AA%E0%B8%B5%E0%B8%9E%E0%B8%B2%E0%B8%AA%E0%B9%80%E0%B8%97%E0%B8%A5%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%97%E0%B8%B1%E0%B8%99%E0%B8%AA%E0%B8%A1%E0%B8%B1%E0%B8%A2-%E0%B8%9B%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%A2%E0%B8%B9%E0%B8%A7%E0%B8%B5-i.167009304.29682378470",
    "country": "TH"
})
print(actor_resp)

# Step 2: Wait for result
final = client.result().wait_for_result(actor_resp, interval=2, max_attempts=10)
print(
    json.dumps(final.result, indent=4, ensure_ascii=False)
)

with open("output/result_{}_shopee_th.json".format(actor_resp.get('request_id')), "w", encoding="utf-8") as f:
    json.dump(final.result, f, indent=4, ensure_ascii=False)
