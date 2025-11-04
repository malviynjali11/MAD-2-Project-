from flask_security import UserDatastore, SQLAlchemyUserDatastore
from database import db
from models import User, Roles

user_datastore = SQLAlchemyUserDatastore(db, User, Roles)
