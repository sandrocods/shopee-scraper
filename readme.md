# Shopee Scraper Product Details

This project is the official Python client for the **Lumintu Scraper API** for Shopee  
The purpose is to make integrating Lumintu Scraper into your Python app as simple as one line of code.

With this SDK, you can call scraping actors, fetch results, and monitor your account usage without worrying about retries, errors, or raw HTTP requests.

The end goal of this tool is to make **Shopee scraping effortless**.  
Currently it supports:

- Scraping product details from Shopee (ID, TH, VN, TW, SG, MY)
- Managing credits and user info
- Handling rate limits, retries, and API errors automatically

Skip the hassle of building and maintaining your own scraper.  
Focus on building your app, not the scraper. we handle the :

- IP Banned
- Captcha Solver
- Rate limit
- Slow Selenium web driver
- Strict header algorithm like x-sap-ri, x-sap-sec, af-ac-cli-id, af-ac-enc-sz-token, AC_CERT_D

Currently supported Shopee marketplaces:

- Indonesia (ID)
- Thailand (TH)
- Vietnam (VN)
- Taiwan (TW)
- Singapore (SG)
- Malaysia (MY)

```HTTP
https://mall.shopee.SITE/api/v4/pdp/get
```

All its from one base API with special algorithm to generate the required headers and parameters.

## Example Response Fresh Data

Access real-time product data from Shopee, one of Asia’s largest e-commerce platforms, through our fast and reliable API. Collect detailed product information, including pricing, variations, seller details, and other
essential data with low latency and high accuracy.

Our Shopee Scraper is designed to handle complex product structures, including multiple variations, shipping information, and promotional details across various regions and languages. Receive clean, structured JSON data
that can be seamlessly integrated into pricing systems, market research platforms, competitive analysis tools, and other applications.

#### Updated at : 2026-09-28

- [Indonesia (ID)](response-data/response_shopee_scrape_product_details_v2_id.json)
- [Thailand (TH)](response-data/response_shopee_scrape_product_details_v2_th.json)
- [Vietnam (VN)]()
- [Taiwan (TW)](response-data/response_shopee_scrape_product_details_v2_tw.json)
- [Singapore (SG)](response-data/response_shopee_scrape_product_details_v2_sg.json)
- [Malaysia (MY)](response-data/response_shopee_scrape_product_details_v2_my.json)

## Key Features

- **Easy to Use**: Simple and intuitive API for quick integration.
- **Robust**: Handles retries, rate limits, and errors automatically.
- **Comprehensive**: Access detailed product information including pricing, stock, ratings, and more.
- **Multi-Marketplace Support**: Works with multiple Shopee marketplaces.

## Usage

- Check the [tests](tests) folder for example usage.
- Replace `YOUR_API_KEY` with your actual Lumintu Scraper API key.
- Install the required dependencies using `pip install -r requirements.txt`.
- Run the example scripts to see how to use the SDK.

## Contact

For any questions or support, please contact us at:

- Homepage: [https://lumintuscraper.com](https://lumintuscraper.com)


