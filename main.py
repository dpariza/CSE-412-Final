import tkinter as tk
from tkcalendar import Calendar
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
from dbms import execute_query

# IN DBMS listings TABLE, NEIGHBORHOOD AND DESC ARE SWAPPED

# Defaults
minimum_bool, maximum_bool, bed_bool, accom_bool, dates_bool = True, True, True, True, True

gui = tk.Tk(className="LA Airbnb Search")
gui.geometry("1100x500")

filters = tk.Frame(gui)
filters.grid(row=0, column=0, sticky='news')

listings = tk.Frame(gui)
listings.grid(row=0, column=0, sticky='news')

canvas = tk.Canvas(filters, width=500, height=500)
canvas.grid(columnspan=100, rowspan=100)


def change_to_filter():
    filters.tkraise()


def change_to_listings():
    listings.tkraise()


def save_selection(value):
    neighborhood = value
    print(neighborhood)


def check_min():
    global minimum_bool
    if check1.get() == 1:
        min_price['state'] = 'disabled'
        minimum_bool = False
    else:
        min_price['state'] = 'normal'
        minimum_bool = True


def check_max():
    global maximum_bool
    if check2.get() == 1:
        max_price['state'] = 'disabled'
        maximum_bool = False
    else:
        max_price['state'] = 'normal'
        maximum_bool = True


def check_beds():
    global bed_bool
    if check3.get() == 1:
        num_bed['state'] = 'disabled'
        bed_bool = False
    else:
        num_bed['state'] = 'normal'
        bed_bool = True


def check_accom():
    global accom_bool
    if check4.get() == 1:
        num_accom['state'] = 'disabled'
        accom_bool = False
    else:
        num_accom['state'] = 'normal'
        accom_bool = True


def check_dates():
    global dates_bool
    if check5.get() == 1:
        cal1['state'] = 'disabled'
        cal2['state'] = 'disabled'
        dates_bool = False
    else:
        cal1['state'] = 'normal'
        cal2['state'] = 'normal'
        dates_bool = True


options = ["All Neighborhoods", "Hollywood", "Venice", "Long Beach", "Newport Beach", "Santa Monica", "West Hollywood",
           "Anaheim", "Downtown", "Irvine"]
dropMen = tk.StringVar()
dropMen.set("All Neighborhoods")
drop = tk.OptionMenu(filters, dropMen, *options, command=save_selection)
drop.grid(column=50, row=0)

# Min price scale
min_text = tk.Label(filters, text="Minimum Price:")
min_text.grid(column=0, row=5)
min_price = tk.Scale(filters, from_=50, to=300, orient=tk.HORIZONTAL)
min_price.grid(column=1, row=5)
check1 = tk.IntVar()
c1 = tk.Checkbutton(filters, text='No Minimum', variable=check1, onvalue=1, offvalue=0, command=check_min)
c1.grid(column=2, row=5)

# Max price scale
max_text = tk.Label(filters, text="Maximum Price:")
max_text.grid(column=0, row=10)
max_price = tk.Scale(filters, from_=50, to=300, orient=tk.HORIZONTAL)
max_price.grid(column=1, row=10)
check2 = tk.IntVar()
c2 = tk.Checkbutton(filters, text='No Maximum', variable=check2, onvalue=1, offvalue=0, command=check_max)
c2.grid(column=2, row=10)

# Num beds scale
bed_text = tk.Label(filters, text="Beds:")
bed_text.grid(column=98, row=5)
num_bed = tk.Scale(filters, from_=1, to=10, orient=tk.HORIZONTAL)
num_bed.grid(column=99, row=5)
check3 = tk.IntVar()
c3 = tk.Checkbutton(filters, text='Any Number of Beds', variable=check3, onvalue=1, offvalue=0, command=check_beds)
c3.grid(column=100, row=5)

# Num accom scale
accom_text = tk.Label(filters, text="Accommodates:")
accom_text.grid(column=98, row=10)
num_accom = tk.Scale(filters, from_=1, to=10, orient=tk.HORIZONTAL)
num_accom.grid(column=99, row=10)
check4 = tk.IntVar()
c4 = tk.Checkbutton(filters, text='Any Number of Guests', variable=check4, onvalue=1, offvalue=0, command=check_accom)
c4.grid(column=100, row=10)

# Checkin calendar
start_text = tk.Label(filters, text="Enter Check-in Date:")
start_text.grid(column=1, row=50)
cal1 = Calendar(filters, selectmode='day', year=2023, month=1, day=1)
cal1.grid(column=1, row=51)

# Checkout calendar
end_text = tk.Label(filters, text="Enter Check-out Date:")
end_text.grid(column=99, row=50)
cal2 = Calendar(filters, selectmode='day', year=2023, month=1, day=1)
cal2.grid(column=99, row=51)

# Availability checkbox
check5 = tk.IntVar()
c5 = tk.Checkbutton(filters, text='Any Availability', variable=check5, onvalue=1, offvalue=0, command=check_dates)
c5.grid(column=50, row=50)


def get():
    if minimum_bool:
        minimum = min_price.get()
    else:
        minimum = None

    if maximum_bool:
        maximum = max_price.get()
    else:
        maximum = None

    if bed_bool:
        bed = num_bed.get()
    else:
        bed = None

    if accom_bool:
        accom = num_accom.get()
    else:
        accom = None

    if dates_bool:
        start_date = cal1.get_date()
        end_date = cal2.get_date()
    else:
        start_date = None
        end_date = None

    neighborhood = dropMen.get()

    # my_results = execute_query(minimum, maximum, bed, accom, neighborhood, start_date, end_date)
    # print(my_results[0][0])
    # build_listings(my_results)


def build_listings(result_dict):
    print('hi')

tk.Button(filters, text="Search for Listings", command=get).grid(column=50, row=95)

filters.tkraise()
gui.mainloop()
