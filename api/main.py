from flask_cors import CORS
from src import create_app, db
from flask_migrate import Migrate
from src.model import MODELS



app = create_app('dev')
Migrate(app, db)
CORS(app, support_credentials=True)



@app.shell_context_processor
def shell_context():
    return dict( 
        app=app,
        db=db,
        **MODELS
        )

if __name__ == '__main__':
    app.run(debug=True)