from peewee import *
from datetime import date

db = PostgresqlDatabase('people', user='postgres', password='', host='localhost', port='5432')

class BaseModel(Model):

    class Meta:
        database = db

class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    birthday = DateField()
    phone = int
    email = CharField()
    address = CharField()

    

# Connect to PSQL Database
db.connect()

db.drop_tables([Contact])

db.create_tables([Contact])

alex = Contact(
    first_name='Alex', 
    last_name='Garcia', 
    birthday=date(1985, 8, 20),
    phone=(5714209209),
    email='afgarcia666@gmail.com', 
    address='Herndon, Va 20171')
alex.save()

# diesel = Pet(name='Diesel', animal_type='Mutt', age=11)
# diesel.save()

# Read: (.get() and .select()) --- .get() is for single and .select() is everything
# print('Read Alex: ', Contact.get(Contact.name == 'Alex')) 

people = Contact.select()
for person in people:
    print(person.first_name)

people = Contact.select().where(Contact.birthday < date(1985, 8, 20))
for person in people:
    print(person.first_name)

# Update:
# alex = Person.get(Person.name == 'Alex')
# alex.birthday = date(1980, 8, 20)
# alex.save()

# Delete:
# alex.delete_instance()

print(f"{alex.first_name} {alex.last_name} {alex.birthday} {alex.phone} {alex.email} {alex.address}")
# from peewee import *
# from datetime import date

# db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port='6060')

# class BaseModel(Model):

#     class Meta:
#         database = db

# class Contact(BaseModel):
#     first_name = CharField()
#     last_name = CharField()
#     birthday = DateField()
#     phone = IntegerField()
#     email = CharField()
#     address = CharField()


# db.connect

# db.drop_tables(Contact)

# db.create_tables(Contact)

# alex = Contact(first_name='Alex', last_name='Garcia', birthday=date(8, 20, 1985), phone=(5714209209), email='afgarcia666@gmail.com', address='Herndon, Va 20171')
# alex.save

# contact = Contact.select()
# for person in contact:
#     print(person.first_name)