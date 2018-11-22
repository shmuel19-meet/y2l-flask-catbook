from flask import Flask, request, redirect
from flask import render_template
from database import *
import requests
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')

def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def profile(id):
    cat = get_cat_by_id(id = id)
    return render_template("cat.html", cat = cat)

@app.route("/addcat", methods = ['GET', 'POST'])
def add_cat():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        name = request.form['cat_name']
        cat = create_cat(name = name)
        cats = get_all_cats()        
        return render_template('home.html', cats = cats)

@app.route("/vote/<int:id>", methods = ['GET', 'POST'])
def vote(id):

    if request.method == 'POST':

        temp_id = id
        vote_cat(temp_id)
        return redirect('/')
	
	#	cats = get_all_cats()
	#    return render_template("home.html", cats=cats)

if __name__ == '__main__':
   app.run(debug = True)