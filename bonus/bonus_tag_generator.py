import json
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download stopwords
nltk.download('stopwords')

# Load product description
with open("../content_generator/product.json", "r") as f:
    product = json.load(f)
    description = product["description"]

# Basic cleaning
words = description.lower().split()
words = [word.strip(".,!?()[]") for word in words]  # Remove punctuation
words = [word for word in words if word and word not in stopwords.words('english')]

# Count top words
word_freq = Counter(words)
top_tags = [tag for tag, count in word_freq.most_common(8)]

# Show and save
print("✅ Auto-generated tags (offline):")
print(top_tags)

# Save inside product.json
product["auto_tags"] = top_tags
with open("../content_generator/product.json", "w") as f:
    json.dump(product, f, indent=4)

# Optionally: Save to bonus/auto_tags.json too
with open("../bonus/auto_tags.json", "w") as f:
    json.dump({"tags": top_tags}, f, indent=4)
