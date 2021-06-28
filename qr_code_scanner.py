from tkinter import *
import pyqrcode
from PIL import ImageTk,Image


root =Tk()


def generate():
    link_name = name_entry.get()
    link = Link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name,scale=8)

    image= ImageTk.PhotoImage(Image.open(file_name)
                              )
    image_label = Label(image=image)

    image_label.image=image

    canvas.create_window(200,450,window=image_label)


canvas = Canvas(root,width=400,height=600)
canvas.pack()

app_label = Label(root,text="QR code generator",fg="blue",font=("Arial",30))
canvas.create_window(200,50,window=app_label)

name_label = Label(root,text="link Name")
Link_label = Label(root,text="Link")

name_entry = Entry(root)
Link_entry = Entry(root)

canvas.create_window(200,100,window=name_label)

canvas.create_window(200,160,window=Link_label)

canvas.create_window(200,130,window=name_entry)
canvas.create_window(200,180,window=Link_entry)
button = Button(text="generate qr code",command=generate)
canvas.create_window(200,230,window=button)

root.mainloop()