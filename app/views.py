from flask import render_template
from app import app
import connect
import copy

@app.route('/')
@app.route('/home')
def index():
    links = [
            {'title': 'Home', 'view': "home"},
            {'title': 'Links', 'view': "links"},
            {'title': 'Interviews', 'view': "interviews"},
            ]
    user = {'nickname': 'Miguel'}
    return render_template("index.html", 
            title = 'ACM@MichiganTech', 
            links = links, 
            user = user,
            active = "home"
            )

@app.route('/admin')
def admin():
    db = connect.getDB()

    db.execute("SELECT * FROM tbUsers;")
    users = copy.deepcopy(db.fetchall())
    uKeys = connect.getColNames("tbUsers")

    db.execute("SELECT * FROM tbPosts;")
    posts = copy.deepcopy(db.fetchall())
    pKeys = connect.getColNames("tbPosts")

    connect.close()

    links = [
            {'title': 'Home', 'view': "home"},
            {'title': 'links', 'view': "home"},
            {'title': 'Interviews', 'view': "home"},
            ]

    user = {'nickname': 'Miguel'}

    return render_template("admin.html", 
            title = 'ACM@MichiganTech', 
            links = links, 
            user = user,
            users=users,
            usersKeys=uKeys,
            posts=posts,
            postsKeys=pKeys,
            )


    
