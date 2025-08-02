import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

# 🧪 Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 🔑 Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# ⚡ Load the lightweight model
model = genai.GenerativeModel("gemini-1.5-flash")

# 🎯 Prompt
prompt = "Generate a creative t-shirt product title and a short, fun description based on a futuristic AI concept."

# 💬 Generate content
response = model.generate_content(prompt)

# 🧾 Parse response
product_data = {
    "title": "Fallback Title",
    "description": "Fallback Description"
}
try:
    lines = response.text.split("\n")
    product_data["title"] = lines[0]
    product_data["description"] = " ".join(lines[1:])
except Exception as e:
    print("⚠️ Gemini error:", e)

# 💾 Save product.json
with open("product.json", "w") as f:
    json.dump(product_data, f, indent=2)

print("✅ Gemini-powered product content generated!")
