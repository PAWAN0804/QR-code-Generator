# QR-code-Generator
A Python-based QR Code Generator Tool that converts text, URLs, and other information into customizable QR code images. Built using Python, qrcode, Pillow, and Tkinter, featuring color customization, QR previews, image saving, and input validation.


# QR Code Generator Tool Using Python 

## 📌 Project Overview

The **QR Code Generator Tool** is a Python-based desktop application that allows users to generate QR codes from text, website URLs, and other information.

The application uses Python's QR code generation and image processing libraries to create customizable QR code images that can be saved and shared easily.

It also provides a graphical user interface (GUI) using Tkinter to make QR code generation simple and user-friendly.

## 🚀 Features

- Generate QR codes from text and URLs.
- Customize QR code foreground and background colors.
- Save generated QR codes in PNG format.
- Preview generated QR codes.
- Automatically adjust QR code size based on input data.
- Support multiple QR code generation requests.
- Handle empty inputs and invalid filenames.
- Prevent accidental overwriting of existing QR images.
- Maintain application logs for tracking activities.
- User-friendly desktop interface using Tkinter.

## 🛠️ Technologies Used

- Python 3
- qrcode
- Pillow (PIL)
- Tkinter
- OS Module
- Pathlib
- Logging

## 📂 Project Structure

```text
QR_Code_Generator/
│
├── main.py
├── gui.py
├── qr_generator.py
├── config.py
├── logger.py
│
├── generated_qr/
├── logs/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### Step 1: Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### Step 2: Navigate to the project directory

```bash
cd QR_Code_Generator
```

### Step 3: Create a virtual environment

```bash
python -m venv my_env
```

### Step 4: Activate the virtual environment

Windows PowerShell:

```powershell
.\my_env\Scripts\Activate.ps1
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the command-line application

```bash
python main.py
```

### Step 7: Run the graphical application

```bash
python gui.py
```

## 💻 How It Works

1. The user enters text, a website URL, or other information.
2. The application validates the provided input.
3. The qrcode library converts the information into a QR code.
4. Pillow processes the QR code image.
5. Users can customize QR code colors.
6. The generated QR code is displayed and saved as a PNG image.

## 🎯 Learning Outcomes

- Practical implementation of Python programming.
- Working with third-party Python libraries.
- Understanding image processing using Pillow.
- Developing desktop applications using Tkinter.
- Implementing input validation and exception handling.
- Understanding modular programming.
- Managing files and directories using Python.

## 🔮 Future Enhancements

- QR code generation with custom logos.
- Bulk QR code generation using CSV and Excel files.
- QR code scanner and decoder functionality.
- QR code history and management system.
- Export QR codes in different image formats.
- Improved GUI with additional customization options.

## 👨‍💻 Author

Developed as a Python programming project to demonstrate practical skills in Python development, image processing, GUI development, and application automation.

**If you find this project useful, don't forget to ⭐ the repository!**
