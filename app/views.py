from flask import render_template, flash, redirect
from app import app
from forms import *
from db import dbUtils 
import copy

links = [
        {'title': 'Home', 'view': "index"},
        {'title': 'Events', 'view': "events"},
        {'title': 'Admin', 'view': "admin"},
        {'title': 'Sponsors', 'view': "sponsors"},
        ]


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return render_template("index.html", 
            title = 'Home', 
            links = links, 
            user = user
            )

@app.route('/events')
def events():
    tbName = "tbEvents"
    rset = dbUtils.getTable(tbName)
    kToI = dict()
    for i in range(0,len(rset['keys'])):
        kToI[rset['keys'][i]] = i

    return render_template("events.html", 
            title = 'Events', 
            links = links, 
            tbl = rset,
            kToI=kToI
            )


@app.route('/admin')
def admin():
    tables = ["tbUsers","tbPosts","tbEvents", "tbSponsors"]
    tblSets = list()
    for tbl in tables:
        rset = dbUtils.getTable(tbl)
        tblSets.append({'tbName':tbl, 'keys':rset['keys'], 'rows':rset['rows']})

    return render_template("admin.html", 
            title = 'Admin', 
            links = links, 
            tables = tblSets
            )

@app.route('/newevent', methods = ['GET', 'POST'])
def newevent():
     form = NewEventForm()
     if form.validate_on_submit():
        dbUtils.createEvent(form.title.data, form.descr.data, form.date.data,
                form.start.data,
                form.end.data,
                form.location.data,
                form.category.data,
                form.entrance.data,
                form.logoName.data
                )
        flash("New event created")
     return render_template('newevent.html', 
        title = 'New Event',
        links = links, 
        form = form)

@app.route('/newsponsorship', methods = ['GET', 'POST'])
def newsponsorship():
    tables = ["tbSponsors", "tbEvents"]
    tblSets = list()
    for tbl in tables:
        rset = dbUtils.getTable(tbl)
        tblSets.append({'tbName':tbl, 'keys':rset['keys'], 'rows':rset['rows']})

    form = NewSponsorshipForm()
    if form.validate_on_submit():
       dbUtils.addSponsorship(form.eventID.data, form.sponsorID.data,
               form.amount.data,
               form.dateRec.data
               )
       flash("New Sponsorship Added")
    return render_template('newsponsorship.html', 
       title = 'Add a Sponsorship',
       links = links, 
       tables=tblSets,
       form = form)

@app.route('/newsponsor', methods = ['GET', 'POST'])
def newsponsor():
     form = NewSponsorForm()
     if form.validate_on_submit():
        dbUtils.addSponsor(form.name.data, form.website.data,
                form.email.data,
                form.phone.data,
                form.pocFirstName.data,
                form.pocLastName.data
                )
        flash("New post created")
     return render_template('newsponsor.html', 
        title = 'Add a Sponsor',
        links = links, 
        form = form)

@app.route('/newpost', methods = ['GET', 'POST'])
def newpost():
     form = NewUserForm()
     if form.validate_on_submit():
        dbUtils.createPost(form.body.data, form.ready.data)
        flash("New post created")
     return render_template('newpost.html', 
        title = 'New Post',
        links = links, 
        form = form)

@app.route('/newuser', methods = ['GET', 'POST'])
def newuser():
     form = NewUserForm()
     if form.validate_on_submit():
        dbUtils.createUser(form.username.data, form.email.data, 0)
        flash("New user created")
     return render_template('newuser.html', 
        title = 'New User',
        links = links, 
        form = form)

@app.route('/sponsors')
def sponsors():
     return render_template('sponsors.html',
        title = 'Sponsorship',
        links = links)

