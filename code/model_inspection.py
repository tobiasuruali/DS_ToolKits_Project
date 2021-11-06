from tensorflow import keras

"""
## Evaluate the trained model
"""

def evaluate_model(x_test, y_test, model):
    score = model.evaluate(x_test, y_test, verbose=0)
    print("Test loss:", score[0])
    print("Test accuracy:", score[1])

# Function Call example
# evaluate_model(x_test, y_test, model)


"""
## Save the trained model
"""

def save_model(model):
    # model.save persists a h5 of your model  
    model.save("keras_model.h5")

# Function call example
# save_model(model)

"""
## Load a specific saved model
"""

def load_model():
    # load_model can then reconstruct the model identically
    reconstructed_model = keras.models.load_model("keras_model.h5")
    return reconstructed_model

# Function call example
# reconstructed_model = load_model()