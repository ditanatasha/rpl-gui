from tkinter import *
import time
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import csv
import os

root = Tk()
root.title("Penilaian")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
#root['bg'] = '#fff1e6'
root.resizable(0, 0)

##def swap_Text():
##    lab['text'] = time.asctime()
##    root.after(1000, swap_Text)

def click_home():
    root.destroy()
    import home_gui

import penilaiandb as db
db.get_all_data_penilaian()
row = db.all_penilaian

#def
def show_all():
    tree.delete(*tree.get_children())
    row = db.all_penilaian
    for i in row:
        tree.insert("", "end", iid=i,
                    values=(i.nama_kegiatan, i.departemen, i.id_tugas, i.nama_tugas,
                            i.nama, i.hasil_tugas, i.nilai, i.komentar))
    btn_edit["state"]=NORMAL
    txt_result.config(text="Successfully read the data from database", fg="black")

def select_record():
    #clear entry boxes
    entry0.config(text="")
    entry1.config(text="")
    entry2.config(text="")
    entry3.config(text="")
    entry4.config(text="")
    entry5.config(text="")
    entry6.delete(0,END)
    entry7.delete(0,END)
    
    #grab record
    selected=tree.focus()
    #grab record values
    values = tree.item(selected,'values')
    #temp_label.config(text=selected)
    if (values[0]=="No Submission"):
        txt_result.config(text="There is no submission yet!", fg="red")
    else:
        #output to entry boxes
        txt_result.config(text="You are editing the score...")
        entry0.config(text=values[0])
        entry1.config(text=values[1])
        entry2.config(text=values[2])
        entry3.config(text=values[3])
        entry4.config(text=values[4])
        entry5.config(text=values[5])
        entry6.insert(0,values[6])
        entry7.insert(0,values[7])
        btn_save["state"]=NORMAL

def save_record():
    selected=tree.focus()
    values = tree.item(selected,'values')
    
    #save new data
    e0=values[0]
    e1=values[1]
    e2=values[2]
    e3=values[3]
    e4=values[4]
    e5=values[5]
    e6=entry6.get()
    e7=entry7.get()
    result=tkMessageBox.askquestion("Submit","Are you sure you want submit this?\n" + "id: " + e2 + "\n" + "nilai:" + e6 + "\n" + "komentar: " + e7)
    if(result =="yes"):
        e2 = int(e2) #id tugas
        e6 = int(e6) #nilai
        db.update_penilaian(e2, e6, e7)
        #e2 = str(e2)
        #e6 = str(e6)
        tree.item(selected,text="",values=(e0,e1,e2,e3,e4,e5,e6,e7))
        txt_result.config(text="DONE!")
    
   #clear entry boxes
    entry0.config(text="")
    entry1.config(text="")
    entry2.config(text="")
    entry3.config(text="")
    entry4.config(text="")
    entry5.config(text="")
    entry6.delete(0,END)
    entry7.delete(0,END)
    btn_save["state"]=DISABLED


#variable input form
nama_kegiatan_input = StringVar()
departemen_input = StringVar()
id_tugas_input = StringVar()
nama_tugas_input = StringVar()
nama_input = StringVar()
hasil_tugas_input =StringVar()
nilai_input = StringVar()
komentar_input = StringVar()

Top = Frame(root, height=30 ,bd=2)
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


##lab = Label(Time, text='0')
##lab.pack()
##swap_Text()


