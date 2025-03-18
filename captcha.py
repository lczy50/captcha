import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def generate_captcha_text(size=5, chars=string.ascii_uppercase + string.ascii_lowercase):
    """Generates a random string for the CAPTCHA."""
    return ''.join(random.choice(chars) for _ in range(size))

def create_blank_image(width=200, height=100, background_color='white'):
    """Creates a blank image for the CAPTCHA."""
    return Image.new('RGB', (width, height), background_color)

def draw_text(draw, text, position, font_path="arial.ttf", font_size=30):
    """Draws text on the image."""
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    draw.text(position, text, fill='black', font=font)

def add_noise(draw, width, height, dot_count=300):
    """Adds random dots (noise) to the CAPTCHA image."""
    for _ in range(dot_count):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill='black')

def add_lines(draw, width, height, line_count=5):
    """Adds random lines to the CAPTCHA image."""
    for _ in range(line_count):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill='black', width=2)

def apply_blur(image, radius=1):
    """Applies a blur effect to the CAPTCHA image."""
    return image.filter(ImageFilter.GaussianBlur(radius))

def generate_captcha():
    """Generates a complete CAPTCHA image with text, noise, and distortion."""
    text = generate_captcha_text()
    img = create_blank_image()
    draw = ImageDraw.Draw(img)
    draw_text(draw, text, position=(50, 40))
    add_lines(draw, img.width, img.height)
    add_noise(draw, img.width, img.height)
    img = apply_blur(img)
    img.show()
    return img, text

if __name__ == "__main__":
    captcha_image, captcha_text = generate_captcha()