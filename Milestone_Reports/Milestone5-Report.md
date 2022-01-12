# Milestone 5 

# TASK 1

Worked through the first flask tutorial stated on the project5.pdf which included downloading NGINX as well.
# TASK 2 & 3 



## First Trials

Thanks to flask's popularity, it was quite easy to find great resources for Tutorials on how to set up Endpoints for our API. 

```
import flask
app = Flask(_name_)

if __name__ == "__main__":
    app.run(
    )

```
These are the basic building blocks to "flask run" your web service.
You quickly see from the cmd line output that your webservice runs on https://localhost:5000/ .



## GET Request

We started with setting up directory and and *app.py* file. For an easy GET Request to begin with, we had the following example form the internet.

```

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

```

the *app.route(/stock)* define where a to what URL the GET Request should be sent: http://localhost:5000/stock. Additionally you can then set up a function that defines the reply you send to the requester.

## POST Request 

Post Requests are similarly defined but they differ because data/parameters/keys get sent to the API.
The setup is the same as before (besides: methods=["POST"]). But now we can receive the data and define a response - like a prediction - to send to the request user.

## JINJA & BOOTSTRAP

It was clear pretty early on that we wanted to implement TASK3 a "website" with a upload form with our endpoint.
Since we had never really worked with html/css before this was great insight into the workings.

