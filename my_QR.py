import qrcode
from tkinter import *

# CREATE MAIN WINDOW
root = Tk()
root.title('QR Code Generator')
root.geometry('700x700')
root.config(bg='Gray40')



# FUNCTION TO GENERATE QRcode AND SAVE IT
def generateCode():
    return



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



# RUN TILL CLOSED
root.mainloop()