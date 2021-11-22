import numpy as np
import psycopg2
import pickle
import data_preparation as data_preparation
import matplotlib.pyplot as plt
from tensorflow import keras
import model_inspection as inspection

def create_milestone3_db():
    #make connection
    conn = psycopg2.connect(
   database="postgres", user='admin', password='secret', host='db', port= '5432'
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
#Example function call
# create_milestone3_db()


def create_input_pred_db():
#make connection
    conn = psycopg2.connect(
   database="milestone_3", user='admin', password='secret', host='db', port= '5432'
)


    cursor = conn.cursor()

#Droping Table if already exists
    cursor.execute("DROP TABLE IF EXISTS input_data")

#Create input_data and predictions table with Foreign Keys 
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS input_data (
        image_id INT GENERATED ALWAYS AS IDENTITY,
        name VARCHAR,
        image BYTEA,
        date TIMESTAMP NOT NULL DEFAULT NOW(),
        PRIMARY KEY (image_id)
    )
    """
)
    conn.commit()
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS predictions(
        prediction_id INT GENERATED ALWAYS AS IDENTITY,
        prediction INT,
        PRIMARY KEY(prediction_id),
        image_id INT REFERENCES input_data (image_id)  
    )
    """
)
    conn.commit()
    conn.close()

# #Call of Function example
# create_input_pred_db()


def insert_load_random_image():
    #make connection
    conn = psycopg2.connect(
   database="milestone_3", user='admin', password='secret', host='db', port= '5432'
)


    cursor = conn.cursor()


    random_img_x, squeezed_random_img_x = data_preparation.random_img_sample()
# x_train = np.random.rand(1500,550)
    print(type(random_img_x.shape))

    name = 'Test Image X'

# sql_insert_array = """
#     INSERT INTO input_data (id, name, x_test_set)
#     VALUES (%s,%s,%s)
#     """
# sql_array = (i[0], 'X Training Set', x_train)

#Persist training set into the db
    cursor.execute(
    """
    INSERT INTO input_data (name, image)
    VALUES (%s,%s)
    """,
    (name, pickle.dumps(random_img_x))
)

#get array back from db
# id = '1'
    cursor.execute(
    """
    SELECT image
    FROM input_data
    ORDER BY date DESC
    LIMIT 1
    """,
    # (id,)
)
    img_from_db = pickle.loads(cursor.fetchone()[0])

# #OR Select Random row 
# cursor.execute(
#     """
#     SELECT image FROM input_data
#     ORDER BY RANDOM()
#     LIMIT 1    
#     """
        
    
# )

    conn.commit()
    conn.close()
    return random_img_x,squeezed_random_img_x,img_from_db
#Example for function call
# random_img_x, squeezed_random_img_x, img_from_db = insert_load_random_image()



def predict_and_persist(img_from_db, loaded_model):
    #make connection
    conn = psycopg2.connect(
   database="milestone_3", user='admin', password='secret', host='db', port= '5432'
)


    cursor = conn.cursor()

    num_classes, input_shape, x_train, y_train, x_test, y_test = data_preparation.prepare_data()

# It can be used to reconstruct the model identically.
    # loaded_model = keras.models.load_model("keras_model.h5")

# Predicting something with loaded_model
    prediction  = loaded_model.predict(img_from_db)
# print(prediction)

#convert to int array 
    int_single_prediction = np.argmax(prediction, axis = 1)
    int_single_prediction = int(int_single_prediction)
    print('Predictions array:', int_single_prediction, type(int_single_prediction))

    cursor.execute(
    """
    SELECT image_id
    FROM input_data
    ORDER BY date DESC
    LIMIT 1
    """,
    # (id,)
)
    get_foreign_key = (cursor.fetchone()[0])

    cursor.execute(
    """
    INSERT INTO predictions (prediction, image_id)
    VALUES (%s,%s)
    """,
    (int_single_prediction, (get_foreign_key))
)


    conn.commit()
    conn.close()

# #Save the 2 photos
# two_d = (np.reshape(squeezed_random_img_x, (28, 28)) * 255).astype(np.uint8)
# plt.imsave(fname="test_inserted_photo.png",arr= two_d, cmap=plt.get_cmap('gray'))

# two_d = (np.reshape(img_from_db, (28, 28)) * 255).astype(np.uint8)
# plt.imsave(fname="test_readDB_photo.png",arr= two_d, cmap=plt.get_cmap('gray'))


# print(img_from_db.shape)
# print(random_img_x.shape)


# #Example for function call
# loaded_model = inspection.load_model()
# predict_and_persist(img_from_db, loaded_model)
