import os
import json
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# 🔐 Load environment variables from .env
load_dotenv()
HF_TOKEN = os.getenv("HF_API_TOKEN")

# 📂 Load latest product content
with open("product.json", "r") as f:
    product = json.load(f)

# 🧠 Use title + description as prompt
prompt = f"{product['title']} — {product['description']}"
print("🎯 Prompt:", prompt)

# ⚡ Hugging Face client via fal-ai
client = InferenceClient(
    provider="fal-ai",
    api_key=HF_TOKEN,
)

print("🎨 Generating image from prompt...")
try:
    image = client.text_to_image(
        prompt,
        model="black-forest-labs/FLUX.1-Krea-dev",
    )
    image_path = "flux_image.png"
    image.save(image_path)
    print(f"✅ Image saved as: {image_path}")
except Exception as e:
    print("❌ Failed to generate image:", e)
