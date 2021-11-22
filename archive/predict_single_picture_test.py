## LOADING AND TESTING MODEL ON SINGLE PREDICTION

import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from PIL import Image as im
import matplotlib.pyplot as plt 
import codepy.data_preparation as data_preparation
import random

num_classes, input_shape, x_train, y_train, x_test, y_test = data_preparation.prepare_data()

# It can be used to reconstruct the model identically.
loaded_model = keras.models.load_model("keras_model.h5")

# The reconstructed model is already compiled and has retained the optimizer
# state, so training can resume:
loaded_model.fit(x_train, y_train)



random_single_number = random.randint(0,9999)
random_plus_one = random_single_number + 1 
print('Random number selected in array:', random_single_number)
one_pic_x = x_test[random_single_number:random_plus_one]
squeezed_one_pic_x = np.squeeze(x_test[random_single_number:random_plus_one], axis=0)
print(one_pic_x.shape, squeezed_one_pic_x.shape)


# def create_random_picture_array():
#     for i in random_single_number:
#         one_pic_x = x_test[i:(i+1)]
#         squeezed_one_pic_x = np.squeeze(x_test[i:(i+1)], axis=0)
#         return squeezed_one_pic_x, one_pic_x
# squeezed_one_pic_x, one_pic_x = create_random_picture_array()

# Predicting something with loaded_model
prediction  = loaded_model.predict(one_pic_x)
# print(prediction)

#convert to int array 
int_single_prediction = np.argmax(prediction, axis = 1)
print('Predictions array:', int_single_prediction, prediction.shape, type(squeezed_one_pic_x))


print(squeezed_one_pic_x.shape, x_test[random_single_number].shape, one_pic_x.shape)

#Plot Predicitions vs their actual numbers
print('Showcase to evaluate predictions:')
for i, number in enumerate(int_single_prediction):
    print('[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]')
    print(int_single_prediction)
    two_d = (np.reshape(squeezed_one_pic_x, (28, 28)) * 255).astype(np.uint8)
    # plt.imshow(squeezed_one_pic_x, cmap=plt.get_cmap('gray'))
    plt.imsave(fname="test_test_photo.png",arr= two_d, cmap=plt.get_cmap('gray'))
    # plt.savefig("test_x_photo.png")
    # plt.show() 
