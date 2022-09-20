from qprocess import dragnet
import csv
import unittest

class TestDragnet(unittest.TestCase):
    def test_dragnet_sanity(self):
        self.cv = csv
        outfile = './test_outfile.csv'
        state = 'downloading'
        ratio = 1.05
        tags = 'ipt'
        added = 1
        age = 240000
        time = 123456
        thash = 'asfasdf23412adfqwer'
        tname = 'thisismynamehahahah'
        dragnet(self.cv,outfile,state,ratio,tags,added,age,time,thash,tname)

if __name__ == '__main__':
    unittest.main()