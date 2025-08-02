import os
import json
import nltk
from nltk.corpus import stopwords
from collections import Counter

# 🔹 Ensure stopwords are downloaded once
nltk.download('stopwords', quiet=True)

# 📂 Load product description
try:
    with open("../content_generator/product.json", "r") as f:
        product = json.load(f)
        description = product.get("description", "")
except FileNotFoundError:
    print("❌ product.json not found.")
    exit()

# 🧼 Clean and process text
words = description.lower().split()
words = [word.strip(".,!?()[]\"'") for word in words]  # Remove punctuation
words = [word for word in words if word and word not in stopwords.words("english")]

# 📊 Generate most common keywords
word_freq = Counter(words)
top_tags = [tag for tag, count in word_freq.most_common(8)]

# ✅ Output and store
print("✅ Auto-generated tags (offline):")
print(top_tags)

# 📝 Save tags inside product.json
product["auto_tags"] = top_tags
with open("../content_generator/product.json", "w") as f:
    json.dump(product, f, indent=4)

# 💾 Also save to bonus/auto_tags.json
os.makedirs("../bonus", exist_ok=True)
with open("../bonus/auto_tags.json", "w") as f:
    json.dump({"tags": top_tags}, f, indent=4)
