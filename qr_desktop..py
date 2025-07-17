import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk
from qr_utils import generate_qr_image, save_qr_to_file

class QRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x400")
        self.root.resizable(True, True)

        self.input_text = tk.StringVar()

        tk.Label(root, text="Enter text:").pack(pady=5)
        self.entry = tk.Entry(root, textvariable=self.input_text, width=40)
        self.entry.pack(pady=5)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Generate", command=self.generate_qr).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="View QR", command=self.view_qr).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Save QR", command=self.save_qr).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Quit", command=root.quit).pack(side=tk.LEFT, padx=5)

        self.qr_image = None
        self.last_text = ""

    def generate_qr(self):
        text = self.input_text.get()
        if not text:
            messagebox.showwarning("Input Error", "Please enter text.")
            return
        save_qr_to_file(text)
        self.last_text = text
        messagebox.showinfo("Success", "QR Code saved as qr.png")

    def view_qr(self):
        if not self.last_text:
            messagebox.showwarning("No QR", "Generate a QR code first.")
            return
        img = generate_qr_image(self.last_text)
        self.qr_image = ImageTk.PhotoImage(img)
        top = tk.Toplevel(self.root)
        top.title("QR Preview")
        tk.Label(top, image=self.qr_image).pack()

    def save_qr(self):
        if not self.last_text:
            messagebox.showwarning("No QR", "Generate a QR code first.")
            return
        filepath = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Save QR Code"
        )
        if filepath:
            save_qr_to_file(self.last_text, filename=filepath)
            messagebox.showinfo("Saved", f"QR Code saved to:\n{filepath}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()
