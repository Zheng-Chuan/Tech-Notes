import os
import pymysql
import pandas as pd

host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DATABASE')

conn = pymysql.connect(
    host=host,
    port=int(3306),
    user="root",
    passwd=password,
    db="[YOUR_DB_NAME]",
    charset='utf8mb4')

df = pd.read_sql_query("SELECT * FROM YOUR_TABLE",
    conn)
df.tail(10)