#code by abhis021@github
import tkinter as tk
from tkinter import messagebox

import pyqrcode
from PIL import Image, ImageTk


class QRCodeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.textEntry = None
        self.qrLabel = None
        self.geometry("500x200")
        self.title("QR Code Generator for PC")
        self.main_ui()

        # Create canvas for displaying the QR code
        self.canvas = tk.Canvas(self, width=174, height=174)  # Set the initial canvas size based on the image size
        self.canvas.pack(pady=20)

        self.qr_image = None  # Store reference to the image

    def main_ui(self):
        #Label and Entry for text input
        label = tk.Label(self, text="Enter Text: ", font=("Times", 16))
        label.pack(pady=10)

        self.textEntry = tk.Entry(self, font=("Times", 16), width=40)
        self.textEntry.pack(pady=10)

        #Buttons to Generate, View and Quit

        buttonFrame = tk.Frame(self)
        buttonFrame.pack(pady=20)

        generateBtn = tk.Button(buttonFrame, text = "Generate QR", command = self.generate_QRCode, width = 10, height=2)
        generateBtn.grid(row=0, column=0, padx=10)

        viewBtn = tk.Button(buttonFrame, text = "View QR", command = self.showQR, width=10, height=2)
        viewBtn.grid(row=0, column=1, padx=10)

        quitBtn = tk.Button(buttonFrame, text = "Quit", command = self.quit, width=10, height=2)
        quitBtn.grid(row=0, column=2, padx=10)

        #Label for displaying the QR Code

        self.qrLabel = tk.Label(self)
        self.qrLabel.pack(pady=20)

    def generate_QRCode(self):
        text = self.textEntry.get().strip()
        if not text:
            messagebox.showwarning("Input Error", "Please enter text to generate QR code.")
            return

        url = pyqrcode.create(text)
        url.png("ResultQR.png", scale=6)
        messagebox.showinfo("Success", "QR code generated successfully as ResultQR.png")


    def showQR(self):
        try:
            # Open the image directly
            image = Image.open("ResultQR.png")

            # Debugging: Show the image using the default viewer to check if it's valid
            image.show()

            self.qr_image = ImageTk.PhotoImage(image)  # Convert to Tkinter format

            # Clear the previous image from the canvas
            self.canvas.delete("all")

            # Adjust canvas size based on image dimensions
            self.canvas.config(width=image.width, height=image.height)

            # Display the image on the canvas at position (0, 0)
            self.canvas.create_image(0, 0, image=self.qr_image, anchor="nw")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {e}")


if __name__ == "__main__":
    app = QRCodeApp()
    app.mainloop()



