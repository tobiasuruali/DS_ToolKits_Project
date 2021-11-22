# **DS_ToolKits_Project**

Toolkit Usage and Python Development by Tobias Hoesli & Marco Colombatti

# *Build Instructions* 

These are instructions on how to run this directory's python scripts with a Python3 VirutalEnvironment on Ubuntu/MacOS or Windows machine.

## **Ubuntu/MacOS**
### **Download Python3.8**

1. Check if python3 is already installed

````
python3 --version
````

2. If the python level is lower than 3.8 or not installed, continue with the next step:  
Update and Refresh Repository List:

```
sudo apt-get update
```
3. Install Python3.8

```
sudo apt-get install python3.8
```

4. Check if it's the Version downloaded:
```
python --version
```

### **PIP & Virtual Environment**
1. Install pip for python3. (Pip is a package manager for python)
```
apt install python3-pip
``` 
2. The **venv** command is used to create python virtual environments. virutalenv allows you to avoid installing packages globally and ensures your project will run on the correct dependencies.
We can download virutalenv using pip.

```
python3 pip install venv
```
3. Create a Virutal Environment in the your projects directory i.e. `cd myProject` to ensure all dependencies are installed correctly.

```
python3 -m venv my_env_project
```

4. Activate the environment

```
source my_env_project/bin/activate
```

5. Check if your python interpreter is now set as the Virutal Environment just created (The directory should be `.../my_env_project/bin/python`):

```
which python 
```

6. If you want to switch projects or leave the virutal environment, run:
```
deactivate
```

### **Install Packages, Clone Github Repo and Run Script**

Before coping our Repo you need to insure that all packages are installed on the virtual environment:
For the `mnist_convnet.py` Script the packages **numpy** and **tensorflow** are required.

1.  Install numpy and tensorflow on your virtual environment:
```
python3 -m pip install numpy
```
```
python3 -m pip install tensorflow
```

2. Make sure that all packages were installed correctly on your virtualenv (make sure your environment is still active **(my_env_project)** should be at the beginning of the command line):
```
python3 -m pip freeze
```

3. When all packages were downloaded correctly, this gitrepo can be cloned on to your system. Make sure git is installed with `git --version`, otherwise install it:

```
sudo apt install git
```
4. Clone this repository in the desired directory

```
git clone https://github.com/tobiasuruali/DS_ToolKits_Project.git
```

5. Run the script

```
python3 Milestone1.py
```

## **Jupyter Notebook**
For anyone running into complications or with the preference to work with Jupyter:

1. Download Jupyter with pip

```
pip install jupyter
```

2. Change to the directory this repo is saved on, and open with Jupyter. 

```
jupyter notebook
```

3. Run the code.


# **Instructions for DOCKER-COMPOSE**
To run the whole Container Backend of our image prediction application, follow these steps:
   1. Make sure you have docker and docker-compose installed
   2. Open our main directory in your terminal and run the following code:
 ````
docker-compose -f "docker-compose.yml" up -d --build 
 ````
The docker images should start completely building. After all the services (PGAdmin & DB) are run the Tensorflow container will start creating a model, fit it. A random image will then be loaded into the DB input_data table. Our script will retrieve it and run our model on it to predict what digit the image is.
The prediction will then be persisted into a predicitons table and the script will succesfully terminate. 


## **Instruction for JOKES TABLE**
1. After running the db/docker-compse.yml and reassuring that pgadmin are up and running
2. Run the main_joke.py script ```python3 db/main_joke.py```
3. Refresh your database and see the new *ms3_jokes* DB and new *jokes* table filled with jokes

## **Instruction for IMAGE TABLE**
1. After running the db/docker-compse.yml and reassuring that pgadmin are up and running
2. Run the main_img.py script ```python3 db/main_img.py```
3. Refresh your database and see the new *image* table inside the *ms3_jokes* db filled with with an image row. Make sure you run the main_jokes.py script prior to running this. Since the database only gets created in that module.
