from flask import render_template
from app import app
import connect
import copy

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

@app.route('/admin')
def admin():
    db = connect.getDB()
    tables = ["tbUsers","tbPosts","tbEvents"]
    tblSets = list()
    for tbl in tables:
        keys = connect.getColNames(tbl)
        s = str()
        for k in keys:
            s += k + ","
        s="SELECT " + s[:-1] + " FROM " + tbl
        print s
        db.execute(s)
        tblSets.append({'tbName':tbl,
            'keys':keys,
            'rows':copy.deepcopy(db.fetchall())})

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
            tables=tblSets
            )

