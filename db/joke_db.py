import pyjokes
import psycopg2
from pyjokes import jokes_de

joke_list = pyjokes.get_jokes(category='all',language='en')
print(len(joke_list))

# for i in enumerate(joke_list):
#     print(i, sep='\n')

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='admin', password='secret', host='172.17.0.1', port= '5432'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS JOKE")

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