"""
Модуль содержащий модель пользователя.
"""

from app import db


class User(db.Model):
    """
    По умолчанию имя таблици(__tabltname__) такое-же как у класс User
    меняем __tablename__ = "users".
    attrs:
        * id -id пользователя.
        * username - логин пользователя.
        * email - почта пользователя.
        * password - пароль пользователя.
        * first_name - имя пользователя.
        * second_name - фамилия пользователя.
        * credit_card - номер кредитной карты пользователя.
        * city - город пользователя.
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(120))
    second_name = db.Column(db.String(120))
    credit_card = db.Column(db.String(19))
    city = db.Column(db.String(50))

    def __init__(self, username: str, email: str, password: str,
                 first_name: str, second_name: str, credit_card: str, city: str):
        """
        Функционал модели User.
        """
        self.id = None
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.second_name = second_name
        self.credit_card = credit_card
        self.city = city

    @classmethod
    def search_username(cls, username: str):
        """
        Проверка User.
        """
        return cls.query.filter_by(username=username).first()

    @classmethod
    def search_email(cls, email: str):
        """
        Проверка Email.
        """
        return cls.query.filter_by(email=email).first()

    @classmethod
    def search_id(cls, _id: int):
        """
        Проверка _id.
        """
        return cls.query.filter_by(id=_id).first()

    def insert(self):
        """
        commit-им в бд.
        """
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        """
        Проверка в shell.
        """
        return f"<User {self.username} {self.email} {self.first_name} {self.second_name} {self.city}>"
