# AI Merch Maker Lite 🎨👕

An end-to-end AI-powered product automation pipeline that generates a T-shirt idea, mockup image, and simulates publishing — all with minimal manual input.

---

## 📦 Project Overview

**AI Merch Maker Lite** is a 4-step project that combines AI + frontend + backend + scripting to simulate a real-world merch product pipeline.
This project:
- Auto-generates a T-shirt **title, description, and tags** using **OpenAI GPT**
- Generates a product **image** using **DALL·E** or fallback
- Creates a **mockup image** by overlaying the design on a T-shirt using **JavaScript canvas**
- Simulates a **publishing API** using **PHP**
- Automates the whole workflow using a **Python Orchestrator**
- Includes an optional **bonus AI/NLP tag extractor** using `nltk`

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

## ✅ Features Covered

### Step 1: Product Content Generator (Python)
- `generate_product.py`: Uses OpenAI GPT & DALL·E to create product data
- `generate_product_offline.py`: Offline fallback using hardcoded JSON
- Saves product info in `product.json`

### Step 2: Mockup Generator (JavaScript)
- HTML + Canvas overlay of design on a base T-shirt image
- Outputs a JSON similar to Printful's API mockup

### Step 3: Fake Publisher API (PHP)
- `publish.php`: Accepts POST JSON and returns fake product ID
- `log.txt`: Logs published data for verification

### Step 4: Automation Orchestrator (Python)
- `run_pipeline.py`: Triggers steps and simulates full product pipeline

### 🏅 Bonus: AI/NLP Tag Generator (Optional)
- Uses NLTK to extract tags from description
- Writes to `auto_tags.json` or directly updates `product.json`

--- 

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
 **Create a .env file in root (or use .env.example) with your OpenAI key:**

```ini
OPENAI_API_KEY=your_openai_key_here
```
---
4.**To run offline fallback only:**

```bash
cd content_generator
python generate_product_offline.py
```

5.**To run full pipeline (requires API key):**

```bash
cd orchestrator
python run_pipeline.py
```

6.**To run mock server (Step 3):**

```bash
cd publisher_api
php -S localhost:8000
```

7.To run mockup generator:

Open mock_generator/index.html in your browser
`
---

## 💡 Sample Output
product.json: Contains generated title, description, tags, and image URL

canvas preview of T-shirt mockup

log.txt: Received JSON with all fields

Bonus: NLP extracted auto_tags

---

## 📸 Sample Output of json

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



