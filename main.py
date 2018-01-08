from flask1 import app
from flask1 import db
from posts.blueprint import posts
import view

app.register_blueprint(posts, url_prefix='/flask1')


if __name__ == '__main__':
    app.run()
# remdom
