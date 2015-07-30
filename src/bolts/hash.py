from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

class HashTable(Bolt):

    def process(self, tup):
        hmap = {0: "b", 1: "b", 2: "r"} # Since both 0 and 1 map to "b" (instead of 0 mapping to "c") this shows the implementation works
        idx = tup.values[0]
        stream = tup.stream
        demon = hmap[idx]
        self.log("stream: %s" % stream)
        self.emit([demon], stream=demon) #the tuple [demon] doesn't really matter, the stream=demon chooses which bolt to emit to


