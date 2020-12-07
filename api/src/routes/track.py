from flask_restplus import Namespace, Resource, fields
from flask import  Response, request
import os



route = Namespace('tracks', description='Rota de que lida com as musicas que estão nas pastas de track')

DTO_TRACK_LIST = route.model('Track', {
    'name': fields.String(required=True, description='Nome do arquivo de musica')
})


DTO_INFO_FILE_TRACK = route.model('Track Information', {
    'name': fields.String(required=True, description='Nome do arquivo de musica'),
    'time': fields.String(required=False, description='Tempo de duração da musica'),
    'size': fields.String(required=True, description='Tamanho do arquivo de musica'),
})

# DTO_SEND_TRACK = route.model('Track Information', {
# })


@route.route('/')
class TrackList(Resource):
    @route.doc('list_tracks')
    @route.marshal_list_with(DTO_TRACK_LIST)
    def get(self):
        '''List all tracks'''
        return [{'name': 'musica1.mp3'}, {'name': 'musica2.mp3'}]


@route.route('/<info_file>')
class TrackInfo(Resource):
    @route.doc('info_file')
    @route.marshal_with(DTO_INFO_FILE_TRACK)
    def get(self, info_file):
        '''informação da track'''
        return {'name': 'musica1.mp3', 'size': '18MB', 'time': '01:15'}


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
        