# src/cli.py
from generator import create_interior
from IPython.display import Image, display


prompt = input("Enter your interior design prompt: ")
style = input("Enter a style (modern, scandinavian, minimalist, etc.): ")

path = create_interior(prompt, style)

# Note: This was made for a colab environment and the image will appear in the notebook. Sorry for any inconveniences.
display(Image(str(path)))


try:
    from google.colab import files
    files.download(str(path))
except ImportError:
    print("Not running in Colab, download manually from outputs folder.")
