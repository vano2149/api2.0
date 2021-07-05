"""
Ресурс отвечающий за работу журнала.
"""
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from app.models.journal import Journal


class JournalResourse(Resource):
    """
    Класс отвечающий за работу одного Journal.
    """
    parser = reqparse.RequestParser()
    parser.add_argument(
        'pages',
        type=int,
        required=True,
        help="Message Invalid jornal json structure")
    parser.add_argument('price', type=float, required=True,
                        help="Message Invalid jornal json structure")
    parser.add_argument(
        'amount',
        type=int,
        required=True,
        help="Message Invalid jornal json structure")

    @jwt_required()
    def get(self, title):
        """
        * GET - Запрос возвращающий один журнал.
        """

        journal = Journal.search_title(title)
        if journal:
            return journal.json(), 200
        return {"Message": f"Journal with that title {title} does not exsist!"}, 400

    @jwt_required()
    def put(self, title):
        """
        * PUT - Возвращает обновленную версию журнала, если токов имеется.
        """
        journal = Journal.search_title(title)
        if journal:
            data = JournalResourse.parser.parse_args()
            journal.pages = data["pages"]
            journal.price = data["price"]
            journal.amount = data["amount"]
            journal.update()
            return journal.json(), 202
        return {"Message": "Journal with that title does not exsists"}, 404

    @jwt_required()
    def delete(self, title):
        """
        * DELETE - Удоляет текущий журнал если таков имеется.
        """
        journal = Journal.search_title(title)
        if journal:
            journal.delete()
            return {"Message": "Journal successfuly delete!"}
        return {"Message": "Journal with that title does not exsists!"}


class JournalsResource(Resource):
    """
    Класс отвечающий за работу с множеством журналов.
    """
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title',
        type=str,
        required=True,
        help="Message Invalid jornal json structure")
    parser.add_argument(
        'pages',
        type=int,
        required=True,
        help="Message Invalid jornal json structure")
    parser.add_argument('price', type=float, required=True,
                        help="Message Invalid jornal json structure")
    parser.add_argument(
        'amount',
        type=int,
        required=True,
        help="Message Invalid jornal json structure")

    @jwt_required()
    def get(self):
        """
        Возвращает все имеющиеся журналы на складе.
        """
        return {"jornals": list(map(lambda x: x.json(), Journal.get_all()))}

    @jwt_required()
    def post(self):
        """
        * POST - добовляет новый журнал в бд.
        """
        request_body = JournalsResource.parser.parse_args()
        if Journal.search_title(request_body['title']):
            return {"Message": "Journal with title alredy exists!"}, 400

        journal = Journal(
            request_body["title"],
            request_body["pages"],
            request_body["price"],
            request_body["amount"])
        journal.insert()
        return {"Message": "Journal successfuly created!"}, 201
