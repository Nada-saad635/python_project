import sqlite3
import pandas as pd
conn = sqlite3.connect('STAFF.db')
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']
file_path = r'C:\Users\hp\OneDrive\Desktop\smster1.1\projects\STAFF.db'


try:
    df = pd.read_csv(file_path, names=attribute_list, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(file_path, names=attribute_list, encoding='ISO-8859-1')

df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
