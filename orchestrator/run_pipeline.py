import json
import requests
from pathlib import Path

# 🔹 Load product data from Step 1
with open("../content_generator/product.json", "r") as f:
    product_data = json.load(f)

# 🔹 Add mockup image (already generated in Step 2)
mockup_image_url = "https://i.ibb.co/8nW09dDw/t-shirt.png"
product_data["mockup_image"] = mockup_image_url

# 🔹 Add image source (from mockup overlay image, optional but good for bonus)
product_data["image_source"] = "https://i.ibb.co/kVQGMB4P/waterfall.jpg"

# 🔹 Load auto_tags from bonus step (if exists)
try:
    with open("../bonus/auto_tags.json", "r") as tag_file:
        product_data["auto_tags"] = json.load(tag_file)["tags"]
except FileNotFoundError:
    print("⚠️ No auto_tags.json found. Skipping bonus tags...")

# 🔹 Send to Step 3: publish.php
print("📡 Sending to fake publisher API...")
print("🔍 JSON Being Sent:")
print(json.dumps(product_data, indent=2))
response = requests.post("http://localhost:8000/publish.php", json=product_data)

# 🔹 Output response
print("\n✅ Response:")
print(response.json())
