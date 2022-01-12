import numpy as np
import psycopg2
import pickle
import matplotlib.pyplot as plt
from PIL import Image
import os
import base64
from io import BytesIO

def create_db():
    # make connection
    conn = psycopg2.connect(
        database="postgres", user='admin', password='secret', host='db', port='5432'
    )
    conn.autocommit = True

# Creating a cursor object using the cursor() method
    cursor_create = conn.cursor()

# Check if DB already exists if not, then Create
    cursor_create.execute(
        "SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'mnist_prediction'")
    exists = cursor_create.fetchone()
    if not exists:
        cursor_create.execute('''CREATE DATABASE mnist_prediction''')
        print("Database created successfully........")
    else:
        print(("Database already existed and initialised successfully........"))


# Closing the connection
    conn.close()


# Example function call
create_db()


def create_table():
    # make connection
    conn = psycopg2.connect(
        database="mnist_prediction", user='admin', password='secret', host='db', port='5432'
    )

    cursor = conn.cursor()

# Droping Table if already exists
    cursor.execute("DROP TABLE IF EXISTS predictions")
    print("Table dropped and created again......")

# Create predictions table
    conn.commit()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS predictions(
        prediction_id INT GENERATED ALWAYS AS IDENTITY,
        prediction INT,
        filename VARCHAR,
        image BYTEA,
        date TIMESTAMP NOT NULL DEFAULT NOW(),
        PRIMARY KEY(prediction_id)

    )
    """
    )
    conn.commit()
    conn.close()


# #Call of Function example
# create_table()


def save_prediction_db(filename, image, prediction):
    # make connection
    conn = psycopg2.connect(
        database="mnist_prediction", user='admin', password='secret', host='db', port='5432'
    )

    cursor = conn.cursor()


# Persist training set into the db
    cursor.execute(
        """
    INSERT INTO predictions (prediction, filename, image)
    VALUES (%s,%s,%s)
    """,
        (prediction, filename, pickle.dumps(image))
    )

    conn.commit()
    conn.close()
# Example for function call
# save_prediction_db(filename, image, prediction )


def select_image_from_db():
    conn = psycopg2.connect(
        database="mnist_prediction", user='admin', password='secret', host='db', port='5432'
    )

    cursor = conn.cursor()
    
    cursor.execute(
    """
    SELECT image
    FROM predictions
    ORDER BY date DESC
    LIMIT 1
    """,
)
    # img_from_db = pickle.loads(cursor.fetchone()[0])
    img_from_db = pickle.loads(cursor.fetchone()[0])
    conn.commit()
    conn.close()
    
    img_from_db = np.asarray(img_from_db)
    print(type(img_from_db))
    # print(img_from_db.shape)
    print(img_from_db.shape)

    two_d = (np.reshape(img_from_db, (28, 28)) * 255).astype(np.uint8)
    plt.imsave(fname="test_readDB_test_photo.png",arr= two_d, cmap=plt.get_cmap('gray'))
    
    