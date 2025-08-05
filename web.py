from flask import Flask, render_template, request
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import io
import os
import csv
from datetime import datetime

app = Flask(__name__)

# === Config ===
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# === Load BLIP model and processor ===
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# === Caption Generation ===
def generate_blip_caption(pil_image):
    inputs = processor(pil_image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# === Log captions ===
def log_caption(filename, caption):
    log_file = os.path.join(UPLOAD_FOLDER, 'captions_log.csv')
    with open(log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), filename, caption])

# === Route ===
@app.route("/", methods=["GET", "POST"])
def index():
    caption = None
    image_url = None

    if request.method == "POST" and 'image' in request.files:
        file = request.files['image']
        if file:
            # Save the image
            filename = file.filename
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(image_path)
            image_url = os.path.join(UPLOAD_FOLDER, filename).replace("\\", "/")

            # Generate caption
            image = Image.open(image_path).convert("RGB")
            caption = generate_blip_caption(image)

            # Log image + caption
            log_caption(filename, caption)

    return render_template("index.html", caption=caption, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
