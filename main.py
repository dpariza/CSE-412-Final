import tkinter as tk
from tkcalendar import Calendar

#IN DBMS listings TABLE, NEIGHBORHOOD AND DESC ARE SWAPPED

gui =tk.Tk(className="LA Airbnb Search")

canvas = tk.Canvas(gui, width=500, height=500)
canvas.grid(columnspan=100, rowspan=100)

def save_selection(value):
    neighborhood=value
    print(neighborhood)


options = ["Hollywood", "Venice", "Long Beach", "Newport Beach", "Santa Monica", "West Hollywood", "Anaheim", "Downtown", "Irvine"]
dropMen = tk.StringVar()
dropMen.set("Santa Monica")
drop = tk.OptionMenu(gui, dropMen, *options, command=save_selection)
drop.grid(column=50, row=0)


min_text = tk.Label(gui, text="Minimum Price:")
min_text.grid(column=0, row=5)
min_price = tk.Scale(gui, from_=50, to=300, orient=tk.HORIZONTAL)
min_price.grid(column=1, row=5)

max_text = tk.Label(gui, text="Maximum Price:")
max_text.grid(column=0, row=10)
max_price = tk.Scale(gui, from_=50, to=300, orient=tk.HORIZONTAL)
max_price.grid(column=1, row=10)

bed_text = tk.Label(gui, text="Beds:")
bed_text.grid(column=99, row=5)
num_bed = tk.Scale(gui, from_=1, to=10, orient=tk.HORIZONTAL)
num_bed.grid(column=100, row=5)

bath_text = tk.Label(gui, text="Bathrooms:")
bath_text.grid(column=99, row=10)
num_bath = tk.Scale(gui, from_=1, to=10, orient=tk.HORIZONTAL)
num_bath.grid(column=100, row=10)

menu = tk.Menu(gui)
gui.config(menu=menu)
backMenu = tk.Menu(menu)
menu.add_cascade(label="Back", menu=backMenu)
backMenu.add_command(label="Back to Filters")

start_text = tk.Label(gui, text="Enter Starting Date")
start_text.grid(column=1, row=90)
cal1 = Calendar(gui, selectmode='day', year=2023, month=1, day=1)
cal1.grid(column=1, row=91)

end_text = tk.Label(gui, text="Enter Ending Date")
end_text.grid(column=99, row=90)
cal2 = Calendar(gui, selectmode='day', year=2023, month=1, day=1)
cal2.grid(column=99, row=91)


def get():
    minimum=min_price.get()
    maximum=max_price.get()
    bed=num_bed.get()
    bath=num_bath.get()
    start_date = cal1.get_date()
    end_date = cal2.get_date()


# Add Button and Label
tk.Button(gui, text="Save Filters", command=get).grid(column=50, row=95)
#date = tk.Label(gui, text="")
#date.grid(column=99, row=99)

gui.mainloop()