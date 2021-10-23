# Milestone 1 

## Task 1
**Read about the data set assigned to you. Explain what it is about and what problem is solved by the machine learning models trained on it.**

- **Is it a classification or regression Problem?**  

  The problem is a classification problem, where the algorithm is optimized to identify pictures of handwritted digits and the perfomance of this algorithm is determined on the error
  rate on the test set. The lower the error rate, the better the model performs. It is interesting to notice that this exercise has been running for quite some time, with the first
  submissions dating the year 1998. In addition, there are example of both supervised and unsupervised machine learning algorithms.

- **What are the characteristics of the dataset?**    

  The data-set consist of a collection of handwritten digits, with a training set of 60,000 examples, and a test set of 10,000 examples. In addition to the data-set, some results are   provided, on the different technique utilized to identify the handwritten digits. 

  According to the description, the data-set is already normalized so that each picture of a handwritten digit fit in a 20x20 pixel box. In the end the pictures were centered in a
  28x28 pixel grid, providing the final resolution. In many OCR algorithms is normal to filter, resize and normalize multiple times the picture, to improve the precision of the 
  classification algorithm selected. Even if we would capture a high resolution picture and we would have an algorithm to identify how many persons are in the picture, the algorithm
  would process the picture in a way that would reduce considerably the original resolution with multiple iteration of post-processing.

## Task 2
**Check out the code base assigned to you from GitHub**

  The second link provides an algorithm linked to the aforementioned data-set. According to the author, it is capable of achieving a high accuracy (99%) in the recognition of
  handwritten characters in the test set. Of course, real world performance may differ. 
  We can see that the code is an example of the advantage of Keras, an API utilized to simplify the implementation of advanced machine learning algorithm and scale the workload to
  train the model. In addition, it utilizes Docker, a common package manager, which allows to run complex application by breaking them into smaller application packages. 
  A small digression, the progress of Docker and other similar applications changed how some companies manage and create software. I work for a firm specialized in building equipment
  and software and this is the way our next generation of software is created, by having single use cases as container, that can be combined to make more powerful solution. In the
  past, with a more unitary approach, large and complex solution were possible, but with clear trade-offs.
  Back to the code, it provides a very easy to read training of the data model, including test of said model.  

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

  Result:  
  ![Results](https://github.com/tobiasuruali/DS_ToolKits_Project/blob/feature/Milestone_Reports/images/Results_PythonScript_mnist.png)




- **Are the versions dependent on the system the code is being run on? (try running it on different machines, by checking out the code onto these machines. Does it work out of the box?)**  
  No

## Task 5  
**Explain what the code does**  
  The Code analyzes pictures of hand written numbers. With the help of TensorFlow & Keras it creates a model that should Predict the number inside an image with a 99% accuracy.
