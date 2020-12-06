from src.infra.model.resultModel import ResultErrorModel


class SendTrackContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, playload):

         person_id = playload.get('person_id')
  
         if not person_id:
            self.add_error('person_id', 'O ID da pessoa é obrigatorio.')

         return self.valid()
