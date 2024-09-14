import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://@DESKTOP-4ID545F/clothesShop?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
