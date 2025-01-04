import os
from rembg import remove # type: ignore
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Powerful Background Remover")
        self.root.geometry("700x550")
        self.root.resizable(False, False)
        
        # Variables to store paths
        self.input_image_path = None
        self.output_image_path = None
        
        # UI Design
        self.create_widgets()

    def create_widgets(self):
        # Header
        header = tk.Label(self.root, text="Powerful Background Remover", font=("Arial", 24, "bold"))
        header.pack(pady=10)

        # Footer
        footer = tk.Label(root, text="Developed by Hassan Ahmed for The Hack Club", bg="#f0f0f0", fg="#999", font=("Helvetica", 10))
        footer.pack(side="bottom", pady=10)

        # Frames for layout
        frame = ttk.Frame(self.root)
        frame.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

        # Input Image Area
        self.input_label = tk.Label(frame, text="Input Image", font=("Arial", 14))
        self.input_label.grid(row=0, column=0, padx=10, pady=10)
        self.input_canvas = tk.Canvas(frame, width=300, height=300, bg="#f0f0f0", relief="ridge", bd=2)
        self.input_canvas.grid(row=1, column=0, padx=10, pady=10)

        # Output Image Area
        self.output_label = tk.Label(frame, text="Output Image", font=("Arial", 14))
        self.output_label.grid(row=0, column=1, padx=10, pady=10)
        self.output_canvas = tk.Canvas(frame, width=300, height=300, bg="#f0f0f0", relief="ridge", bd=2)
        self.output_canvas.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        self.upload_button = ttk.Button(button_frame, text="Upload Image", command=self.upload_image)
        self.upload_button.grid(row=0, column=0, padx=10)

        self.remove_bg_button = ttk.Button(button_frame, text="Remove Background", command=self.remove_background, state=tk.DISABLED)
        self.remove_bg_button.grid(row=0, column=1, padx=10)

        self.save_button = ttk.Button(button_frame, text="Save Output", command=self.save_output, state=tk.DISABLED)
        self.save_button.grid(row=0, column=2, padx=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not file_path:
            return
        
        try:
            self.input_image_path = file_path
            img = Image.open(self.input_image_path)
            img.thumbnail((300, 300))  # Resize to fit the canvas
            self.input_image = ImageTk.PhotoImage(img)
            self.input_canvas.create_image(150, 150, image=self.input_image)
            self.remove_bg_button.config(state=tk.NORMAL)  # Enable "Remove Background" button
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    def remove_background(self):
        if not self.input_image_path:
            messagebox.showwarning("Warning", "Please upload an image first!")
            return

        try:
            with open(self.input_image_path, 'rb') as input_file:
                input_data = input_file.read()
                output_data = remove(input_data)

            self.output_image_path = "temp_output.png"  # Temporary file
            with open(self.output_image_path, 'wb') as output_file:
                output_file.write(output_data)

            img = Image.open(self.output_image_path)
            img.thumbnail((300, 300))  # Resize to fit the canvas
            self.output_image = ImageTk.PhotoImage(img)
            self.output_canvas.create_image(150, 150, image=self.output_image)
            self.save_button.config(state=tk.NORMAL)  # Enable "Save Output" button
            messagebox.showinfo("Success", "Background removed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove background: {e}")

    def save_output(self):
        if not self.output_image_path:
            messagebox.showwarning("Warning", "No output image to save!")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG Files", "*.png")])
        if not save_path:
            return

        try:
            os.rename(self.output_image_path, save_path)
            self.output_image_path = None  # Clear temporary file reference
            messagebox.showinfo("Success", "Output image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {e}")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()