from app import app
from flask import redirect, render_template, url_for
from flask_login import current_user


@app.route('/dashboard', methods=['GET'])
def dashboard():

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    username = current_user.name.upper()
    return render_template('dashboard.html', username=username)
