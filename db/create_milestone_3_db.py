import psycopg2

#make connection
conn = psycopg2.connect(
   database="postgres", user='admin', password='secret', host='localhost', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor_create = conn.cursor()

#Check if DB already exists if not, then Create
# cursor.execute('''DROP DATABASE IF EXISTS ms3_jokes''')
cursor_create.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'milestone_3'")
exists = cursor_create.fetchone()
if not exists:
    cursor_create.execute('''CREATE DATABASE milestone_3''')


#So DB can be created in transaction block

print("Database created successfully........")

#Closing the connection
conn.close()