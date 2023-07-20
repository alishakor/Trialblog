#!/usr/bin/python3

from flask import Flask, render_template

#create the flask Instance
app = Flask(__name__)
app.debug = True

#create route decorator
@app.route('/')

def index():
   # return "<h1>Hello world!</h1>"
    first_name = "John"
    stuff = "This is bold text"
    favourite_pizza = ["Pepporini", "Cheese", "Mushroom", 41]
    return render_template("index.html", 
            first_name=first_name,
            stuff=stuff,
            favourite_pizza=favourite_pizza)

@app.route('/user/<name>') 

def user(name):
    return render_template("user.html", user_name=name)
    #return "Hello {}".format(name)

#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
