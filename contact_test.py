import pyperclip
import unittest #importing the unittest module
from contact import Contact #importing the contact class


class TestContact(unittest.TestCase):
    
    def setUp(self):
        self.new_contact = Contact('Shiko', 'Kimita', '0780047102', 'kimita.wanjiku@gmail.com')# creating the contact object

    def test_init(self):
        self.assertEqual(self.new_contact.first_name, 'Shiko')
        self.assertEqual(self.new_contact.last_name, 'Kimita')
        self.assertEqual(self.new_contact.phone_number,'0780047102')
        self.assertEqual(self.new_contact.email,'kimita.wanjiku@gmail.com')

    def tearDown(self):
        '''
        tearDown method that does cleanup after each test case has run
        '''
        Contact.contact_list = []

    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into the contact list
        '''
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact objects to our contact_list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test", "user", "0721216565", "test@user.com")
            test_contact.save_contact()
            self.assertEqual(len(Contact.contact_list),2)

    def test_delete_test(self):
            '''
            test_delete_test to test if we can remove a contact from our contact list
            '''
            self.new_contact.save_contact()
            test_contact = Contact("Test", "user", "0734499942", "kev@gmail.com")
            test_contact.save_contact()

            self.new_contact.delete_contact()
            self.assertEqual(len(Contact.contact_list),1)

    def test_find_contact_by_number(self):
            '''
            test_find_contact_by_number tests to check if we can find a contact by number and display the information
            '''

            self.new_contact.save_contact()
            test_contact = Contact("Kijo", "Kimita", "0720327460", "kijo@gmail.com")
            test_contact.save_contact()

            found_contact = Contact.find_by_number("0720327460")
            self.assertEqual(found_contact.email, test_contact.email)

    def test_contact_exists(self):
        '''
        test to check if we can return a boolean if we cannot find a contact.
        '''

        self.new_contact.save_contact()
        test_contact = Contact ("Kare", "Kimita","0780047102","shiko@gmail.com")
        test_contact.save_contact()

        contact_exists = Contact.contact_exist("0780047102")
        self.assertTrue(contact_exists)

    def test_display_all_contacts(self):
        '''
        method taht returns a list of all the contacts saved
        '''

        self.assertEqual(Contact.display_contacts(), Contact.contact_list)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_contact.save_contact()
        Contact.copy_email("0780047102")

        self.assertEqual(self.new_contact.email, pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
        
