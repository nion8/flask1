from flask import Flask
from config import Configuration

#
app = Flask(__name__)
app.config.from_object(Configuration)

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
# # remdom
