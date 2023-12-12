from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Doctor(db.Model):

    __tablename__ = "doctors"
  
    id = db.Column(db.Integer, 
                 primary_key = True,
                 auto_increment= True)
    
    first_name = db.Column(db.String(25),
                           nullable = False,
                            unique = False)
    
    last_name = db.Column(db.String(25),
                           nullable = False,
                            unique = False)
    
    phone_number = db.Column(db.Integer,
                             nullable = False,
                             unique = True)
    
    speciality = db.Column(db.String, 
                           nullable = False, 
                           unique= False
                        )