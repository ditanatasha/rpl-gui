from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib
import os
import sqlalchemy
from datetime import date, datetime, timedelta

from sqlalchemy.sql.expression import null
from sqlalchemy import String,Boolean,Integer,Column,Text,ForeignKey,Date
from sqlalchemy.orm import relationship

host_server = os.environ.get('host_server', 'fastapi-server.postgres.database.azure.com')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'rpl')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'fastapiadmin@fastapi-server')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'Rpl12345')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)

database = DATABASE_URL

metadata = sqlalchemy.MetaData()

engine = create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
db = SessionLocal()

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

def get_all_tugas():
    global all_tugas
    all_tugas=db.query(Tugas).all()
    for i in all_tugas:
        print(i.id_tugas, i.nama_tugas)
    return all_tugas


def add_tugas(id_kegiatan:int, nama_tugas:str, nama:str, tanggal_pemberian:date, tenggat_waktu:date, description:str):
    db_tugas =Tugas(
        id_kegiatan=id_kegiatan,
        nama_tugas=nama_tugas,
        nama=nama,
        tanggal_pemberian=tanggal_pemberian,
        tenggat_waktu=tenggat_waktu,
        description=description
    )

    db_penilaian=Penilaian(
        nama_tugas=nama_tugas
    )

    db.add(db_tugas)
    db.add(db_penilaian)
    db.commit()
    db.refresh(db_tugas)
    # db.refresh(db_penilaian)

    return db_tugas

def edit_tugas(id_tugas : int, hasil_tugas:str, status: str): 
    check_db_tugas = db.query(Tugas).filter(Tugas.id_tugas==id_tugas).first()
    check_db_tugas.hasil_tugas = hasil_tugas
    check_db_tugas.status = status
    db.commit()

    return check_db_tugas

def delete_tugas(id_tugas: int):
    db_tugas = db.query(Tugas).filter(Tugas.id_tugas==id_tugas).first()
    delete_penilaian=db.query(Penilaian).filter(Penilaian.id_tugas==id_tugas).first()
    db.delete(db_tugas)
    db.delete(delete_penilaian)
    db.commit()
    return db_tugas


    


		
