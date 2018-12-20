import main,dbsetup,unittest

# Value and type testing for ListUser class
class TestListUser(unittest.TestCase):

    def test_adduser(self):
        testuser3 = main.ListUser('Joe', 'Smith')
        self.assertEqual(testuser3.firstname, 'Joe')
        self.assertEqual(testuser3.lastname, 'Smith')
        self.assertTrue(testuser3.userid)

    def test_adduser_empty(self):
        with self.assertRaises(Exception) as context:
            main.ListUser('', 'Smith')
        self.assertTrue('Empty string!' in str(context.exception))

    def test_adduser_int(self):
        with self.assertRaises(Exception) as context:
            main.ListUser('Joe', 5)
        self.assertTrue('Invalid data type' in str(context.exception))


    # def test_dbinsert(self):
    #     with dbsetup.connect:
    #         c = dbsetup.connect.cursor()
    #     for row in c.execute('SELECT * from users'):
    #         print(row)


class TestListItem(unittest.TestCase):

    def test_additem(self):
        socks = main.ListItem(5, 'Socks')
        self.assertEqual(socks.itemname, "Socks")

    def test_additem_blank(self):
        with self.assertRaises(Exception) as context:
            main.ListItem(5, '')
        self.assertTrue('No item name entered.' in str(context.exception))


usr = main.ListUser('Guy', 'Fieri')
print(usr.userid, usr.firstname, usr.lastname)
usr.addlistitem(usr.userid, "Sorkc")

if __name__ == '__main__':
    unittest.main()