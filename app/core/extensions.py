from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
swagger = Swagger()
cors = CORS()
