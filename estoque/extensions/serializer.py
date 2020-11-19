from flask_marshmallow import Marshmallow
from .database import Manufacturer
from .database import Stock
from .database import Product

ma = Marshmallow()

def init_app(app):
    ma.init_app(app)

class ManufacturerSchema(ma.ModelSchema):
    class Meta:
        model = Manufacturer

class StockSchema(ma.ModelSchema):
    class Meta:
        model = Stock

class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product