from app import app
from flask import render_template, flash, redirect, url_for

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
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me = {}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    
    return render_template('login.html',title='Sing In', form=form)
