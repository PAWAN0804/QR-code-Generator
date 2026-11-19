import qrcode
import re
from pathlib import Path
from logger import logger

def generate_qr(data, filename, fill_color="black",
                back_color="white"):

    if not data or not data.strip():
        raise ValueError("Input data cannot be empty.")

    if not filename.strip():
        raise ValueError("Filename cannot be empty.")

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    # Add user data
    qr.add_data(data)

    # Automatically adjust QR code size
    qr.make(fit=True)

    # Generate QR image
    image = qr.make_image(
        fill_color=fill_color,
        back_color=back_color
    )

    # Save generated image
    output_folder = Path("generated_qr")
    output_folder.mkdir(exist_ok=True)

    safe_filename = re.sub(
    r"[^a-zA-Z0-9_-]",
    "_",
    filename.strip()
)

    if not safe_filename:
        raise ValueError("Invalid filename")

    file_path = output_folder/f"{safe_filename}.png"

    counter = 1
    while file_path.exists():
        file_path = output_folder/(f"{safe_filename}_{counter}.png")
        counter += 1

    image.save(file_path)
    logger.info(f"QR code generated successfully: {file_path}")

    return file_path
