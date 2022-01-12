import requests
import json
import data_preparation
import base64
from PIL import Image
from io import BytesIO


num_classes, input_shape, x_train, y_train, x_test, y_test = data_preparation.prepare_data()


# Select first image of test data and convert to list
image = x_test[0].tolist()

print(type(image))

# Transform input to dictionary
requestDict = {'image':image}





with open("flask_app/static/img/uploads/patrick.png", "rb") as image_file:
    data = base64.b64encode(image_file.read())
    data_as_string = data.decode("utf-8")
    print(type(data_as_string))
    

im = Image.open(BytesIO(base64.b64decode(data_as_string)))
im.save('image2.png', 'PNG')

# image = Image.open("flask_app/static/img/uploads/sample_number.png")
# # image.tolist()
# print(image)
# requestDict = {"description" : "lottery", "amount" : data_as_string}
# response = requests.post("http://localhost:5000/incomes", json = requestDict)
# print(response.json())


