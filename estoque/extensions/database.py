from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Session = db.session
def init_app(app):
    db.init_app(app)
    db.create_all(app=app)
    app.db = db

class Manufacturer(db.Model):
    __name__ = "manufacturer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    stock = db.relationship("Stock", backref="manufacturer", lazy="select")

class Stock(db.Model):
    __name__ = "stock"
    id = db.Column(db.Integer, primary_key=True)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    products = db.relationship("Product", backref="stock", lazy="select")

class Product(db.Model):
    __name__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))
    production_cost = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sold_price = db.Column(db.String(150), nullable=True)