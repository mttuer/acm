import connect
users = [
        {'name':'Mike','email':'a@a','priv':'1'}, 
        {'name':'Taylor','email':'a@a','priv':'1'}, 
        {'name':'Joe','email':'a@a','priv':'0'}, 
        {'name':'Candice','email':'a@a','priv':'0'}, 
        ]
posts = [
        {'body':'Welcome to the ACM webpage!','ready':'true'},
        {'body':'This is the second post','ready':'true'},
        {'body':'A pending post','ready':'false'},
        ]

db = connect.getDB()

for user in users:
    db.execute("SELECT id FROM tbUsers WHERE username = '" + user['name'] + "'")
    if len(db.fetchall()) > 0:
        print 'User ' + user["name"] + ' is already a user.'
    else:
        print 'Inserting user ' + user['name']
        db.execute("INSERT INTO tbUsers (username,email,lastLogin,privledge) VALUES ('" + user["name"] + "','" + user["email"] + "', CURDATE()," + user["priv"] + ")")
       
for post in posts:
    print "Inserting post: " + post["body"]
    db.execute("INSERT INTO tbPosts (body,date,private) VALUES ('" + post["body"] + "',CURDATE()," + post["ready"] + ")")
    
connect.commit()
connect.close()
