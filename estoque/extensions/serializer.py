from flask_marshmallow import Marshmallow
from .database import Provider

ma = Marshmallow()

def init_app(app):
    ma.init_app(app)

class Provider(ma.ModelSchema):
    class Meta:
        model = Provider
