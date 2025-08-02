# 🤖 AI Merch Maker 🛍️

Generate & publish AI-designed T-shirts to Shopify – completely automated.
### 🔮 Sample AI-Generated T-Shirt Mockup

![AI T-Shirt](https://raw.githubusercontent.com/zahid-web-coder/AI-Merch-Maker/main/flux_image.png)

🔥 Features
✨ Gemini API: Generates creative T-shirt titles & descriptions.

🎨 Hugging Face FLUX.1: Turns Gemini prompt into unique product artwork.

🧵 Mockup Generator: Overlays AI image on a T-shirt template.

📤 Shopify Integration: Automatically uploads products via Shopify API.

📦 Fully automated pipeline: From text prompt to live product.

## 📦 Project Overview

**AI Merch Maker Lite** is a 4-step project that combines AI + frontend + backend + scripting to simulate a real-world merch product pipeline.
This project:
- Auto-generates a T-shirt **title, description, and tags** using **Gemini API**
- Generates a product **image** using **Hugging Face API** or fallback
- Creates a **mockup image** by overlaying the design on a T-shirt using **JavaScript canvas**
- Simulates a **publishing API** using **PHP**
- Automates the whole workflow using a **Python Orchestrator**
- **Shopify integration** Pushes the product to Shopify Website
- Includes an optional **bonus AI/NLP tag extractor** using `nltk`

---

## 🛠️ Tech Stack

| Task                       | Tech Used           |
|----------------------------|---------------------|
| Content Generator          | Python + Gemini API |
| Image Generator            | Higging Face API |
| Mockup Visualizer          | HTML + CSS + JavaScript (Canvas API) |
| Fake Product Publisher     | PHP (Server + API)  |
| Pipeline Orchestrator      | Python              |
| Shopify integration        | Python              |
| Bonus (Offline Tag Gen)    | Python + NLTK       |

---

## 📂 Folder Structure

# AI-Merch-Maker

```
AI-Merch-Maker/
├── bonus/                         # 🔹 Bonus NLP Tag Generator
│   ├── bonus_tag_generator.py    # Extracts tags from description using NLTK
│   └── auto_tags.json            # (Optional) Saved tags from the bonus script

├── content_generator/
│   ├── generate_product.py       # Uses Gemini to generate prompt
│   ├── generate_image.py         # Uses Hugging Face (FLUX.1) to create image
│   ├── flux_image.png            # AI image (auto-generated)
│   └── product.json              # Contains title + description

├── mock_generator/               Mockup Generator (HTML + JS + CSS)
│   ├── index.html                # Canvas-based UI for T-shirt mockup
│   ├── style.css                 # Styling for the mockup UI
│   └── script.js                 # Logic to overlay design on T-shirt

├── publisher_api/                 Fake Publisher API (PHP)
│   ├── publish.php               # Receives and logs JSON product data
│   └── log.txt                   # Log file with published data

├── orchestrator/                 # Automation Pipeline (Python)
│   └── run_pipeline.py           # Combines all steps and sends data

├── shopify_integration/
│   └── upload_to_shopify.py      # Pushes the product to Shopify

├── .env.example                  # 🔐 Sample environment config (API key placeholder)
├── requirements.txt              # 📦 Python dependencies
└── README.md                     # 📘 Project documentation (you’re reading it!)
```

---
## ⚙️ How It Works

This project automates the creation and upload of AI-generated T-shirt products using Gemini API (text), Hugging Face FLUX.1 (image), a custom mockup canvas, and the Shopify API.

---

## ✅ Features Covered

### 🧠 Step 1: Product Content Generator (Python)
- `generate_product.py`: Uses **Gemini API** to generate a creative T-shirt title and description.
- Saves the content into `product.json` for use in the pipeline.


### 🎨 Step 2: Image Generator (Python)
- `generate_image.py`: Sends the Gemini prompt to **Hugging Face FLUX.1 API** (via fal.ai provider) to generate an AI image.
- Saves it as `flux_image.png`.

### 👕 Step 3: Mockup Generator (HTML + JS)
- `mockup.html` + `script.js`: Uses **HTML5 Canvas** to place the generated image on a base T-shirt.
- Creates a visual preview and a JSON metadata output.
- Optional: uploads the mockup image manually to image hosting.

### 🚀 Step 4: Shopify Product Uploader (Python)
- `upload_to_shopify.py`: Reads product data and mockup image URL.
- Sends a **POST request** to the Shopify Admin API with title, description, tags, and product image.
- Requires a `.env` file with `SHOPIFY_STORE` and `SHOPIFY_ACCESS_TOKEN`.

### 🛰️ Step 5: Full Automation Orchestrator (Python)
- `run_pipeline.py`: Calls all steps in order.
- Automates reading product, attaching images, and posting the final product to Shopify.

### 🏅 Bonus: AI/NLP Tag Generator (Optional)
- Uses NLTK or hardcoded logic to generate product tags.
- Stores tags in `auto_tags.json` or directly updates `product.json`.

---


---

## 🔐 Environment Setup (.env file)
```env
GEMINI_API_KEY=your-gemini-api-key
HF_API_TOKEN=your-huggingface-token
SHOPIFY_STORE=your-store.myshopify.com
SHOPIFY_ACCESS_TOKEN=your-shopify-access-token`
```

--- 


## ⚙️ Setup Instructions

1. **Clone this repo:**

```bash
git clone https://github.com/zahid-web-coder/AI-Merch-Maker.git
cd AI-Merch-Maker
```
---

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```
---
3. Set up .env file:
 **Create a .env file in root (or use .env.example) with your Gemini API key:**

```ini
GEMINI_API_KEY=your_google_gemini_api_key
HF_API_TOKEN=your_huggingface_token
SHOPIFY_STORE=your-store-name.myshopify.com
SHOPIFY_ACCESS_TOKEN=your_shopify_access_token
```
---

4. **Generate AI content (Gemini):**
```bash
python content_generator/generate_product.py
```
---
5.**Generate AI image (Hugging Face FLUX.1)**
```bash
python content_generator/generate_image.py
```
---
6. **Preview mockup (optional, frontend)**
Open mockup_generator/mockup.html in browser.
---

7 **EXTRA- To run offline fallback only:**

```bash
cd content_generator
python generate_product_offline.py
```

8.**To run mock server :**

```bash
cd publisher_api
php -S localhost:8000
```

9 .**Upload to Shopify**
```bash
python shopify_integration/upload_to_shopify.py
```
---
10.**OR Run entire pipeline**
```bash
python run_pipeline.py
```
---

---

## 📸 Sample Output 

```json
{
  "title": "Neo-Mind: Glitch in the Matrix Tee",
  "description": "Got that AI-induced existential crisis? Embrace the glitch...",
  "image": "flux_image.png"
}

```
---

## 🧠 Credits
Built by: Mohammed Zahid

Models used:

Gemini 1.5 Flash

FLUX.1

---

🛡️ Disclaimer
This project is for educational and portfolio use only. API tokens and secrets should be stored securely.
---