We were quickly introduced to Jinja Templates. **JINJA** (https://jinja.palletsprojects.com/en/3.0.x/) essentially is a template engine for python where you can define a "standard template" and implement additional various dynamic pages that keep the essential parts of the standard website with dynamic additions that are compatible with flask (render_template).
We additionally implemented **BOOTSTRAP** (https://getbootstrap.com/) in our *standard_template.html* which is a frontend development framework that gives us an extensive variety and choice of Website building blocks - such as, in our case, navbars, file upload forms and so much more.

```
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    return render_template("image_upload.html")
```
With code as simple as this, it was already possible to set up a upload form for images:

```
{% extends "jinja_template/standard_template.html" %}

{% block title %}Upload{% endblock %}

{% block main %}

<div class="container">
  <div class="row">
    <div class="col">

      <h1><strong>Upload an Image</strong></h1>
      <hr>

      <form action="/upload-image" method="POST" enctype="multipart/form-data">
        <div class="form-group">
          <label style = "color:white"><strong>Select a hand drawn digit image and our Model will predict the exact number.</strong></label>
          <div class="custom-file">
            <input type="file" class="custom-file-input" name="image" id="image">
            <label class="custom-file-label" for="image">Select image...</label>
          </div>
        </div>

        <button type="submit" class="btn btn-info">Upload</button>

      </form>

    </div>
  </div>
</div>

{% endblock %} 
```
as you can tell from the flask part, the post request doesn't do anything yet with the image saved. Which turned out to be a lot of a hassle than expected

![Starting Website]()


With a lot headaches we additionally implemented that alerts, image name, displayed the picture and displaying the predicted number our model made.


![Image Upload Page]()


## Processing Images through JSON and base64

Because the website part turned out to be much more difficult than the actual API task at hand, we switched our focus on being able to receive POST Request images and then responding with a prediction from our model.

We noticed pretty early on that the processing is gonna be not as easy as the DB part. 

First off was finding a tool to make our image readable through "string".
Making an Image Base 64 https://base64.guru/converter/encode/image was quite easy. We first thought about implementing "key/value" pairs in link format for the POST request but then decided for JSON cause the tools and online documentation on how to convert images was much more extensive. 

Our set up for POST Requests: "filename": "", "image":""

```
import requests

#Get A sample of how your POST Request should look like:
response = requests.get("http://localhost:5000/image-predict")
print(response.json())

#POST Request that gets you a prediction number for your image

#To enconde an image to base64, please use this website https://base64.guru/converter/encode/image
# and copy the string into your "image" : (your string)

response = requests.post("http://localhost:5000/image-predict", 
                         json = ({"image": "iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8/fFQqAAAACXBIWXMAAA9hAAAPYQGoP6dpAAABfElEQVR4nO1W0Y2DMAw16LpFukf2aDJHmzVAqGuEroGI2m7RrlE5776aAxJoOOn6caolyxImvDw/26IgItAbrXwn2AfwA/gr+8p5qW1bAkCXy4WOx2OUN8YQESVzKcOSSykBAMwMAKjrGt57MHMy1nW9+L1FQGMMrLVgZjwej+xojFkPOGU2jClmXddlMS2eqFOz1pLWmrz3VJZlFJumoev1SgCoKAo6n8+03+/pcDiE9zabTZ6GTdMkmbVtCynlbLmccyPm2SVNaVNV1atmgBACXdeFczMXjA/e73dYa0PjvGiCyKcaD3PJOQR+ZM2dren5oeZRfuoAoJRaxYqIoLVG3/eBmTEmr6TMjN1ulw30LPlU+5kGW8ci5d57KKUCsxfdHD88nU6haXKcmUfduXrTSClxu93gnIPWGtvtFlrrkVZDz2S2XFIpZbhx3/dhruZ2a1VVueMzn3TORTsyFVfO6XxSCAEhBJRSI43WbqChzy7vv7L//0/zdsBvGrApTDvwxZ0AAAAASUVORK5CYII="
                                 ,"filename": "request_test.png"}))
print(response.json())
```

And this is what we do with the given data. JSON cant accept dict from python so json.dumps() and json.loads is necessary due to differing object structures/names, we decode the image so it can be read and opened by PILLOW for resizing (28x28), we convert it into a nparray and then the preprocessing follows as per previous milestones.

Since the nparray must be (1, 28, 28, 1) to be processed by our model we additionally created if functions for 2 dim arrays (greyscale that don't have a color 3rd dimension) and for 3 dim arrays which "normal/color" pictures usually are as well. The model predicts the number and we then ship it back as a response to the user in a json.


```
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
    print(type(img))
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
    #Save to db
    db.save_prediction_db(filename, img_np, int_single_prediction)
    # img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # Return the processing result to the client

    response = {
        "prediction": int_single_prediction,
        "img_shape": img_shape
    }

    return jsonify(response)
```
 
Response from JSON:

```
{'img_shape': [28, 28], 'prediction': 0}
```

## Database

Database initialization was pretty straight forward. We created a new script that created DB and table and then inserted whatever image data we give it with (BYTEA). We decided to save the images as **NPARRAYS** cause that's what the model expects and it creates the least amount of programming to display the image. All of the functions are in **flask_app/db_pred.py**. Selecting the posted image and saving it locally:

```
def select_image_from_db():
    conn = psycopg2.connect(
        database="mnist_prediction", user='admin', password='secret', host='db', port='5432'
    )

    cursor = conn.cursor()
    
    cursor.execute(
    """
    SELECT image
    FROM predictions
    ORDER BY date DESC
    LIMIT 1
    """,
)
    # img_from_db = pickle.loads(cursor.fetchone()[0])
    img_from_db = pickle.loads(cursor.fetchone()[0])
    conn.commit()
    conn.close()
    
    img_from_db = np.asarray(img_from_db)
    print(type(img_from_db))
    # print(img_from_db.shape)
    print(img_from_db.shape)

    two_d = (np.reshape(img_from_db, (28, 28)) * 255).astype(np.uint8)
    plt.imsave(fname="test_readDB_test_photo.png",arr= two_d, cmap=plt.get_cmap('gray'))
    
    
```


We then implemented the process for the Website where we additionally need to locally save the image so that the image can be displayed after uploaded and accessed by our render_template
 
```
            # img_PIL.save(os.path.join(app.config['UPLOAD_FOLDER'], "test_to.png"))
            db.save_prediction_db(filename, image, prediction)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below', "success")

            return render_template('image_upload.html', filename=filename, prediction=prediction)
        else:
            flash('Allowed image types are -> png, jpg, jpeg, gif', "danger")
            return redirect(request.url)

    return render_template("image_upload.html")


@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
```

send_uploaded_file() accesses the filename and finds the image locally to and previews it for the client. Additionally the prediction will also be displayed 

## DOCKERIZING

Dockerization was thankfully a bit more rudimentary than before. 
We had little issues with accessing the server (since localhost doesn't work) but with help of arguments in main statement, we could then easily access it. 

```
if __name__ == "__main__":
    app.run( 
            #for local (non docker use), comment this line out
            host="0.0.0.0", debug=True
    )

```

A slight issue accured with finding the image after it was uploaded (since filepaths are different depending on docker image) so we changed the ["UPLOAD FOLDER"] path to os.getcwd() so flask has no issues accessing the image to display.

```
UPLOAD_FOLDER = os.getcwd()
```

## Commands

On POSTMAN you can send POST Request likes this:


To display base64 images, upload the string on this tool:

Vice Versa:
https://devpal.co/base64-image-decode/

