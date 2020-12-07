from src.model.dto.trackDto import TRACK_DTO
from src import db
from src.model.trackModel import Track
from src.infra.model.resultModel import ResultModel
from flask_restplus import marshal


class TrackRepository:
    
    def __init__(self):
        pass

    def get(self):
        return Track().query.filter().get()

    def get_by_id(self, playload):
        try:
            _id = playload.get('id')
            track = Track.query.get(_id)
            if not track:
                return ResultModel('ID não encontrado', False, True).to_dict()
            result = marshal(track, TRACK_DTO)
            return ResultModel('Sucesso', result, False).to_dict()
        except Exception as e:
            return ResultModel('Problema ao acessar banco de dados', False, True, str(e)).to_dict()
    
    def insert(self, data):
        try:
            track = Track(data)
            db.session.add(track)
            db.session.commit()
            return ResultModel('Sucesso', True, False).to_dict()
        except Exception as e:
            return ResultModel('Falha ao salvar dados', False, True, str(e)).to_dict()

