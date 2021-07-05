"""
Модуль содержащий класс для конфигурации внутренней работы приложения.
"""

import os

class Config(object):
    """
    Класс с конфигами.
        attrs:
            * SECRET_KEY - секретный ключ приложения.
            * SQLALCHEMY_DATABASE_URI - Строка подключения бд.
            * SQLALCHEMY_TRECK_MODIFICATION - флажок, который будет логировать изменения в бд.  
    """
    SECRET_KEY = os.environ.get("SECRET_KEY") or 1234567890
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///app.db"
    SQLALCHEMY_TERCK_MODIFICATION = False


# -> поменять ссылку на github к репе.
