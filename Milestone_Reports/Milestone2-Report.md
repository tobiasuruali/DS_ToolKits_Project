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

## Task 2 Questions
Add the answers to the following questions to your report:
- What is a Hash function? What are some of the use cases?
  A Hash function map data from one table to fixed-size value, a unique identifier. A popular use case is to check the integrity of a file or a transaction. When we transfer a file we aim to send the exact copy of what we have. However, a file can get corrupted due to multiple reasons. A hash algorithm can generate a unique identifier of the file and by checking the identifier, we can verify the integrity of the file. However, we can never reconstruct from a hash code the original file. Therefore, we can only check if the file is the same or not. Another use case is for storing password. For example if we are a firm, we might have the passwords of multiple users. We can store the hash of the password. This way if the database is leaked, the original password is harder to obtain. For example, if we only apply encrpytion, once a hacker has the encrpytion key, it is easier to obtain all the original passwords. 
  In fact for the encryption, the whole file is preserved, making it easier to obtain all the credentials, once a decryption key is found. Of course, a hash function can only be a single element of a complex and safe solution.

- What is a Python module, package and script? How do they differ from one another?
A Python script is a python file (.py) that contains commands in logical order and it is meant to be run directly. A minimum requirement of a script is to be able to do a task and create an output. On the other hand we have modules. A module is meant to be imported and they usually contains classes, functions and variables. A script may for example load multiple modules to produce its output, while a module by itself is only a container. Therefore what is a package? A package is a collection of modules (usually more than 1) that are bundled together. Usually they are used for the same scope. 

- How would you explain a Docker container and volume to a child?
A docker container contains all the necessary information and files to create an application. Imagine building a house. For building a house you need a lot of parts: Windows, doors, furniture etc. You don't need only the right components but also the right size. A door of 3 meter in height would not fit many houses. Therefore those components to make an house they need to fit together, otherwise you will not have a roof over your head for a long time. In the end,a docker container provides all the information and the components needed to build the house. The only difference is that is not used for houses but for applications. 

A docker volume is used to save, so to remember, information in a docker container. The docker container allows to build and run applications. An example of an application could be a simple system in a store that tells if the product you search is available or not. The full container will allow us to search if apples are in stock and the volume is responsible to keep a full list of all the products of the store, from apple to the toilet paper. 

- What is your preference concerning the use of Python virtualenv and Docker? When would you use one
or the other?

With the experience collected so far I would use virtualenv when the focus is only on showing the results of a project, and taking advantage of the possibility of encapsulating the Python dependencies, without corrupting the machine that I am using. 
If I would have to share the code behind, I would now set up everything in a Docker image, to allow the code to be run in any environment, regardless if the other users are having a different version of Python or a different OS.
In addition, I would still prefer to use Docker if I plan to run my code for a longer time than a sememster, even if the code would never leave my local machine. In that case, Docker would ensure that if I upgrade OS, install software that update dependencies or any new variable is introduced, I will still be able to run the code written. 

- What is the Docker build context?
Docker build is a command to build an image from a Dockerfile. If we think about a virtual environment, it could be compared to the Python command virtualenv.   
A good description of what Docker build does is available in the official Docker documentation:
https://docs.docker.com/engine/reference/commandline/build/ 
A docker image can be cloned from a repository, or be available locally on our machine. A docker image can contatin a .dockerignore file, which excludes certain files and directories from being loaded with the docker imamge. 
A docker image would contain the code to run the app info on the OS (usually a lightweight linux distro), Pyhton version and other dependencies to load.
With the command docker run we can then run the Docker we built. 

- How can you assess the quality of a python package on PyPI?

With 337,533 projects (at the time of writing) there are no third-party checks on the code that is uploaded to PyPI. The fastest way to check the quality (or better the popularity) would be to check the starts associated to each project.
https://pypi.org/project/numpy/ 
As an example NumPy, a popular Python project has 18,720 stars (at the time of writing). Of course, for security concerns, the best is always to deep dive on the code of the project, often hosted on GitHub.  

## Task 3 Code Functionalities 

Make sure your code has the following functionality (extend if necessary):
- Can load data
- Can train (fit) a neural network on the data
- Can save a fitted model to a ".h5" file
- Can load a ".h5" file, using Keras
- Can perform predictions using a "fitted" model, using Keras


## Task 4 Seperating Code into Modules
Your code bases are badly structured, as they are essentially a script, which is read top down. This creates
Python files that are large and not maintainable. It is good practice to create modules that contain code
snippets which "logically" belong together. The modules contain python functions that are imported by other
modules and scripts, where they are executed.
- Split your code base into modules (for example the creation of the neural network might be in a
"neuralnet_architecture.py" module). Explain the reasoning behind your modularization. Why did you choose
to structure the code like this?
- There has to be one "main.py" script that calls the code in all the other modules. This is the script that you
run with the "python" command.
- The modules are only allowed to contain imports and functions (for example "def create_neuralnet(): ...")
- Ensure PEP8 conformity

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