# Powerful Background Remover

A desktop application built with Python and Tkinter to remove image backgrounds seamlessly. This tool uses the `rembg` library to process images and provides a user-friendly graphical interface for ease of use.

---

## Features
- **Upload Images**: Supports `.png`, `.jpg`, and `.jpeg` image formats.
- **Background Removal**: Powered by the `rembg` library for accurate background elimination.
- **Preview Images**: View both input and output images directly in the app.
- **Save Output**: Save the processed image to your desired location.

---

## Prerequisites
- Python 3.8 to 3.11 (recommended)
- Required Python libraries:
  - `rembg`
  - `Pillow`

---

## Installation

1. Clone this repository or download the project files.
2. Navigate to the project directory:
   ```bash
   cd powerful-background-remover
   ```
3. Install the required libraries:
   ```bash
   pip install rembg pillow
   ```

4. (Optional) Ensure `onnxruntime` is installed:
   ```bash
   pip install onnxruntime
   ```

---

## How to Run the App

1. Open a terminal in the project directory.
2. Run the Python script:
   ```bash
   python app.py
   ```
3. The app window will open, allowing you to upload images, remove backgrounds, and save the results.

---

## Usage
1. **Upload Image**: Click the "Upload Image" button to select an image file.
2. **Remove Background**: After uploading, click the "Remove Background" button to process the image.
3. **Save Output**: Once the background is removed, click "Save Output" to store the result.

---

## Project Structure
```
├── program.py          # Main application script
├── temp_output.png # Temporary file for output images
└── README.md       # Project documentation
```
