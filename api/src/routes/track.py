from flask_restplus import Namespace, Resource


route = Namespace('tracks', description='Rota de que lida com as musicas que estão nas pastas de track')

DOC_SEND = route.parser()
DOC_SEND.add_argument('name', type=str, help='Nome da musica.', location='form')
DOC_SEND.add_argument('file', type=bytes, help='Arquivo MP3.', location='files')

DOC_SEARCH = route.parser()
DOC_SEARCH.add_argument('search', required=True, location='args')

DOC_LIST = route.parser()
DOC_LIST.add_argument('page',  location='args', type=str)
DOC_LIST.add_argument('limit',  location='args', type=str)

@route.route('/list')
class TrackList(Resource):
    @route.doc('list_tracks')
    @route.expect(DOC_LIST)
    def get(self):
        '''List all tracks'''
        from src.handler.tracksHandler import TracksHandler
        return TracksHandler().get_paginate()

@route.route('/search')
class TrackList(Resource):
    @route.doc('search')
    @route.expect(DOC_SEARCH)
    def get(self):
        '''Search tracks'''
        from src.handler.tracksHandler import TracksHandler
        return TracksHandler().get_by_like_name_paginate()


@route.route("/play/<_id>")
class PlayMp3(Resource):
    @route.doc('play')
    def get(self, _id):
        from src.handler.tracksHandler import TracksHandler
        return TracksHandler().play(_id)
        
@route.route("/")
class PlayMp3(Resource):
    @route.doc('send_files')
    @route.expect(DOC_SEND)
    def post(self):
        from src.handler.tracksHandler import TracksHandler
        return TracksHandler().send()
