import pyqrcode
import png
from pyqrcode import QRCode

s = input("Enter the URL/TEXT for QRCode...\n")

url = pyqrcode.create(s)

url.svg("ResultQR.svg", scale = 8)

url.png("ResultQR.png", scale =6)
