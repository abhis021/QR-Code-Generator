import pyqrcode
import png
from pyqrcode import QRCode
import pandas as pd
# s = pd.read_csv("contactdetails.csv")
# print(s)
# import ContactDetails
# from ContactQR import ContactDetails
# import ContactQR
s = input("Enter text to create qr:\n")

url = pyqrcode.create(s)
# url = pyqrcode.create(ContactQR.ContactDetails)
# print(temp_list)
url.svg("ResultQR.svg", scale = 8)

url.png("ResultQR.png", scale =6)
