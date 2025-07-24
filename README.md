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
├── bonus/                         # 🔹 Bonus NLP Tag Generator (Offline)
│   ├── bonus_tag_generator.py    # Extracts tags from description using NLTK
│   └── auto_tags.json            # (Optional) Saved tags from the bonus script

├── content_generator/            # ✅ Step 1: Product Content Generator (Python)
│   ├── generate_product.py       # Uses OpenAI GPT + DALL·E
│   ├── generate_product_offline.py # Offline fallback with hardcoded content
│   └── product.json              # Generated product data

├── mock_generator/               # ✅ Step 2: Mockup Generator (HTML + JS + CSS)
│   ├── index.html                # Canvas-based UI for T-shirt mockup
│   ├── style.css                 # Styling for the mockup UI
│   └── script.js                 # Logic to overlay design on T-shirt

├── publisher_api/                # ✅ Step 3: Fake Publisher API (PHP)
│   ├── publish.php               # Receives and logs JSON product data
│   └── log.txt                   # Log file with published data

├── orchestrator/                 # ✅ Step 4: Automation Pipeline (Python)
│   └── run_pipeline.py           # Combines all steps and sends data

├── .env.example                  # 🔐 Sample environment config (API key placeholder)
├── requirements.txt              # 📦 Python dependencies
└── README.md                     # 📘 Project documentation (you’re reading it!)


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



