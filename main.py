from tkinter import *
from tkcalendar import Calendar

gui = Tk(className='Airbnb Data')
# set window size
gui.geometry("500x500")

options = ["Santa Monica","Hollywood","Venice Beach"]
dropMen = StringVar()
dropMen.set("Santa Monica")
drop = OptionMenu(gui,dropMen,*options)
drop.pack()

min_text = Label(gui, text = "Enter Minimum Price")
min_text.pack()
min_price = Scale(gui,from_=50,to=300,orient=HORIZONTAL)
min_price.pack()

max_text = Label(gui, text = "Enter Maximum Price")
max_text.pack()
max_price = Scale(gui,from_=50,to=300,orient=HORIZONTAL)
max_price.pack()

bed_text = Label(gui, text = "Enter Num of Desired Beds")
bed_text.pack()
num_bed = Scale(gui,from_=1,to=10,orient=HORIZONTAL)
num_bed.pack()

bath_text = Label(gui, text = "Enter Num of Desired Baths")
bath_text.pack()
num_bath = Scale(gui,from_=1,to=10,orient=HORIZONTAL)
num_bath.pack()

menu = Menu(gui)
gui.config(menu=menu)
backMenu = Menu(menu)
menu.add_cascade(label="Back",menu=backMenu)
backMenu.add_command(label="Back to Filters")


cal = Calendar(gui,selectmode='day',year=2023,month=1,day=1)
cal.pack(pady=20)
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
# Add Button and Label
Button(gui, text = "Get Date",
command = grad_date).pack(pady = 20)
date = Label(gui, text = "")
date.pack(pady = 20)

gui.mainloop() 