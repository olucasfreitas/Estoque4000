from dynaconf import FlaskDynaconf
from importlib import import_module

dyna = FlaskDynaconf()

def init_app(app):
    dyna.init_app(app)

def load_modules(app):
    for module in app.config.get('EXTENSIONS'):
        mod = import_module(module)
        mod.init_app(app)