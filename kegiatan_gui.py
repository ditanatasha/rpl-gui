import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from sqlalchemy.orm import Session
from datetime import date, datetime, timedelta
import kegiatandb as fungsi
from importlib import reload
from subprocess import call


root = Tk()
root.title("Task Management System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1000 
height = 600 
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
font = "Arial"
title = "Kegiatan-Tugas"
root.title("TaskManager" + " - " + title)

#Fungsi button pada halaman kegiatan
def click_tugas():
    call(["python", "tugas_gui.py"])
    
def show_tugas():
    treeTugas.delete(*treeTugas.get_children())
    selected=treeKegiatan.focus()
    values = treeKegiatan.item(selected,'values')
    entryKegiatan=values[1]
    row = fungsi.get_all_tugas()
    for i in row:
        if (entryKegiatan==i.nama_kegiatan):
            treeTugas.insert("", "end", iid=i,
                    values=(i.nama_tugas, i.nama, i.tanggal_pemberian, i.tenggat_waktu))

def show_kegiatan():
    treeKegiatan.delete(*treeKegiatan.get_children())
    row = fungsi.get_all_kegiatan()
    for i in row:
        treeKegiatan.insert("", "end", iid=i,
                    values=(i.id_kegiatan, i.nama_kegiatan, i.start_kegiatan, i.end_kegiatan))

def add_kegiatan(): 
    e0=inputNamaKeg.get()
    e1=dated.get()
    e2=datef.get()
    fungsi.create_kegiatan(e0, e1, e2)
    inputNamaKeg.delete(0,END)
    dated.delete(0,END)
    datef.delete(0,END)
    isiStatus.config(text="Done!")

def edit_kegiatan(): 
    e0=inputIdKeg.get()
    e0=int(e0)
    e1=inputNamaKeg.get()
    e2=dated.get()
    e3=datef.get()
    row = fungsi.get_all_kegiatan()
    for i in row:
        if (e0 == i.id_kegiatan):
            fungsi.update_kegiatan(e0, e1, e2, e3)
    inputIdKeg.delete(0,END)
    inputNamaKeg.delete(0,END)
    dated.delete(0,END)
    datef.delete(0,END)
    isiStatus.config(text="Done!") 

#Pengaturan Frame pada halaman Kegiatan
Top = Frame(root, width=900, height=50 ,bd=8)
Top.pack(side=TOP)
Left = Frame(root, width=200, height=500, bd=8)
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500,bd=8)
Right.pack(side=RIGHT)
Bottom = Frame(root, width=900, height=100 ,bd=0)
Bottom.pack(side=BOTTOM)
Kegiatan = Frame(Left, width=300, height=500)
Kegiatan.pack(side=TOP)
Tugas = Frame(Right, width=300, height=250, bd=8)
Tugas.pack(side=TOP)
List=Frame(Left, width=300, height= 100, bd=8)
List.pack(side=BOTTOM)

#Judul Halaman
kegiatanHeading=Label(Top, font=('arial', 24), text="Kegiatan")
kegiatanHeading.grid(row=0, column=0, columnspan=4)

#Form Create Kegiatan
idKeg = Label(Kegiatan, text="ID: ", font="Arial")
idKeg.grid(row=1, column=0, sticky="W")

IDKegiatan = IntVar()
inputIdKeg = Entry(Kegiatan, textvariable=IDKegiatan , width=10,font="Arial", highlightthickness=1)
inputIdKeg.grid(row=2, column=0, sticky="w")

namaKeg = Label(Kegiatan, text="Nama Kegiatan: ", font="Arial")
namaKeg.grid(row=1, column=1, columnspan=3, sticky="W")

NamaKegiatan = StringVar()
inputNamaKeg = Entry(Kegiatan, textvariable=NamaKegiatan, width=35, font="Arial", highlightthickness=1)
inputNamaKeg.grid(row=2, column=1, columnspan=3, sticky="w")

inputStart=Label(Kegiatan, text="Start Kegiatan: ", font="Arial")
inputStart.grid(row=3,column=0, sticky="w")

