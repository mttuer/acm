from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    links = [
            {'title': 'Home', 'view': "home"},
            {'title': 'links', 'view': "home"},
            {'title': 'Interviews', 'view': "home"},
            ]
    user = {'nickname': 'Miguel'}
    return render_template("index.html", 
            title = 'ACM@MichiganTech', 
            links = links, 
            user = user
            )
    
