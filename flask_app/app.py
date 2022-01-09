# compose_flask/app.py
from flask import Flask
from flask import render_template, request, redirect, flash
from redis import Redis


UPLOAD_FOLDER = 'static/img/uploads/'

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

app.config["SECRET_KEY"] = "Super Secret Key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

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
        
        if request.files:
             
             image = request.files["image"]

             print(image)
             flash("image uploaded!", "success")
             
             return redirect(request.url)        
    
    return render_template("image_upload.html")

if __name__ == "__main__":
    app.run(#host="0.0.0.0", debug=True
            )
    app.secret_key = "super secret key"
