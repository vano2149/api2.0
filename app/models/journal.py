"""
Модуль содержащий модель журнала.
"""

from app import db


class Journal(db.Model):
    """
    По умолчанию имя таблици(__tabltname__) такое-же как у класс Journal
    меняем __tablename__ = "jornals".
    attrs:
        * id - Идентификатор журнала в бд.
        * title - Название журнала.(Уникальное)
        * pages - Колличество страниц в журнале.
        * price - Цена журнала.
        * amount - Колличество копий данного журнала.

    """
    __tablename__ = "jornals"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    pages = db.Column(db.Integer)
    price = db.Column(db.Float)
    amount = db.Column(db.Integer)

    def __init__(self, title: str, pages: int, price: float, amount: int):
        """
        Функционал модели Jornal.
        """
        self.title = title
        self.pages = pages
        self.price = price
        self.amount = amount

    def json(self):
        """
        Запихуеваем в JSON journal.
        """
        return {
            "title": self.title,
            "pages": self.pages,
            "price": self.price,
            "amount": self.amount,
        }

    @classmethod
    def search_title(cls, title: str):
        """
        Проверяет есть ли журнал в бд.
        """
        return cls.query.filter_by(title=title).first()

    @classmethod
    def get_all(cls):
        """
        Возвращает все журналы.
        """
        return cls.query.all()

    def insert(self):
        """
        Коммитим в бд
        """
        db.session.add(self)
        db.session.commit()

    def update(self):
        """
        Update - журнала.
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        Delete - журнала.
        """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """
        Проверка в shell.
        """
        return f"<Jornal {self.title} {self.pages} {self.price} {self.amount}>"
