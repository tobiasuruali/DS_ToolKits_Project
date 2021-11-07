# Milestone 2 

## Task 1 Git Commit Copying
The .gitignore file was created quite early and additions needed to be made every once in a while due to applications, different OS's and functionalities added (such as python venv's).
While working on different branches being able to obtain changes on various files such as .gitignore, we made use of `git cherry-pick` functionality.

1. checkout the wanted branch and commits of that branch.
If you wanted to see the specific changes made on that commit use `git log -p`
````
git checkout milestone2_marco
````
````
git log
````
2. Now copy the hash of the specific commit you want to add to your branch and then add it to your branch. Make sure you change to your original branch first
````
git checkout milestone2_feature
````
````
git cherry-pick 0d71863a
````

If you just wanted to change a specific file (in our case *.gitignore*) and the specific commit has various changes on multiple files. There's a work around to adding those changes to your tree:

````
git diff mileston2_feature milestone2_marco ./.gitignore | git apply
````

In our case there were never conflicts but it's better practice incase there's no major changes to specific branches to just merge the branches to avoid further possible conflict

## Task 2: Add the answers to the following questions to your report
**What is a Hash function? What are some of the use cases**

- A Hash function maps data from one table to a fixed-size value, a unique identifier. A popular use case is to check the integrity of a file or a transaction. When we transfer a file we aim to send the exact copy of what we have. However, a file can get corrupted due to multiple reasons. A hash algorithm can generate a unique identifier of the file and by checking the identifier, we can verify the integrity of the file. However, we can never reconstruct from a hash code the original file. Therefore, we can only check if the file is the same or not. Another use case is for storing passwords. For example, if we are a firm, we might have the passwords of multiple users. We can store the hash of the password. This way if the database is leaked, the original password is harder to obtain. For example, if we only apply encryption, once a hacker has the encryption key, it is easier to obtain all the original passwords. In fact for the encryption, the whole file is preserved, making it easier to obtain all the credentials, once a decryption key is found. Of course, a hash function can only be a single element of a complex and safe solution.

**What is a Python module, package and script? How do they differ from one another?**

- A Python script is a python file (.py) that contains commands in a logical order and is meant to be run directly. A minimum requirement of a script is to be able to do a task and create an output. On the other hand, we have modules. A module is meant to be imported and it usually contains classes, functions and variables. A script may for example load multiple modules to produce its output, while a module by itself is only a container. Therefore what is a package? A package is a collection of modules (usually more than 1) that are bundled together. Usually, a package contains modules used for the same scope. 

**How would you explain a Docker container and volume to a child?**

- A docker container contains all the necessary information and files to create an application. Imagine building a house. For building a house you need a lot of parts: Windows, doors, furniture etc. You don't need only the right components but also the right size. A door of 3 meters in height would not fit many houses. Therefore those components to make a house need to fit together, otherwise, you will not have a roof over your head for a long time. In the end, a docker container provides all the information and the components needed to build the house. The only difference is that is not used for houses but applications.

- A docker volume is used to save, so to remember, information in a docker container. The docker container allows to build and run applications. An example of an application could be a simple system in a store that tells if the product you search is available or not. The docker container will allow us to search if apples are in stock and the volume is responsible to keep a full list of all the products of the store, from apples to the toilet paper.

**What is your preference concerning the use of Python virtualenv and Docker? When would you use one or the other?**

- With the experience collected so far, I would use virtualenv when the focus is only on showing the results of a project and taking advantage of the possibility of encapsulating the Python dependencies, without corrupting the machine that I am using. If I would have to share the code behind it, I would now set up everything in a Docker image, to allow the code to be run in any environment, regardless if the other users are having a different version of Python or a different OS. In addition, I would still prefer to use Docker if I plan to run my code for a longer time than a semester, even if the code would never leave my local machine. In that case, Docker would ensure that if I upgrade OS, install software that update dependencies or any new variable is introduced, I will still be able to run the code written. 

**What is the Docker build context?**

- Docker build is a command to build an image from a Dockerfile. If we think about a virtual environment, it could be compared to the Python command virtualenv. A good description of what Docker build does is available in the official Docker documentation: https://docs.docker.com/engine/reference/commandline/build/ A docker image can be cloned from a repository, or be available locally on our machine. A docker image can contain a .dockerignore file, which excludes certain files and directories from being loaded with the docker image. A docker image would contain the code to run the app info on the OS (usually a lightweight Linux distro), Pyhton version and other dependencies to load. With the command docker run, we can then run the Docker we built. 

**How can you assess the quality of a python package on PyPI?**

