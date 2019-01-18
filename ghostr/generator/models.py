# from google.appengine.ext import ndb

# class User(ndb.Model):
#     google_id = nbd.IntegerProperty()
#     email = nbd.StringProperty()
#     first_name = ndb.StringProperty()
#     last_name = ndb.StringProperty()
#     ghost_name = ndb.StringProperty()
from random import shuffle

class Ghosts:

    names = ["Jimmy", "Paul", "Bret"]

    def random_three(self):
        shuffle(self.names)
        return self.names
