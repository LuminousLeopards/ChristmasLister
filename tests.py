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



if __name__ == '__main__':
    unittest.main()