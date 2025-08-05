from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

def generate_blip_caption(image_path: str):
    # Load pre-trained BLIP model and processor
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Load and preprocess image
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    # Generate caption
    output = model.generate(**inputs, max_new_tokens=30)
    caption = processor.decode(output[0], skip_special_tokens=True)
    
    return caption

# Example usage
if __name__ == "__main__":
    image_path = "your_image.jpg"  # 🔁 Replace with your image filename
    caption = generate_blip_caption(image_path)
    print("Generated Caption:", caption)
