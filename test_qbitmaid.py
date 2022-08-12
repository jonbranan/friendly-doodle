import unittest
from qprocess import torprocessor
import json
import logging
import sys
class TestQprocess(unittest.TestCase):
    def test_log_and_test_data(self):
        self.log= logging.getLogger( "SomeTest.testSomething" )
        self.tracker_list = open("./test/torrentinfo.txt", "r")
        self.log.debug(self.tracker_list)
        assert self.tracker_list
        
        # torprocessor(self)    

if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "SomeTest.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()