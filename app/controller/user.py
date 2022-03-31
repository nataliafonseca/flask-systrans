from app import app, db
from app.model.forms.login import LoginForm
from app.model.forms.register import RegisterForm
from app.model.tables.user import User
from bcrypt import checkpw, gensalt, hashpw
from flask import redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegisterForm()
    username_taken = False
    cpf_exists = False

    if form.validate_on_submit():
        username_taken = (
            len(User.query.filter_by(username=f'{form.username.data}').all())
            > 0
        )

        cpf_exists = (
            len(User.query.filter_by(cpf=f'{form.cpf.data}').all()) > 0
        )

        if not (username_taken or cpf_exists):
            hashed_password = hashpw(
                form.password.data.encode('utf8'), gensalt()
            )
            new_user = User(
                form.cpf.data,
                form.name.data,
                form.birth_date.data,
                form.address.data,
                form.username.data,
                hashed_password,
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('dashboard'))

    return render_template(
        'register.html',
        form=form,
        username_taken=username_taken,
        cpf_exists=cpf_exists,
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()
    authentication_error = False

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and checkpw(form.password.data.encode('utf8'), user.password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            authentication_error = True

    return render_template(
        'login.html', form=form, authentication_error=authentication_error
    )


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
