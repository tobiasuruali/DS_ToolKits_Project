import numpy as np
import psycopg2
import pickle
from tensorflow import keras

#make connection
conn = psycopg2.connect(
   database="milestone_3", user='admin', password='secret', host='localhost', port= '5432'
)


cursor = conn.cursor()

#Droping Table if already exists
cursor.execute("DROP TABLE IF EXISTS input_data")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS input_data (
        id INT NOT NULL,
        name VARCHAR,
        x_test_set BYTEA,
        PRIMARY KEY (id)
    )
    """
)

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# x_train = np.random.rand(1500,550)

id = '1'
name = 'Training Set X'

# sql_insert_array = """
#     INSERT INTO input_data (id, name, x_test_set)
#     VALUES (%s,%s,%s)
#     """
# sql_array = (i[0], 'X Training Set', x_train)

#Persist training set into the db
cursor.execute(
    """
    INSERT INTO input_data (id, name, x_test_set)
    VALUES (%s,%s,%s)
    """,
    (id, name, pickle.dumps(x_train))
)

#get array back from db
id = '1'
cursor.execute(
    """
    SELECT x_test_set
    FROM input_data
    WHERE id=%s
    """,
    (id,)
)
x_train_from_db = pickle.loads(cursor.fetchone()[0])

print(x_train_from_db.shape)
print(x_train.shape)
conn.commit()
conn.close()
