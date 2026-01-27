import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


@app.route("/")
def index():
    # template found in templates/index.html
    return render_template("index.html")


@app.route("/laureates/")
def laureate_list():
    # template found in templates/laureate.html
    results = []
    if not request.args.get("flName"):
        return jsonify(results)

    search_string = request.args.get("flName").lower().strip()
    search_terms = [term for term in search_string.split() if term]

    # tip: remember that laureate["name"] contains a first name
    for laureate in laureates:
        surname = laureate["surname"].lower()
        first_name = laureate['name'].lower()
        # your code here
        if not search_terms:
            continue

        if any(term in surname or term in first_name for term in search_terms):
            results.append(laureate)

    return jsonify(results)


app.run(debug=True)
