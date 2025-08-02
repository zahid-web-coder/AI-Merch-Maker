import os
import json
import requests
from dotenv import load_dotenv

# 🔐 Load credentials
load_dotenv()
SHOPIFY_STORE = os.getenv("SHOPIFY_STORE")
SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")

# 📦 Load generated product
with open("../content_generator/product.json", "r") as f:
    product_data = json.load(f)

# 🌐 Shopify API setup
url = f"https://{SHOPIFY_STORE}/admin/api/2023-04/products.json"
headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN
}

# 📸 Upload mockup image URL manually generated or hosted
payload = {
    "product": {
        "title": product_data.get("title", "Fallback Title"),
        "body_html": product_data.get("description", "Fallback description"),
        "vendor": "AI Merch Maker",
        "product_type": "T-Shirt",
        "tags": "AI, Generated, Gemini, Fun, FLUX.1",
        "images": [
            {
                "src": "https://i.ibb.co/k29tVd7T/tshirt-mockup.png"  # replace if auto-hosted elsewhere
            }
        ]
    }
}

# 🚀 Upload to Shopify
response = requests.post(url, headers=headers, data=json.dumps(payload))

# ✅ Response
if response.status_code == 201:
    print("✅ Product uploaded to Shopify!")
    print(json.dumps(response.json(), indent=2))
else:
    print("❌ Failed to upload product:")
    print(response.status_code, response.text)
