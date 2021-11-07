import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import data_preparation
import model_inspection
import matplotlib.pyplot as plt 
import random
import build_model

# num_classes, input_shape, x_train, y_train, x_test, y_test = data_preparation.prepare_data()
# loaded_model = model_inspection.load_model('keras_model.h5')

"""
## Perform Predictions with your fitted model
"""

"""
# Incase fitting is needed:

def fit_loaded_model(x_train, y_train, loaded_model):
    #train loaded model on training data
    fitted_model = build_model.train_model(x_train, y_train, loaded_model)
#No Epochs for speed and testing reasons
    #fitted_model = loaded_model.fit(x_train,y_train)

# Example for function call up
# fit_loaded_model(x_train, y_train, loaded_model)

"""

def predict_on_data(x_test, y_test, loaded_model):
# Predicting something with loaded_model
    prediction  = loaded_model.predict(x_test)
# print(prediction)

#convert to int array 
    int_predictions = np.argmax(prediction, axis = 1)
    print('Predictions array:', int_predictions)

    print('Shape of x_test:', x_test.shape,'Shape of y_test:', y_test.shape)

    random_numbers = random.sample(range(0,10000),5)
    print('Random Numbers selected in array:', random_numbers)

#Plot Predicitions vs their actual numbers
    print('Showcase to evaluate predictions:')
    for i, number in enumerate(random_numbers):
        print('[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]')
        print(y_test[random_numbers[i]])
        plt.imshow(x_test[random_numbers[i]], cmap=plt.get_cmap('gray'))
        plt.show()


# Example for function call up
# predict_on_data(x_test, y_test, loaded_model)