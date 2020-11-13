from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email
from db_connect import display_recent_sermons, display_all_series, display_all_preachers, sermon_search, get_sermon_by_id

class LoginForm(FlaskForm):
    user = StringField('username', validators=[Email()])
    user_password = PasswordField('password', validators=[DataRequired()])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'iwasborninohiobutmyheartisofteninmanyotherplaces'

@app.route('/')
def index():
    sermons = display_recent_sermons(12)
    series_dropdown = display_all_series()
    preacher_dropdown = display_all_preachers()
    return render_template('index.html', sermons=sermons, series_dropdown=series_dropdown, preacher_dropdown=preacher_dropdown)

@app.route('/sermon_search', methods=['post','get'])
def sermon_search_form():
    if request.method == 'POST':
        sermon_title = request.form.get('sermon_title')
        sermon_date = request.form.get('sermon_date')
        sermon_preacher = request.form.get('sermon_preacher')
        sermon_series = request.form.get('sermon_series')
        search_result = sermon_search(sermon_title, sermon_date, sermon_preacher, sermon_series)
    series_dropdown = display_all_series()
    preacher_dropdown = display_all_preachers()
    return render_template('index.html', sermons=search_result, series_dropdown=series_dropdown, preacher_dropdown=preacher_dropdown)


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

@app.route('/sermon/<id>')
def sermon_page(id):
    sermon = get_sermon_by_id(id)
    return render_template('sermons.html', sermon=sermon)

if __name__ == '__main__':
    app.run(debug=True)
