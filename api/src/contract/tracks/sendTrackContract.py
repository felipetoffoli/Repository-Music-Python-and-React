from src.infra.model.resultModel import ResultErrorModel
import re

class SendTrackContract(ResultErrorModel):
    def __init__(self):
        super().__init__()

    def validate(self, playload):
         if (not playload.form):
             self.add_error('Multipart Form', 'Os dados precisam serem enviados no formato "Multipart Form".')
             return self.valid()
            
         if not playload.files:
             self.add_error('Multipart Form', 'O arquivo precisa ser enviado no formato "Multipart Form".')
             return self.valid()
            
         if not playload.form.get('name'):
             self.add_error('name', 'O parametro name é obrigatorio.')
         
         if not playload.files.get('file'):
             self.add_error('file', 'O arquivo é obrigatorio.')
        
  
         if playload.files.get('file') and playload.files.get('file').filename and not re.search(r'mp3$', playload.files.get('file').filename):
             self.add_error('file', 'O arquivo precisa ser mp3.')
  
         return self.valid()
