from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

# Both the Bats and Rants bolts will fire, this shows that the hashmap bolt before was able to dictate
# which bolt it would emit to.

class Cats(Bolt):

    def process(self, tup):
        _id = tup.stream
        demon = tup.values[0]
        self.log("eggs")
        self.log('»»»ID: %s' % (_id))

class Bats(Bolt):

    def process(self, tup):
        _id = tup.stream
        demon = tup.values[0]
        self.log("cabbage")
        self.log('»»»ID: %s' % (_id))

class Rats(Bolt):

    def process(self, tup):
        _id = tup.stream
        demon = tup.values[0]
        self.log("spinach")
        self.log('»»»ID: %s' % (_id))

