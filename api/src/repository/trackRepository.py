from src import db
from src.model.trackModel import Track
from src.infra.model.resultModel import ResultModel


class TrackRepository:
    
    def __init__(self):
        pass

    def get(self):
        return Track().query.filter().get()
    
    def insert(self, data):
        try:
            track = Track(data)
            db.session.add(track)
            db.session.commit()
            return ResultModel('Sucesso', True, False).to_dict()
        except Exception as e:
            return ResultModel('Falha ao salvar dados', False, True, str(e)).to_dict()

