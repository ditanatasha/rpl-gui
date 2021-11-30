from tkinter import *
import psycopg2
from importlib import reload
from subprocess import call

def signup(): #Halaman Signup
    global signup_screen
    signup_screen = Tk()
    signup_screen.geometry("400x500")
    signup_screen.title("Sign up")
    global e1, e2, e3, e4, e5, e6, e7,e8, e9

    Label(signup_screen, text="ID Anggota: ").grid(row=0)
    Label(signup_screen, text="Email: ").grid(row=1)
    Label(signup_screen, text="Username: ").grid(row=2)
    Label(signup_screen, text="Password: ").grid(row=3)
    Label(signup_screen, text="Name: ").grid(row=4)
    Label(signup_screen, text="Departemen: ").grid(row=5)
    Label(signup_screen, text="Birth date: ").grid(row=6)
    Label(signup_screen, text="Phone Number: ").grid(row=7)
    Label(signup_screen, text="Role(Supervisor/Associate): ").grid(row=8)

    e1 = Entry(signup_screen)
    e2 = Entry(signup_screen)
    e3 = Entry(signup_screen)
    e4 = Entry(signup_screen)
    e5 = Entry(signup_screen)
    e6 = Entry(signup_screen)
    e7 = Entry(signup_screen)
    e8 = Entry(signup_screen)
    e9 = Entry(signup_screen)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)
    e7.grid(row=6, column=1)
    e8.grid(row=7, column=1)
    e9.grid(row=8, column=1)

    Button(signup_screen, text="Sign Up", command=register_user).grid(row=10, column=1)

 
def register_user(): #Klik tombol register
 
    id_anggota = e1.get()
    email = e2.get()
    username = e3.get()
    password = e4.get()
    nama = e5.get()
    departemen = e6.get()
    ttl = e7.get()
    no_telp = e8.get()
    role = e9.get()
    
    conn = psycopg2.connect(
        host = "fastapi-server.postgres.database.azure.com",
        database = "rpl",
        user = "fastapiadmin@fastapi-server",
        password = "Rpl12345",
        port = "5432"
    )
    c = conn.cursor()

    c.execute("SELECT * FROM t_akun WHERE id_anggota = %s", (id_anggota,))
    
    row = c.fetchone()

    if row is None:
        c.execute("INSERT INTO t_akun VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s)", (id_anggota, email, username, password, nama, departemen, ttl, no_telp, role))
        c.close()
        conn.commit()
        conn.close()
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)
        signup_success()
    else:
        existing_id()

def login_verify(): #Klik tombol login
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    conn = psycopg2.connect(
        host = "fastapi-server.postgres.database.azure.com",
        database = "rpl",
        user = "fastapiadmin@fastapi-server",
        password = "Rpl12345",
        port = "5432"
    )
    c = conn.cursor()
    c.execute("SELECT * FROM t_akun WHERE username = %s and password = %s", (username1, password1))
    row = c.fetchone()
    if row is not None:
        login_sucess()
    else:
        password_not_recognised()

def login_sucess():
    login_screen.destroy()
    call(["python", "home_gui.py"])
    #import home_gui
    #reload(home_gui)

def signup_success():
    global signup_success_screen
    signup_success_screen = Toplevel(signup_screen)
    signup_success_screen.title("Success")
    signup_success_screen.geometry("300x100")
    Label(signup_success_screen, text="Account created").pack()
    Button(signup_success_screen, text="OK", command=delete_signup_success).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("300x100")
    Label(password_not_recog_screen, text="Invalid Username or Password").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
def existing_id():
    global existing_id_screen
    existing_id_screen = Toplevel(signup_screen)
    existing_id_screen.title("Error")
    existing_id_screen.geometry("300x100")
    Label(existing_id_screen, text="Error, user with the same ID already exist!").pack()
    Button(existing_id_screen, text="OK", command=delete_user_exist).pack()

def delete_signup_success():
    signup_success_screen.destroy()
    signup_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_exist():
    existing_id_screen.destroy()

# Main Window
 
def login_windows():
    global login_screen
    login_screen = Tk()
    login_screen.geometry("900x500")
    login_screen.title("Login")
    Label(text="Task Management System", fg = "white", bg="#008CBA", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    
    global username_verify
    global password_verify
    
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username: ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="Password: ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=18, height=1, bg = "#008CBA", fg="white", command = login_verify).pack()
    Label(login_screen, text="").pack()
    
    Label(login_screen, text="Don't have an account?").pack()
    Button(login_screen, text="Sign up", height=1, width=18, command=signup).pack()
 
    login_screen.mainloop()

login_windows()
