from tkinter import *
def Train():
    """GUI"""
from tkinter import *
from tkinter import ttk 
import tkinter as tk
import numpy as np
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from PIL import Image, ImageTk

root = tk.Tk()


w, h = root.winfo_screenwidth(), root.winfo_screenheight( )
root.geometry("%dx%d+0+0" % (w, h))
root.title("Airfare price prediction")
root.configure(background="skyblue")

Gender = tk.IntVar()
Bookingday = tk.IntVar()
Bookingmonth = tk.IntVar()
Journeyday = tk.IntVar()
Journeymonth = tk.IntVar()
Airlineclass = tk.StringVar()
Departuretime = tk.DoubleVar()
Arrivaltime = tk.DoubleVar()
Source = tk.StringVar()
Destination = tk.StringVar()
TotalStops = tk.StringVar()


    
    #===================================================================================================================
def Detect():
    e1=Gender.get()
    print(e1)
    
    e2=Bookingday.get()
    print(e2)
   
    e3=Bookingmonth.get()
    print(e3)
    
    
    e4=Journeyday.get()
    print(e4)
    
    e5=Journeymonth.get()
    print(e5)
    
    e6=Airlineclass.get()
    if e6=="SpiceJet":
        e6=1
    elif e6=="Indigo":
        e6=2
    elif e6=="GO FIRST":
        e6=3
    elif e6=="Air India":
        e6=4
    elif e6=="Air Asia":
        e6=5
    else: 
        e6=6
    print(e6)
    
    e7=Departuretime.get()
    print(e7)
    
    e8=Arrivaltime.get()
    print(e8)
    
    e9=Source.get()
    if e9=="Chennai":
        e9=1
    elif e9=="Delhi":
        e9=2
    elif e9=="Kolkata":
        e9=3
    elif e9=="Mumbai":
        e9=4
    elif e9=="Cochin":
        e9=5
    elif e9=="Hyderabad":
        e9=6
    else: 
        e9=7
    print(e9)
    
    e10=Destination.get()
    if e10=="Chennai":
        e10=1
    elif e10=="Delhi":
        e10=2
    elif e10=="Kolkata":
        e10=3
    elif e10=="Mumbai":
        e10=4
    elif e10=="Cochin":
        e10=5
    elif e10=="Hyderabad":
        e10=6
    else: 
        e10=7
    print(e10)
    
    e11=TotalStops.get()
    if e11=="non stop":
        e11=0
    elif e11=="one stop":
        e11=1
    else: 
        e11=2
    print(e11)
    
 
   
   
     
        
        
#########################################################################################
    from joblib import dump , load
    a1=load('airfaremodel5.joblib')
    v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11]])
    print(v)
    yes = tk.Label(root,text="Predict Price :"  +'\n'+ str(v),background="blue",foreground="white",font=('times', 20, ' bold '),width=30)
    yes.place(x=700,y=590)
   
 

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 = Image.open('GettyImages-1237164836-rental-housing-costs-prices-property-real-estate-renting-inequality-1120.jpg')
# image2 = image2.resize((w,h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

        
        
#########################################################################################
    
    

# frame_alpr = tk.LabelFrame(root, text=" --Form-- ", width=800, height=600, bd=5, font=('times', 14, ' bold '),fg="white",bg="#607B8B")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=450, y=200)


frame_alpr1 = tk.LabelFrame(root, text="Booking Date", width=230, height=130, bd=5, font=('times', 14, ' bold '),fg="blue",bg="skyblue")
frame_alpr1.grid(row=0, column=0, sticky='nw')
frame_alpr1.place(x=350, y=80)

l1=tk.Label(frame_alpr1,text="DAY",background="skyblue",font=('times', 10, ' bold '),width=15)
l1.place(x=1,y=1)
DateofBooking=tk.Entry(frame_alpr1,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Bookingday)
DateofBooking.place(x=15,y=25)


l2=tk.Label(frame_alpr1,text="MONTH",background="skyblue",font=('times', 10, ' bold '),width=15)
l2.place(x=100,y=1)
DateofJourney=tk.Entry(frame_alpr1,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Bookingmonth)
DateofJourney.place(x=120,y=25)



