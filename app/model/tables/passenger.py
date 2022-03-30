from msilib.schema import Class
from app import db
from app.model.tables.person import Person

class Passenger(Person):
    __tablename__ = 'passengers'

    id = db.Column(db.Integer, db.ForeignKey('people.id'), primary_key=True)
    cidade = db.Column(db.String, nullable=False)
    uf = db.Column(db.String, nullable=False) 

    def get_id(self):
        return str(self.id)

    def __init__(self, cpf, name, birth_date, address, cidade, uf):
        self.cpf = cpf
        self.name = name
        self.birth_date = birth_date
        self.address = address
        self.cidade = cidade
        self.uf = uf

#    def __repr__(self):
#        return f'<User {self.cpf}>'