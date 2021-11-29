from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib
import os
import sqlalchemy

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


#function penilaian
def get_all_data_penilaian():
    global all_penilaian
    all_penilaian=db.query(Penilaian).all()
    for i in all_penilaian:
        print(i.id_tugas, i.nama_tugas)
    return all_penilaian

#get yang belom dinilai saja
def get_penilaian_null():
    global all_penilaian_null
    all_penilaian_null=db.query(Penilaian).filter(Penilaian.nilai==0).all()
    return all_penilaian_null

#get 1 penilaian spesifik
def get_satu_data_penilaian(id_tugas:int):
    one_penilaian=db.query(Penilaian).filter(Penilaian.id_tugas==id_tugas).first()
    return one_penilaian

#update nilai dan komentar
def update_penilaian(id_tugas:int,input_nilai: int, input_komentar: str):
    item_to_update=db.query(Penilaian).filter(Penilaian.id_tugas==id_tugas).first()
    item_to_update.nilai= input_nilai #penilaian.nilai
    item_to_update.komentar = input_komentar #penilaian.komentar
    #print(item_to_update.nilai, item_to_update.price)
    db.commit()
    return item_to_update

#def get_all_kegiatan(db: Session = Depends(get_db), user: schemas.User = Depends(authorization)):
    #kegiatan=db.query(models.Kegiatan).all()
