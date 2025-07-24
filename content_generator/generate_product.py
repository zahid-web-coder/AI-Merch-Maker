import os
import openai
import json
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#Step 1: Generated product info using ChatGPT
def generate_product_info():
    prompt = (
        "Generate a cool and funny T-shirt product idea for an online merch store. "
        "Return a JSON with the following keys:\n"
        "- title\n- description\n- tags (as a list of keywords)\n"
    )

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )

    message = response.choices[0].message.content
    return json.loads(message)

#Step 2: Generated image using DALL·E
def generate_image(prompt_text):
    response = openai.images.generate(
        prompt=prompt_text,
        n=1,
        size="512x512"
    )
    return response.data[0].url

#Step 3: Saved result to file
def main():
    product = generate_product_info()
    print("✅ Generated Product Info:")
    print(json.dumps(product, indent=2))

    image_url = generate_image(product['title'])
    print("🖼️ Image URL:", image_url)

    output = {
        "title": product["title"],
        "description": product["description"],
        "tags": product["tags"],
        "image_url": image_url
    }

    with open("product.json", "w") as f:
        json.dump(output, f, indent=2)

    print("\n✅ Saved to product.json")

if __name__ == "__main__":
    main()
