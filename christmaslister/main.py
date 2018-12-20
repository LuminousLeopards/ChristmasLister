import dbsetup


class ListUser:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.userid = dbsetup.adduser(firstname, lastname)
        if not (isinstance(firstname, str) and isinstance(lastname, str)):
            print('Please enter a sequence of letters.')
            raise Exception('Invalid data type')
        if not (firstname and lastname):
            print('Please enter a valid first and last name.')
            raise Exception('Empty string!')

    def addlistitem(self, userid, itemname):
        ListItem(userid, itemname)

class ListItem:
    def __init__(self, userid, itemname):
        self.userid = userid
        self.itemname = itemname
        self.itemid = dbsetup.additem(userid, itemname)
        if not self.itemname:
            print('Please enter a link or the name of an item.')
            raise Exception('No item name entered.')