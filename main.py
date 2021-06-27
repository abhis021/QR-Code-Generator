import pyqrcode
import png
from pyqrcode import QRCode
import pandas as pd
from ContactQR import ContactDetails
# import ContactQR
s = ContactDetails

url = pyqrcode.create(s)
# url = pyqrcode.create(ContactQR.ContactDetails)
# print(temp_list)
url.svg("ResultQR.svg", scale = 8)

url.png("ResultQR.png", scale =6)
