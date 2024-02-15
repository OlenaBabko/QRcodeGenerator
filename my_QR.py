import qrcode
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# CREATE MAIN WINDOW
root = Tk()
root.title('My_QR')
root.geometry('700x700')
root.config(bg='Gray40')


# ADD IMAGE
bg = PhotoImage(file="third_91.png")
bg_image = Label(root, image=bg)
bg_image.place(relwidth=1, relheight=1)                         # if use a .pack() this will not work as a bg




# FUNCTION TO GENERATE QRcode AND SAVE IT
def generateCode():
    qr = qrcode.QRCode(version=qr_size_textbox.get(), box_size=10, border=5)  # creating a QRcode of specified size
    qr_data = qr.add_data(getURL_textbox.get())                 # adding data to be encoded to the QRCode
    qr_creation = qr.make(fit=True)                             # making the entire QRcode space utilized
    qr_img_generation = qr.make_image()                         # generating the QRcode
    qr_fileDirectory = qr_location_textbox.get() + '\\' + qr_name_textbox.get()  # getting the directory to be save
    qr_img_generation.save(f'{qr_fileDirectory}.png')           # saving the QRcode
    satisfaction = satisfaction_value.get()
    messagebox.showinfo("QR Code Generator", "QR Code is saved successfully!")  # pop up message on saving the file



# LABEL FOR WINDOW
title_Label = Label(root, text = "Generate QR Code", font=('Times', 18, 'bold'))
title_Label.pack(pady=50)



# INPUT TEXT/URL TO GET QRcode
getURL_Label = Label(root, text="Enter the URL(text): ", fg='black', font=('Courier', 12, 'bold'))
getURL_Label.pack(anchor=CENTER, pady=10)
getURL_textbox = Entry(root)
getURL_textbox.pack(anchor=CENTER)



# GETTING INPUT OF SIZE OF QRcode
qr_size_Label = Label(root, text="Size from 1 to 40 (1=21x21): ", fg='black', font=('Courier', 12, 'bold'))
qr_size_Label.pack(anchor=CENTER, pady=10)
qr_size_textbox = Entry(root)
qr_size_textbox.pack(anchor=CENTER)



# GETTING INPUT OF LOCATION TO SAVE QRcode
qr_location_Label = Label(root, text="Location to save the QR Code: ", font=('Courier', 12, 'bold'))
qr_location_Label.pack(anchor=CENTER, pady=10)
qr_location_textbox = Entry(root)
qr_location_textbox.pack(anchor=CENTER)



# GETTING INPUT OF QRcode IMAGE NAME
qr_name_Label = Label(root, text="Name of the QR Code: ", font=('Courier', 12, 'bold'))
qr_name_Label.pack(anchor=CENTER, pady=10)
qr_name_textbox = Entry(root)
qr_name_textbox.pack(anchor=CENTER)



# CHECKBOX
satisfaction_value = IntVar()                           # uncheck=0 uncheck=1
satisfaction_checkbox = ttk.Checkbutton(root, text="I like your app!", variable=satisfaction_value)
satisfaction_checkbox.pack(anchor=CENTER, pady=10)



# BUTTON TO GENERATE AND SAVE QRcode
button = Button(root, text='Generate Code', font=('Courier', 13, 'bold'), command=generateCode)
button.place(relx=0.35, rely=0.9, relwidth=0.25, relheight=0.05)


# RUN TILL CLOSED
root.mainloop()