# compose_flask/app.py
import os
from flask import Flask
from flask import render_template, request, redirect, flash, url_for, jsonify, make_response
from redis import Redis
from werkzeug.utils import secure_filename
import numpy as np
import base64
import json
from PIL import Image
from io import BytesIO

import codepy.model_inspection as inspection

# import cv2
# import jsonpickle

UPLOAD_FOLDER = 'static/img/uploads/'

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

app.config["SECRET_KEY"] = "Super Secret Key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Allow only pictures to be uploaded
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/redis')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if 'image' not in request.files:
            flash('No image part', 'danger')
            return redirect(request.url)
        image = request.files['image']
        # image_bytes = base64.b64encode(image.read())
        # image_string = image_bytes.decode("utf-8")
        # print(type(image))
        # print(type(image_bytes))
        # print(type(image_string))
        if image.filename == '':
            flash('No image selected for uploading', "warning")
            return redirect(request.url)
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below', "success")
            prediction = 2 #PLACEHOLDER
            return render_template('image_upload.html', filename=filename, prediction=prediction)
        else:
            flash('Allowed image types are -> png, jpg, jpeg, gif', "danger")
            return redirect(request.url)

    return render_template("image_upload.html")


@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route('/uploads/<prediction>')
def send_prediction(prediction=''):
    return prediction

# @app.route("/upload-image/<image>", methods=["POST"])
# def post_upload_image(image):
#     if request.method == "POST":
#         image = request.files['image']
#         if image.filename == '':
#             flash('No image selected for uploading', "warning")
#             return redirect(request.url)
#         if image and allowed_file(image.filename):
#             filename = secure_filename(image.filename)
#             image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             print('upload_image filename: ' + filename)
#             flash('Image successfully uploaded and displayed below', "success")
#             return render_template('image_upload.html', filename=filename)
#         else:
#             flash('Allowed image types are -> png, jpg, jpeg, gif', "danger")
#             return redirect(request.url)

#     return render_template("image_upload.html")


stock = {
    "fruit": {
        "apple": 30,
        "banana": 45,
        "cherry": 1000
    }
}


@app.route('/stock', methods=["GET"])
def get_stock():

    res = make_response(jsonify(stock), 200)

    return res


images = [
    {'image': 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8/fFQqAAAACXBIWXMAAA9hAAAPYQGoP6dpAAABfElEQVR4nO1W0Y2DMAw16LpFukf2aDJHmzVAqGuEroGI2m7RrlE5776aAxJoOOn6caolyxImvDw/26IgItAbrXwn2AfwA/gr+8p5qW1bAkCXy4WOx2OUN8YQESVzKcOSSykBAMwMAKjrGt57MHMy1nW9+L1FQGMMrLVgZjwej+xojFkPOGU2jClmXddlMS2eqFOz1pLWmrz3VJZlFJumoev1SgCoKAo6n8+03+/pcDiE9zabTZ6GTdMkmbVtCynlbLmccyPm2SVNaVNV1atmgBACXdeFczMXjA/e73dYa0PjvGiCyKcaD3PJOQR+ZM2dren5oeZRfuoAoJRaxYqIoLVG3/eBmTEmr6TMjN1ulw30LPlU+5kGW8ci5d57KKUCsxfdHD88nU6haXKcmUfduXrTSClxu93gnIPWGtvtFlrrkVZDz2S2XFIpZbhx3/dhruZ2a1VVueMzn3TORTsyFVfO6XxSCAEhBJRSI43WbqChzy7vv7L//0/zdsBvGrApTDvwxZ0AAAAASUVORK5CYII=', 'filename': "test_number"}
]

loaded_model = inspection.load_model()


@app.route('/image-predict', methods=['GET'])
def get_images():
    return jsonify(images)


@app.route('/image-predict', methods=['POST'])
def add_images():
    json_data = request.get_json()  # Get the POSTed json
    json_data = json.dumps(json_data) 
    dict_data = json.loads(json_data)  # Convert json to dictionary

    img = dict_data["image"]  # Take out base64# str
    # Convert image data converted to base64 to original binary data# bytes
    img = base64.b64decode(img)
    img = BytesIO(img)  # _io.Converted to be handled by BytesIO pillow
    img = Image.open(img)
    img = img.resize((28, 28))
    img_np = np.array(img)
    print(img_np.shape)
    print(type(img_np))
    print(img_np.ndim)

    # all 3 dimensional images will need to be resized to (1, 28, 28, 1) for the model
    if img_np.ndim == 3:
        img_np = img_np.astype("float32") / 255
        print(img_np.shape)
        img_np = img_np[:, :, 0]
        print(img_np.shape)
        img_np = np.expand_dims(img_np, -1)
        print(img_np.shape)
        img_np = np.array([img_np])
        print(img_np.shape)

    # incase image/array is already 2 dimensional (grey scale) we proceed as milestone 1
    if img_np.ndim == 2:
        img_np = img_np.astype("float32") / 255
        img_np = np.expand_dims(img_np, -1)
        img_np = np.array([img_np])  # Model expects shape (x, 28, 28, 1)

    prediction = loaded_model.predict(img_np)
    int_single_prediction = np.argmax(prediction, axis=1)
    int_single_prediction = int(int_single_prediction)

    img_shape = img.size  # Appropriately process the acquired image

    filename = dict_data["filename"]  # Properly process with imagename
    img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # Return the processing result to the client

    response = {
        "prediction": int_single_prediction,
        "img_shape": img_shape
    }

    return jsonify(response)


# @app.route('/api/test', methods=['POST'])
# def test():
#     r = request
#     # convert string of image data to uint8
#     nparr = np.fromstring(r.data, np.uint8)
#     # decode image
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     filename = "test.png"
#     img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#     # do some fancy processing here....

#     # build a response dict to send back to client
#     response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
#                 }
#     # encode response using jsonpickle
#     response_pickled = jsonpickle.encode(response)

#     return make_response(response=response_pickled, status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(  # host="0.0.0.0", debug=True
    )
