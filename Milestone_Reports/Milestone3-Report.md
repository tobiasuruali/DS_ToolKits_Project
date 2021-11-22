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
database="ms3_jokes", user='admin', password='secret', host='db', port= '5432'
```
With the cursor class we can use Python code to execute PostgreSQL command in our database. An example of cursor.

```
#Droping Table if already exists
cursor.execute("DROP TABLE IF EXISTS joke")
```

**Download the PGADMIN Tool (https://www.pgadmin.org/download/). It also exists as a Docker Image :) Connect to your running PostgreSQL Database. Can you see your database and table?**

- We load a Docker Image of PGAdmin (dpage/pgadmin4:6.0). This allows to see the database and the table contained in it. 

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


**Describe Process and Difficulties**

1. How is your data structured (you can download and load it from the source. Some of you may use the Keras function to download it).

- 

1. Explain how you would define your relational database tables in terms of their attributes to save your data. What kind of data types could you use
(https://www.postgresql.org/docs/12/datatype.html) 

3. What additional relational database table attributes might make sense to easily query your data (f.e. find all pictures of giraffes)



 ## Task 4 Docker Compose Backend

 **Create Docker-Compose file for whole Backend**
 
 
**Structuring of DB**


**Wait-for-it.sh and Scheduling**