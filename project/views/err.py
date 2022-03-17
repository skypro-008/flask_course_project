from flask_restx import fields, Namespace

error_ns = Namespace('')
error = error_ns.model('Сообщение об ошибке', {'message': fields.String, })
