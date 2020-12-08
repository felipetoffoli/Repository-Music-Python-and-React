from flask_restplus import fields

PAGINATE = {
    'page' : fields.Integer,
    'pages' : fields.Integer,
    'per_page' : fields.Integer,
    'prev_num' : fields.Integer,
    'total' : fields.Integer
}