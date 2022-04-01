from app import db
from app.model.tables.person import Person


class Driver(Person):
    __tablename__ = 'drivers'

    id = db.Column(db.Integer, db.ForeignKey('people.id'), primary_key=True)

    def __init__(self, cpf, name, birth_date, address):
        self.cpf = cpf
        self.name = name
        self.birth_date = birth_date
        self.address = address

    def __repr__(self):
        return f'<Driver {self.cpf}>'
