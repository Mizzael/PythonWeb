from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return 'About Page'


# para mantenerla escuchando siempre
if __name__ == '__main__':
    app.run(debug=True)
