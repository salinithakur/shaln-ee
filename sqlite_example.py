import sqlite3
sqliteConn = sqlite3.connect('first_example.db')
print('database connected')
cursor = sqliteConn.cursor()
print('database initialized')


create_table_query = """
CREATE TABLE IF NOT EXISTS emp (id integer primary key AUTOINCREMENT, name text);
"""

cursor.execute(create_table_query)

insert_table_query = """
INSERT INTO emp( name, address) VALUES ( "salini" ,"rajbiraj")
"""

cursor.execute(insert_table_query)
insert_table_query = """
INSERT INTO emp(name, address) VALUES( "ramita", "kavre")
"""
cursor.execute(insert_table_query)
insert_table_query = """
INSERT INTO emp(name, address) VALUES( "sagar", "kavre")
"""
cursor.execute(insert_table_query)
insert_table_query = """
INSERT INTO emp(name, address) VALUES( "milan", "kavre")

"""
cursor.execute(insert_table_query)
sqliteConn.commit()

sqliteConn.close()