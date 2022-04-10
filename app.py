import flask
import json
from flask import request, jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    file = open("index.html", "r")
    return file.read()


@app.route('/contacts.json')
def data():
    file = open("contacts.json", "r")
    return file.read()


@app.route('/results.json')
def results():
    file = open("results.json", "r")
    return file.read()

@app.route('/fullList.html')
def list():
    file = open("fullList.html", "r")
    return file.read()

@app.route('/addForm.html', methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        with open('contacts.json') as f:
            data = json.load(f)
        data.append(request.form)
        with open('contacts.json', 'w') as f:
            json.dump(data, f)
            
    file = open("addForm.html", "r")
    return file.read()


@app.route('/lookUp.html', methods=['POST', 'GET'])
def search():
    results = []

    with open('contacts.json') as f:
        data = json.load(f)

    if request.method == "POST":
        for i in data:
            if request.form['value'].lower() in i[request.form['foo']].lower() and request.form['value'] != "":
                results.append(i)
        with open('results.json', 'w') as f:
            json.dump(results, f)
        file = open("results.html", "r")
        return file.read()
            
    file = open("lookUp.html", "r")
    return file.read()


if __name__ == "__main__":
    app.run(host="0.0.0.0")