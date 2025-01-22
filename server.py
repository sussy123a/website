from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Publicly Accessible Website!</h1>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This website is accessible from anywhere.</p>"

if __name__ == "__main__":
    # Change port to a custom one, e.g., 5000, but hosting requires port forwarding/public tunnel.
    app.run(host="0.0.0.0", port=5000)
