from flask import Flask, render_template, request

from tinydb import TinyDB, Query
from categories import get_categories
from location import get_location
from others import similar_categories

app = Flask(__name__)

db = TinyDB('db/db.json')
"""
@app.route("/")
def test2():
    return render_template("index.html")
"""

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form.to_dict()
        result["city"] = get_location()
        result["category"] = get_categories(result["Pain"])
        result["Location"] = request.form.get("Location")
        print(str(request.form.get("Location")))
        db.insert(result)
        similar = similar_categories(result["category"])
        return render_template("result.html",result = result, similar = similar)

@app.route('/', methods = ['POST', 'GET'])
def dnb():
    return render_template("DNB.html")

if __name__ == "__main__":
    app.run(debug=True)