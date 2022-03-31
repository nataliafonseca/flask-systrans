from app import app
from app.model.forms.report import ReportForm
from app.model.tables.ride import Ride
from flask import redirect, render_template, url_for
from flask_login import current_user
from datetime import datetime


@app.route('/report', methods=['GET', 'POST'])
def report():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    username = current_user.name.upper()
    form = ReportForm()

    rides_list = Ride.query.all()

    if form.validate_on_submit():
        start = datetime(
            year=form.initial_date.data.year,
            month=form.initial_date.data.month,
            day=form.initial_date.data.day,
            hour=0,
            minute=0,
            second=0,
        )
        end = datetime(
            year=form.final_date.data.year,
            month=form.final_date.data.month,
            day=form.final_date.data.day,
            hour=23,
            minute=59,
            second=59,
        )

        rides_list = (
            Ride.query.filter(Ride.date_time >= start)
            .filter(Ride.date_time <= end)
            .all()
        )

    total = 0
    for ride in rides_list:
        total += ride.price

    return render_template(
        'report.html',
        rides_list=rides_list,
        username=username,
        form=form,
        total=total,
    )
