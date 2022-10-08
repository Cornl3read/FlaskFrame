import time
from datetime import timedelta

from flask import Flask, render_template, redirect, render_template_string
from flask_security import Security, current_user, auth_required, hash_password, \
     SQLAlchemySessionUserDatastore, logout_user
from config import DevConf
from database import db_session, init_db
from models import User, Role

app = Flask(__name__)
app.config.from_object(DevConf)

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
app.security = Security(app, user_datastore)


# Create a user to test with
def do_db_stuff():
    init_db()
    if not app.security.datastore.find_user(email="test@me.com"):
        app.security.datastore.create_user(email="test@me.com", password=hash_password("password"))
    db_session.commit()


@app.route('/')
@auth_required()
def hello_world():  # put application's code her
    return render_template('main.html', user=current_user.email.split('@')[0], yellow='brown')


@app.route('/home')
@auth_required()
def home_dashboard():
    return render_template('dashboard/home.html', email=current_user.email, title='Corn')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')
