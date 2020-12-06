from src import db
from src.model.trackModel import Track

class TrackRepository:
    
    def __init__(self):
        pass

    def get(self):
        return Track().query.filter().get()
