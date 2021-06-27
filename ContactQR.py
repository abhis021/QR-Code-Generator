# import main
import sys


def ContactDetails():
    temp_list = [2000]
    print("Contact QR Creator")
    s = input("First Name: \n").split()
    temp_list.append(s)
    s = input("Last Name: \n").split()
    temp_list.append(s)
    s = input("Organization: \n").split()
    temp_list.append(s)
    s = input("Email: \n").split()
    temp_list.append(s)
    s = input("Phone: \n").split()
    temp_list.append(s)
    s = input("Cell: \n").split()
    temp_list.append(s)
    s = input("Fax: \n").split()
    temp_list.append(s)
    s = input("Street: \n").split()
    temp_list.append(s)
    s = input("ZIP/PIN: \n").split()
    temp_list.append(s)
    s = input("City: \n").split()
    temp_list.append(s)
    s = input("Region/State: \n").split()
    temp_list.append(s)
    s = input("Country: \n").split()
    temp_list.append(s)
    s = input("URL/Website: \n").split()
    temp_list.append(s)
    print(temp_list)
    print("Is this content Correct? Y/N \n")
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n'}
    choice = input().lower()
    if choice in yes:
        breakpoint
    elif choice in no:
        ContactDetails()
    else:
        print("Please respond with y/n or yes/no")
ContactDetails()