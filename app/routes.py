from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'Username':'Gabriel'}
    
    return '''
<html>
    <head> 
        <title> Home Page - Microblog </title>
    </head>
        
    <body>
        <h1> Hello ''' + user['Username']+ '''!</h1>
    </body>
</html>
'''
