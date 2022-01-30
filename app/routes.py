from app import app
from flask import render_template

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
