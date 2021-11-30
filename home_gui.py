from tkinter import *
import time
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import csv
import os
from subprocess import call

root = Tk()
root.title("Home")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.iconbitmap('sticker1.ico')
root['background'] = '#856ff8'
root.resizable(0, 0)

frame1=Frame(root, width=200, height=100, bg='#856ff8')
frame1.pack(fill=BOTH, side=LEFT, expand=True)

frame2 = Frame(root, width=100)
frame2.pack(fill=BOTH, side=LEFT, expand=True)

Top = Frame(frame2, width=600, height=20 ,bd=5)
Top.pack(side=TOP)
Time = Frame(Top)
Time.pack(side=RIGHT)
User = Frame(Top)
User.pack(side=LEFT)
Title = Frame(frame2, bd=3)
Title.pack()
Button1 = Frame(frame2, bd=20)
Button1.pack()
Button2 = Frame(Button1)
Button2.pack(side=BOTTOM)

def swap_Text():
    lab['text'] = time.asctime()
    root.after(1000, swap_Text)

def click_kegiatan():
    root.destroy()
    import kegiatan_gui
def click_tugas():
    root.destroy()
    import tugas_gui
def click_timeline():
    root.destroy()
    import timeline_gui
def click_penilaian():
    root.destroy()
    import penilaian_gui
def click_logout():
    root.destroy()
    import login


lab = Label(Top, text='0', font=("Helvetica", 10), anchor=E)
lab.pack(side=RIGHT)
swap_Text()

Label_User = Label(Top, text="Hello!", font=("Helvetica", 10), anchor=W)
Label_User.pack(side=LEFT)

txt_title = Label(Top, width=900, font=('Helvetica', 16),text = "")
txt_title.pack()

Label_Welcome = Label(Title, text="WELCOME TO TSM", font=("Helvetica", 22))
Label_Welcome.pack()
Menu1 = Button(Button1, height =2, width = 40, text="Kegiatan", relief=RIDGE, font=("Helvetica", 14), bg='white', fg="Black", command=click_kegiatan)
Menu1.pack(pady=3)
Menu2 = Button(Button1, height =2, width = 40, text="Tugas", relief=RIDGE, font=("Helvetica", 14), bg='white', fg="Black", command=click_tugas)
Menu2.pack(pady=3)
Menu3 = Button(Button1, height =2, width = 40, text="Timeline", relief=RIDGE, font=("Helvetica", 14), bg='white', fg="Black", command=click_timeline)
Menu3.pack(pady=3)
Menu4 = Button(Button1, height =2, width = 40, text="Penilaian", relief=RIDGE, font=("Helvetica", 14), bg='white', fg="Black", command=click_penilaian)
Menu4.pack(pady=3)
Exit = Button(Button2, height =1, width = 15, text="Close", relief=RIDGE, font=("Helvetica", 14), bg='white', fg="Black")
Exit.pack(side=LEFT, pady =10, padx=50)
LogOut = Button(Button2, height =1, width = 15, text="Log Out", relief=RIDGE, font=("Helvetica", 14), bg='white', fg="Black", command=click_logout)
LogOut.pack(side=LEFT, padx=50)

Label_Closing = Label(frame2, text="Made with love by G17 RPL STI 2021/22", bd=8, font=("Helvetica", 10))
Label_Closing.pack(side=BOTTOM)
