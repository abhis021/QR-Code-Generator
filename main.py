import pyqrcode
import png
from pyqrcode import QRCode
from ContactQR import ContactDetails

url = pyqrcode.create(ContactDetails)

url.svg("ResultQR.svg", scale = 8)

url.png("ResultQR.png", scale =6)