- With 337,533 projects (at the time of writing) there are no third-party checks on the code that is uploaded to PyPI. The fastest way to check the quality (or better the popularity) would be to check the stars associated with each project.As an example NumPy ( https://pypi.org/project/numpy/ ), a popular Python project has 18,720 stars (at the time of writing). Of course, for security concerns, the best is always to deep dive into the code of the project, often hosted on GitHub.  

## Task 3 Code Functionalities 


Added functionality to save and load a model inside **model_inspection.py** and prediction functionality added in module **predictions.py**

We attempted to implement a visualization of prediction an given photo through matplotlib pyplot package. But since docker images don't necessarily have GUI functionality, we encountered tons of errors trying to visualize the analyzed fotos. We tried to download python-tk3 and other matplotlib GUI visualization packages which helped up visualize it on our local Ubuntu machines. But on docker those same hotfixes didn't seem to work.

For reference, check out **Loaded_Model_Eval.ipynb**, there it works perfectly.
 


## Task 4 Seperating Code into Modules

Modulization of code was made trying to keep the logic of the initial script in mind.
We decided to go for a modul structure like this:  
- **data_preparation.py**  - For preparing the data and initialising the variables   
- **build_model.py**  for building and training the model
- **model_inspection.py**  saves, loads a model and evaluates it 
- **prediction.py**  predicting on a given set of data
- ***main.py***  runs the whole script

Naming was created ensuring PEP8 conformity with lowercases.  
### data_preparation

- functions:  
def prepare_data() - Defines number of classes, input_shape, train and  test data
### build model 
- functions:
def build_model(num_classes, input_shape) - creates our keras model  
def train_model(x_train, y_train, model) - trains the model on given training data  
### model_inspection
- functions:
def save_model(model) - Saves the just created model as an .h5 file  
def load_model() - Loads the model with the given name  
def evaluate_loaded_model(x_test, y_test, loaded_model) - evaluates Model's Test loss and accuracy  
### prediction
- functions:
def predict_on_data(x_test, y_test, loaded_model) - Predicts the the number of given image dataset and saves it in an array. Added 5 random number visualization as well to show prediction accuracy 
### main
````
if __name__ == "__main__":
    num_classes, input_shape, x_train, y_train, x_test, y_test = data_preparation.prepare_data()
    model = build.build_model(num_classes, input_shape)
    build.train_model(x_train, y_train, model)
    inspection.save_model(model)
    loaded_model = inspection.load_model()
    inspection.evaluate_loaded_model(x_test, y_test, loaded_model)
    predictions.predict_on_data(x_test, y_test, loaded_model)
```` 


## Task 5 Pip Requirements File

To create a requirements file at first code on the stackoverflow suggested while being in a virutal environment to `pip freeze -> requirements.txt` but this ended up creating a big requirements file, including all packages already preinstalled in a python environment. 

On pipy we then discovered **pipreqs**. Pipreqs analyzes a specific directory defined in the command, and analyzes what packages are actually being used inside the directories script. It then writes a requirements.txt into that directory with only **essential** packages to run the code.

````
pipreqs /code 
````

**matplotlib==3.1.2  
tensorflow==2.7.0  
numpy==1.19.2**

In future use, regardless of what OS or Image someone is utilizing, when running `pip install requirements.txt` for example. The code will run with the right required packages.  

## Task 6 Dockerizing
  - The first step was to install Docker on our machines. Based on the distro there are different installation possibilities. After we can run the command on our Linux terminal:
  ```
   sudo systemctl start docker.service
  ``` 
  -This will run with root privileges in the Docker service. It is usually not recommended to run an app with root privileges, but for me, it was the only way to solve the problem "Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running? errors pretty printing info".
  The steps I describe now are not necessary by themselves for task 6 itself but are a part of getting to know better Docker. 
  We can have additional info on our installation on Docker by running the command:
  ```
   docker info
  ``` 
- This will also highlight if there are existing problems, like the one mentioned in the previous paragraph. We can then run a simple Docker image. 
  ```
   docker run hello-world
  ``` 
- After I wanted to test the image that I used for the GitHub repository. Because we needed to use TensorFlow later, I decided to use an official image made for that purpose. For this reason, I loaded by using the command: 
  ```
   docker run -it --rm tensorflow/tensorflow bash
  ```
- This command checks first if the image is already downloaded on our disk and if not it will get it from https://hub.docker.com/. After downloading the image(if necessary), the command will start the docker container. The flag --rm will remove the image after the process will be closed. After I run the required pip install and the python code, I check whether the system is suitable for our script or not. I don't encounter any major problems and I decide to start dockerizing our script. This is where more difficulties were met. At first, we had an excessively long list of dependencies to install. This caused difficulties in creating the Docker image because even if the problem was for a single PyPI package, the whole installation would fail.  After we optimized the list of dependencies. An additional problem was due to the COPY and the ADD function inside Docker. For some reason, we struggled to ADD or COPY our Phyton script to the Docker container. For this reason, we used the . . notation to copy all elements. On one hand, this is not ideal, but given the existing structure of the GitHub project, with an adequate .dockerignore file, this notation is not too detrimental. If we look for space for improvements we might use a more lightweight distro as a starting image or add an image to Docker that supports NVIDIA GPUs. Given that we both lack a discrete graphic card, we couldn't test the latter possibility. In conclusion, our dockerfile loads an official image from TensorFlow and the required dependencies to run the code, in addition, to loading our modulized code. 