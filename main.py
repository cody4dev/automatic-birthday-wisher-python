import pywhatkit
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageOps, ImageDraw, ImageFont
import textwrap
from datetime import datetime
import json

# read json file
birthdays = open('birthdays.json', 'r')
birthdaydata = birthdays.read()
# print(birthdaydata)

# parse json data
birthdayobj = json.loads(birthdaydata)
# print(birthdayobj['birthdays'])

# [0].get("dob_date")

currentMonth = datetime.now().month
currentDay = datetime.now().day

# print("Month - "+str(currentMonth))
# print("Day - "+str(currentDay))

# print(len(birthdayobj['birthdays']))

# wish functionality


def wish(i):
    print(i)
    ImageOps.expand(Image.open(i.get("image")), border=(300, 150),
                    fill='white').save('img/birthday_wish.png')

    ImageOps.pad(Image.open('img/birthday_wish.png'), (500, 700), method=Image.BICUBIC,
                 color='white', centering=(0, 0)).save('img/birthday_wish.png')

    opening_image = Image.open('img/birthday_wish.png')
    fnt = ImageFont.truetype("NanumPenScript-Regular.ttf", 28)

    text_image = ImageDraw.Draw(opening_image)

    new_text = i.get("caption")
    new_text_wrapped = textwrap.wrap(new_text, width=47)
    # print(new_text_wrapped)

    str = ""

    for i in new_text_wrapped:
        str += i
        str += '\n'

    text_image.text((55, 380), str, font=fnt, fill=(0, 0, 0))

    opening_image.save('img/birthday_wish.png')


def wishing():
    print("Wishing Function")


for i in birthdayobj['birthdays']:
    # print(i)
    if(currentMonth == i.get("dob_month") and currentDay == i.get("dob_date")):

        # Tkinter window
        window = Tk()
        window.geometry("300x200")
        window['background'] = '#856ff8'
        window.title("Birthday Wisher")

        # Label(window, text="Today's Birthday!",
        #       bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=W)

        label = tk.Label(window, text="Today Birthday",
                         fg="black", bg="#856ff8", font="none 12 bold")
        label.place(anchor='center', relx=.5, rely=.2)

        label = tk.Label(window, text=i.get("name"),
                         fg="black", font="none 14")
        label.place(anchor='center', relx=.5, rely=.4)

        btn = ttk.Button(window, text="Wish",
                         command=lambda: wish(i)).pack(side=BOTTOM, pady=20)

        print("There is a birthday")

        window.mainloop()
