from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
class Person(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    Type = db.Column(db.String())
    age = db.Column(db.Integer())
    description = db.Column(db.String())
    date = db.Column(db.Integer())
 
    def __init__(self, id, name, Type, age, description, date):
        self.id = id
        self.name = name
        self.Type = Type
        self.age = age
        self.description = description
        self.date = date


class PersonSchema(ma.Schema):
    class Meta:
        fields = ('name', 'Type', 'age', 'description', 'date')

person_schema = PersonSchema()