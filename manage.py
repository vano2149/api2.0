"""
Пакет откуда стартует наше приложение.
"""

from app import app, db
from app.models.user import User
from app.models.book import Book


@app.shell_context_processor
def make_shell_context():
    """
    Тестируем через shell.
    """
    return {
        "app": app,
        "db": db,
        "User": User,
        "Book": Book
    }


if __name__ == "__main__":
    app.run()
