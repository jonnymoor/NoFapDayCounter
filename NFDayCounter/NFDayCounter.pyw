from tkinter import *
import datetime
import csv
import os

root = Tk()
root.title("NoFap: DayCounter")
root.iconbitmap("Strong.ico")
root.geometry("384x141")
root.configure(background='red')

current_date = datetime.date.today()

def check_ex():
    if os.path.isfile("lastfap.txt") == True:
        with open("lastfap.txt", "r") as file:
            file_contents = file.read()
            date_list = file_contents.split("/")
    
            fap_data = str(date_list[0] + date_list[1] + date_list[2])
            last_fap = datetime.datetime.strptime(fap_data, "%d%m%Y").date()
            day_number = (current_date - last_fap).days
    
            dd_entry.insert(0, date_list[0])
            mm_entry.insert(0, date_list[1])
            yyyy_entry.insert(0, date_list[2])
    
            #LOWER FRAME
            root.geometry("384x226")
            lo_frame = LabelFrame(root, padx=41, pady=20, bg='#00a825')
            lo_frame.grid(row=1, column=0, padx=2)
            
            you_are_on_text = Label(lo_frame, text="YOU ARE ON DAY %.2i!" %day_number, bg='#00a825', fg="white")
            you_are_on_text.config(font=("Ariel", 21, "bold"))
            you_are_on_text.grid(row=1, column=0)

#FUNCTIONALITY
def update():
    fap_date = str(dd_entry.get()[-2:] + mm_entry.get()[-2:] + yyyy_entry.get()[-4:]) # ! NEEDS TO BE MORE ROBUST ! #
    last_fap = datetime.datetime.strptime(fap_date, "%d%m%Y").date()
    day_number = (current_date - last_fap).days

    #LOWER FRAME
    root.geometry("384x226")
    lo_frame = LabelFrame(root, padx=41, pady=20, bg='#00a825')
    lo_frame.grid(row=1, column=0, padx=2)
    
    you_are_on_text = Label(lo_frame, text="YOU ARE ON DAY %.2i!" %day_number, bg='#00a825', fg="white")
    you_are_on_text.config(font=("Ariel", 21, "bold"))
    you_are_on_text.grid(row=1, column=0)

    #SAVE DATA
    file_name = "lastfap.txt"
    with open(file_name, "w") as file:
        file.write(fap_date[0:2] + "/" + fap_date[2:4] + "/" + fap_date[4:8])

#HIGHER FRAME
hi_frame = LabelFrame(root, padx=20, pady=11, bg='red')
hi_frame.grid(row=0, column=0, padx=2, pady=2)

last_fap_text = Label(hi_frame, text="YOUR LAST FAP WAS ON:", bg='red', fg='white')
last_fap_text.config(font=("Ariel", 12, "bold"))
last_fap_text.grid(row=1, column=0, padx=7, sticky=W)

dd_text = Label(hi_frame, text="DD", bg="red", fg="white")
dd_text.config(font=("Ariel", 8, "italic"))
dd_text.grid(row=0, column=1, padx=4, pady=3)
mm_text = Label(hi_frame, text="MM", bg="red", fg="white")
mm_text.config(font=("Ariel", 8, "italic"))
mm_text.grid(row=0, column=2, padx=5)
yyyy_text = Label(hi_frame, text="YYYY", bg="red", fg="white")
yyyy_text.config(font=("Ariel", 8, "italic"))
yyyy_text.grid(row=0, column=3, padx=7)

dd_entry = Entry(hi_frame, width=2, borderwidth=3, relief=RIDGE)
dd_entry.config(font=("bold"))
dd_entry.grid(row=1, column=1)
mm_entry = Entry(hi_frame, width=2, borderwidth=3, relief=RIDGE)
mm_entry.config(font=("bold"))
mm_entry.grid(row=1, column=2)
yyyy_entry = Entry(hi_frame, width=4, borderwidth=3, relief=RIDGE)
yyyy_entry.config(font=("bold"))
yyyy_entry.grid(row=1, column=3)
dd_entry.focus_set()

update_button = Button(hi_frame, text="Update", borderwidth=5, command=update, bg="red", fg="white")
update_button.grid(row=2, column=1, columnspan=3, pady=13, padx=1, ipadx=27)

check_ex()

root.mainloop()

