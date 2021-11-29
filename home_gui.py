from tkinter import *
import time
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import csv
import os

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
#root['bg'] = '#AC99F2'
root.resizable(0, 0)

Top = Frame(root, width=900, height=20 ,bd=5)
Top.pack(side=TOP)
Time = Frame(Top)
Time.pack(side=RIGHT)
User = Frame(Top)
User.pack(side=LEFT)
Title = Frame(root)
Title.pack()
Button1 = Frame(root, bd=30)
Button1.pack()
Button2 = Frame(Button1)
Button2.pack(side=BOTTOM)

def swap_Text():
    lab['text'] = time.asctime()
    root.after(1000, swap_Text)

lab = Label(Top, text='0', font=("arial bold", 10), anchor=E)
lab.pack(side=RIGHT)
swap_Text()

Label_User = Label(Top, text="Hello!", font=("Helvetica", 10), anchor=W)
Label_User.pack(side=LEFT)

txt_title = Label(Top, width=900, font=('Helvetica', 16),text = "")
txt_title.pack()

Label_Welcome = Label(Title, text="WELCOME TO TSM", font=("Helvetica", 22))
Label_Welcome.pack()
Menu1 = Button(Button1, height =2, width = 40, text="Kegiatan", font=("Arial", 15), bg='white', fg="Black")
Menu1.pack(pady=3)
Menu2 = Button(Button1, height =2, width = 40, text="Tugas", font=("Arial", 15), bg='white', fg="Black")
Menu2.pack(pady=3)
Menu3 = Button(Button1, height =2, width = 40, text="Timeline", font=("Arial", 15), bg='white', fg="Black")
Menu3.pack(pady=3)
Menu4 = Button(Button1, height =2, width = 40, text="Penilaian", font=("Arial", 15), bg='white', fg="Black")
Menu4.pack(pady=3)
Exit = Button(Button2, height =1, width = 15, text="Close", font=("Arial", 15), bg='white', fg="Black")
Exit.pack(side=LEFT, pady =10, padx=50)
LogOut = Button(Button2, height =1, width = 15, text="Log Out", font=("Arial", 15), bg='white', fg="Black")
LogOut.pack(side=LEFT, padx=50)

Label_Closing = Label(root, text="Made with love by G17 RPL STI 2021/22", bd=8)
Label_Closing.pack(side=BOTTOM)
