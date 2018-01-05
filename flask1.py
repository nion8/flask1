from flask import Flask, render_template

#
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('first.html', title='Главная страница')
    #
    # @app.route('/user/<username>')
    # def xxx(username):
    #     return render_template('first.html', name=username)
    #


if __name__ == '__main__':
    app.run()
#
#
# # remdom
