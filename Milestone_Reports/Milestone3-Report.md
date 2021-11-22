# Milestone 3
## Task 1 Docker-Compose

**Which services are being used for the application (described in the link above)? How do they relate to the host names in terms of computer networks?**

- Short answer, web and redis are the services used by the application. Web allows the docker contained application and the local machine to use the exposed port. Redis load the redis image, to be used as a data structure server. They use the ip address 127.0.0.1, the localhost. They communicate by using the exposed port 5000. The dockerized application run locally on the machine, and we can access though the local host directory at the port 5000. 
- In details, the link https://docs.docker.com/compose/gettingstarted/ shows how to leverage docker to create a small application running in a docker environment and accesible through the local network. It contains the following elements: a simple application written in Python, a dockerfile, a docker-compose and the requirements.
- The application defines what will happen, after we access to the exposed port. It is a counter on how many times we have accessed the port. The dockerfile specify which docker image to build. This allows us to load predefined environments (in this case python:3.7-alpine), the requirements and the port to be used. This will ensure that all the dependencies are correctly loaded. The docker-compose allows us to manage all the services for Docker. In this example, web and redis. With the compose up command, the aformentioned services and the dockerfile are started. 

**What ports are being used (within the application and in the docker-compose file)?**

- The port 5000 is used by the dockerfile and the dockercompose. The Flask web server uses the same port. The redis service uses port 6379. 

**How does the host machine (e.g. your computer) communicate with the application inside the Docker container. Which ports are exposed from the application to the host machine?**

