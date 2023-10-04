# este es nuestro archivo principal para ejecutar nuestra app
from todor import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
