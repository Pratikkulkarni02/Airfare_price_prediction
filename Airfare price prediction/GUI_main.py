import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Airfare price prediction")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('1.png')
image2 = image2.resize((w,h), Image.Resampling.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)



#
label_l1 = tk.Label(root, text="Airfare \n price \n prediction",font=("Times New Roman", 35, 'bold'),
                    background="skyblue", fg="white", width=10, height=6)
label_l1.place(x=130, y=190)

# img = Image.open('logo.png')
# img = img.resize((100,70), Image.ANTIALIAS)
# logo_image = ImageTk.PhotoImage(img)

# logo_label = tk.Label(root, image=logo_image)
# logo_label.image = logo_image
# logo_label.place(x=40, y=10)


# img1 = Image.open('h2.jpg')
# img1 = img1.resize((750,600), Image.ANTIALIAS)
# logo_image1 = ImageTk.PhotoImage(img1)

# logo_label1 = tk.Label(root, image=logo_image1)
# logo_label1.image = logo_image1
# logo_label1.place(x=15, y=150)


# frame_alpr = tk.LabelFrame(root, text=" --Login & Register-- ", width=595, height=225, bd=5, font=('times', 14, ' bold '),bg="#E066FF")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=430, y=200)


# def Main():
#     from subprocess import call
#     call(["python","GUI_main.py"])
#     root.destroy()
    
  
def log():
    from subprocess import call
    call(["python","Log.py"])
    root.destroy()

def reg():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()
    
    
def window():
    root.destroy()
    
    
    # For Buttons on frame
    
    
button1 = tk.Button(root, text="Login", command=log, width=11, height=1,font=('times', 15, ' bold '), bg="white", fg="black")
button1.place(x=20, y=90)
def on_enter(e):
  button1['background'] = '#FF7D40'

def on_leave(e):
  button1['background'] = '#3CB371'

button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

button2 = tk.Button(root, text="Registration",command=reg,width=11, height=1,font=('times', 15, ' bold '), bg="white", fg="black")
button2.place(x=200,y=90)
def on_enter(e):
  button2['background'] = '#FF7D40'

def on_leave(e):
  button2['background'] = '#3CB371'

button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)

# button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times',15, ' bold '), bg="#8470FF", fg="white")
# button3.place(x=140, y=150)
# def on_enter(e):
#   button3['background'] = '#EEC900'

# def on_leave(e):
#   button3['background'] = '#8470FF'

# button3.bind("<Enter>", on_enter)
# button3.bind("<Leave>", on_leave)

    # For Buttons on label
    
# button1 = tk.Button(label_l1, text="LOGIN", command=con, width=12, height=1,font=('times 15 bold underline'),bd=0, bg="brown", fg="white")
# button1.place(x=1190, y=50)

# button2 = tk.Button(label_l1, text="REGISTER",command=reg,width=12, height=1,font=('times 15 bold underline'), bd=0,bg="brown", fg="white")
# button2.place(x=1310, y=50)

# button4 = tk.Button(label_l1, text="EXIT", command=con, width=10, height=1,font=('times 15 bold underline'),bd=0,bg="brown", fg="white")
# button4.place(x=1430, y=50)




label_l1 = tk.Label(root, text="**Airfare price prediction @2023 By **",font=("Times New Roman", 10, 'bold'),
                    background="black", fg="white", width=60, height=2)
label_l1.place(x=50, y=600)




root.mainloop()