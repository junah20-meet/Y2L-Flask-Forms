from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(id, name, price, price_link, description ):
    product_object = Product(
        ID=id,
        Name=name,
        Price=price,
        price_link=price_link,
        Description=discription,)
    session.add(product_object)
    session.commit()


def edits_specific_product(id, name, price, price_link, description):
    product_object = session.query(
       Product).filter_by(
       ID=id).first()
   product_object.ID=id
   product_object.Name=name
   product_object.Price=price
   product_object.price_link=price_link
   product_object.Description=discription
   session.commit()

def delete_product(id):
   session.query(Porduct).filter_by(
       id=ID).delete()
   session.commit()

def query_all_products():
   products = session.query(
      Product).all()
   return products

def query_by_id(id):
   product = session.query(
       Product).filter_by(
       id=ID).first()
   return product

   def add_to_cart(productID):
    productID_object = Cart(
      productID=ProductID)
    session.add(productID_object)
    session.commit()



