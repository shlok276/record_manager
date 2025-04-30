# init_db.py
from database.db_setup import Base, engine
from models.user import User

Base.metadata.create_all(bind=engine)
