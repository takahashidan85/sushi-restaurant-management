# Provide db to models by importing from app.extensions
from app.extensions import db
from .models import define_models
# define_models(db) will be used by services
