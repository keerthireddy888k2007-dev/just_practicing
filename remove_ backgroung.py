from rembg import remove
from PIL import Image

# Define file paths
input_path = r"C:\Users\keert\image.webp"
output_path = "output_image.png"  # Always save as PNG for transparency

# Open, remove background, and save
input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)

print("Background removed successfully!")