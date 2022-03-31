from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


lm = LoginManager(app)


from app.controller import index, user, driver, dashboard
from app.model.tables import user, passenger, driver, vehicle
