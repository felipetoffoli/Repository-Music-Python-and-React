from src.contract.tracks.playTrackContract import PlayTrackContract
from src import contract
from flask import request
from src.contract.tracks.sendTrackContract import SendTrackContract
from src.infra.model.resultModel import ResultModel
from src.repository.trackRepository import TrackRepository
import os
from datetime import datetime
from flask import Response



class TracksHandler:
    def __init__(self):
        pass

    def __parse_int_or_value_default(self, data, value_default=1):
        if data and data.isnumeric():
            return int(data)
        return value_default

    def get_paginate(self):
        try:
            params = request.args
            page = self.__parse_int_or_value_default(params.get('page'))
            limit = self.__parse_int_or_value_default(params.get('limit'), 10)
            repository = TrackRepository()
            paginate = dict(page=page, per_page=limit)
            
            return repository.get_paginate(paginate)
        except Exception as e:
            return ResultModel('Erro ao acessar o banco de dados.', False, True, str(e)).to_dict(), 500

  
        

    def play(self, _id):
        contract = PlayTrackContract()
        if not(contract.validate(_id)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        repository = TrackRepository()
        _id = int(_id)
        track_result = repository.get_by_id(dict(id=_id))
        if track_result.get('error') or track_result.get('exeption'):
            return track_result, 406
        track = track_result['data']['result']
        filename = track.get('filename')
        def generate():
            with open(os.getcwd()+ f"/src/tracks/{filename}", "rb") as fwav:
                data = fwav.read(1024)
                while data:
                    yield data
                    data = fwav.read(1024)
        return Response(generate(), mimetype="audio/mp3")
    
    def send(self):
        playload = request
        contract = SendTrackContract()
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        name = playload.form.get('name')
        name = name.title().strip()
        iso_date_str = datetime.isoformat(datetime.now()).replace(':', '.')
        real_filename = playload.files.get('file').filename.split('.mp3')[0]
        new_filename = f'{real_filename}-{iso_date_str}.mp3'
        save_path =  f'{os.getcwd()}/src/tracks/'
        abisolute_path = os.path.join(save_path, new_filename)
        file = request.files['file']
        file.save(abisolute_path)
        file_size = os.stat(abisolute_path).st_size
        repository = TrackRepository()
        data_insert = {'filename': new_filename, 'name': name, 'size': file_size}
        result = repository.insert(data_insert)
        return result
        
