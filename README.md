# AI Merch Maker Lite 🎨👕

An end-to-end automation pipeline that generates creative T-shirt product content, overlays design mockups, and simulates publishing — built using Python, JavaScript, and PHP.

---

## 📦 Project Overview

This project was developed as part of the Smart Ecom Tech Internship Assignment. It simulates an AI-driven merchandising system that:

- Generates unique product content using GPT.
- Creates mockup visuals using HTML5 Canvas.
- Publishes the product through a mock PHP API.
- Includes an optional bonus feature for AI-based tag generation.

---

## 🛠️ Tech Stack

| Task                       | Tech Used           |
|----------------------------|---------------------|
| Content Generator          | Python + OpenAI GPT |
| Image Generator            | OpenAI DALL·E or Unsplash |
| Mockup Visualizer          | HTML + CSS + JavaScript (Canvas API) |
| Fake Product Publisher     | PHP (Server + API)  |
| Pipeline Orchestrator      | Python              |
| Bonus (Offline Tag Gen)    | Python + NLTK       |

---

## 📂 Folder Structure

# AI-Merch-Maker

AI-Merch-Maker/
├── bonus/ # Bonus NLP tag generator   |
│ └── bonus_tag_generator.py   |
│ └── auto_tags.json
├── content_generator/ # Step 1: GPT + DALL·E product.json   |
│ └── generate_product.py   |
│ └── product.json   |
├── mock_generator/ # Step 2: Canvas-based T-shirt mockup   |
│ └── index.html   |
│ └── style.css   |
│ └── script.js   |
├── orchestrator/ # Step 4: Runs entire pipeline   |
│ └── run_pipeline.py   |
├── publisher_api/ # Step 3: Fake API (PHP)   |
│ └── publish.php   |
│ └── log.txt   |
├── .env.example # Sample env file   |
├── requirement.txt   |
└── README.md    |
---
---

## ⚙️ How It Works

### 1. Content Generation (`content_generator/generate_product.py`)
- Uses GPT to generate title, description, tags.
- Uses DALL·E API or placeholder image to generate product image.
- Stores everything in `product.json`.

### 2. Mockup Generator (`mock_generator/index.html`)
- Overlays the image onto a T-shirt template using HTML Canvas.
- Generates mockup JSON like Printful.

### 3. Publisher API (`publisher_api/publish.php`)
- Accepts product data via POST.
- Logs JSON data and returns a mock `product_id`.

### 4. Orchestrator (`orchestrator/run_pipeline.py`)
- Runs the entire flow: content → mockup → publishing.

### ⭐ Bonus: NLP-Based Tag Generator
- Extracts keywords from product description.
- Adds `auto_tags` to product JSON.

---

## 📸 Sample Output

```json
{
  "title": "Retro Pizza Astronaut Tee",
  "description": "Bring the calm and majesty of nature with you wherever you go...",
  "tags": ["waterfall", "nature", "serene", ...],
  "mockup_image": "https://i.ibb.co/8nW09dDw/t-shirt.png",
  "auto_tags": ["nature", "flow", "calm", ...]
}
```
---
## 🔐 Environment Setup
Create a .env file with:
OPENAI_API_KEY=your_openai_api_key_here
For demo purposes, the repo includes an offline fallback using product.json.

---
## ✅ Completed Features
 Product content generation (offline fallback included)

 T-shirt design mockup (HTML Canvas)

 Fake publishing API (PHP)

 Pipeline orchestrator

 Bonus: NLP auto-tag generator
---



