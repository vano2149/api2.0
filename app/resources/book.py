"""
Ресурс отвечающий за работу Book.
"""

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from app.models.book import Book


class BookResource(Resource):
    """
    Ресурс отвечающий за работу одной книги.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('author', type=str, required=True,
                        help="Message Invalid book json structure")
    parser.add_argument(
        'year_pub',
        type=int,
        required=True,
        help="Message Invalid book json structure")
    parser.add_argument('price', type=float, required=True,
                        help="Message Invalid book json structure")
    parser.add_argument('amount', type=int, required=True,
                        help="Message Invalid book json structure")
    parser.add_argument(
        'isbn',
        type=str,
        required=True,
        help="Message Invalid book json structure")

    @jwt_required()
    def get(self, title):
        """
        * GET - Запрос возвращающий одну книгу.
        """

        book = Book.search_title(title)
        if book:
            return book.json(), 200
        return {"Message": f"Book with that title {title} does not exists"}, 404

    @jwt_required()
    def put(self, title):
        """
        * PUT - Возвращает обновленную версию книги, если токова имеется.
        """
        book = Book.search_title(title)
        if book:
            data = BookResource.parser.parse_args()
            book.author = data["author"]
            book.year_pub = data["year_pub"]
            book.price = data["price"]
            book.amount = data["amount"]
            book.isbn = data["isbn"]
            book.update()
            return book.json(), 202
        return {"Message": "Book with that title does not exists"}, 404

    @jwt_required()
    def delete(self, title):
        """
        * DELETE - Удоляет текущую книгу если есть.
        """
        book = Book.search_title(title)
        if book:
            book.delete()
            return {"Message": "Book successfuly delete!"}
        return {"Message": "Book with that title does not exists!"}


class BooksResource(Resource):
    """
    Русурс товечающий за работу с множеством книг.
    """

    parser = reqparse.RequestParser()
    parser.add_argument(
        'title',
        type=str,
        required=True,
        help="Message Invalid book json structure")
    parser.add_argument('author', type=str, required=True,
                        help="Message Invalid book json structure")
    parser.add_argument(
        'year_pub',
        type=int,
        required=True,
        help="Message Invalid book json structure")
    parser.add_argument('price', type=float, required=True,
                        help="Message Invalid book json structure")
    parser.add_argument('amount', type=int, required=True,
                        help="Message Invalid book json structure")
    parser.add_argument(
        'isbn',
        type=str,
        required=True,
        help="Message Invalid book json structure")

    @jwt_required()
    def get(self):
        """
        * GET Возвращает все имеющиеся книги на складе.
        """
        return {
            "Books": list(map(lambda x: x.json(), Book.get_all()))
        }

    @jwt_required()
    def post(self):
        """
        * POST - добовляет новую книгу в бд.
        """
        request_body = BooksResource.parser.parse_args()
        if Book.search_title(request_body["title"]):
            return{"Message": "Book with that title already exists!"}, 400

        book = Book(
            request_body["title"],
            request_body["author"],
            request_body["year_pub"],
            request_body["price"],
            request_body["amount"],
            request_body["isbn"])
        book.insert()
        return {"Message": "Book successfuly created"}, 201
