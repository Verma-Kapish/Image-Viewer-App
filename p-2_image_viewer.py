from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Gallery🖼️📷")

my_imagea = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/a.png"))
my_imageb = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/b.png"))
my_imagec = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/c.png"))
my_imaged = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/d.png"))
my_imagee = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/e.png"))
my_imagef = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/f.png"))
my_imageg = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/g.png"))
my_imageh = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/h.png"))
my_imagei = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/i.png"))
my_imagej = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/j.png"))
my_imagek = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/k.png"))
my_imagel = ImageTk.PhotoImage(Image.open("/Users/kapishverma/Documents/Coding/Images/l.png"))

image_list = [my_imagea, my_imageb, my_imagec, my_imaged,
              my_imagee, my_imagef, my_imageg, my_imageh,
              my_imagei, my_imagej, my_imagek, my_imagel]

label = Label(image=my_imagea)
label.grid(row=0, column=0, columnspan=3)

# Counter
counter = Label(root, text="1/" + str(len(image_list)))
counter.grid(row=2, column=0, columnspan=3)

# Next Function
def next(image_number):
    global label
    global button_next
    global button_back

    label.grid_forget()
    label = Label(root, image=image_list[image_number])

    button_next = Button(root, text=">>", command=lambda: next(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

    # Update counter
    counter.config(text=str(image_number + 1) + "/" + str(len(image_list)))

    if image_number == len(image_list) - 1:
        button_next = Button(root, text=">>", state=DISABLED)
        button_next.grid(row=1, column=2)

# Back Function
def back(image_number):
    global label
    global button_next
    global button_back

    label.grid_forget()
    label = Label(root, image=image_list[image_number])

    button_next = Button(root, text=">>", command=lambda: next(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

    # Update Counter
    counter.config(text=str(image_number + 1) + "/" + str(len(image_list)))

    if image_number == 0:
        button_back = Button(root, text="<<", state=DISABLED )
        button_back.grid(row=1, column=0)

# Initial Buttons
button_back = Button(root, text="<<", state=DISABLED)
button_next = Button(root, text=">>", command=lambda: next(1))
button_exit = Button(root, text="Exit Program", command=root.quit)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_next.grid(row=1, column=2)

root.mainloop()
