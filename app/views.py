from flask import render_template, flash, redirect
from app import app
from forms import *
import connect
import copy

@app.route('/')
@app.route('/index')
def index():
    links = [
            {'title': 'Home', 'view': "index"},
            {'title': 'Events', 'view': "events"},
            {'title': 'Admin', 'view': "admin"},
            ]
    user = {'nickname': 'Miguel'}
    return render_template("index.html", 
            title = 'ACM@MichiganTech', 
            links = links, 
            user = user
            )

@app.route('/events')
def events():
    db = connect.getDB()

    tbName = "tbEvents"
    keys = connect.getColNames(tbName)
    kToI = dict()
    for i in range(0,len(keys)):
        kToI[keys[i]] = i
    getRowsForKeys(tbName, keys, db)
    tbl = {'keys':keys, 'rows':copy.deepcopy(db.fetchall())}

    links = [
            {'title': 'Home', 'view': "index"},
            {'title': 'Events', 'view': "events"},
            ]

    user = {'nickname': 'Miguel'}

    return render_template("events.html", 
            title = 'ACM@MichiganTech', 
            links = links, 
            user = user,
            tbl = tbl,
            kToI=kToI
            )


@app.route('/admin')
def admin():
    db = connect.getDB()
    tables = ["tbUsers","tbPosts","tbEvents"]

    tblSets = list()
    for tbl in tables:
        keys = connect.getColNames(tbl)
        getRowsForKeys(tbl, keys, db)
        tblSets.append({'tbName':tbl, 'keys':keys,
            'rows':copy.deepcopy(db.fetchall())})

    links = [
            {'title': 'Home', 'view': "index"}
            ]

    user = {'nickname': 'Miguel'}

    return render_template("admin.html", 
            title = 'ACM@MichiganTech', 
            links = links, 
            user = user,
            tables=tblSets
            )

@app.route('/newuser', methods = ['GET', 'POST'])
def login():
     links = [
            {'title': 'Home', 'view': "index"}
            ]

     user = {'nickname': 'Miguel'}


     form = NewUserForm()
     if form.validate_on_submit():
         flash("New user created")
         db = connect.getDB()
         values = list()
         values.append(form.username.data)
         values.append(form.email.data)
         db.execute("INSERT INTO tbUsers (username, email, privledge) VALUES (%s,%s,0);", values)
         connect.commit()
         connect.close()
     return render_template('newuser.html', 
        title = 'ACM@MichiganTech',
        links = links, 
        user = user,
        form = form)

def getRowsForKeys(tbl, keys, db):
    s = str()
    for k in keys:
        s += k + ","
    s="SELECT " + s[:-1] + " FROM " + tbl
    db.execute(s)

