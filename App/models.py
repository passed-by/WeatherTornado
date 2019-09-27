# models.py
#   这里写模型
#   模型:数据库表
from utils.conn import Base
from sqlalchemy import Column, Integer, String


def create_db():
    Base.metadata.create_all()


class User(Base):
    __tablename__ = 't_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True)
    password = Column(String(32), nullable=False)


