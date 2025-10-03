# Shopee Scraper

This project is the official Python client for the **Lumintu Scraper API** for shopee  
The purpose is to make integrating Lumintu Scraper into your Python app as simple as one line of code.

With this SDK, you can call scraping actors, fetch results, and monitor your account usage without worrying about retries, errors, or raw HTTP requests.

The end goal of this tool is to make **Shopee scraping effortless**.  
Currently it supports:

- Scraping product details from Shopee (ID, TH, VN, TW)
- Managing credits and user info
- Handling rate limits, retries, and API errors automatically

Skip the hassle of building and maintaining your own scraper.  
Focus on building your app, not the scraper. we handle the :

- IP Ban
- Captcha
- Rate limit
- Slow Selenium web driver
- Strict header algorithm like x-sap-ri, x-sap-sec, af-ac-cli-id, af-ac-enc-sz-token, AC_CERT_D

Currently supported Shopee marketplaces:

- Indonesia (ID)
- Thailand (TH)
- Vietnam (VN)
- Taiwan (TW)

```HTTP
https://mall.shopee.SITE/api/v4/pdp/get
```
All its from one base API with special algorithm to generate the required headers and parameters.

## Example Response
- [Indonesia (ID)](tests/output/result_12cc1728-2a9a-4945-b7b2-c2a9bbcfb0ee_shopee_id.json)
- [Thailand (TH)](tests/output/result_30dfcaf1-8ff2-412c-bb40-f451e1f80222_shopee_th.json)
- [Vietnam (VN)](tests/output/result_b6e075c2-5867-4967-81d8-d93e88961a11_shopee_vn.json)
- [Taiwan (TW)](tests/output/result_bf447882-19c4-4047-9f64-387f169e6fd9_shopee_tw.json)

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


