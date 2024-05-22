import sqlite3
sqliteconn = sqlite3.connect('first_example.db')
print('database connected')
cursor = sqliteconn.cursor()
print('database initialized')

sql_read_query = "SELECT * FROM emp;"
cursor.execute(sql_read_query)
print(cursor.fetchall())

sqliteconn.close()
      