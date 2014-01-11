import connect
tables = {
        'tbUsers': [
        {'username':'Mike','email':'a@a','privledge':'1'}, 
        {'username':'Taylor','email':'a@a','privledge':'1'}, 
        {'username':'Joe','email':'a@a','privledge':'0'}, 
        {'username':'Candice','email':'a@a','privledge':'0'}, 
        ],

        'tbPosts': [
        {'body':'Welcome to the ACM webpage!','private':True},
        {'body':'This is the second post','private':True},
        {'body':'A pending post','private':False},
        ],

        'tbEvents': [
        {'title':'TechHacks', 'descr':'A hackathon on Michigan Tech\'s acmpus', 
            'start':'2014-02-13 06:30:00', 'end':'2014-02-14 12:30:00',
            'location':'Michigan Tech Fisher and Rehki', 'category':1,
            'entrance':0, 'logoName':'th.jpg'},
        {'title':'MHacks', 'descr':'A hackathon on the University of Michigan', 
            'start':'2014-01-15 06:30:00', 'end':'2014-01-16 12:30:00',
            'location':'Detroit: The Qube', 'category':1,
            'entrance':0, 'logoName':'mh.jpg'},
        {'title':'Virtual Career Fair', 'descr':'A career fair with West Coast companies over Skype', 
            'start':'2014-02-01 18:30:00', 'end':'2014-02-01 20:30:00',
            'location':'Michigan Tech Ball Room', 'category':0,
            'entrance':0, 'logoName':'vcf.jpg'}
        ]
}

db = connect.getDB()

for tbName, tbRows in tables.iteritems(): 
    cnt = "SELECT id FROM " + tbName
    db.execute(cnt)
    if len(db.fetchall()) > 0:
        continue

    for row in tbRows:
        ins= "INSERT INTO " + tbName + " (" 
        for colName in row.keys():
            ins += colName + ","

        ins = ins[:-1] + ") VALUES ("
        for x in range(0, len(row)):
            ins += "%s,"

        ins = ins[:-1] + ");"
        print ins
        
        db.execute(ins, row.values()) 
           
connect.commit()
connect.close()
