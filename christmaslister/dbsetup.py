import sqlite3

connect = sqlite3.connect(':memory:')

c = connect.cursor()

c.execute("""CREATE TABLE gifts (
            giftid integer PRIMARY KEY,
            userid integer,
            itemname text,
            bought integer,
            deleted integer
            )""")

c.execute("""CREATE TABLE users (
        userid integer primary key,
        firstname text,
        lastname text
        )
    """)

def adduser(firstname,lastname):
    with connect:
        c.execute("INSERT INTO users VALUES (:userid, :firstname, :lastname)", {'userid':rowid,'firstname':firstname,'lastname':lastname})

def getuserid(firstname):
    with connect:
        c.execute("SELECT userid FROM users where firstname=?", (firstname,))
        return c.fetchall()

def additem(userid,itemname):
    with connect:
        c.execute("INSERT INTO gifts VALUES (:userid, :itemname, :bought)", {'userid':userid,'itemname':itemname,'bought':0})

def buyitem(itemid):
    with connect:
        c.execute("UPDATE gifts SET bought = 1 WHERE gifts.itemid = itemid")

connect.commit()
#connect.close()