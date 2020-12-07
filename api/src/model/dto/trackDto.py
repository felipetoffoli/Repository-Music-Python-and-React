from flask_restplus import fields

TRACK_DTO = {
        'name': fields.String,
        'filename': fields.String,
        'size': fields.Float
}