from src.infra.model.resultModel import ResultErrorModel

class PlayTrackContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, _id):
         if (not _id.isnumeric()):
             self.add_error('id', 'O parametro precisa ser numerico.')
             return self.valid()
         return self.valid()
