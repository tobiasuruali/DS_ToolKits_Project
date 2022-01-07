# compose_flask/app.py
from flask import Flask
from flask import render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

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
    return render_template("image_upload.html")

if __name__ == "__main__":
    app.run(#host="0.0.0.0", debug=True
            )
