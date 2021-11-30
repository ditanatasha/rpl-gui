from tkinter import *
import time
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import os
from datetime import date, datetime, timedelta
import tugasdb as db
from importlib import reload

db.get_all_tugas()
row = db.all_tugas

root=Tk()
root.title('Timeline')
root.geometry("500x400")

frame_judul = LabelFrame(root, padx=50, pady=10)
frame_judul.pack(side=TOP)
timeline = Label(frame_judul, text="Timeline\n"+"September 2021")
timeline.pack(side=TOP)

main_frame=Frame(root,borderwidth = 4,width = 10, relief="ridge")
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)

my_scrollbar = ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
my_scrollbar.pack(side=BOTTOM, fill=X)

my_canvas.configure(xscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))

my_canvas.pack(side=LEFT, fill=BOTH, expand=True)

frame2 = Frame(my_canvas)
my_canvas.create_window((0,0), window=frame2,anchor="nw")

for i in range(32):
    Label(frame2,text=f'{i}', borderwidth = 4,width = 10, relief="groove").grid(row=0, column=i, padx=10,pady=10)
    for Tugas in row :
        year =Tugas.tenggat_waktu.year
        month = Tugas.tenggat_waktu.month
        day=Tugas.tenggat_waktu.day
        if (year==2021):
            if(month==9):
                if day==i :
                    Label(frame2,text=Tugas.nama_kegiatan +"\n"+Tugas.nama_tugas+"\n"+Tugas.status,borderwidth = 4,width = 10, relief="sunken",bg="blue",fg="white").grid(row=1, column=i, padx=10,pady=10)
         


root.mainloop()
