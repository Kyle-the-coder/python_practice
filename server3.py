from flask import Flask

app = Flask(__name__)

@app.route('/hello_world')
def index():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/hey/<name>')
def hey(name):
    return f"Hey {name}"

@app.route('/times/<string:name>/<int:num>')
def times(name,num):
    return name * num

@app.route('/<error>')
def error(error):
    return "error"



if __name__ == "__main__":
    app.run(debug=True)