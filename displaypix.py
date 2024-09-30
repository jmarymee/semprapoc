from PIL import Image

# Path to the image file
image_path = '/path/to/your/image.jpg'

# Open an image file
with Image.open(image_path) as img:
    # Display image
    img.show()