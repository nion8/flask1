from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def xxx(username):
    return render_template('first.html', name=username)

if __name__ == '__main__':
    app.run()
    fg

