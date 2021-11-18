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
    CREATE TABLE input_data (
        id INT NOT NULL,
        name VARCHAR,
        x_test_set BYTEA,
        PRIMARY KEY (id)
    )
    """
)

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()


some_array_uuid = 'some_array'

cursor.execute(
    """
    INSERT INTO numpy_arrays(id, name, x_test_set)
    VALUES (1,'Training Set X' ,%s)
    """,
    (pickle.dumps(x_train))
)

