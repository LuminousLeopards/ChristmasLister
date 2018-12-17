import main,dbsetup


# def returntables():
#     with dbsetup.connect:
#         c = dbsetup.connect.cursor()
#         for row in c.execute('SELECT rowid from users'):
#             print(row)


brian = main.ListUser('Brian', 'Peterson')
main.ListUser.adduser(brian, brian.firstame, brian.lastname)
# print(dir(brian))
# print(type(brian))
print("User name: ", brian.firstame, brian.lastname, ". Userid: ", brian.userid)

noella = main.ListUser('Noella', 'Peterson')
main.ListUser.adduser(noella, noella.firstame, noella.lastname)

print("User name: ", noella.firstame, noella.lastname, ". Userid: ", noella.userid)

#####To do : figure out workflow of how userid is associated with the list item
#candles = main.ListItem()