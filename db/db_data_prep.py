import numpy as np
from tensorflow import keras
import random


def random_img_sample():
    num_classes = 10

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

#define random Number and select that img from dataset
    random_single_number = random.randint(0,9999)
    random_plus_one = random_single_number + 1 
    print('Random number selected in array:', random_single_number)
    random_img_x = x_test[random_single_number:random_plus_one]
    squeezed_random_img_x = np.squeeze(x_test[random_single_number:random_plus_one], axis=0)
    print('Shape random img: ', random_img_x.shape, 'Shape random img squeezed:', squeezed_random_img_x.shape)
    return random_img_x, squeezed_random_img_x

# Example Function Call
# random_img_sample()