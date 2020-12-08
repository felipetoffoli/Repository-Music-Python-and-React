from flask_restplus import marshal
from src import db
from src.model.dto.trackDto import TRACK_DTO
from src.model.trackModel import Track
from src.infra.model.resultModel import ResultModel
from src.infra.model.dto.paginateDto import PAGINATE



class TrackRepository:
    
    def __init__(self):
        pass

    def get_paginate(self, paginate):
        tracks = Track.query.filter().paginate(**paginate)
        data_paginate = marshal(tracks, PAGINATE )
        data_paginate = dict(
            page=data_paginate.get('page'),
            pages=data_paginate.get('pages'),
            total=data_paginate.get('total'),
            limit=data_paginate.get('per_page'),
            prev_num=data_paginate.get('prev_num'),
            )
        data = marshal(tracks.items, TRACK_DTO)
        return ResultModel('Pesquisa realizada com sucesso.', data, False).to_dict(data_paginate)

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