frame_alpr2 = tk.LabelFrame(root, text="Journey Date", width=230, height=130, bd=5, font=('times', 14, ' bold '),fg="blue",bg="skyblue")
frame_alpr2.grid(row=0, column=0, sticky='nw')
frame_alpr2.place(x=630, y=80)
              
l1=tk.Label(frame_alpr2,text="DAY",background="skyblue",font=('times', 10, ' bold '),width=15)
l1.place(x=1,y=1)
DateofBooking=tk.Entry(frame_alpr2,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Journeyday)
DateofBooking.place(x=15,y=25)

l2=tk.Label(frame_alpr2,text="MONTH",background="skyblue",font=('times', 10, ' bold '),width=15)
l2.place(x=100,y=1)
DateofJourney=tk.Entry(frame_alpr2,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Journeymonth)
DateofJourney.place(x=120,y=25)



l1=tk.Label(root,text="gender",background="darkolivegreen1",font=('times', 20, ' bold '),width=15)
l1.place(x=400,y=240)
tk.Radiobutton(root, text="Male", padx=5, width=5, bg="snow", font=("bold", 15), variable=Gender, value=1).place(x=700,
                                                                                                                y=240)
tk.Radiobutton(root, text="Female", padx=20, width=4, bg="snow", font=("bold", 15), variable=Gender, value=2).place(
    x=800, y=240)



l4=tk.Label(root,text="Departure Time",background="darkolivegreen1",font=('times', 20, ' bold '),width=15)
l4.place(x=400,y=290)
DepartureTime=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Departuretime)
DepartureTime.place(x=700,y=290)


l4=tk.Label(root,text="Arrival Time",background="darkolivegreen1",font=('times', 20, ' bold '),width=15)
l4.place(x=400,y=340)
ArrivalTime=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Arrivaltime)
ArrivalTime.place(x=700,y=340)

l3=tk.Label(root,text="Airline-Class",background="darkolivegreen1",font=('times', 20, ' bold '),width=15)
l3.place(x=400,y=390)
monthchoosen= ttk.Combobox(root, width = 27, textvariable = Airlineclass)
# Adding combobox drop down list
monthchoosen['values'] = (' SpiceJet',
						' Indigo',
						' GO FIRST',
                        'Air India',
                        'Air Asia',
                        'Vistara')
monthchoosen.place(x=700,y=390)
#monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()

l3=tk.Label(root,text="Source",background="darkolivegreen1",font=('times', 20, ' bold '),width=15)
l3.place(x=400,y=440)
monthchoosen= ttk.Combobox(root, width = 27, textvariable = Source)
# Adding combobox drop down list
monthchoosen['values'] = (' Chennai',
						' Delhi',
						' Kolkata',
                        'Mumbai',
                        'cochin',
                        'Hyderabad',
                        'New Delhi')
monthchoosen.place(x=700,y=440)
#monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()

l3=tk.Label(root,text="Destination",background="darkolivegreen1",font=('times', 20, ' bold '),width=15)
l3.place(x=400,y=490)
monthchoosen= ttk.Combobox(root, width = 27, textvariable = Destination)
# Adding combobox drop down list
monthchoosen['values'] = (' Chennai',
						' Delhi',
						' Kolkata',
                        'Mumbai',
                        'cochin',
                        'Hyderabad',
                        'New Delhi')
monthchoosen.place(x=700,y=490)
#monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()


l11=tk.Label(root,text="Total Stops",background="darkolivegreen1",font=('times', 20, ' bold '),width=15)
l11.place(x=400,y=540)
monthchoosen = ttk.Combobox(root, width = 27, textvariable = TotalStops)
# Adding combobox drop down list
monthchoosen['values'] = (' non stop',
						' one stop',
                        'two stop',
						)
monthchoosen.place(x=700,y=540)
#monthchoosen.grid(column = 1, row = 5)
monthchoosen.current()


button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
button1.place(x=400,y=590)

# button1 = tk.Button(root,text="Chance of Admit ",command=Detect1,font=('times', 20, ' bold '),width=15)
# button1.place(x=500,y=600)


root.mainloop()
            
Train()

        
       
          



    
    
    