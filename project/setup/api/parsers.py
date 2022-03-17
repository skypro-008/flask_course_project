from flask_restx.inputs import email
from flask_restx.reqparse import RequestParser

auth_parser: RequestParser = RequestParser()
auth_parser.add_argument(name='email', type=email(), required=True, nullable=False)
auth_parser.add_argument(name='password', type=str, required=True, nullable=False)

change_password_parser: RequestParser = RequestParser()
change_password_parser.add_argument(name='old_password', type=str, required=True, nullable=False)
change_password_parser.add_argument(name='new_password', type=str, required=True, nullable=False)

change_user_info_parser: RequestParser = RequestParser()
change_user_info_parser.add_argument(name='name', type=str, required=False)
change_user_info_parser.add_argument(name='surname', type=str, required=False)
change_user_info_parser.add_argument(name='favourite_genre', type=int, required=False)

page_parser: RequestParser = RequestParser()
page_parser.add_argument(name='page', type=int, location='args', required=False)

movie_state_and_page_parser: RequestParser = page_parser.copy()
movie_state_and_page_parser.add_argument('state', choices=('new',), required=False, help="Only have to be 'new'")
