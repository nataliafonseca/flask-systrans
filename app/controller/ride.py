from app import app, db
from app.model.forms.ride import RideForm
from app.model.tables.ride import Ride
from app.model.tables.vehicle import Vehicle
from app.model.tables.passenger import Passenger
from flask import redirect, render_template, url_for
from flask_login import current_user
from datetime import datetime


@app.route('/ride', methods=['GET', 'POST'])
def list_rides():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    username = current_user.name.upper()

    rides_list = Ride.query.all()

    return render_template(
        'ride/list.html', rides_list=rides_list, username=username
    )


@app.route('/ride/register', methods=['GET', 'POST'])
def register_ride():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    username = current_user.name.upper()

    form = RideForm()

    plate_invalid = False
    cpf_invalid = False

    if form.validate_on_submit():
        plate_invalid = (
            len(
                Vehicle.query.filter_by(
                    plate=f'{form.vehicle_plate.data.upper()}'
                ).all()
            )
            == 0
        )

        cpf_invalid = (
            len(
                Passenger.query.filter_by(
                    cpf=f'{form.passenger_cpf.data}'
                ).all()
            )
            == 0
        )

        date_time = datetime(
            year=form.date.data.year,
            month=form.date.data.month,
            day=form.date.data.day,
            hour=form.time.data.hour,
            minute=form.time.data.minute,
        )

        if not (plate_invalid or cpf_invalid):
            new_ride = Ride(
                form.vehicle_plate.data.upper(),
                form.passenger_cpf.data,
                date_time,
                form.distance.data,
                (form.distance.data * 40),
            )
            db.session.add(new_ride)
            db.session.commit()
            return redirect(url_for('list_rides'))

    return render_template(
        'ride/register.html',
        form=form,
        plate_invalid=plate_invalid,
        cpf_invalid=cpf_invalid,
        username=username,
    )
