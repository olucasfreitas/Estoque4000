from flask_migrate import Migrate, init, migrate, upgrade

mg = Migrate()

def init_app(app):
    mg.init_app(app, app.db)