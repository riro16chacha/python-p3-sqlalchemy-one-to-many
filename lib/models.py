from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)

    orders = relationship('Order', backref='customer')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('customers.id'))

class OrderMetadata(Base):
    __tablename__ = 'orders_metadata'

    id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey("order.id"))

    order = relationship('Order',
        backref=backref('order_metadata', uselist=False))    
