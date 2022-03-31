from app import app, db
from app.model.forms.passenger import PassengerForm
from app.model.tables.passenger import Passenger
from flask import redirect, render_template, url_for
from flask_login import current_user


@app.route('/passenger', methods=['GET', 'POST'])
def list_passengers():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    username = current_user.name.upper()

    passengers_list = Passenger.query.all()

    return render_template(
        'passenger/list.html',
        passengers_list=passengers_list,
        username=username,
    )


@app.route('/passenger/register', methods=['GET', 'POST'])
def register_passenger():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    username = current_user.name.upper()

    form = PassengerForm()
    cpf_exists = False

    if form.validate_on_submit():
        cpf_exists = (
            len(Passenger.query.filter_by(cpf=f'{form.cpf.data}').all()) > 0
        )

        if not (cpf_exists):
            new_passenger = Passenger(
                form.cpf.data,
                form.name.data,
                form.birth_date.data,
                form.address.data,
                form.city.data,
                form.state.data,
            )
            db.session.add(new_passenger)
            db.session.commit()
            return redirect(url_for('list_passengers'))

    return render_template(
        'passenger/register.html',
        form=form,
        cpf_exists=cpf_exists,
        username=username,
    )
