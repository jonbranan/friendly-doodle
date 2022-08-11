import unittest
from qprocess import torprocessor
from json import loads
class TestQprocess(unittest.TestCase):
    def test_protected_ratio_below(self):
        self.ti = open("./test/torrentinfo.txt")
        self.tracker_list = loads(self.ti)
        torprocessor(self)
            

if __name__ == '__main__':
    unittest.main()