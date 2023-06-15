import os
from flask import Flask
from flask import render_template, request, redirect, flash, url_for, jsonify, make_response
from flask import send_from_directory
from werkzeug.utils import secure_filename
import numpy as np
import base64
import json
from PIL import Image
from io import BytesIO
import db_pred as db
import model_inspection as inspection
from markupsafe import escape

# Model Preparation
loaded_model = inspection.load_model()

# Create table
db.create_db()
db.create_table()

app = Flask(__name__)

app.config["SECRET_KEY"] = "Super Secret Key"
app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Allow only pictures to be uploaded
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")

# About and Instructions on how to use the API
@app.route("/about", methods=["GET"])
def about():
    user_agent = request.headers.get("User-Agent", "")
    if "Mozilla" in user_agent or "Chrome" in user_agent or "Safari" in user_agent:
        return render_template("about.html")
    else:
        data = {
            "status": "success",
            "message": "Welcome to our sophisticated Flask application, designed meticulously by our dedicated team of data scientists. The purpose of this application is to predict digits from hand-drawn images.",
            "instructions": {
                "description": "To get started with our application, you are invited to follow these instructions:",
                "steps": [
                    {
                        "step1": {
                            "description": "Create a POST request with a JSON body. The JSON body should incorporate the following data format:",
                            "data_format": {
                                "filename": "(your-filename.png/jpg/jpeg)",
                                "image": "(Image as Base64 String)"
                            }
                        }
                    },
                    {
                        "step2": "Send your request to the /image-predict endpoint of our application."
                    },
                    {
                        "step3": "Alternatively, you can use the 'Upload Image' button on our website to upload your image directly through the browser."
                    }
                ]
            },
            "suggestions": [
                "You can explore our Github page to get insight into our work and contributions.",
                "Stay informed about our latest thoughts, ideas, and innovations by visiting our blog.",
                "We value your feedback and queries. Please feel free to contact us anytime."
            ]
        }
        return jsonify(data), 200, {"Content-Type": "application/json"}



# Website UI Part


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if 'image' not in request.files:
            flash('No image part', 'danger')
            return redirect(request.url)
        image = request.files['image']
        if image.filename == '':
            flash('No image selected for uploading', "warning")
            return redirect(request.url)
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            prediction = 2 # PLACEHOLDER

            # Convert image data converted to base64 to original binary data# bytes
            # Filestorage item has to be encoded so we can resize with PIL and np
            image_bytes = base64.b64encode(image.read())
            image_string = image_bytes.decode("utf-8")
            img = base64.b64decode(image_string)
            img = BytesIO(img) # _io.Converted to be handled by BytesIO pillow
            img = Image.open(img)
            img = img.resize((28, 28))
            img_np = np.array(img)

            # all 3 dimensional images will need to be resized to (1, 28, 28, 1) for the model
            if img_np.ndim == 3:
                img_np = img_np.astype("float32") / 255
                img_np = img_np[:, :, 0]
                img_np = np.expand_dims(img_np, -1)
                img_np = np.array([img_np])

            # incase image/array is already 2 dimensional (grey scale) we proceed as milestone 1
            if img_np.ndim == 2:
                img_np = img_np.astype("float32") / 255
                img_np = np.expand_dims(img_np, -1)
                # Model expects shape (x, 28, 28, 1)
                img_np = np.array([img_np])

            prediction = loaded_model.predict(img_np)
            int_single_prediction = np.argmax(prediction, axis=1)
            int_single_prediction = int(int_single_prediction)
            prediction = str(int_single_prediction)

            img_PIL = Image.open(image)
            image = img_PIL.copy()
            db.save_prediction_db(filename, image, prediction)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Image successfully uploaded and displayed below', "success")

            return render_template('image_upload.html', filename=filename, prediction=prediction)
        else:
            flash('Allowed image types are -> png, jpg, jpeg', "danger")
            return redirect(request.url)

    return render_template("image_upload.html")


@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route('/uploads/<prediction>')
def send_prediction(prediction=''):
    return escape(prediction)


#API JSON Part

images = [
    {'image': 'iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8/fFQqAAAACXBIWXMAAA9hAAAPYQGoP6dpAAABfElEQVR4nO1W0Y2DMAw16LpFukf2aDJHmzVAqGuEroGI2m7RrlE5776aAxJoOOn6caolyxImvDw/26IgItAbrXwn2AfwA/gr+8p5qW1bAkCXy4WOx2OUN8YQESVzKcOSSykBAMwMAKjrGt57MHMy1nW9+L1FQGMMrLVgZjwej+xojFkPOGU2jClmXddlMS2eqFOz1pLWmrz3VJZlFJumoev1SgCoKAo6n8+03+/pcDiE9zabTZ6GTdMkmbVtCynlbLmccyPm2SVNaVNV1atmgBACXdeFczMXjA/e73dYa0PjvGiCyKcaD3PJOQR+ZM2dren5oeZRfuoAoJRaxYqIoLVG3/eBmTEmr6TMjN1ulw30LPlU+5kGW8ci5d57KKUCsxfdHD88nU6haXKcmUfduXrTSClxu93gnIPWGtvtFlrrkVZDz2S2XFIpZbhx3/dhruZ2a1VVueMzn3TORTsyFVfO6XxSCAEhBJRSI43WbqChzy7vv7L//0/zdsBvGrApTDvwxZ0AAAAASUVORK5CYII=', 'filename': "test_number.png"}
]


@app.route('/image-predict', methods=['GET'])
def get_images():
    return jsonify(images)


@app.route('/image-predict', methods=['POST'])
def add_images():
    json_data = request.get_json() # Get the POSTed json
    json_data = json.dumps(json_data)
    dict_data = json.loads(json_data) # Convert json to dictionary

    img = dict_data["image"] # Take out base64# str
    # Convert image data converted to base64 to original binary data# bytes
    img = base64.b64decode(img)
    img = BytesIO(img) # _io.Converted to be handled by BytesIO pillow
    img = Image.open(img)
    img_shape = img.size
    img = img.resize((28, 28))
    img_np = np.array(img)

    # all 3 dimensional images will need to be resized to (1, 28, 28, 1) for the model
    if img_np.ndim == 3:
        img_np = img_np.astype("float32") / 255
        img_np = img_np[:, :, 0]
        img_np = np.expand_dims(img_np, -1)
        img_np = np.array([img_np])

    # incase image/array is already 2 dimensional (grey scale) we proceed as milestone 1
    if img_np.ndim == 2:
        img_np = img_np.astype("float32") / 255
        img_np = np.expand_dims(img_np, -1)
        # Model expects shape (x, 28, 28, 1)
        img_np = np.array([img_np])

    prediction = loaded_model.predict(img_np)
    int_single_prediction = np.argmax(prediction, axis=1)
    int_single_prediction = int(int_single_prediction)

    filename=dict_data["filename"]
    
    db.save_prediction_db(filename,img,int_single_prediction)

    
    response={
      'prediction':int_single_prediction,
      'filename':filename,
      'status':'success',
      'original_img_shape':img_shape
      }
    
    return jsonify(response), 200, {"Content-Type": "application/json"}


if __name__ == "__main__":
    app.run( 
            #for local (non docker use), comment this line out
            host="0.0.0.0", debug=False
    )
