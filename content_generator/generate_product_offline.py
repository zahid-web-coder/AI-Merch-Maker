import json

def generate_product_info():
    return {
        "title": "Retro Pizza Astronaut Tee",
        "description": "Bring the calm and majesty of nature with you wherever you go. The Nature Flow Serenity Tee features a stunning waterfall print captured in brilliant daylight, symbolizing peace, energy, and flow. Ideal for nature lovers, explorers, and those who crave tranquility in motion.",
        "tags": [
            "waterfall", "nature", "serene", "outdoor", "adventure",
            "scenic", "daylight", "landscape", "travel", "peaceful"
        ],
        "image_url": "https://unsplash.com/photos/waterfalls-on-rocky-ground-during-daytime-Mece81fY8mk",
        "auto_tags": [
            "nature", "bring", "calm", "majesty", "wherever",
            "flow", "serenity", "tee"
        ]
    }

def main():
    product = generate_product_info()

    with open("product.json", "w") as f:
        json.dump(product, f, indent=4)

    print("✅ Offline product.json written successfully!")

if __name__ == "__main__":
    main()
