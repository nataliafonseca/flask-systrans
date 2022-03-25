from app import app, db
from app.model.forms.register import RegisterForm
from app.model.tables.user import User
from bcrypt import gensalt, hashpw
from flask import redirect, render_template, url_for
from flask_login import login_user, current_user


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
