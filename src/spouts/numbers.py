from __future__ import absolute_import, print_function, unicode_literals

import itertools
from streamparse.spout import Spout

class NumberSpout(Spout):

    def initialize(self, stormconf, context):
        self.numbers = itertools.cycle([0, 1, 2])

    def next_tuple(self):
        number = next(self.numbers)
        self.emit([number])
