from flask_restplus import Api
from src.routes.track import route as track

routes = Api(
    title='Api de Musicas Cliquei Mudei',
    version='1.0',
    description='API desafio para processo seletivo ',
)

routes.add_namespace(track)