import random
import string
import os
import uuid

from PIL import Image, ImageDraw, ImageFont


def generate_captcha():

    # Generate random CAPTCHA text
    captcha_text = "".join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=5
        )
    )

    # Image dimensions
    width = 180
    height = 60

    # Create background
    image = Image.new(
        "RGB",
        (width, height),
        color="#14294A"
    )

    draw = ImageDraw.Draw(image)

    # Add random noise lines
    for _ in range(6):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)

        x2 = random.randint(0, width)
        y2 = random.randint(0, height)

        draw.line(
            (x1, y1, x2, y2),
            fill="#3585FF",
            width=1
        )

    # Load font
    try:
        font = ImageFont.truetype("arial.ttf", 32)
    except OSError:
        font = ImageFont.load_default()

    # Draw CAPTCHA characters
    for index, char in enumerate(captcha_text):

        x = 18 + index * 31
        y = random.randint(8, 18)

        draw.text(
            (x, y),
            char,
            font=font,
            fill="#8CC4FF"
        )

    # Add random noise dots
    for _ in range(35):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        draw.point(
            (x, y),
            fill="#FFFFFF"
        )

    # Save image
    folder = os.path.dirname(__file__)

    image_path = os.path.join(
    folder,
    f"captcha_{uuid.uuid4().hex}.png"
)

    image.save(image_path)

    return captcha_text, image_path
if __name__ == "__main__":

    text, path = generate_captcha()

    print("CAPTCHA Code:", text)
    print("Image saved at:", path)