from datetime import datetime
from app import db
from app.models.models import User

def user_exists(username: str) -> bool:
    return db.session.query(User.id).filter_by(username=username).first() is not None

def create_user(username: str, password: str, remember=False, last_login=None) -> User:
    user = User(username=username, remember=remember, last_login=last_login or datetime.utcnow())
    user.set_password(password)  # salva hash seguro
    db.session.add(user)
    db.session.commit()
    return user

def validate_user_password(username: str, password: str) -> User | None:
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None
