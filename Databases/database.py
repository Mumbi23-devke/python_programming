from peewee import *
from os import path

# creating our first

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Mumbi's database.db"))


# creating table inside db

class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)


class Student(Model):
    name = CharField()
    number = IntegerField()
    age = IntegerField()
    code = IntegerField()
    gender = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)
