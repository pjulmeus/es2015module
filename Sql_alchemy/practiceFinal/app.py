from flask import Flask, render_template, session, redirect, request, session 
from flask_debugtoolbar import DebugToolbarExtension
from models import db, conneted_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_intro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
