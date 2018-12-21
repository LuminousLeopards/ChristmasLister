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


class TestListItem(unittest.TestCase):

    def test_additem(self):
        socks = main.ListItem(5, 'Socks')
        self.assertEqual(socks.itemname, "Socks")

    def test_additem_blank(self):
        with self.assertRaises(Exception) as context:
            main.ListItem(5, '')
        self.assertTrue('No item name entered.' in str(context.exception))


class TestGiftUpdates(unittest.TestCase):

    def test_setbought(self):
        abe = main.ListUser('Abe', 'Lincoln')
        pipe = main.ListItem(abe.userid, 'corncob pipe')
        with dbsetup.connect:
            c = dbsetup.connect.cursor()
        bought = c.execute("SELECT bought FROM gifts WHERE rowid = (:rowid)", {'rowid': pipe.itemid}).fetchone()
        bought = bought[0]
        self.assertEqual(bought, 0)
        pipe.setbought(pipe.itemid)
        bought = c.execute("SELECT bought FROM gifts WHERE rowid = (:rowid)", {'rowid': pipe.itemid}).fetchone()
        bought = bought[0]
        self.assertEqual(bought, 1)
        deleted = c.execute("SELECT deleted FROM gifts WHERE rowid = (:rowid)", {'rowid': pipe.itemid}).fetchone()
        deleted = deleted[0]
        self.assertEqual(deleted, 0)
        pipe.setdeleted(pipe.itemid)
        deleted = c.execute("SELECT deleted FROM gifts WHERE rowid = (:rowid)", {'rowid': pipe.itemid}).fetchone()
        deleted = deleted[0]
        self.assertEqual(deleted, 1)


if __name__ == '__main__':
    unittest.main()
