# Milestone 1 

## Task 1
**Read about the data set assigned to you. Explain what it is about and what problem is solved by the machine learning models trained on it.**

- **Is it a classification or regression problem?**  

  The problem is a classification problem, where the algorithm is optimized to identify pictures of handwritten digits and the performance of this algorithm is determined on the error rate on the test set. The lower the error rate, the better the model performs. It is interesting to notice that this exercise has been running for quite some time, with the first submissions dating back to 1998. In addition, there are examples of both supervised and unsupervised machine learning algorithms.

- **What are the characteristics of the dataset?**    

  The data-set consists of a collection of handwritten digits, with a training set of 60,000 examples, and a test set of 10,000 examples. In addition to the data-set, some results are provided, on the different techniques utilized to identify the handwritten digits. 

  According to the description, the data-set is already normalized so that each picture of a handwritten digit fit in a 20x20 pixel box. In the end the pictures were centered in a
  28x28 pixel grid, providing the final resolution. In many OCR algorithms is normal to filter, resize and normalize multiple times the picture, to improve the precision of the 
  classification algorithm selected. Even if we would capture a high resolution picture and we would have an algorithm to identify how many persons are in the picture, the algorithm
  would process the picture in a way that would reduce considerably the original resolution with multiple iterations of post-processing of the image.

## Task 2
**Check out the code base assigned to you from GitHub**

  The second link provides a python script linked to the aforementioned data-set. According to the author, it is capable of achieving a high accuracy (99%) in the recognition of
  handwritten characters in the test set. Of course, real world performance may differ. 
  We can see that the code is an example of the advantage of Keras, an API utilized to simplify the implementation of advanced machine learning algorithm and scale the workload to
  train the model.  
  The code is very easy to read, providing info regarding the required packages, how the data is prepared, how the model is trained and evaluated. 
  
## Task 3
**Commit the relevant python file to your Git Repo.

## Task 4

**Run the python code**

- **Explain in detail which steps were necessary to run the code**  
  We run a Ubuntu20.04 Virtual Machine. To set up the virtual environment we used the integrated virtual environment in python, by using the command 
  ```
  python3 -m venv "venv" 
  ```
  In this case the virtual environment is named venv and is hosted in the home directory, as per default.
  We can then activate the virtual environment by using the command.
  ```
  source env/bin/activate venv 
  ```
  We can see now from the terminal that the virtual environment is activated. In our case in the /env directory.
  To exit the virtual environment we can simply input
  ```
  deactivate 
  ```  
  Firstly we'll need to download python3.8  
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

  - **What is the input to and the output from the neural network**  
  
  The input is an archive of pictures of handwritten numbers and the output is a model that estimates the corresponding number associated with each picture. 
  
  - **What is Keras? And how does it relate to Tensorflow?**
  
  Keras is a Python interface for artifical networks. It provides a more readable code and output and it allows to distribute the training of deep-learning models to GPU and TPU.
  GPUs are suited for deep-learning models, thanks to the possibility of running more parallel processes. This helps to reduce drastically the time used to 
  "train" a model. 
  TensorFlow is a solution created by Google, to provide an open-source library for machine learning models. It helps to create ML models with (potentially) only few lines of code.
  In addition to the content generated by Google, TensorFlow has an active community and is used as well in the academic world. Keras acts as an interface for the TensorFlow. 
  
 - **How is the data loaded**  
 
  The following command load the data: 
  ```
  (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
  ```
  And the data is downloaded from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
  This loads 60,000 points to train the model and 10,000 to test the accuracy of our model (test samples).
  
  - **Which dependencies are imported**  
  
  See question 4
  
  - **What kind of neural network architecture are you dealing with**  
  
  In this instance, we have an example of a deep learning model used for Object Character Recognition (OCR).  
  We know from the description of the data set that we have a 28x28 pixel image.  
  We have convolution layers that apply an array of filters in parallel to increase the amount of information each pixel provides. We can see this action in the output of the code.  
  **(conv2d)**: This marginally reduce also the shape of the image (26x26). How many filters were applied? 32.   
  This brings the data set from a 28X28X1 to 26x26x32 
  To reduce the dimensionality further the model applies MaxPooling2D. Pooling can be seen as zooming out, reducing the resolution. The reason why this is possible is that neighbouring pixels tend to have similar values, therefore some of the information is redundant.   
  Pooling applies operations like average, maximize, minimize etc to reduce dimensionality.
  This reduces the dimensionality from 26x26x32 to 13x13x32.  
  These operations are then run a second time, bringing each variable to a value of 5x5x64.  
  However, the final goal of this classification model is to associate each picture with a value that ranges from 0 to 9 (so 10 possibilities).   
  This mapping process happens in the last stage of the model. The result is a probability distribution, where the algorithm assigns the probability that each picture is one of the 10 numbers (in percentage). This allows us to see how clear the prediction is expected to be. In the end, the number with the highest probability is associated with each picture. This is the prediction element of the model.
  Which elements is the algorithm training? Early layers learn basic structures called features. Some deep neural nets are also pre-trained on large image datasets because some of the features are domain-independent. 
  
 
  
  
  
