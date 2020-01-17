from peewee import *
from datetime import date

db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port='5432')

class BaseModel(Model):

    class Meta:
        database = db

class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    birthday = DateField()
    phone = CharField()
    email = CharField()
    address = CharField()
 
db.connect()
 
def welcome():
    print('Welcome my simple friend \n 1: Show Contacts \n 2: Create Contact \n 3: Update Contact \n 4: Delete Contact \n 5: Exit')
    greet = input('Enter the number of what you want to do: ')
    if greet == '1':
        show_contact()
    elif greet == '2':
        create_contact()
    elif greet == '3':
        update_contact()
    elif greet == '4':
        delete_contact()
    else:
        print('Bye Felicia')
        exit()

def show_contact():
    contacts = Contact.select()
    for contact in contacts:
        print(contact.first_name)
    show = input("Enter name for full info \nCase sensitive \nOr 'q' to go back to main menu: ")
    if show == 'q':
        welcome()
    contact = Contact.get(Contact.first_name == show)
    print(f' Full Name: {contact.first_name} {contact.last_name} \n Birthday: {contact.birthday} \n Phone Number: {contact.phone} \n Email: {contact.email} \n Address: {contact.address}')
    show_contact()

def create_contact():
    new_first_name = input('Insert First Name: ')
    new_last_name = input('Insert Last Name: ')
    new_birthday = input('Insert Birthday: ')
    new_phone = input('Insert Phone Number: ')
    new_email = input('Insert Email: ')
    new_address = input('Insert Address: ')

    add_contact = Contact(
        first_name = new_first_name,
        last_name = new_last_name,
        birthday = new_birthday,
        phone = new_phone,
        email = new_email,
        address = new_address
    )
    add_contact.save()
    welcome()

def update_contact():
    contacts = Contact.select()
    for contact in contacts:
        print(contact.first_name)
    ask1 = input('Enter name of contact to update \nCase Sensitive: ')
    if ask1 == Contact.first_name:
        print(' 1: First name \n 2: Last name \n 3: Birthday \n 4: Phone number \n 5: Email \n 6: Address')
        ask2 = input('Enter number of subject to update: ')
        if ask2 == '1':
            contact = Contact.get(Contact.first_name == ask1)
            contact.first_name = input('New first name: ')
            contact.save()
            welcome()
        elif ask2 == '2':
            contact = Contact.get(Contact.first_name == ask1)
            contact.last_name = input('New last name: ')
            contact.save()
            welcome()
        elif ask2 == '3':
            contact = Contact.get(Contact.first_name == ask1)
            contact.birthday = input('New birthday: ')
            contact.save()
            welcome()
        elif ask2 == '4':
            contact = Contact.get(Contact.first_name == ask1)
            contact.phone = input('New phone number: ')
            contact.save()
            welcome()
        elif ask2 == '5':
            contact = Contact.get(Contact.first_name == ask1)
            contact.email = input('New email: ')
            contact.save()
            welcome()
        elif ask2 == '6':
            contact = Contact.get(Contact.first_name == ask1)
            contact.address = input('New address: ')
            contact.save()
            welcome()
        else:
            welcome()

def delete_contact():
    contacts = Contact.select()
    for contact in contacts:
        print(contact.first_name)
    bye = input('Pick a name to get rid off: ')
    if bye == Contact.first_name:
        sure = input('Are you sure you want to delete this Dirtbag? y/n: ')
        if sure == 'y':
            contact = Contact.get(Contact.first_name == bye)
            contact.delete_instance()
            welcome()
        else:
            delete_contact()
    else:
        welcome()

welcome()