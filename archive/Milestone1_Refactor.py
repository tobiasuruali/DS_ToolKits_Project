#Data set: http://yann.lecun.com/exdb/mnist/
#Code: https://github.com/keras-team/keras-io/blob/master/examples/vision/mnist_convnet.py

"""
Title: Simple MNIST convnet
Author: [fchollet](https://twitter.com/fchollet)
Date created: 2015/06/19
Last modified: 2020/04/21
Description: A simple convnet that achieves ~99% test accuracy on MNIST.
"""

"""
## Setup
"""

import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

"""
## Prepare the data
"""

def prepare_data():
    # Model / data parameters
    num_classes = 10
    input_shape = (28, 28, 1)

# the data, split between train and test sets
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range
    x_train = x_train.astype("float32") / 255
    x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)
    print("x_train shape:", x_train.shape)
    print(x_train.shape[0], "train samples")
    print(x_test.shape[0], "test samples")


# convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)
    return num_classes,input_shape,x_train,y_train,x_test,y_test

num_classes, input_shape, x_train, y_train, x_test, y_test = prepare_data()

"""
## Build the model
"""

def build_model(num_classes, input_shape):
    model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

    model.summary()
    return model

model = build_model(num_classes, input_shape)

"""
## Train the model
"""

def train_model(x_train, y_train, model):
    batch_size = 128
    epochs = 15

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

train_model(x_train, y_train, model)

"""
## Evaluate the trained model
"""

def evaluate_model(x_test, y_test, model):
    score = model.evaluate(x_test, y_test, verbose=0)
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])

evaluate_model(x_test, y_test, model)

"""
## Save the model
"""


def save_model(model):
    # model.save persists a h5 of your model  
    model.save("keras_model.h5")

save_model(model)

def load_model():
    # load_model can then reconstruct the model identically
    reconstructed_model = keras.models.load_model("keras_model.h5")
    return reconstructed_model

reconstructed_model = load_model()

# Check Reconstructed models performance
np.testing.assert_allclose(
    model.predict(x_train), reconstructed_model.predict(x_train)
)

# The reconstructed model is already compiled and has retained the optimizer
# state, so training can resume:
reconstructed_model.fit(x_train, y_train) 