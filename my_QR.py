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
title_Label = Label(root, text = "Generate QR Code", font=('Times', 18, 'bold'))
title_Label.pack(pady=50)



# INPUT TEXT/URL TO GET QRcode
getURL_Label = Label(root, text="Enter the URL(text): ", fg='black', font=('Courier', 12, 'bold'))
getURL_Label.pack(anchor=CENTER, pady=10)
getURL_textbox = Entry(root)
getURL_textbox.pack()



# GETTING INPUT OF SIZE OF QRcode
qr_size_Label = Label(root, text="Size from 1 to 40 (1=21x21): ", fg='black', font=('Courier', 12, 'bold'))
qr_size_Label.pack(anchor=CENTER, pady=10)
qr_size_textbox = Entry(root)
qr_size_textbox.pack()



# GETTING INPUT OF LOCATION TO SAVE QRcode
qr_location_Label = Label(root, text="Location to save the QR Code: ", font=('Courier', 12, 'bold'))
qr_location_Label.pack(anchor=CENTER, pady=10)
qr_location_textbox = Entry(root)
qr_location_textbox.pack()



# GETTING INPUT OF QRcode IMAGE NAME
qr_name_Label = Label(root, text="Name of the QR Code: ", font=('Courier', 12, 'bold'))
qr_name_Label.pack(anchor=CENTER, pady=10)
qr_name_textbox = Entry(root)
qr_name_textbox.pack()



# BUTTON TO GENERATE AND SAVE QRcode
button = Button(root, text='Generate Code', font=('Courier', 13, 'bold'), command=generateCode)
button.place(relx=0.35, rely=0.9, relwidth=0.25, relheight=0.05)


# RUN TILL CLOSED
root.mainloop()