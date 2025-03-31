from flask import Flask
# app is an object of "Flask"
app = Flask(__name__)
# "@" is called "Decorator"
@app.route("/")
def hello_world():
  return "<p>Hello World</p>"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)