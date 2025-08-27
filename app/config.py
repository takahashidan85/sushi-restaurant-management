import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///sushi.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://sa:Ahihi1234!@localhost\\SQLEXPRESS/SushiDB?driver=ODBC+Driver+17+for+SQL+Server"
