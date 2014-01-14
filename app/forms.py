from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, DateField, DateTimeField, DecimalField, RadioField, IntegerField
from wtforms.validators import Required, Optional

class NewUserForm(Form):
    username = TextField('username', validators = [Required()])
    email = TextField('email', validators = [Required()])

class NewPostForm(Form):
    body = TextField('body', validators = [Required()])
    ready = BooleanField('ready', default=False) 

class NewEventForm(Form):
    title = TextField('title', validators =[Required()])
    descr = TextField('descr', validators =[Required()])
    date = DateField('date', validators =[Required()])
    start = DateTimeField('start', validators =[Required()])
    end = DateTimeField('end', validators =[Required()])
    location = TextField('location', validators =[Required()])
    category = RadioField('category', validators = [Required()],
            choices =[('a','Speaker'),('c','Hackathon'),('c','Competition'),('d','Career Development')])
    entrance = DecimalField('entrance', validators = [Required()])
    logoName = TextField('logoName')

class NewSponsorForm(Form):
    name = TextField('name', validators =[Required()])
    phone = TextField('phone', validators =[Required()])
    email = TextField('email', validators =[Required()])
    website = TextField('website', validators =[Required()])
    pocFirstName = TextField('pocFirstName', validators =[Required()])
    pocLastName = TextField('pocLastName', validators =[Required()])

class NewSponsorshipForm(Form):
    eventID = IntegerField('eventID', validators =[Required()])
    sponsorID = IntegerField('sponsorID', validators =[Required()])
    amount = DecimalField('amount', validators =[Required()])
    dateRec = DateField('dateRec', validators =[Optional()])
