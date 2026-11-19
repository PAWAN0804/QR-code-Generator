
from qr_generator import generate_qr
from logger import logger


def main():

    print("===== QR CODE GENERATOR =====")

    data = input("Enter text or URL: ").strip()

    filename = input("Enter QR code filename: ").strip()

    fill_color = input(
        "Enter QR foreground color (default black): "
    ).strip() or "black"

    back_color = input(
        "Enter background color (default white): "
    ).strip() or "white"

    try:

        file_path = generate_qr(
            data,
            filename,
            fill_color,
            back_color
        )

        print("\nQR Code generated successfully!")
        print(f"Saved at: {file_path}")

        logger.info("Application completed successfully")

    except (ValueError, OSError) as error:

        print(f"\nError: {error}")
        logger.exception("QR generation failed")


if __name__ == "__main__":
    main()
