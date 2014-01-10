import connect

tbUsers="""CREATE TABLE IF NOT EXISTS tbUsers (
    id          INT NOT NULL AUTO_INCREMENT,
    username    VARCHAR(64),
    email       VARCHAR(64),
    lastLogin   DATE,
    privledge   INT,
    PRIMARY KEY (id)
    );"""

tbPosts="""CREATE TABLE IF NOT EXISTS tbPosts (
    id      INT NOT NULL AUTO_INCREMENT,
    body    VARCHAR(256),
    date    DATE,
    private BOOL,
    PRIMARY KEY (id)
    );"""

db = connect.getDB()

db.execute(tbUsers)
db.execute(tbPosts)

db.close()
