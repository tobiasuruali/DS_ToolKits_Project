import pyjokes
import psycopg2
import pyjokes 

def create_jokes_db():
    #make connection
    conn = psycopg2.connect(
   database="postgres", user='admin', password='secret', host='localhost', port= '5432'
)
    conn.autocommit = True

#Creating a cursor object using the cursor() method
    cursor_create = conn.cursor()

#Check if DB already exists if not, then Create
# cursor.execute('''DROP DATABASE IF EXISTS ms3_jokes''')
    cursor_create.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'ms3_jokes'")
    exists = cursor_create.fetchone()
    if not exists:
        cursor_create.execute('''CREATE DATABASE ms3_jokes''')


#So DB can be created in transaction block

    print("Database created successfully........")

#Closing the connection
    conn.close()

create_jokes_db()



def fill_jokes_db():
    joke_list = pyjokes.get_jokes(category='all',language='en')
    print(len(joke_list))

# for i in enumerate(joke_list):
#     print(i, sep='\n')

    """ Creating DB -> Shifted to seperate script
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
"""

#make connection
    conn = psycopg2.connect(
   database="ms3_jokes", user='admin', password='secret', host='localhost', port= '5432'
)


    cursor = conn.cursor()

#Droping Table if already exists
    cursor.execute("DROP TABLE IF EXISTS joke")

#Creating table as per requirement
    sql_create_joke ='''CREATE TABLE IF NOT EXISTS joke (
  joke_id INT NOT NULL,
  joke_text TEXT NOT NULL,
  PRIMARY KEY (joke_id)
)'''

    cursor.execute(sql_create_joke)
    print("Table created successfully........")

    def insert_jokes():
        sql_insert_jokes = '''
INSERT INTO joke (joke_id, joke_text)
VALUES (%s, %s)
'''
        jokes_list_index = (i[0],i[1])
        cursor.execute(sql_insert_jokes, jokes_list_index)
    # print(sql_insert_jokes, jokes_list_index)
    for i in enumerate(joke_list): 
        insert_jokes()

    conn.commit()
#Closing the connection
    conn.close()

fill_jokes_db()