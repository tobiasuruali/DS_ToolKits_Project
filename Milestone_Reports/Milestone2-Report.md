# Milestone 2 

## Task 1 Git Commit Copying
Git Cherry Picking:


## Task 2 Questions
Add the answers to the following questions to your report:
- What is a Hash function? What are some of the use cases?
- What is a Python module, package and script? How do they differ from one another?
- How would you explain a Docker container and volume to a child?

- What is your preference concerning the use of Python virtualenv and Docker? When would you use one
or the other?
- What is the Docker build context?
- How can you assess the quality of a python package on PyPI?

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
Create a pip "requirements file" for your code base and explain how you make it work within a virtualenv
(step by step).
Did you have to install virtualenv?

## Task 6 Dockerizing