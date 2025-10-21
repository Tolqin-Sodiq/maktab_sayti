from flask import Flask, render_template
from datetime import datetime   # ← shu qator juda muhim

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', datetime=datetime)

@app.route('/about')
def about():
    return render_template('about.html', datetime=datetime)

@app.route('/clubs')
def clubs():
    return render_template('clubs.html', datetime=datetime)

@app.route('/contact')
def contact():
    return render_template('contact.html', datetime=datetime)

@app.route('/register')
def register():
    return render_template('register.html', datetime=datetime)

if __name__ == '__main__':
    app.run(debug=True)
