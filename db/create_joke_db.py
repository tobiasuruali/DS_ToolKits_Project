import psycopg2

#make connection
conn = psycopg2.connect(
   database="postgres", user='admin', password='secret', host='localhost', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor_create = conn.cursor()

#Preparing query to create a database
sql_create_db = '''CREATE database ms3_jokes''';

#Creating a database
cursor_create.execute(sql_create_db)
#So DB can be created in transaction block

print("Database created successfully........")

#Closing the connection
conn.close()