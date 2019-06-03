from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from api.routes import bp
from api.config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


def start_api():
    app.register_blueprint(bp, api_prefix='/api')
    app.run(debug=True, host='0.0.0.0')