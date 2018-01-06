from flask1 import app
from flask import render_template

@app.route('/')
def index():
    return render_template('first.html')