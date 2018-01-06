from flask1 import app
from flask import render_template

@app.route('/')
def index():
    name = 'Алексей'
    return render_template('first.html', n=name)
