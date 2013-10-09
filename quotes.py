QUOTES = [
    ("Gerber", "If all you want from a business is the opportunity to do what you did before you started your business, get paid more for it and have more freedom, your self indulgence will eventually consume both you and the business."),
    ("Gerber", "What you do with your model is not nearly as important as doing it the same way, every time."),
    ("Gerber", "Creativity thinks up new things, Innovation does new things."),
    ("Gerber", "The difference between a warrior and an ordinary man is that the warrior sees everything as a challenge, while the ordinary man sees everything as a blessing or a curse."),
    ("Ackoff", "A problem never exists in isolation; it is surrounded by other problems in space and time. The more of the context of a problem that a scientist can comprehend, the greater are his chances of finding a truly adequate solution."),
]

import os
from peewee import *


db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'inspirator.db')
db = SqliteDatabase(db_path)

class Quote(Model):
    text = TextField()
    author = CharField()

    class Meta:
        database = db


def main():
    Quote.create_table(fail_silently=True)
    for author, text in QUOTES:
        Quote.create(author=author, text=text)


if __name__ == '__main__':
    main()