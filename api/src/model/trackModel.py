from src import db

class Track(db.Model):
    __tablename__ = 'track'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    filename = db.Column(db.String(128), nullable=False)
    size = db.Column(db.Float, nullable=False)

    def __init__(self, data):
        self.name = data.get('name')
        self.filename = data.get('filename')
        self.size = data.get('size')
 