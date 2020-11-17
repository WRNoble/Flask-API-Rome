import datetime

from peewee import *

DATABASE = SqliteDatabase('emperors.sqlite')

class Emperor(Model):
    title = CharField()
    url = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Bio(Model):
    emperor = ForeignKeyField(Emperor, related_name='life')
    comment = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Emperor, Bio], safe=True)
    DATABASE.close()