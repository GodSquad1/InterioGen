# src/generator.py
from pathlib import Path
import base64
from dalle_client import generate_interior

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def save_image(image_b64, filename):
    """
    Decode base64 image and save locally.
    """
    path = OUTPUT_DIR / filename
    with open(path, "wb") as f:
        f.write(base64.b64decode(image_b64))
    return path

def create_interior(prompt, style="modern"):
    """
    Generate interior design image and save locally.
    """
    image_b64 = generate_interior(prompt, style)
    filename = f"{prompt.replace(' ','_')}.png"
    path = save_image(image_b64, filename)
    print(f"Image saved at {path}")
    return path
