from flask_marshmallow import Marshmallow
from .database import Provider
from .database import Stock
from .database import Product

ma = Marshmallow()

def init_app(app):
    ma.init_app(app)

class ProviderSchema(ma.ModelSchema):
    class Meta:
        model = Provider

class StockSchema(ma.ModelSchema):
    class Meta:
        model = Stock

class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product