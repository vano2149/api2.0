"""
Ресурс отвечающий за работу User.
"""
from flask_restful import Resource, reqparse
from app.models.user import User


class UserResource(Resource):
    """
    Класс отвечающий за работу User-a.
    """
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username",
        type=str,
        required=True,
        help="Username field required!")
    parser.add_argument(
        "email",
        type=str,
        required=True,
        help="Email field required!")
    parser.add_argument(
        "password",
        type=str,
        required=True,
        help="Password field required!")
    parser.add_argument(
        "first_name",
        type=str,
        required=True,
        help="First name field required!")
    parser.add_argument(
        "second_name",
        type=str,
        required=True,
        help="Second name field required!")
    parser.add_argument(
        "credit_card",
        type=str,
        required=True,
        help="Credit Card field required!")
    parser.add_argument(
        "city",
        type=str,
        required=True,
        help="City field required!")

    def post(self):
        """
        Вызывается при регистрации пользователя.
        """
        request_body = UserResource.parser.parse_args()
        if User.search_username(request_body["username"]):
            return {
                "Message": "User with that username or email already exists!"}, 401
        if User.search_email(request_body["email"]):
            return {
                "Message": "User with that username or email already exists!"}, 401

        user = User(
            request_body["username"],
            request_body["email"],
            request_body["password"],
            request_body["first_name"],
            request_body["second_name"],
            request_body["credit_card"],
            request_body["city"])
        user.insert()
        return {"Message": "User successfuly registred"}, 201
