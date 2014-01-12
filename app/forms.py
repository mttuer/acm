from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, DateField, DateTimeField, DecimalField, RadioField
from wtforms.validators import Required

class NewUserForm(Form):
    username = TextField('username', validators = [Required()])
    email = TextField('email', validators = [Required()])

class NewPostForm(Form):
    body = TextField('body', validators = [Required()])
    ready = BooleanField('ready', default=False) 

class NewEventForm(Form):
    title = TextField('Title', validators =[Required()])
    descr = TextField('Description', validators =[Required()])
    date = DateField('Date of Event', validators =[Required()])
    start = DateTimeField('Date of Event', validators =[Required()])
    end = DateTimeField('Date of Event', validators =[Required()])
    location = TextField('Location of Event', validators =[Required()])
    category = RadioField('Type of Event', validators = [Required()],
            choices =['Speaker','Hackathon','Competition','Career Development'])
    entrance = DecimalField('Entrance Fee', validators = [Required()])
    logoName = TextField('Logo Image File')

