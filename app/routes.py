from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Owen'}
    posts = [
        {
            'author': {'username': 'Mike'},
            'body': 'Beautiful day in the UK!'
        },
        {
            'author': {'username': 'Amy'},
            'body': 'Having a dating with Connor'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)