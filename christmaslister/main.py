import dbsetup

class listuser():

    def __init__(self,firstname,lastname):
        self.firstame = firstname,
        self.lastname = lastname

    def adduser(firstname,lastname):
        dbsetup.adduser(firstname,lastname)
    
    def getuser(firstname):
        dbsetup.getuserid(firstname)

#class listitem():
#    def __init__(self,userid,itemname)
#    self.userid = userid
#    self.itemname = itemname

    #def addlistitem(userid,itemname):


brian = listuser('Brian', 'Peterson')

listuser.adduser('brian','peterson')

print(brian.firstame)
print(listuser.getuser('Brian'))