from flask import request
from src.contract.tracks.sendTrackContract import SendTrackContract
from src.infra.model.resultModel import ResultModel
from src.repository.trackRepository import TrackRepository

class TracksHandler:


    def play(self, id):
        pass
    
    def send(self):
        playload = request.form
        contract = SendTrackContract()
        if not(contract.validate(playload)):
            return ResultModel('Problema nos parametros enviados.', False, contract.errors).to_dict(), 406
        