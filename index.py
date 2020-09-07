from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


@app.route('/about')
# para mantenerla escuchando siempre
if __name__ == '__main__':
    app.run()
