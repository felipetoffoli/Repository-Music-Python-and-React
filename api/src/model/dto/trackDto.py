from flask_restplus import fields

TRACK_DTO = {
        'id': fields.Integer,
        'name': fields.String,
        'filename': fields.String,
        'size': fields.Float
}