"""
Ядро приложения.
"""

from flask import Flask
from app.configs import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt import JWT

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models.user import User
from app.models.book import Book
from app.models.journal import Journal
from app.resources.book import BookResource, BooksResource
from app.resources.user import UserResource
from app.resources.journal import JournalsResource, JournalResourse
from app.utils.secure import authenticate, identity

api = Api(app)
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)

api.add_resource(BooksResource,"/api/v1/books")
api.add_resource(BookResource,"/api/v1/book/<string:title>")
api.add_resource(UserResource,"/api/v1/register")
api.add_resource(JournalsResource,"/api/v1/journals")
api.add_resource(JournalResourse,"/api/v1/journal/<string:title>")
