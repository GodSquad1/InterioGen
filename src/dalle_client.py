# src/dalle_client.py
import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()  # load API key from .env if exists

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_interior(prompt, style="modern", size="1024x1024"):
    """
    Generate an interior design image using DALL·E 3.
    Returns base64-encoded image data.
    """
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"You are an experienced interior designer. {prompt}, interior design style: {style}",
        n=1,
        size=size,
        response_format="b64_json"  # returns base64
    )
    image_b64 = response.data[0].b64_json
    return image_b64
