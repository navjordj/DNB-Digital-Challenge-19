from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from tinydb import TinyDB, Query
from categories import get_categories
from location import get_location

app = Flask(__name__)

db = TinyDB('db/db.json')

@app.route("/")
def test2():
    return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form.to_dict()
        result["city"] = get_location()
        result["kategori"] = get_categories(result["Pain"])
        print(result["Pain"], result["Age"])
        #db.insert({'pain': result["Pain"], 'age': result["Age"], 'city': get_location() , 'kategori': get_categories()})
        db.insert(result)

        return render_template("result.html",result = result)
    else:
        print("funka ikke")

if __name__ == "__main__":
    app.run(debug=True)
