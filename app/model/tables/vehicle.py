from app import db


class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    plate = db.Column(db.String, unique=True, nullable=False)
    car_make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    passenger_capacity = db.Column(db.String, nullable=False)
    driver_cpf = db.Column(
        db.String, db.ForeignKey('people.cpf'), nullable=False
    )

    def get_id(self):
        return str(self.id)

    def __init__(
        self,
        type,
        plate,
        car_make,
        model,
        year,
        passenger_capacity,
        driver_cpf,
    ):
        self.type = type
        self.plate = plate
        self.car_make = car_make
        self.model = model
        self.year = year
        self.passenger_capacity = passenger_capacity
        self.driver_cpf = driver_cpf

    def __repr__(self):
        return f'<Vehicle {self.plate}>'
