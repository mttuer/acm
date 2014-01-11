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

tbEvents="""CREATE TABLE IF NOT EXISTS tbEvents (
    id          INT NOT NULL AUTO_INCREMENT,
    title       VARCHAR(64),
    descr       VARCHAR(256),
    date        DATE,
    start       DATETIME,
    end         DATETIME,
    location    VARCHAR(128),
    category    INT,
    entrance    INT,
    logoName    VARCHAR(64),
    PRIMARY KEY (id)
    );"""

tbSponsors = """CREATE TABLE IF NOT EXISTS tbSponsors (
    id              INT NOT NULL AUTO_INCREMENT,
    name            VARCHAR(64),
    website         VARCHAR(128),
    email           VARCHAR(64),
    phone           VARCHAR(10),
    pocFirstName    VARCHAR(64),
    pocLastName     VARCHAR(64),
    PRIMARY KEY (id)
    );"""
 
tbEventSpons= """CREATE TABLE IF NOT EXISTS tbEventSpons(
    id          INT NOT NULL AUTO_INCREMENT,
    eventID     INT,
    eventNum    INT,
    dateRec     DATE,
    amount      DECIMAL(8,2),
    FOREIGN KEY (eventID) REFERENCES tbSponsors(id),
    PRIMARY KEY (id)
    );"""

db = connect.getDB()

db.execute(tbUsers)
db.execute(tbPosts)
db.execute(tbEvents)
db.execute(tbSponsors)
db.execute(tbEventSpons)

db.close()
