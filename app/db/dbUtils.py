from connect import *
import datetime

#######################
# Update Methods
#######################

######## USERS ################
def setUserName(sID, username):
    updateRowValsWhere("tbUsers",{'username':username, 'id':sID})

def setEmail(sID, email):
    updateRowValsWhere("tbUsers",{'email':email, 'id':sID})

def setLastLogin(sID, lastLogin):
    updateRowValsWhere("tbUsers",{'lastLogin':lastLogin, 'id':sID})

def setPrivledge(sID, privledge):
    updateRowValsWhere("tbUsers",{'privledge':privledge, 'id':sID})

######### SPONSORS #############
def setName(sID, name):
    updateRowValsWhere("tbSponsors", {'name':name},{'id':sID})

def setWebsite(sID, web):
    updateRowValsWhere("tbSponsors", {'website':web},{'id':sID})

def setEmail(sID, email):
    updateRowValsWhere("tbSponsors", {'email':email},{'id':sID})

def setPhone(sID, phone):
    updateRowValsWhere("tbSponsors", {'phone':phone},{'id':sID})
    
def setPOCFirst(sID, pocFirst):
    updateRowValsWhere("tbSponsors", {'pocFirstName':pocFirst},{'id':sID})
    
def setPOCLast(sID, pocLast):
    updateRowValsWhere("tbSponsors", {'pocLastName':pocLast},{'id':sID})
    
######### EVENTS #############
def setActive(eventID, active):
    updateRowValsWhere("tbEvents",{'active':active},{'id':eventID})

def setLocation(eventID, location):
    updateRowValsWhere("tbEvents",{'location':location},{'id':eventID})

def setLogo(eventID, logoName):
    updateRowValsWhere("tbEvents",{'logoName':logoName},{'id':eventID})

def setDate(eventID, date):
    updateRowValsWhere("tbEvents",{'date':date},{'id':eventID})

def setDescr(eventID, descr):
    updateRowValsWhere("tbEvents",{'descr':descr},{'id':eventID})

def setTitle(eventID, title):
    updateRowValsWhere("tbEvents",{'title':title},{'id':eventID})

def setEndDate(eventID, end):
    updateRowValsWhere("tbEvents",{'end':end},{'id':eventID})

def setStartDate(eventID, start):
    updateRowValsWhere("tbEvents",{'start':start},{'id':eventID})

def setSponsorshipPaid(eventID, sponsID, dateRec):
    updateRowValsWhere("tbEventSpons", {"dateRec":dateRec}, 
            {"eventID":eventID, "sponsID":sponsID})

#######################
# Create Methods
#######################
def addSponsorship(eventID, sponsID, amount, dateRec=None):
    if dateRec is None:
        dateRec = str(datetime.date.today())
    vals = {'eventID':eventID, 'sponsID':sponsID, 'amount':amount, 'dateRec':dateRec}
    insertVals("tbEventSpons", vals)

def addSponsor(name, website, email, phone, pocFirstName, pocLastName):
    vals = {'name':name, 'website':website, 'email':email, 
            'phone':phone, 'pocFirstName':pocFirstName, 'pocLastName':pocLastName}
    insertVals("tbSponsors", vals)

def createEvent(title, descr, date, start, end, location, category, entrance, logoName):
    vals = {'title':title, 'descr':descr, 'date':date, 'start':start, 'end':end, 'location':location, 'category':category, 'entrance':entrance, 'logoName':logoName}
    insertVals('tbEvents',vals)

def createUser(username, email, privledge):
    vals = {'username':username, 'email':email, 'privledge':privledge}
    insertVals("tbUsers", vals)

def createPost(body, ready, date=None):
    if date is None:
        date = str(datetime.date.today())
    vals = {'body':body, 'ready':ready, 'date':str(date)}
    insertVals("tbPosts", vals)


#######################
# Get Methods
#######################

