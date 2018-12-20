import dbsetup


class ListUser:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        if not (isinstance(firstname, str) and isinstance(lastname, str)):
            print('Please enter a sequence of letters.')
            raise Exception('Invalid data type')
        if not (firstname and lastname):
            print('Please enter a valid first and last name.')
            raise Exception('Empty string!')
        self.userid = dbsetup.adduser(firstname, lastname)


class ListItem:
    def __init__(self, userid, itemname):
        self.userid = userid
        self.itemname = itemname

    @staticmethod
    def addlistitem(self, userid, itemname):
        dbsetup.additem(userid, itemname)
