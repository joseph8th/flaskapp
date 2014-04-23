from flask import render_template, flash, redirect
from facepy import GraphAPI
from pymongo import MongoClient

from demo import app
from forms import AccessTokenForm


# MongoDB setup
client = MongoClient()
db = client.flaskapp_db


@app.route('/')
@app.route('/index')
def index():

    fb_users = db.fb_users

    # create 'user' dict from MongoDB for this demo ...
    users = []
    for user in fb_users.find():
        users.append(user['name'])

        print users

    return render_template("index.html",
                           title = 'Home',
                           users = users)



@app.route('/get_token', methods = ['GET', 'POST'])
def get_token():

    form = AccessTokenForm()

    if form.validate_on_submit():
        graph = GraphAPI(form.access_token.data)
        # add user to MongoDB
        fb_user = graph.get('me')
        fb_users = db.fb_users
        fb_users.insert(fb_user)

        return redirect('/index')

    return render_template('get_token_form.html',
                           title = 'Get Access Token',
                           form = form)
