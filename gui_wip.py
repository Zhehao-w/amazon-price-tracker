#GUI CODE STARTS BELOW:
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from PIL import Image, ImageTk


def next():
    product_win = Toplevel()
    product_win.title("Amazon Price Traker")
    product_win.geometry('1200x1000')
    
    image1 = Image.open('AMAZON.png')
    logo = ImageTk.PhotoImage(image1)
    photo = Label(window, image=logo)
    photo.pack()

    show1 = Label(product_win, text="Product Information Form", font=("Helvetica Bold", 16))
    show1.pack()



window = Tk()
window.title("Amazon Price Traker")
window.geometry('1200x1000')

image = Image.open('AMAZON.png')
display = ImageTk.PhotoImage(image)
label = Label(window, image=display)
label.pack()

lbl = Label(window, text="Welcome! Let us help you track your desire products!", font=("Helvetica Bold", 14))
lbl.pack()


# User's email address text box
label1 = Label(window, text="\n\nEnter your email address:", font=("Helvetica", 12))
label1.pack()
e1 = Entry(window,width=30)
e1.pack()

# products number drop-down box
label2 = Label(window, text="\n\nHow many products you want to track:", font=("Helvetica", 12))
label2.pack()
e2 = Entry(window,width=30)
e2.pack()


next_button = Button(window, text="Next", command = next)
next_button.pack()

 
window.mainloop()

