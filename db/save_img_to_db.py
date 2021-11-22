import numpy as np
import psycopg2
import pickle
import db_data_prep as data_preparation
import matplotlib.pyplot as plt


def create_image_db():
#make connection
    conn = psycopg2.connect(
   database="ms3_jokes", user='admin', password='secret', host='localhost', port= '5432'
)


    cursor = conn.cursor()

#Droping Table if already exists
    cursor.execute("DROP TABLE IF EXISTS images")

#Create input_data and predictions table with Foreign Keys 
    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS images (
        image_id INT GENERATED ALWAYS AS IDENTITY,
        name VARCHAR,
        image BYTEA,
        date TIMESTAMP NOT NULL DEFAULT NOW(),
        PRIMARY KEY (image_id)
    )
    """
)
    conn.commit()
    conn.close()

#Call of Function example
create_image_db()


def insert_random_image():
    #make connection
    conn = psycopg2.connect(
   database="ms3_jokes", user='admin', password='secret', host='localhost', port= '5432'
)
    cursor = conn.cursor()

    random_img_x, squeezed_random_img_x = data_preparation.random_img_sample()
# x_train = np.random.rand(1500,550)
    print(type(random_img_x.shape))

    name = 'Random Image X'

# sql_insert_array = """
#     INSERT INTO input_data (id, name, x_test_set)
#     VALUES (%s,%s,%s)
#     """
# sql_array = (i[0], 'X Training Set', x_train)

#Persist training set into the db
    cursor.execute(
    """
    INSERT INTO images (name, image)
    VALUES (%s,%s)
    """,
    (name, pickle.dumps(random_img_x))
)

#get array back from db
# id = '1'
    cursor.execute(
    """
    SELECT image
    FROM images
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

#now compare the 2 photos
    two_d = (np.reshape(squeezed_random_img_x, (28, 28)) * 255).astype(np.uint8)
    plt.imsave(fname="test_inserted_photo.png",arr= two_d, cmap=plt.get_cmap('gray'))

    two_d = (np.reshape(img_from_db, (28, 28)) * 255).astype(np.uint8)
    plt.imsave(fname="test_readDB_photo.png",arr= two_d, cmap=plt.get_cmap('gray'))
    
#in case you have pyplot and UI enabled on your machine you can also run plt.imshow()
    # plt.imshow(squeezed_random_img_x, cmap=plt.get_cmap('gray'))
    # plt.show()
    # plt.imshow(img_from_db, cmap=plt.get_cmap('gray'))
    # plt.show()

    print(img_from_db.shape)
    print(random_img_x.shape)
    conn.commit()
    conn.close()

insert_random_image()

