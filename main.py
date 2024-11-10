#code by abhis021@github
import pyqrcode
import tkinter as tk
from tkinter import messagebox, Canvas
from PIL import Image, ImageTk


class QRCodeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.textEntry = None
        self.qrLabel = None
        self.geometry("500x200")
        self.title("QR Code Generator for PC")
        self.main_ui()

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
        url.png("ResultQR.png", scale = 6)
        messagebox.showinfo("Success", "QR code generated successfully as ResultQR.png")

    def showQR(self):
        try:
            canvas = Canvas(self, width=300, height=300)
            canvas.pack(pady=20)
            img = ImageTk.PhotoImage(Image.open("ResultQR.png"))
            canvas.create_image(20,20, image=img)
        except FileNotFoundError:
            messagebox.showerror("Error", "QR code image not found. Please generate it first.")


if __name__ == "__main__":
    app = QRCodeApp()
    app.mainloop()



