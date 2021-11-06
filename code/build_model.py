import numpy as np
import tensorflow as keras
import tensorflow.keras as layers 

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

# Variable Call example
# model = build_model(num_classes, input_shape)

"""
## Train the model
"""

def train_model(x_train, y_train, model):
    batch_size = 128
    epochs = 15

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# Function Call example
# train_model(x_train, y_train, model)
