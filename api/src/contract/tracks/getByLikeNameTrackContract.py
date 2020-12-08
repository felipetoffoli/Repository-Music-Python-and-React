from src.infra.model.resultModel import ResultErrorModel

class GetByLikeNameTrackContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, playload):
        
        if (not playload):
            self.add_error('json', 'Os dados precisam serem enviados no formato "JSON".')
            return self.valid()
        
        search = playload.get('search')

        if not search:
            self.add_error('search', 'O parametro é obrigatrio.')
            return self.valid()

        if search and type(search) != str:
            self.add_error('search', 'O parametro precisa estar em formato de texto.')
            return self.valid()
            
        return self.valid()
