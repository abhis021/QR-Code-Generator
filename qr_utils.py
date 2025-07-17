import qrcode
from PIL import Image
import io

def generate_qr_image(text: str, size: int = 200) -> Image.Image:
    """Generate a QR code image from text."""
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img.resize((size, size))

def save_qr_to_file(text: str, filename: str = "qr.png"):
    """Save QR code to a file."""
    img = generate_qr_image(text)
    img.save(filename)

def get_qr_bytes(text: str) -> bytes:
    """Return QR code image as PNG bytes."""
    img = generate_qr_image(text)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf.read()
