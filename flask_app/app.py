# compose_flask/app.py
import os
from flask import Flask
from flask import render_template, request, redirect, flash, url_for
from redis import Redis
from werkzeug.utils import secure_filename

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


@app.route("/about")
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
        if image.filename == '':
            flash('No image selected for uploading', "warning")
            return redirect(request.url)
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('upload_image filename: ' + filename)
            flash('Image successfully uploaded and displayed below', "success")
            return render_template('image_upload.html', filename=filename)
        else:
            flash('Allowed image types are -> png, jpg, jpeg, gif', "danger")
            return redirect(request.url)

    return render_template("image_upload.html")


@app.route('/uploads/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(  # host="0.0.0.0", debug=True
    )
