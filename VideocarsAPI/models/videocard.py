from db import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Videocard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    manufacturer = db.Column(db.String(80), nullable=False)
    memory_size_in_gb = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Double, nullable=False)
    release_date = db.Column(db.Date, nullable=False)


class VideocardSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Videocard
        load_instance = True