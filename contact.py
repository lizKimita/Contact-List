import pyperclip

class Contact:
    '''
    Class that generates new instances of contacts
    '''
    contact_list = [] #empty array for the contact list, accessible by all instances of the class.It will store the created contact objects.
    def __init__(self, first_name, last_name, phone_number, email):

        '''
        _init_ method that help us define properties for our objects.

        Args:
        first_name: New contact first name.
        last_name: New contact last name.
        number: New contact phone number.
        email: New contact email address
        '''
        
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_contact(self):

        '''
        save contact method saves contact objects into contact_list
        '''
        Contact.contact_list.append(self)

    def delete_contact(self):
        '''
        delete contact method deletes a saved contact from the list
        '''
        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number
        Args:
            number: Phone number to search for

        Returns:
            Contact of the person the number matches.

        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact

    @classmethod
    def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list

        Args:
            number: Phone number to search if it exists

        Returns:
            Boolean: True or false depending on if the contact exists
        '''

        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True

        return False
        
    @classmethod
    def display_contacts(cls):
        '''
        Method that returns the contact list
        '''
        return cls.contact_list

    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)

