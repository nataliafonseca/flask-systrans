from app import db


class Ride(db.Model):
    __tablename__ = 'rides'

    id = db.Column(db.Integer, primary_key=True)
    vehicle_plate = db.Column(
        db.String, db.ForeignKey('vehicles.plate'), nullable=False
    )
    passenger_cpf = db.Column(
        db.String, db.ForeignKey('people.cpf'), nullable=False
    )
    date_time = db.Column(db.DateTime, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def get_id(self):
        return str(self.id)

    def __init__(
        self, vehicle_plate, passenger_cpf, date_time, distance, price
    ):
        self.vehicle_plate = vehicle_plate
        self.passenger_cpf = passenger_cpf
        self.date_time = date_time
        self.distance = distance
        self.price = price

    def __repr__(self):
        return f'<Ride {self.date_time}>'
