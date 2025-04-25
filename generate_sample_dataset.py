import os
from PIL import Image, ImageDraw, ImageFont
import random

# Create folders
os.makedirs('dataset/authentic', exist_ok=True)
os.makedirs('dataset/tampered', exist_ok=True)

# Create sample authentic images
def generate_authentic_images(num=5):
    for i in range(num):
        img = Image.new('RGB', (256, 256), color=(random.randint(100,255), random.randint(100,255), random.randint(100,255)))
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), f"Real {i}", fill=(0, 0, 0))
        img.save(f'dataset/authentic/real_{i}.jpg')

# Create tampered images by modifying authentic ones
def generate_tampered_images():
    auth_files = os.listdir('dataset/authentic')
    for file in auth_files:
        path = os.path.join('dataset/authentic', file)
        img = Image.open(path).copy()
        draw = ImageDraw.Draw(img)
        # Simulate tampering: draw a black box
        draw.rectangle([150, 150, 200, 200], fill=(0, 0, 0))
        img.save(f'dataset/tampered/fake_{file}')

generate_authentic_images()
generate_tampered_images()

print("✅ Sample dataset created in 'dataset/' with authentic and tampered images.")