StartKegiatan = StringVar()
dated = Entry(Kegiatan, width=23, textvariable=StartKegiatan, font="Arial", highlightthickness=1)
dated.grid(row=4,column=0,sticky="w", columnspan=2)

inputEnd=Label(Kegiatan, text="End Kegiatan: ", font="Arial")
inputEnd.grid(row=3,column=2,sticky="w")

EndKegiatan = StringVar()
datef = Entry(Kegiatan, width=25, textvariable=EndKegiatan, font="Arial", highlightthickness=1)
datef.grid(row=4,column=2, sticky="w", columnspan=2)

EditKeg=Button(Kegiatan,width=25,height=2, text="Edit Kegiatan", font="Arial", command=edit_kegiatan)
EditKeg.grid(row=5, column=0, sticky="W",columnspan=2)

AddKeg = Button(Kegiatan,width=25,height=2,text="Add Kegiatan",  font="Arial", command=add_kegiatan)
AddKeg.grid(row=5, column=2, sticky="W", columnspan=2)

status = Label(Kegiatan, text="Status: ", font="Arial") 
status.grid(row=6, column=1, sticky="W")

isiStatus = Label(Kegiatan)
isiStatus.grid(row=6, column=2, sticky="W")


#List Kegiatan
listKeg = Label(Kegiatan, text="List Kegiatan: ", font="Arial")
listKeg.grid(row=7, column=0, columnspan=4, sticky="W")

treeKegiatan = ttk.Treeview(List,  columns=( "id","nama_kegiatan", "start_kegiatan", "end_kegiatan"))
treeKegiatan.grid(row=0, column=0, columnspan=4, sticky="NWES")

treeKegiatan.heading('id', text="ID", anchor=CENTER)
treeKegiatan.heading('nama_kegiatan', text="Nama Kegiatan", anchor=CENTER)
treeKegiatan.heading('start_kegiatan', text="Start Date", anchor=CENTER)
treeKegiatan.heading('end_kegiatan', text="End Date", anchor=CENTER)
treeKegiatan.column('#0', minwidth=0, width=0)
treeKegiatan.column('#1', anchor=CENTER, width=5) 
treeKegiatan.column('#2', anchor=CENTER, width=90)
treeKegiatan.column('#3', anchor=CENTER, width=90)
treeKegiatan.column('#4', anchor=CENTER, width=90)

#Button untuk view kegiatan dan view tugas berdasarkan kegiatan
RefreshKeg = Button(List, width=25, height=2, text="Refresh",  font="Arial", command=show_kegiatan)
RefreshKeg.grid(row=1, column=0, sticky="E", columnspan=2)
ViewTug = Button(List, width=25, height=2, text="View Tugas",  font="Arial", command=show_tugas)
ViewTug.grid(row=1, column=2, sticky="E", columnspan=2)

#List Tugas berdasarkan Kegiatan
listTugas = Label(Tugas, text="List Tugas: ", font="Arial")
listTugas.grid(row=0, column=0, columnspan=4, sticky="W")

treeTugas = ttk.Treeview(Tugas, height=18, columns=( "nama_tugas", "nama","tgl_pemberian", "deadline"))
treeTugas.grid(row=1, column=0, columnspan=6, sticky="NWES")

treeTugas.heading('nama_tugas', text="Nama Tugas", anchor=CENTER)
treeTugas.heading('nama', text="Nama Anggota", anchor=CENTER)
treeTugas.heading('tgl_pemberian', text="Start Date", anchor=CENTER)
treeTugas.heading('deadline', text="Due Date", anchor=CENTER)
treeTugas.column('#0', minwidth=0, width=0)
treeTugas.column('#1', anchor=CENTER, width=95) 
treeTugas.column('#2', anchor=CENTER, width=95)
treeTugas.column('#3', anchor=CENTER, width=95)
treeTugas.column('#4', anchor=CENTER, width=95)

ManageTugas = Button(Tugas, width=25,height=2, text="Manage Tugas",  font="Arial", command=click_tugas)
ManageTugas.grid(row=2, column=4, sticky="E", columnspan=2)

if __name__ == '__main__':
    root.mainloop()









