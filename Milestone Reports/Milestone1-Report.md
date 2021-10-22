# Milestone 1 

## Task 1
**Read about the data set assigned to you. Explain what it is about and what problem is solved by the machine learning models trained on it.**

- **Is it a classification or regression Problem?**  
    Text

- **What are the characteristics of the dataset?**    
    Handwritten digits


## Task 4

**Run the python code**

- **Explain in detail which steps were necessary to run the code**  
  We run a Ubuntu20.04 Virtual Machine. Firstly we'll need to download python3.8  
  ```
  sudo apt install python3.8
  ```
  
  A trial to get the python copying from the original github didn't seem to work. 
  The file ended up being displayed in XML (I assume). Was unrunnable:
  ```
  wget https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py
  ```
  So a CTRL + C of the raw code from the github repo had to suffice. Added new txt. file, pasted the raw code into it, then renamed the file ending.
  `cat > mnist_convnet.txt`, CTRL + V, `mv mnist_convnet.txt mnist_convnet.py`  
  Before then running the code we first evaluate the code with our text editor.  
  1. After Eval, we will need the packages that are listed in the "import" section at the beginning of the code.
  2. We'll use pip to install all these packages
    ```
    sudo apt install pip3 &&
    pip3 install numpy &&
    pip3 install tensorflow 
    ```
  3. Run the script
    ```
    python3 mnist_convnet.py
    ```
    
  




- **Find out what versions are being used to run the code (python version and all dependencies)**  
  Find out Python version:
  ```
  python3 -version
  ```
  To Find out what Requirements & Dependencies as used for our specific script we'll use the pipreqs package
  ```
  pip3 install pipreqs
  ```
  pipreqs analyzes the defined directory and what packages are needed to run the files in that directory
  ```
  pipreqs ~/Documents/DS_Toolkits_Project/
  ```
  The Pythons and Dependencies being used for running this script:  
  **Python 3.8.10  
  numpy==1.19.5  
  tensorflow==2.6.0**



- **Are the versions dependent on the system the code is being run on? (try running it on different machines, by checking out the code onto these machines. Does it work out of the box?)**  
  No

## Task 5  
**Explain what the code does**  
  The Code analyzes pictures of hand written numbers. With the help of TensorFlow & Keras it creates a model that should Predict the number inside an image with a 99% accuracy.