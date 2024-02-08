import qrcode
from tkinter import *

# CREATE MAIN WINDOW
root = Tk()
root.title('QR Code Generator')
root.geometry('700x700')
root.config(bg='Gray40')



# FUNCTION TO GENERATE QRcode AND SAVE IT
def generateCode():
    qr = qrcode.QRCode(version=qr_size_textbox.get(), box_size=10, border=5)  # creating a QRcode of specified size
    qr_data = qr.add_data(getURL_textbox.get())                 # adding data to be encoded to the QRCode
    qr_creation = qr.make(fit=True)                             # making the entire QRcode space utilized
    qr_img_generation = qr.make_image()                         # generating the QRcode
    qr_fileDirectory = qr_location_textbox.get() + '\\' + qr_name_textbox.get()  # getting the directory to be save
    qr_img_generation.save(f'{qr_fileDirectory}.png')           # saving the QRcode
    


# LABEL FOR WINDOW
title_Label = Label(root, text = "Generate QR Code")
title_Label.pack()



# INPUT TEXT/URL TO GET QRcode
getURL_Label = Label(root, text="Enter the text/URL: ")
getURL_Label.pack()
getURL_textbox = Entry(root)
getURL_textbox.pack()



# GETTING INPUT OF SIZE OF QRcode
qr_size_Label = Label(root, text="Size from 1 to 40 with 1 being 21x21: ")
qr_size_Label.pack()
qr_size_textbox = Entry(root)
qr_size_textbox.pack()



# GETTING INPUT OF LOCATION TO SAVE QRcode
qr_location_Label = Label(root, text="Location to save the QR Code: ")
qr_location_Label.pack()
qr_location_textbox = Entry(root)
qr_location_textbox.pack()



# GETTING INPUT OF QRcode IMAGE NAME
qr_name_Label = Label(root, text="Name of the QR Code: ")
qr_name_Label.pack()
qr_name_textbox = Entry(root)
qr_name_textbox.pack()



# RUN TILL CLOSED
root.mainloop()