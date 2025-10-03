import json
from lumintu_scraper_client import LumintuScraperClient

client = LumintuScraperClient(api_key="YOUR_API_KEY")

# Step 1: Call actor
actor_resp = client.actor("shopee/scrape").call({
    "url": "https://shopee.vn/Gi%C3%A0y-Th%E1%BB%83-Thao-N%E1%BB%AF-Sneaker-(Fullbox)-Ph%E1%BB%91i-Ho%E1%BA%A1-Ti%E1%BA%BFt-N%C6%A1-%C4%90%E1%BA%BF-Cao-3cm-M%C3%A3-T-525-i.868047560.40113598149",
    "country": "VN"
})
print(actor_resp)

# Step 2: Wait for result
final = client.result().wait_for_result(actor_resp, interval=2, max_attempts=10)
print(
    json.dumps(final.result, indent=4, ensure_ascii=False)
)

with open("output/result_{}_shopee_vn.json".format(actor_resp.get('request_id')), "w", encoding="utf-8") as f:
    json.dump(final.result, f, indent=4, ensure_ascii=False)
