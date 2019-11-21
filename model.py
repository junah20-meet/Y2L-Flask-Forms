from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Products(Base):
   __tablename__ = 'products'
   Id = Column(String, primary_key=True)
   Name Column(String)
   Price = Column(Integer)
   Picture_Link = Column(String)
   Description = Column(String)

class Cart(Base):
   __tablename__ = 'Cart'
   productID = Column(String, primary_key=True)