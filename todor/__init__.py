from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# creamos la extensón

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    # configuracion del proyecto
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///todolist.db"
    )
    # initialize the app with the extension
    db.init_app(app)
    # registrar Bliprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    # con esto migramos todos los modelos a la base de datos
    with app.app_context():
        db.create_all()
    return app
