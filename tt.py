import sys
import datetime
from peewee import *

db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'activities.db')
db = SqliteDatabase(db_path)

class Activity(Model):
    name = TextField()
    time_spent = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def start(*args):
    Activity.create(args)

def do_action(action, values):
    action()


def main():
    args = sys.argv
    if len(sys.argv) == 3:
        name = sys.argv[1]
        action = sys.argv[2]
        do_action(action)
