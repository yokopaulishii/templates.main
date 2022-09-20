from flask import Flask, render_template, redirect, url_for, request
from markupsafe import escape
from jinja2 import Template

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route("/home", methods= ['GET'])
def home():
    if request.method == ['GET']:
        return redirect (302, '/')

@app.route("/", methods= ['GET'])
def index(title):
    if request.method == ['GET']:
        return render_template(index.html, title=Index})

@app.route("/about", methods= ['GET'])
def about(title):
    if request.method == ['GET']:
        return render_template(about.html, title=About})

@app.route("/third", methods= ['GET'])
def third(title):
    if request.method == ['GET']:
        return render_template(third.html, title=Third})

if __name__=='__main__':
    app.run(debug=True)
