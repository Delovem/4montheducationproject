from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("postgresql+psycopg2://postgres:Delovem!1@localhost/4months")
engine.connect()

Base = declarative_base()

class DBproduct(Base):
    __tablename__ = 'ProductsTable'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)

Base.metadata.create_all(engine)