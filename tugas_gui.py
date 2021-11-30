from tkinter import *
import time
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
from datetime import date, datetime, timedelta
from importlib import reload

root = Tk()
root.title("Tugas")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

root.resizable(0, 0)

import tugasdb as db

#def
def show_all():
    tree.delete(*tree.get_children())
    row = db.get_all_tugas()
    for i in row:
        tree.insert("", "end", iid=i,
                    values=(i.id_tugas, i.nama_tugas, i.id_anggota, i.nama,
                            i.departemen, i.id_kegiatan, i.nama_kegiatan, i.tanggal_pemberian, 
                            i.tenggat_waktu, i.status,i.hasil_tugas,i.description))

def click_home():
    root.destroy()
    import home_gui
    reload(home_gui)

def select_record():
    btn_add["state"]=DISABLED
    
    
    #clear entry boxes
    entry1.delete(0,END)
    entry3.delete(0,END)
    entry5.delete(0,END)
    entry7.delete(0,END)
    entry8.delete(0,END)
    entry11.delete(0,END)
    entry12.delete(0,END)
    entry13.delete(0,END)
    #grab record
    selected=tree.focus()
    #grab record values
    values = tree.item(selected,'values')

    #temp_label.config(text=selected)
    if (values[0]=="No Submission"):
        txt_result.config(text="There is no Tugas yet!", fg="red")
    else:
        #output to entry boxes
        txt_result.config(text="You are editing the Tugas...")
        entry1.insert(0,values[1])
        entry3.insert(0,values[3])
        entry5.insert(0,values[5])
        entry7.insert(0,values[7])
        entry8.insert(0,values[8])
        entry11.insert(0,values[11])
        entry12.insert(0,values[10])
        entry13.insert(0,values[9])
        entry14.insert(0,values[0])
    btn_save["state"]=NORMAL
    
    
        
def save_record():
    selected=tree.focus()
    values = tree.item(selected,'values')
    
    #save new data
    e1=values[1]
    e2=values[2]
    e3=values[3]
    e4=values[4]
    e5=values[5]
    e6=values[6]
    e7=values[7]
    e8=values[8]
    e11=values[11]
    e12=entry12.get()
    e13=entry13.get()
    e14=values[0]
    result=tkMessageBox.askquestion("Submit","Are you sure you want change this?\n")
    if(result =="yes"):
        db.edit_tugas(e14, e12, e13)
        tree.item(selected,text="",values=(e14,e1,e2,e3,e4,e5,e6,e7,e8,e13,e12,e11))
        txt_result.config(text="DONE!")
    
   #clear entry boxes
    
    entry1.delete(0,END)
    entry3.delete(0,END)
    entry5.delete(0,END)
    entry7.delete(0,END)
    entry8.delete(0,END)
    entry11.delete(0,END)
    entry12.delete(0,END)
    entry13.delete(0,END)
    entry14.delete(0,END)
    btn_add["state"]=NORMAL
    btn_save["state"]=DISABLED

def add_record():
    selected=tree.focus()
    values = tree.item(selected,'values')
    
    #save new data
    e1=entry1.get()
    e3=entry3.get()
    e5=entry5.get()
    e7=entry7.get()
    e8=entry8.get()
    e11=entry11.get()
    result=tkMessageBox.askquestion("Submit","Are you sure you want to add this Tugas?\n")
    if(result =="yes"):
        db.add_tugas(e5,e1,e3,e7,e8,e11)

    
   #clear entry boxes
    entry1.delete(0,END)
    entry3.delete(0,END)
    entry5.delete(0,END)
    entry7.delete(0,END)
    entry8.delete(0,END)
    entry11.delete(0,END)


def delete_record():
    selected=tree.focus()
    values = tree.item(selected,'values')
    e14=values[0]
    result=tkMessageBox.askquestion("Submit","Are you sure you want to delete this?\n")
    if(result =="yes"):
        db.delete_tugas(e14)
        txt_result.config(text="DONE!")
   

#variable input form
id_anggota_input = StringVar()
id_kegiatan_input = StringVar()
tanggal_pemberian_input = StringVar()
tenggat_waktu_input = StringVar()
status_input =StringVar()
nama_kegiatan_input = StringVar()
departemen_input = StringVar()
id_tugas_input = StringVar()
nama_tugas_input = StringVar()
nama_input = StringVar()
hasil_tugas_input =StringVar()
description_input=StringVar()

Top = Frame(root, width=900, height=30 ,bd=2)
Top.pack(side=TOP)
Time = Frame(Top)
Time.pack(side=BOTTOM)
Table = Frame(root, width=900, height=100 ,bd=0)
Table.pack(side=TOP)
Isi = Frame(root, width=900, height = 250, bd=8)
Isi.pack(side=TOP)
Buttons1 = Frame(Table, width=300, height=150, bd=2)
Buttons1.pack(side=BOTTOM)
Buttons2 = Frame(root, width=300, height=250, bd=2)
Buttons2.pack(side=TOP)


txt_title = Label(Top, width=900, font=('arial', 16),text = "Tugas")
txt_title.pack()

