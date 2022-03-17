from flask_restx import Api

api: Api = Api(
    authorizations={
        'Bearer': {'type': 'apiKey', 'in': 'header', 'name': 'Authorization'}
    },
    title='Flask Course Project 3',
    description='Welcome to the Swagger UI documentation site!',
    doc='/ui',
    contact_email='painassasin@icloud.com',
    version='1.4.0',
)
