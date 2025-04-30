# services/auth_service.py
import bcrypt
from sqlalchemy.orm import Session
from models.user import User
from database.db_setup import SessionLocal

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(username: str, password: str):
    db = SessionLocal()
    existing_user = get_user_by_username(db, username)
    if existing_user:
        return False, "Username already exists."
    
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = User(username=username, password_hash=hashed.decode('utf-8'))
    db.add(user)
    db.commit()
    db.close()
    return True, "Account created successfully."

def authenticate_user(username: str, password: str):
    db = SessionLocal()
    user = get_user_by_username(db, username)
    db.close()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        return True
    return False
