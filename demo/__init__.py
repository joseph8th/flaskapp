from flask import Flask

# init Flask app
app = Flask(__name__)
app.config.from_object('config')

from demo import views

