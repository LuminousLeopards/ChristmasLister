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

    def addlistitem(userid, itemname):
        ListItem(userid, itemname)


class ListItem:
    def __init__(self, userid, itemname):
        self.userid = userid
        self.itemname = itemname
        if not self.itemname:
            print('Please enter a link or the name of an item.')
            raise Exception('No item name entered.')
        if not self.userid:
            print('No userid associated with the item (how did this happen?)')
            raise Exception('No userid associated.')
        self.itemid = dbsetup.additem(userid, itemname)

    def setbought(self, itemid):
        dbsetup.buyitem(itemid)

    def setdeleted(self, itemid):
        dbsetup.deleteitem(itemid)
