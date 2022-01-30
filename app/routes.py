from app import app
from app.models import User

from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user

from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Gabriel'}
    
    posts = [
        {
            'author' : {'username':'Maria'},
            'body' : 'Beatiful day in Partland!'
        },
        
        {
            'author' : {'username':'Victor'},
            'body' : 'The Avengers movie was so cool!'
        }
    ]
    
    return render_template('index.html', title = 'Home', user=user, posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!')
            return redirect(url_for('login'))
        login_user(user, remenber=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html',title='Sing In', form=form)
