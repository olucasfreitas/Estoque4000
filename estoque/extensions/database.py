from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    app.db = db

class Provider(db.Model):
  __name__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(150))
  email = db.Column(db.String(150))
  registered_number = db.Column(db.String(150))
  password = db.Column(db.String(150))

  def __init__(self, name, registered_number, email, password):
    self.name = name
    self.registered_number = registered_number
    self.email = email
    self.password = password
