from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    body = db.Column(db.String(1200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Create a "car" model, with the same columns we had earlier
# name, year, selling_price, user_id
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    selling_price = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))