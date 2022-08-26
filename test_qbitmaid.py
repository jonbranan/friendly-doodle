import unittest
from qlist import ispreme,iscatignored,istrackerblank,isprotectedtracker

class TestQbitmaid(unittest.TestCase):
    def test_ispreme_sanity(self):
        self.assertTrue(ispreme(1,1,1))
        self.assertFalse(ispreme(1,1,3))
    
    def test_ispreme(self):
        pass

    def test_iscatignored_sanity(self):
        self.assertTrue(iscatignored('a', ['a','b','c']))
        self.assertTrue(iscatignored('b', ['a','b','c']))
        self.assertTrue(iscatignored('c', ['a','b','c']))
        self.assertFalse(iscatignored('d', ['a','b','c']))
        self.assertFalse(iscatignored(1, ['a','b','c']))
        self.assertFalse(iscatignored(1.0000000, ['a','b','c']))

    def test_iscatignored(self):
        pass

    def test_istrackerblank_sanity(self):
        self.assertTrue(istrackerblank(''))
        self.assertFalse(istrackerblank('a'))
        self.assertFalse(istrackerblank(1))
        self.assertFalse(istrackerblank(1.00000000))

    def test_istrackerblank(self):
        pass

    def test_isprotectedtracker_sanity(self):
        self.assertTrue(isprotectedtracker('https://a.com/',['a.com','b.me','c.io']))
        self.assertFalse(isprotectedtracker('https://google.com/',['a.com','b.me','c.io']))
        self.assertFalse(isprotectedtracker('https://d.com',['a.com','b.me','c.io']))

    def test_isprotectedtracker(self):
        pass

    def test_isnotprotectedtracker_sanity(self):
        pass

    def test_isnotprotectedtracker(self):
        pass

    def test_istagblank(self):
        pass

    def test_(self):
        pass
    
    def test_(self):
        pass
        
if __name__ == '__main__':
    unittest.main()