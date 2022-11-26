import tkinter as tk
from tkcalendar import Calendar
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO

#IN DBMS listings TABLE, NEIGHBORHOOD AND DESC ARE SWAPPED

gui =tk.Tk(className="LA Airbnb Search")
gui.geometry("850x500")

filter=tk.Frame(gui)
filter.grid(row=0, column=0, sticky='news')
display=tk.Frame(gui)
display.grid(row=0, column=0, sticky='news')

canvas = tk.Canvas(filter, width=500, height=500)
canvas.grid(columnspan=100, rowspan=100)
def change_to_filter():
    print("change to filter")
    filter.tkraise()

def change_to_display():
    print("change to display")
    display.tkraise()

def save_selection(value):
    neighborhood=value
    print(neighborhood)


options = ["Hollywood", "Venice", "Long Beach", "Newport Beach", "Santa Monica", "West Hollywood", "Anaheim", "Downtown", "Irvine"]
dropMen = tk.StringVar()
dropMen.set("Santa Monica")
drop = tk.OptionMenu(filter, dropMen, *options, command=save_selection)
drop.grid(column=50, row=0)


min_text = tk.Label(filter, text="Minimum Price:")
min_text.grid(column=0, row=5)
min_price = tk.Scale(filter, from_=50, to=300, orient=tk.HORIZONTAL)
min_price.grid(column=1, row=5)

max_text = tk.Label(filter, text="Maximum Price:")
max_text.grid(column=0, row=10)
max_price = tk.Scale(filter, from_=50, to=300, orient=tk.HORIZONTAL)
max_price.grid(column=1, row=10)

bed_text = tk.Label(filter, text="Beds:")
bed_text.grid(column=99, row=5)
num_bed = tk.Scale(filter, from_=1, to=10, orient=tk.HORIZONTAL)
num_bed.grid(column=100, row=5)

bath_text = tk.Label(filter, text="Bathrooms:")
bath_text.grid(column=99, row=10)
num_bath = tk.Scale(filter, from_=1, to=10, orient=tk.HORIZONTAL)
num_bath.grid(column=100, row=10)


start_text = tk.Label(filter, text="Enter Starting Date")
start_text.grid(column=1, row=90)
cal1 = Calendar(filter, selectmode='day', year=2023, month=1, day=1)
cal1.grid(column=1, row=91)

end_text = tk.Label(filter, text="Enter Ending Date")
end_text.grid(column=99, row=90)
cal2 = Calendar(filter, selectmode='day', year=2023, month=1, day=1)
cal2.grid(column=99, row=91)





def get():
    minimum=min_price.get()
    maximum=max_price.get()
    bed=num_bed.get()
    bath=num_bath.get()
    start_date = cal1.get_date()
    end_date = cal2.get_date()


# Add Button and Label
tk.Button(filter, text="Save Filters", command=get).grid(column=50, row=95)
#date = tk.Label(gui, text="")
#date.grid(column=99, row=99)


menubar = tk.Menu(gui)
menu = tk.Menu(menubar)
menu.add_command(label="Listings", command=lambda: change_to_display())
menu.add_command(label="Filters", command=lambda: change_to_filter())
menu.add_command(label="Quit", command=gui.quit)
menubar.add_cascade(label="Menu", menu=menu)
menu = tk.Menu(menubar)
gui.config(menu=menubar)

img_url = "https://a0.muscache.com/pictures/1170205/e259632f_original.jpg"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
panel = tk.Label(display, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

display.tkraise()
gui.mainloop()