label5 = Label(Isi, text="ID Kegiatan", font=("bold", 10), bd=10)
label5.grid(row=0, column=1, stick="w")
label1 = Label(Isi, text="Nama Tugas", font=("bold", 10), bd=10)
label1.grid(row=1, column=1, stick="w")
label3 = Label(Isi, text="Anggota", font=("bold", 10), bd=10)
label3.grid(row=2, column=1, stick="w")
label7 = Label(Isi, text="Tanggal Pemberian", font=("bold", 10), bd=10)
label7.grid(row=0, column=3, stick="w")
label8 = Label(Isi, text="Tenggat Waktu", font=("bold", 10), bd=10)
label8.grid(row=1, column=3, stick="w")
labe21 = Label(Isi, text="Description", font=("bold", 10), bd=10)
labe21.grid(row=2, column=3, stick="w")
labe22 = Label(Isi, text="Hasil Tugas", font=("bold", 10), bd=10)
labe22.grid(row=0, column=5, stick="w")
labe22 = Label(Isi, text="Status", font=("bold", 10), bd=10)
labe22.grid(row=1, column=5, stick="w")
labe23 = Label(Isi, text="ID Tugas", font=("bold", 10), bd=10)
labe23.grid(row=2, column=5, stick="w")
txt_result = Label(Buttons1)
txt_result.pack(side=TOP)

entry5 = Entry(Isi, textvariable=id_kegiatan_input, width=25)
entry5.grid(row=0, column=2)
entry1 = Entry(Isi, textvariable=nama_tugas_input,width=25)
entry1.grid(row=1, column=2)
entry3 = Entry(Isi, textvariable=nama_input,width=25)
entry3.grid(row=2, column=2)
entry7 = Entry(Isi, textvariable=tanggal_pemberian_input, width=25)
entry7.grid(row=0, column=4)
entry8 = Entry(Isi, textvariable=tenggat_waktu_input, width=25)
entry8.grid(row=1, column=4)
entry11 = Entry(Isi, textvariable=description_input, width=25)
entry11.grid(row=2, column=4)
entry12 = Entry(Isi, textvariable=hasil_tugas_input, width=25)
entry12.grid(row=0, column=6)
entry13 = Entry(Isi, textvariable=status_input, width=25)
entry13.grid(row=1, column=6)
entry14 = Entry(Isi, textvariable=id_tugas_input, width=25)
entry14.grid(row=2, column=6)


btn_show = Button(Buttons1, height =1, width=15, text="Refresh", bg='white', fg="blue", command = show_all)
btn_show.pack(side=LEFT, padx = 10)
btn_update = Button(Buttons1, height =1, width=15, text="Edit", bg='white', fg="blue", command = select_record)
btn_update.pack(side=LEFT, padx = 10)
btn_delete = Button(Buttons1, height =1, width=15, text="Delete", bg='white', fg="red", command = delete_record)
btn_delete.pack(side=RIGHT, padx = 10)
btn_add = Button(Buttons2, height =1, width=15, bg='white', text="Add Tugas", command = add_record)
btn_add.pack(side=LEFT, padx = 10)
btn_save = Button(Buttons2, height =1, width=15, bg='white', text="Save Update", command = save_record, state=DISABLED)
btn_save.pack(side=RIGHT, padx = 10)

scrollbary = Scrollbar(Table, orient=VERTICAL)
scrollbarx = Scrollbar(Table, orient=HORIZONTAL)
tree = ttk.Treeview(Table, columns=( "id_tugas_input", "nama_tugas_input", "id_anggota_input", "nama_input", "departemen_input","id_kegiatan_input", 
                                    "nama_kegiatan_input", "tanggal_pemberian_input","tenggat_waktu_input",
                                    "status_input","hasil_tugas_input","description_input"),
                    height=7, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('id_tugas_input', text="ID Tugas", anchor=CENTER)
tree.heading('nama_tugas_input', text="Nama Tugas", anchor=CENTER)
tree.heading('id_anggota_input', text="ID Anggota", anchor=CENTER)
tree.heading('nama_input', text="Anggota", anchor=CENTER)
tree.heading('departemen_input', text="Departemen", anchor=CENTER)
tree.heading('id_kegiatan_input', text="ID Kegiatan", anchor=CENTER)
tree.heading('nama_kegiatan_input', text="Nama Kegiatan", anchor=CENTER)
tree.heading('tanggal_pemberian_input', text="Tanggal Pemberian", anchor=CENTER)
tree.heading('tenggat_waktu_input', text="Tenggat Waktu", anchor=CENTER)
tree.heading('status_input', text="Status", anchor=CENTER)
tree.heading('hasil_tugas_input', text="Hasil Tugas", anchor=CENTER)
tree.heading('description_input', text="Description", anchor=CENTER)
tree.column('#0', minwidth=0, width=0)
tree.column('#1', anchor=CENTER, width=100) 
tree.column('#2', anchor=CENTER, width=100)
tree.column('#3', anchor=CENTER, width=100)
tree.column('#4', anchor=CENTER, width=100)
tree.column('#5', anchor=CENTER, width=100)
tree.column('#6', anchor=CENTER, width=100)
tree.column('#7', anchor=CENTER, width=100)
tree.column('#8', anchor=CENTER, width=105)
tree.column('#9', anchor=CENTER, width=100)
tree.column('#10', anchor=CENTER, width=100)
tree.column('#11', anchor=CENTER, width=100)
tree.pack()


if __name__ == '__main__':
    root.mainloop()
