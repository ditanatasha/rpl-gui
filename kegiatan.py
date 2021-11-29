from os import stat
from datetime import date, datetime, timedelta
from typing import List, Optional
from database import SessionLocal, engine, database, db, metadata, Base
from sqlalchemy.orm import Session
import sqlalchemy
from sqlalchemy.sql.expression import null
from sqlalchemy import String,Boolean,Integer,Column,Text,ForeignKey,Date
from sqlalchemy.orm import relationship
from tkinter import messagebox


# Pengaturan class  
class User(Base):
    __tablename__='t_akun'
    id_anggota=Column(Integer, primary_key=True, autoincrement=True,nullable=False,unique=True)
    email=Column(String(255),nullable=False,unique=True)
    username=Column(String(255),nullable=False,unique=True)
    password=Column(String(255),nullable=False)
    nama=Column(String(255),nullable=False,unique=True)
    departemen=Column(String(255), nullable=False)
    ttl=Column(Date, nullable=False)
    no_telp=Column(String(15), nullable=False)
    role=Column(String(50), nullable=False)
    relation_tugas = relationship("Tugas")

class Kegiatan(Base):
    __tablename__='t_kegiatan'
    id_kegiatan=Column(Integer, primary_key=True, autoincrement=True, unique=True)
    nama_kegiatan=Column(String(255),nullable=False,unique=True)
    start_kegiatan = Column(Date, nullable=False)
    end_kegiatan = Column(Date, nullable=False)
    relation_tugas = relationship("Tugas")

class Tugas(Base):
    __tablename__='t_tugas'
    id_tugas=Column(Integer,primary_key=True, autoincrement=True, unique=True)
    nama_tugas=Column(String(255),nullable=False, unique=True)
    id_anggota=Column(Integer)
    nama=Column(String(255),ForeignKey('t_akun.nama'))
    departemen=Column(String(255))
    id_kegiatan=Column(Integer)
    nama_kegiatan=Column(String(255),ForeignKey('t_kegiatan.nama_kegiatan'))
    description=Column(String(255), nullable=False)
    tanggal_pemberian = Column(Date)
    tenggat_waktu = Column(Date)
    status=Column(String(50), nullable=False, default="Assigned")
    hasil_tugas=Column(String(255),nullable=True, default="No Submission")
    relation_penilaian = relationship("Penilaian")

class Penilaian(Base):
    __tablename__='t_penilaian'
    id_tugas=Column(Integer, primary_key=True)
    nama_tugas=Column(String(255),ForeignKey('t_tugas.nama_tugas'), nullable=False)
    id_kegiatan=Column(Integer)
    nama_kegiatan=Column(String(255))
    id_anggota=Column(Integer)
    nama=Column(String(255))
    departemen=Column(String(255))
    hasil_tugas=Column(String(255), nullable=True, default="No Submission")
    nilai=Column(Integer, nullable=True, default=0)
    komentar=Column(String(255), nullable=True, default="No comment")  


def get_all_kegiatan():
    kegiatan=db.query(Kegiatan).all()

    return kegiatan

def get_one_kegiatan(id_kegiatan:int):
    db_kegiatan=db.query(Kegiatan).filter(Kegiatan.id_kegiatan == id_kegiatan).first()
    if db_kegiatan is None:
        print("Kegiatan not found")
    return db_kegiatan

def input_dbkegiatan(nama_kegiatan:str, start_kegiatan: date, end_kegiatan: date):
    
    db_kegiatan = Kegiatan(
        nama_kegiatan=nama_kegiatan,
        start_kegiatan=start_kegiatan,
        end_kegiatan=end_kegiatan
    )

    db.add(db_kegiatan)
    db.commit()
    db.refresh(db_kegiatan)

    return db_kegiatan

def create_kegiatan(nama_kegiatan:str, start_kegiatan:date, end_kegiatan: date): 
    check_db_kegiatan = db.query(Kegiatan).filter(Kegiatan.nama_kegiatan==nama_kegiatan).first()
    if check_db_kegiatan is not None:
        messagebox.showinfo("Kegiatan","Kegiatan already registered")
    else:
        db_kegiatan = input_dbkegiatan(nama_kegiatan, start_kegiatan, end_kegiatan)
        return (db_kegiatan)

def update_kegiatan(id_kegiatan:int, new_nama_kegiatan:str, new_start_kegiatan: date, new_end_kegiatan: date):
    update_db_kegiatan = db.query(Kegiatan).filter(Kegiatan.id_kegiatan==id_kegiatan).first()
    if update_db_kegiatan is None:
        messagebox.showinfo("Kegiatan","No Kegiatan registered")
    update_db_kegiatan.nama_kegiatan=new_nama_kegiatan
    update_db_kegiatan.start_kegiatan=new_start_kegiatan
    update_db_kegiatan.end_kegiatan=new_end_kegiatan

    db.commit()

    return update_db_kegiatan
    # print('Kegiatan failed to update.')


def get_all_tugas():
    all_tugas=db.query(Tugas).all()

    return all_tugas

