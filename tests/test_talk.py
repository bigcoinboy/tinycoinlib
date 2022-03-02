
import unittest

from tinycoinlib.talk import TinyCoinTalk


class Test(unittest.TestCase):

    def setUp(self):
        self.talk = TinyCoinTalk('litecoin')


    def test_call(self):

        self.talk.call('getblock')

