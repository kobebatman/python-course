from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    name = 'Батаа'
    age = 23
    return render_template('about.html', name=name, age=age)

@app.route('/contact')
def contact():
    phone = '99898989'
    return render_template('contact.html', phone=phone)

if __name__ == '__main__':
    app.run(debug=True)