back_btn = Button(root, width=15, bg="#e9edc9", text="Home", command=click_home)
back_btn.place(relx = 0.01, rely = 0.01, anchor ='nw')
#back_btn.pack(side=LEFT)
txt_title = Label(Time, width=100,font=('Helvetica', 15),text = "Penilaian")
txt_title.pack()
label0 = Label(Isi, text="Nama Kegiatan", font=("bold", 10), bd=10)
label0.grid(row=0, column=0, stick="w")
label1 = Label(Isi, text="Departemen", font=("bold", 10), bd=10)
label1.grid(row=1, column=0, stick="w")
label2 = Label(Isi, text="Id Tugas", font=("bold", 10), bd=10)
label2.grid(row=2, column=0, stick="w")
label3 = Label(Isi, text="Nama Tugas", font=("bold", 10), bd=10)
label3.grid(row=3, column=0, stick="w")
label4 = Label(Isi, text="Anggota", font=("bold", 10), bd=10)
label4.grid(row=0, column=2, stick="w")
label5 = Label(Isi, text="Hasil Tugas", font=("bold", 10), bd=10)
label5.grid(row=1, column=2, stick="w")
label6 = Label(Isi, text="Nilai", font=("bold", 10), bd=10)
label6.grid(row=2, column=2, stick="w")
label7 = Label(Isi, text="Komentar", font=("bold", 10), bd=10)
label7.grid(row=3, column=2, stick="w")
txt_result = Label(Buttons1)
txt_result.pack(side=TOP)

entry0 = Label(Isi, text="", bd=10, width=25, fg="blue")
entry0.grid(row=0, column=1) 
entry1 = Label(Isi, text="", bd=10, width=25, fg="blue")
entry1.grid(row=1, column=1)
entry2 = Label(Isi, text="", bd=10, width=25, fg="blue")
entry2.grid(row=2, column=1)
entry3 = Label(Isi, text="", bd=10, width=25, fg="blue")
entry3.grid(row=3, column=1)
entry4 = Label(Isi, text="", bd=10, width=25, fg="blue")
entry4.grid(row=0, column=3)
entry5 = Label(Isi, text="", bd=10, width=25, fg="blue")
entry5.grid(row=1, column=3)
entry6 = Entry(Isi, textvariable=nilai_input, width=25)
entry6.grid(row=2, column=3)
entry7 = Entry(Isi, textvariable=komentar_input, width=25)
entry7.grid(row=3, column=3)

btn_show = Button(Buttons1, height =1, width=15, text="Refresh", bg='white', fg="blue", command = show_all)
btn_show.pack(side=LEFT, padx = 10)
btn_edit = Button(Buttons1, height =1, width=15, text="Edit", bg='white', fg="red", state=DISABLED, command = select_record)
btn_edit.pack(side=LEFT, padx = 3)
btn_save = Button(Buttons2, height =1, width=15, bg='white', text="Submit", state=DISABLED, command = save_record)
btn_save.pack()

scrollbary = Scrollbar(Table, orient=VERTICAL)
scrollbarx = Scrollbar(Table, orient=HORIZONTAL)
tree = ttk.Treeview(Table, columns=( "nama_kegiatan_input", "departemen_input", "id_tugas_input", "nama_tugas_input", "nama_input","hasil_tugas_input", "nilai_input", "komentar_input"),
                    height=7, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('nama_kegiatan_input', text="Kegiatan", anchor=CENTER)
tree.heading('departemen_input', text="Dept.", anchor=CENTER)
tree.heading('id_tugas_input', text="ID Tugas", anchor=CENTER)
tree.heading('nama_tugas_input', text="Tugas", anchor=CENTER)
tree.heading('nama_input', text="PIC", anchor=CENTER)
tree.heading('hasil_tugas_input', text="Hasil", anchor=CENTER)
tree.heading('nilai_input', text="Nilai", anchor=CENTER)
tree.heading('komentar_input', text="Komentar", anchor=CENTER)
tree.column('#0', minwidth=0, width=0)
tree.column('#1', anchor=CENTER, width=100) 
tree.column('#2', anchor=CENTER, width=100)
tree.column('#3', anchor=CENTER, width=70)
tree.column('#4', anchor=CENTER, width=170)
tree.column('#5', anchor=CENTER, width=100)
tree.column('#6', anchor=CENTER, width=100)
tree.column('#7', anchor=CENTER, width=100)
tree.column('#8', anchor=CENTER, width=120)
tree.pack()


if __name__ == '__main__':
    root.mainloop()