- The host machine, in my example my laptop have stored locally the necessary information to pull from the internet a dockerized environment, wiht all the necessary dependencies. As long as I can join the localhost at the exposed port 5000 (http://localhost:5000 or the equivalent http://127.0.0.1:5000/ ), I can interact with the dockerized application. 

**What is localhost, why is it useful in the domain of web applications?**
- Localhost refers to the device we are using. If we are on our laptop it would be the laptop. It is the default name used to establish a connection from our device. The default address is 127.0.0.1 (usually, but the range goes from 127.0.0.0 to 127.255.255.255). It is useful because this range of ip addresses are reserved for loopback communication, so that we can only connect to our local machine. It is often used for testing web applications, like in our docker-compose example.  

## Task 2 PostgreSQL & JokesDB

**What is PostgreSQL? Is it SQL or no-SQL (why?)**

- PostgreSQL is an open source object-relational database system, based on SQL (Structured Query Language), with a strong focus on data integrity and reliability. In PostgreSQL, data is often stored as a table. It follows SQL standards albeit in some scenarios there might be difference in syntax. It allows to define new data types, write code in several programming language (including python) and build custom functions. With PostgreSQL we can create, maintain, update and query a relational database. 
- A no-sql database system (like MongoDB) tackle a different necessity, where it is more important to access in a short time to large data set, at the expense of data reliability and consistency (e.g. an entry might not be unique). Usually no-sql databases don't use tables to store data but document, key-value, graph, or wide-column stores. NoSQL databases are non-relational, with dynamic schemas to store unstructured data. 

**Run a PostgreSQL Server (current version is 14.0) using a Docker image from the official PostgreSQL Docker Hub page**

- We create a docker-compose with 2 services. The first service is built around the postgres:14.1 image and it allows to host the PostgreSQL database. The second will allow to manage the PostgreSQL database. To do that we are using the pgAdmin4 tool, and we used the official image. Some details on how the docker-compose is set up. We are adding the policy "restart: always" which allows to restart all stopped and running services. In addition, we are specifying the credential to access the database, the port which will be exposed and the volumes used. 

**Make sure you expose the correct ports when running the Docker container (read the documentation on Docker Hub)** 

- The official documentation https://docs.docker.com/samples/postgresql_service/ uses the port 5432 and we exposing the same port. A problem arised for 1 of the 2 machines. In one instance the port was already used by a another service. For that reason, we had to identify the process id and terminate the process to avoid being unable to expose the port 5432 to our docker container. 

**Find an appropriate Python package (Postgres adapter) that allows you to communicate with the database server**

- As a Postgres adapter we are using "psycopg" https://www.psycopg.org/ . It supports the Python version used in this project, it is popular and with good documentation. 

**Write a little python script**

To establish the connection from the database server and our local machine we are leveraging the package psycopg. It allows to pass the information to access to the database itself.

```
database="ms3_jokes", user='admin', password='secret', host='localhost', port= '5432'
```
With the cursor class we can use Python code to execute PostgreSQL command in our database. An example of filling our jokes_db with a list of jokes.

```
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
```

To then the if the database was filled, we open pgadmin (http://localhost:5050), connect to the database server and write a quick SELECT statement like the following:

  ![JokesDB in PG Admin](https://github.com/tobiasuruali/DS_ToolKits_Project/blob/ce22e6eff2916e0599e978fa006b47b3ba2bc755/Milestone_Reports/images/jokes_select_db.PNG)

**Instruction to Recreate**
1. After running the db/docker-compse.yml and reassuring that pgadmin are up and running
2. Run the main_joke.py script ```python3 db/main_joke.py```
3. Refresh your database and see the new *ms3_jokes* DB and new *jokes* table filled with jokes

**Download the PGADMIN Tool (https://www.pgadmin.org/download/). It also exists as a Docker Image :) Connect to your running PostgreSQL Database. Can you see your database and table?**

- We load a Docker Image of PGAdmin (dpage/pgadmin4:6.0). This allows to see the database and the table contained in it. 
When first initizialing you will need to "create server..". You simply give it a name and in the "Connections Tab" you can type in "db", leave the port number, and type "admin" as the username and "secret" as the pw.  

**If you stopped and deleted the Docker container running the database and restarted it. Would your joke still be in the database? Why or why not?** 
- Yes, it would be available locally on our machines. This is based on how we set up the docker-compose script. In our setup the database use the following volume.: 
  
volumes:
      - db-data:/var/lib/postgresql/data 
- As mentioned in the official docker documentation (https://docs.docker.com/storage/volumes/) a volume is the official way for persisting data generated by and used by Docker containers. If we needed to have large volumes of data, maybe even different from a normal SQL table, there would be more efficient way to store data, like the Amazon S3 service. In our scenario, where we have only a table of jokes, storing it in a database is enough. 
If we were not using volumes, by stopping and deleting the Docker container, the database would be lost. 
However, by using volumes, the changes that are written in the dockerized application are stored in the volume. In this way, it's like we mounted our physical local storage to the virtual file system of Docker, allowing the dockerized application to read and write our volume. 
## Task 3 Save Image into Database

**How do you need to represent/transform image data to save it to a relational database?**

- Relational database are not ideal to store images. A better way to store pictures in a database is to save the pictures on a separate data container and then reference them in the database. In this way, it is possible to avoid 2 major drawbacks: 
1) It is not efficient, as relational databases like PostgreSQL are not optimized for pictures.
2) You loose many of the functionalities of a relational databases, by storing the pictures directly in a BLOB field (Binary Large Object)

Since our MNIST image samples are pretty small, we can save them as either **BYTEA** or **BLOB** Datatypes. We decided to go with **BYTEA**  

**Instruction to Recreate**
1. After running the db/docker-compse.yml and reassuring that pgadmin are up and running
2. Run the main_img.py script ```python3 db/main_img.py```
3. Refresh your database and see the new *image* table inside the *ms3_jokes* db filled with with an image row. Make sure you run the main_jokes.py script prior to running this. Since the database only gets created in that module.

**Describe Process and Difficulties**

1. How is your data structured (you can download and load it from the source. Some of you may use the Keras function to download it).

- For the images database we decided to use our current MNIST dataset of hand written digits. We load it with the help of Keras, the images are stored as multi dimensional numpy arrays with multiple records. We reshape it to a 28x28x1 dimensional array and select one single picture by random as such:
````
#define random Number and select that img from dataset
    random_single_number = random.randint(0,9999)
    random_plus_one = random_single_number + 1 
    print('Random number selected in array:', random_single_number)
    random_img_x = x_test[random_single_number:random_plus_one]
    squeezed_random_img_x = np.squeeze(x_test[random_single_number:random_plus_one], axis=0)
    print('Shape random img: ', random_img_x.shape, 'Shape random img squeezed:', squeezed_random_img_x.shape)
    return random_img_x, squeezed_random_img_x
````

  - Firstly, we create a table for our images to be stored with the help of psycopg2
  - Then we load a random image (in form of a nparray) from the *db_data_prep.random_img_sample() function and module. 
  - The selected image then get loaded into the *image* table with help of serialization (**pickle**).
  - With help of the timestamp, a select statement can be run (to receive the latest entry). Python' **pickle** helps us to de-serialize the data and we can then either show or save the images with the help of pyplot. To *imsave* the image you will have assure that the image is a 2D np array.:
  
````
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

````


2. Explain how you would define your relational database tables in terms of their attributes to save your data. What kind of data types could you use
(https://www.postgresql.org/docs/12/datatype.html) 
- For the image id and the prediction id, we utilize integers. They have a limit in range but this would never be a problem in our small application. In addition, it is easy to create consecutives integers. The picture itself can be stored as bytea. This allow the possibility to store the picture in a separate database and serve multiple tables, in case of expansion of the application- 
In addition to the ID to identify each picture, we can store additional information like the date (as timestamp) and a name (as varchar).
As the purpose of the application is to identify a handwritten digit, the prediction should be stored as an integer as well. 

3. What additional relational database table attributes might make sense to easily query your data (f.e. find all pictures of giraffes)

- To expand the scope of the application we could (hypothetically) have multiple prediction models, to accomodate different categories, expanding from the sphere of character recognition. In order to achieve we can create a table to store different categories, with as a classified_category (as varchar). The table would also contain the image id (as int) and the image (as a bytea). In this way, we a first classifier, to identify the type of category and on a second stage a more refined model, trained for that category. We expect that some of the weights learned by the model might be similar and a single model could be optimized for each category. 


 ## Task 4 Docker Compose Backend

  **Create Docker-Compose file for whole Backend**
 ````
docker-compose -f "docker-compose.yml" up -d --build 
 ````
 
**Structuring of DB**

We decided to create a simple table structure for our current data set. We defined the following tables and columns: 

  ![ERD Backend](https://github.com/tobiasuruali/DS_ToolKits_Project/blob/ce22e6eff2916e0599e978fa006b47b3ba2bc755/Milestone_Reports/images/erd_db.png)

We figured that for what now these are the essential columns:  
*input_data:*  
name_id, name, image, date (timestamp)  

*predictions:*  
prediction_id, prediction, *image_id*  

the date column helps us retrieve the correct persisted picture that we then retrieve for our prediction. *image_id* is the **FOREIGN KEY** used to link the prediction with the specific picture. 

**Scheduling**
- For the scheduling we noticed that a waitfor.sh was not necessary in our use case. We attempted to run the whole backend and there were no scheduling conflict due to code added to the docker-compose:

````
  ...
  dstoolkitsproject:
    image: dstoolkitsproject:1.0.6
    build:
      context: .
      dockerfile: ./dockerfile
    volumes:
      - .:/app
    depends_on:
      - db
...
````

the ***depends_on*** statement makes sure this service part does not get run till the db: service is done.