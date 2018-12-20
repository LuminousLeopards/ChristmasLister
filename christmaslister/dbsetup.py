import sqlite3

connect = sqlite3.connect('listdb.db')

c = connect.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS gifts (
            userid integer,
            itemname text,
            bought integer,
            deleted integer
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS users (
        firstname text,
        lastname text
        )
    """)


def adduser(firstname, lastname):
    with connect:
        c.execute("INSERT INTO users VALUES (:firstname, :lastname)", {'firstname': firstname, 'lastname': lastname})
        connect.commit()
        return c.lastrowid


def additem(userid, itemname):
    with connect:
        c.execute("INSERT INTO gifts VALUES (:userid, :itemname, :bought, :deleted)", {'userid': userid, 'itemname': itemname, 'bought': 0, 'deleted': 0})
        connect.commit()
        return c.lastrowid


def buyitem(itemid):
    with connect:
        c.execute("UPDATE gifts SET bought = 1 WHERE gifts.itemid = (:itemid)", {'itemid': itemid})


def deleteitem(itemid):
    with connect:
        c.execute("UPDATE gifts SET deleted = 1 WHERE gifts.itemid = (:itemid)", {'itemid': itemid})


#connect.close()
