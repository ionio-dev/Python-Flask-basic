from flask import Flask, render_template
from app.property import server_config

app = Flask(__name__)


@app.route('/')
def start_app():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=server_config.HOST, port=server_config.PORT)

