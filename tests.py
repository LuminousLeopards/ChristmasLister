import main,dbsetup

brian = main.listuser('Brian', 'Peterson')
#main.adduser(brian.firstname,brian.lastname)
print(dir(brian))
print(type(brian))

print("User name: ", brian.firstame, brian.lastname)
print(main.listuser.getuserid('Brian'))
print(dbsetup.returntables())

