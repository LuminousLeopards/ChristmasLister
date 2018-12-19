import dbsetup


class ListUser:

    def __init__(self, firstname, lastname):
        self.firstame = firstname
        self.lastname = lastname

    @staticmethod
    def adduser(self, firstname, lastname):
        self.userid = dbsetup.adduser(firstname, lastname)


class ListItem:
    def __init__(self, userid, itemname):
        self.userid = userid
        self.itemname = itemname

    @staticmethod
    def addlistitem(self, userid, itemname):
        dbsetup.additem(userid, itemname)
