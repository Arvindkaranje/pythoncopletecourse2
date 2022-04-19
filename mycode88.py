from tkinter import *
import time

app_window=Tk()
app_window.title("Digital clock")
app_window.geometry("420150")
app_window.resizable(1,1)

text_font=("Bounder", 68, 'bold')
background="#f2e750"
foreground="#363529"
border_width= 25

label=Label(app_window, font=text_font, bg=background)
label.grid(row=0, column=1)

def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock())

digital_clock()
