import mysql.connector
from sqlalchemy import create_engine

def db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='inventorymanagementsystem'
    )

# SQLAlchemy engine for Pandas reports
engine = create_engine("mysql+mysqlconnector://root:root@localhost/inventorymanagementsystem")