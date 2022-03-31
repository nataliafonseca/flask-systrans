from app import app, db
from app.model.forms.driver import DriverForm
from app.model.tables.driver import Driver
from flask import redirect, render_template, url_for
from flask_login import current_user


@app.route('/driver', methods=['GET', 'POST'])
def list_drivers():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    username = current_user.name.upper()

    drivers_list = Driver.query.all()

    return render_template(
        'driver/list.html', drivers_list=drivers_list, username=username
    )


@app.route('/driver/register', methods=['GET', 'POST'])
def register_driver():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    username = current_user.name.upper()

    form = DriverForm()
    cpf_exists = False

    if form.validate_on_submit():
        cpf_exists = (
            len(Driver.query.filter_by(cpf=f'{form.cpf.data}').all()) > 0
        )

        if not (cpf_exists):
            new_driver = Driver(
                form.cpf.data,
                form.name.data,
                form.birth_date.data,
                form.address.data,
            )
            db.session.add(new_driver)
            db.session.commit()
            return redirect(url_for('list_drivers'))

    return render_template(
        'driver/register.html',
        form=form,
        cpf_exists=cpf_exists,
        username=username,
    )
