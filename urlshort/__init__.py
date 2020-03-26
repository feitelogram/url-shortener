from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__) 
    app.secret_key = 'flask_is_silly'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app

app = create_app()