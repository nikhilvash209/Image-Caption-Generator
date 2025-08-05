# 🖼️ Image Caption Generator

A web-based application that generates natural language captions for images using a powerful Transformer-based model (BLIP). Built with Flask, enhanced with Bootstrap for UI, and supports drag-and-drop upload, preview, and caption logging.

---

## 🚀 Features

- ✅ Upload or drag-and-drop image
- ✅ View image preview instantly
- ✅ Auto-generate a caption using BLIP model from Hugging Face
- ✅ Logs each uploaded image and its caption
- ✅ Responsive, modern UI using Bootstrap
- ✅ Ready for deployment on Render or Hugging Face Spaces

---

## 🧠 Powered By

- 🤖 **BLIP**: [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)
- 🌐 **Flask**: Lightweight Python web framework
- 🎨 **Bootstrap 5**: For styling and responsiveness

---

## 📂 Folder Structure

```
image-caption-generator/
├── web.py                   # Main Flask app
├── templates/
│   └── index.html           # UI template
├── static/
│   └── logs/                # Saved images + captions
├── requirements.txt
├── render.yaml              # Render deployment config
├── Procfile                 # Web service command for gunicorn
└── README.md
```

---

## 🛠️ Installation & Running Locally

### 1. Clone the Repository

```terminal
git clone https://github.com/yourusername/image-caption-generator.git
cd image-caption-generator
```

### 2. Create & Activate a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```terminal
pip install -r requirements.txt
```

### 4. Run the App

```bash
python web.py
```

Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📦 Deployment (Render)

1. Push this repo to GitHub.
2. Make sure these files exist:
   - `requirements.txt`
   - `Procfile`
   - `render.yaml`
3. Go to [https://render.com](https://render.com) → “New Web Service”
4. Connect your GitHub repo and deploy!

---

## 📸 Example

| Upload Image | Generated Caption |
|--------------|-------------------|
| ![Example](static/logs/example.jpg) | `A dog sitting on a chair in the living room` |


---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).
