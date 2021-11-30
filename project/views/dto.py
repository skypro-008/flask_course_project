from flask_restx.inputs import email
from flask_restx.reqparse import RequestParser

auth_parser = RequestParser()
auth_parser.add_argument(name='email', type=email(), required=True, nullable=False)
auth_parser.add_argument(name='password', type=str, required=True, nullable=False)

login_parser = RequestParser()
login_parser.add_argument(name='email', type=email(), required=True, nullable=False)
login_parser.add_argument(name='password', type=str, required=True, nullable=False)
