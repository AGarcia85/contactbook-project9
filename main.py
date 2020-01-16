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
 

# Connect to PSQL Database
db.connect()

# db.drop_tables([Contact])

# db.create_tables([Contact])

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

# alex = Contact(
#     first_name = 'Alex', 
#     last_name = 'Garcia', 
#     birthday = date(1985, 8, 20),
#     phone = (5714209209),
#     email = 'afgarcia666@gmail.com', 
#     address = 'Herndon, Va 20171')
# alex.save()

# adam = Contact(
#     first_name = 'Adam', 
#     last_name = 'Bates',  
#     birthday = date(1985, 1, 16),
#     phone = (2026660666),
#     email = 'crazylegs@gmail.com', 
#     address = 'College Park, MD')
# adam.save()

# Read: (.get() and .select()) --- .get() is for single and .select() is everything
# print('Read Alex: ', Contact.get(Contact.name == 'Alex')) 



def create_new():
    ask = input("Would you like to add a new contact? ")
    if ask == 'yes':
        create_contact()
    else:
        print("Bye Felicia")

# people = Contact.select().where(Contact.birthday < date(1985, 8, 20))
# for person in people:
#     print(person.first_name)

# Update:
# alex = Person.get(Person.name == 'Alex')
# alex.birthday = date(1980, 8, 20)
# alex.save()

# Delete:
# alex.delete_instance()

# print(f"{alex.first_name} {alex.last_name} {alex.birthday} {alex.phone} {alex.email} {alex.address}")
create_new()