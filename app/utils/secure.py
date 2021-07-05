"""
Ресурс отвечающий за аунтентификацию пользователя.
"""

from app.models.user import User
from werkzeug.security import safe_str_cmp

def authenticate(username, password):
    """
    Аунтентификация (проверка на совпадение поролий)
    """
    user = User.search_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(data):
    _id = data["identity"]
    return User.search_id(_id)

