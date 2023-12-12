from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///medical_retry'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route('/')
def homepage():
    return render_template("home.html")