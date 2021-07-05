"""
Модуль содержащий модель книги.
"""

from app import db


class Book(db.Model):
    """
    По умолчанию имя таблици(__tabltname__) такое-же как у класс Book
    меняем __tablename__ = "books".
    attrs:
        * id - id книги.
        * title - Название книги (Уникальное).
        * author - ФИО автора кники.
        * year_pub - Дата публикации книги.
        * price - Цена книги.
        * amount - Колличество книг на складе.
        * isbn - ISBN книги.
    """
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    author = db.Column(db.String(128))
    year_pub = db.Column(db.Integer)
    price = db.Column(db.Float)
    amount = db.Column(db.Integer)
    isbn = db.Column(db.String(50))


    def __init__(self, title: str, author: str, year_pub: int,
                 price: float, amount: int, isbn: int):
        """
        Функционал модели Book.
        """
        self.title = title
        self.author = author
        self.year_pub = year_pub
        self.price = price
        self.amount = amount
        self.isbn = isbn


    def json(self):
        """
        Запихиваем в JSON.
        """
        return {"title": self.title, "author": self.author, "year_pub": self.year_pub,
                "price": self.price, "amount": self.amount, "isbn": self.isbn}


    @classmethod
    def search_title(cls, title: str):
        """
        Проверка есть ли книга в бд.
        """
        return cls.query.filter_by(title=title).first()


    @classmethod
    def get_all(cls):
        """
        Возвращает все книги.
        """
        return cls.query.all()


    def insert(self):
        """
        commit-им в бд.
        """
        db.session.add(self)
        db.session.commit()


    def update(self):
        """
        Обновление книги.
        """
        db.session.add(self)
        db.session.commit()


    def delete(self):
        """
        Удаление книги.
        """
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        """
        Проверка в shell.
        """
        return f"<Book {self.title} {self.author} {self.year_pub} {self.price} {self.amount} {self.isbn}>"
