from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email
from db_connect import display_recent_sermons

class LoginForm(FlaskForm):
    user = StringField('username', validators=[Email()])
    user_password = PasswordField('password', validators=[DataRequired()])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iwasborninohiobutmyheartisofteninmanyotherplaces'

@app.route('/')
def index():
    sermons = display_recent_sermons(12)
    return render_template('index.html', sermons=sermons)

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/parenting-book')
def book_page():
    return render_template('resource-parenting.html')

@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('user-login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
