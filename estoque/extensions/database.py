from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Session = db.session
def init_app(app):
    db.init_app(app)
    db.create_all(app=app)
    app.db = db

class Provider(db.Model):
    __name__ = "provider"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))

    def __init__(self, name):
        self.name = name

class Stock(db.Model):
    __name__ = "stock"
    id = db.Column(db.Integer, primary_key=True)
    quantity_products = db.Column(db.Float, nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    sold_price = db.Column(db.String(150), nullable=False)

    def __init__(self, quantity_products, products, sold_price):
        self.quantity_products = quantity_products
        self.products = products
        self.sold_price = sold_price

class Product(db.Model):
    __name__ = "product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    products = db.relationship("Stock", backref="product", lazy="select")
    provider_id = db.Column(db.Integer, nullable=False)
    purchased_price = db.Column(db.String(150), nullable=False)

    def __init__(self, name, purchased_price, provider_id):
        self.name = name
        self.provider_id = provider_id
        self.purchased_price = purchased_price