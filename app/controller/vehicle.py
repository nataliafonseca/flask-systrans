from app import app, db
from app.model.forms.vehicle import VehicleForm
from app.model.tables.vehicle import Vehicle
from app.model.tables.driver import Driver
from flask import redirect, render_template, url_for
from flask_login import current_user


@app.route('/vehicle', methods=['GET', 'POST'])
def list_vehicles():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    username = current_user.name.upper()

    vehicles_list = Vehicle.query.all()

    return render_template(
        'vehicle/list.html', vehicles_list=vehicles_list, username=username
    )


@app.route('/vehicle/register', methods=['GET', 'POST'])
def register_vehicle():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    username = current_user.name.upper()

    form = VehicleForm()

    plate_exists = False
    cpf_invalid = False

    if form.validate_on_submit():
        plate_exists = (
            len(
                Vehicle.query.filter_by(
                    plate=f'{form.plate.data.upper()}'
                ).all()
            )
            > 0
        )

        cpf_invalid = (
            len(Driver.query.filter_by(cpf=f'{form.driver_cpf.data}').all())
            == 0
        )

        if not (plate_exists or cpf_invalid):
            new_vehicle = Vehicle(
                form.type.data,
                form.plate.data.upper(),
                form.car_make.data,
                form.model.data,
                form.year.data,
                form.passenger_capacity.data,
                form.driver_cpf.data,
            )
            db.session.add(new_vehicle)
            db.session.commit()
            return redirect(url_for('list_vehicles'))

    return render_template(
        'vehicle/register.html',
        form=form,
        plate_exists=plate_exists,
        cpf_invalid=cpf_invalid,
        username=username,
    )
