from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__) #like obeject creation
app.config.from_object(Config)

db = SQLAlchemy(app) # we are adding our app to SQLALCHEMY under the name db

migrate = Migrate(app,db)

from app import views,forms,model,db