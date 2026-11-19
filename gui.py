
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import ImageTk

from qr_generator import generate_qr


class QRCodeGeneratorApp:

    def __init__(self, root):

        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("500x650")

        self.qr_image = None
        self.preview_image = None

        tk.Label(
            root,
            text="QR Code Generator",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        tk.Label(root, text="Enter Text or URL").pack()

        self.data_entry = tk.Entry(root, width=45)
        self.data_entry.pack(pady=10)

        tk.Label(root, text="Enter Filename").pack()

        self.filename_entry = tk.Entry(root, width=45)
        self.filename_entry.pack(pady=10)

        self.fill_color = "black"
        self.back_color = "white"

        tk.Button(
            root,
            text="Choose QR Color",
            command=self.choose_fill_color
        ).pack(pady=5)

        tk.Button(
            root,
            text="Choose Background Color",
            command=self.choose_back_color
        ).pack(pady=5)

        tk.Button(
            root,
            text="Generate QR Code",
            command=self.generate
        ).pack(pady=15)

        self.preview = tk.Label(root)
        self.preview.pack(pady=10)

        tk.Button(
            root,
            text="Save QR Code",
            command=self.save_qr
        ).pack(pady=10)

    def choose_fill_color(self):

        color = colorchooser.askcolor()[1]

        if color:
            self.fill_color = color

    def choose_back_color(self):

        color = colorchooser.askcolor()[1]

        if color:
            self.back_color = color

    def generate(self):

        data = self.data_entry.get().strip()
        filename = self.filename_entry.get().strip()

        try:

            file_path = generate_qr(
                data,
                filename,
                self.fill_color,
                self.back_color
            )

            from PIL import Image

            self.qr_image = Image.open(file_path)

            preview = self.qr_image.copy()
            preview.thumbnail((250, 250))

            self.preview_image = ImageTk.PhotoImage(preview)

            self.preview.config(image=self.preview_image)

            messagebox.showinfo(
                "Success",
                "QR Code generated successfully!"
            )

        except (ValueError, OSError) as error:

            messagebox.showerror("Error", str(error))

    def save_qr(self):

        if self.qr_image is None:
            messagebox.showwarning(
                "Warning",
                "Generate a QR code first!"
            )
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Images", "*.png")]
        )

        if file_path:
            self.qr_image.save(file_path)

            messagebox.showinfo(
                "Success",
                "QR Code saved successfully!"
            )


if __name__ == "__main__":

    root = tk.Tk()

    app = QRCodeGeneratorApp(root)

    root.mainloop()
