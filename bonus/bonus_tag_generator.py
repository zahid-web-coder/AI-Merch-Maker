import json
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download stopwords only (we don’t use punkt tokenizer anymore)
nltk.download('stopwords')

# Load product description
with open("../content_generator/product.json", "r") as f:
    product = json.load(f)
    description = product["description"]

# Simple word split (no punkt needed)
words = description.lower().split()
words = [word.strip(".,!?()[]") for word in words if word.isalpha()]
filtered_words = [word for word in words if word not in stopwords.words('english')]

# Get top tags
word_freq = Counter(filtered_words)
top_tags = [tag for tag, count in word_freq.most_common(8)]

# Print and update product.json
print("✅ Auto-generated tags (offline):")
print(top_tags)

product["auto_tags"] = top_tags
with open("../content_generator/product.json", "w") as f:
    json.dump(product, f, indent=4)
