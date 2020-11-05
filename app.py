from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/parenting-book')
def book_page():
    return render_template('resource-parenting.html')

@app.route('/login')
def login_page():
    return render_template('user-login.html')

if __name__ == '__main__':
    app.run(debug=True)
