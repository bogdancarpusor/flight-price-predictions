from api import db


class Flight(db.Model):

    __tablename__ = 'flights'

    id = db.Column(db.Integer, primary_key=True)
    city_from = db.Column(db.String(64), index=True)
    city_to = db.Column(db.String(64), index=True)
    distance = db.Column(db.Numeric)
    airport_from = db.Column(db.String(64))
    airport_to = db.Column(db.String(64))
    kiwi_flight_id = db.Column(db.String(64))
    price = db.Column(db.Numeric, index=True)
    departure_time = db.Column(db.Time)
    arrival_time = db.Column(db.Time)
    flight_number = db.Column(db.String(64))
    cabin_class = db.Column(db.String(64))
    airline_code = db.Column(db.String(64))

    def __repr__(self):
        return '<Flight {0} from {1} to {2}>'.format(self.flight_number, self.city_from, self.city_to)
