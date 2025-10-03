import json
from lumintu_scraper_client import LumintuScraperClient

client = LumintuScraperClient(api_key="YOUR_API_KEY")

# Step 1: Call actor
actor_resp = client.actor("shopee/scrape").call({
    "url": "https://shopee.tw/%E5%A4%8F%E5%AD%A3%E5%A4%9A%E5%B7%B4%E8%83%BA%E5%A5%97%E8%A3%9D%E5%A5%B32025%E6%96%B0%E6%AC%BE%E6%B5%B7%E9%82%8A%E9%98%B2%E6%9B%AC%E8%A5%AF%E8%A1%AB%E6%90%AD%E9%85%8D%E6%89%8E%E6%9F%93%E5%90%8A%E5%B8%B6%E9%80%A3%E8%A1%A3%E8%A3%99%E5%85%A9%E4%BB%B6%E5%A5%97-i.426774685.41804272685?xptdk=19c6ec2e-7e3a-4784-adbb-1b123e37596e",
    "country": "TW"
})
print(actor_resp)

# Step 2: Wait for result
final = client.result().wait_for_result(actor_resp, interval=2, max_attempts=10)
print(
    json.dumps(final.result, indent=4, ensure_ascii=False)
)

with open("output/result_{}_shopee_tw.json".format(actor_resp.get('request_id')), "w", encoding="utf-8") as f:
    json.dump(final.result, f, indent=4, ensure_ascii=False)
