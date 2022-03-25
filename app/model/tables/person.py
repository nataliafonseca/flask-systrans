from app import db


class Person(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    address = db.Column(db.String, nullable=False)

    def __init__(self, cpf, name, birth_date, address):
        self.cpf = cpf
        self.name = name
        self.birth_date = birth_date
        self.address = address

    def __repr__(self):
        return f'<Person {self.cpf}>'
