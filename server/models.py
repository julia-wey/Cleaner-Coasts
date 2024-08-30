from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

class Trash():
    __tablename__ = 'trash'

    id=db.Column(db.Integer, primary_key=True)
    type=db.Column(db.String, nullable=False)
    amount=db.Column(db.Integer, nullable=False)
    collector_id=db.Column(db.Integer, db.ForeignKey('collectors.id'), nullable=False)
    location_id=db.Column(db.Integer, db.ForeignKey('locations.id', nullable=False))

class Collector():
    __tablename__ = 'collectors'

    id=db.Column(db.Integer, )
    username=db.Column(db.String, unique=True, nullable=False)
    first_name=db.Column(db.String)
    last_name=db.Column(db.String)

class Location():
    __tablename__ = 'locations'

    id=db.Column(db.Integer)
    name=db.Column(db.String)
    city=db.Column(db.String, nullable=False)
    state=db.Column(db.String, nullable=False)
    zipcode=db.Column(db.Integer, nullable=False)

