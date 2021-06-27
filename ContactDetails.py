import pandas as pd

fname = []
lname = []
org = []
email = []
phone = []
cell = []
fax = []
street = []
postal_code = []
city = []
region = []
country = []
website = []

s = input("First Name: \n").split()
fname.append(s)
s = input("Last Name: \n").split()
lname.append(s)
s = input("Organization: \n").split()
org.append(s)
s = input("Email: \n").split()
email.append(s)
s = input("Phone: \n").split()
phone.append(s)
s = input("Cell: \n").split()
cell.append(s)
s = input("Fax: \n").split()
fax.append(s)
s = input("Street: \n").split()
street.append(s)
s = input("ZIP/PIN: \n").split()
postal_code.append(s)
s = input("City: \n").split()
city.append(s)
s = input("Region/State: \n").split()
region.append(s)
s = input("Country: \n").split()
country.append(s)
s = input("URL/Website: \n").split()
website.append(s)


dict = {'First Name': fname, 'Last Name': lname, 'Email': email,
        'Phone': phone, 'City': city, 'Region': region, 'Country': country, 'Url': website}

df = pd.DataFrame(dict)

df.to_csv('contactdetails.csv')
print(s)
