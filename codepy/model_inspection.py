from tensorflow import keras

"""
## Save the trained model
"""

def save_model(model):
    # model.save persists a h5 of your model  
    print("Saving Model:", model)
    model.save("ds_keras_model.h5")

# Function call example
# save_model(model)

"""
## Load a specific saved model
"""

def load_model():
    # load_model can then reconstruct the model identically
    print("Loading Model from volumes..")
    loaded_model = keras.models.load_model("ds_keras_model.h5")
    return loaded_model

# Function call example
# loaded_model = load_model()

"""
## Evaluate the loaded model on test data
"""

def evaluate_loaded_model(x_test, y_test, loaded_model):
    score = loaded_model.evaluate(x_test, y_test, verbose=0)
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])

# Function call example
# evaluate_loaded_model(x_test, y_test, loaded_model)