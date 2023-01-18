# config
from flask import Flask
from flask_migrate import Migrate

# factory
def create_app():
    app = Flask(__name__)
    from . import pet, facts, models

    # database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Aero1998!@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["TEMPLATES_AUTO_RELOAD"] = True    

    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return 'Hello, Petfax'

            #register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    from . import facts
    app.register_blueprint(facts.bp)

    # return the app
    return app