from flask import Flask, render_template
# app is an object of "Flask"
app = Flask(__name__)
# "@" is called "Decorator"
@app.route("/")
def hello_world():
  return render_template('home.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5000, debug=True)