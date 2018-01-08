from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

#
# @app.route('/')
# def hello_world():
#     return render_template('first.html', title='Главная страница')
#
# @app.route('/user/<username>')
# def xxx(username):
#     return render_template('first.html', name=username)
#


# if __name__ == '__main__':
#     app.run()
#
#
#  remdom
