from flask_restplus import Namespace, Resource, fields


route = Namespace('tracks', description='Rota de que lida com as musicas que estão nas pastas de track')

DTO_TRACK_LIST = route.model('Track', {
    'name': fields.String(required=True, description='Nome do arquivo de musica')
})


DTO_INFO_FILE_TRACK = route.model('Track Information', {
    'name': fields.String(required=True, description='Nome do arquivo de musica'),
    'time': fields.String(required=False, description='Tempo de duração da musica'),
    'size': fields.String(required=True, description='Tamanho do arquivo de musica'),
})


@route.route('/')
class TrackList(Resource):
    @route.doc('list_tracks')
    def get(self):
        '''List all tracks'''
        from src.handler.tracksHandler import TracksHandler
        return TracksHandler().get_paginate()


@route.route("/play/<_id>")
class PlayMp3(Resource):
    @route.doc('play')
    def get(self, _id):
        from src.handler.tracksHandler import TracksHandler
        return TracksHandler().play(_id)
        
@route.route("/")
class PlayMp3(Resource):
    @route.doc('send_files')
    def post(self):
        from src.handler.tracksHandler import TracksHandler
        return TracksHandler().send()
        