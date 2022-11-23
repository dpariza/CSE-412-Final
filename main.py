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

price = Scale(gui,from_=50,to=300,orient=HORIZONTAL)
price.pack()

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