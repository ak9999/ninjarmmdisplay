from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def slash():
    return render_template('base.html')

from ninjadisplay import views