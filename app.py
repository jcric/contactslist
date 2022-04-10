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





































# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()