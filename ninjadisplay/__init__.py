from flask import Flask, render_template

from ninjadisplay import api

app = Flask(__name__)

client = api.create_client()

@app.route('/')
def slash():
    return render_template('base.html')

from ninjadisplay import views