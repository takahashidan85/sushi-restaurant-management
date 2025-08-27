import os

class Config:
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "supersecretkey"
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://sa:Ahihi1234!@localhost\\SQLEXPRESS/SushiDB?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
