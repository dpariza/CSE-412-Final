from tkinter import *
from tkcalendar import Calendar

gui = Tk(className='Airbnb Data')
# set window size
gui.geometry("500x1000")


def save_selection(value):
    neighborhood=value
    print(neighborhood)


options = ["Santa Monica", "Hollywood", "Venice Beach"]
dropMen = StringVar()
dropMen.set("Santa Monica")
drop = OptionMenu(gui, dropMen, *options, command=save_selection)
drop.pack()

min_text = Label(gui, text="Enter Minimum Price")
min_text.pack()
min_price = Scale(gui, from_=50, to=300, orient=HORIZONTAL)
min_price.pack()

max_text = Label(gui, text="Enter Maximum Price")
max_text.pack()
max_price = Scale(gui, from_=50, to=300, orient=HORIZONTAL)
max_price.pack()

bed_text = Label(gui, text="Enter Num of Desired Beds")
bed_text.pack()
num_bed = Scale(gui, from_=1, to=10, orient=HORIZONTAL)
num_bed.pack()

bath_text = Label(gui, text="Enter Num of Desired Baths")
bath_text.pack()
num_bath = Scale(gui, from_=1, to=10, orient=HORIZONTAL)
num_bath.pack()

menu = Menu(gui)
gui.config(menu=menu)
backMenu = Menu(menu)
menu.add_cascade(label="Back", menu=backMenu)
backMenu.add_command(label="Back to Filters")

start_text = Label(gui, text="Enter Starting Date")
start_text.pack()
cal1 = Calendar(gui, selectmode='day', year=2023, month=1, day=1)
cal1.pack(pady=20)

end_text = Label(gui, text="Enter Ending Date")
end_text.pack()
cal2 = Calendar(gui, selectmode='day', year=2023, month=1, day=1)
cal2.pack(pady=20)


def get():
    minimum=min_price.get()
    maximum=max_price.get()
    bed=num_bed.get()
    bath=num_bath.get()
    start_date = cal1.get_date()
    end_date = cal2.get_date()


# Add Button and Label
Button(gui, text="Save Filters", command=get).pack(pady=20)
date = Label(gui, text="")
date.pack(pady=20)

gui.mainloop()
