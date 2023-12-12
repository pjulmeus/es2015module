from flask import Flask, request, redirect, render_template, session
from models import db, connect_db, Doctor


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///medical_retry'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route('/')
def homepage():
    print(db.session.execute(db.select('1')))
    return render_template("home.html")