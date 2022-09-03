import unittest
from qlist import ispreme,iscatignored,istrackerblank,isprotectedtracker,isnotprotectedtracker,istagblank,isignoredtag
from qprocess import isdownloading,isprotectedunderratio,isoldtor,isprotectedoverratio,isnonprotectedtor

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
        self.assertFalse(isnotprotectedtracker('https://a.com/',['a.com','b.me','c.io']))
        self.assertTrue(isnotprotectedtracker('https://google.com/',['a.com','b.me','c.io']))
        self.assertTrue(isnotprotectedtracker('https://d.com',['a.com','b.me','c.io']))

    def test_isnotprotectedtracker(self):
        pass

    def test_istagblank(self):
        self.assertTrue(istagblank(''))
        self.assertFalse(istagblank('a'))
        self.assertFalse(istagblank(1))
        self.assertFalse(istagblank(1.0001))
        self.assertFalse(istagblank(False))
        self.assertFalse(istagblank(True))

    def test_isdownloading_sanity(self):
        self.assertTrue(isdownloading('downloading'))
    
    def test_isdownloading(self):
        self.assertFalse(isdownloading('DOWNLOADING'))
        self.assertFalse(isdownloading('dOwNlOaDiNg'))

    def test_isprotectedunderratio_sanity(self):
        self.assertTrue(isprotectedunderratio(0.5,1,'a','a,b,c'))

    def test_isprotectedunderratio(self):
        pass

    def test_isoldtor_sanity(self):
        self.assertTrue(isoldtor(1,2,4))

    def test_isoldtor(self):
        self.assertFalse(isoldtor(1661150664,2419200,1662049004.2101078))
        self.assertFalse(isoldtor(1661150664,2419200,1662049004))
        self.assertFalse(isoldtor(1661150664.000000,2419200.0000000,1662049004.2101078))

    def test_isprotectedoverratio_sanity(self):
        self.assertTrue(isprotectedoverratio(2,1,'a','a,b,c'))

    def test_isprotectedoverratio(self):
        pass

    def test_isnonprotectedtor_sanity(self):
        self.assertTrue(isnonprotectedtor('a','a,b,c'))

    def test_isnonprotectedtor(self):
        pass

    def test_isignoredtag_sanity(self):
        self.assertTrue(isignoredtag(['a','b','c'], 'first,second,third,a'))
    
    def test_isignoredtag_sanity(self):
        self.assertTrue(isignoredtag(['a','b','c'], 'first,second,third,a'))

    # def test__sanity(self):
    #     pass

    # def test_(self):
    #     pass
        
if __name__ == '__main__':
    unittest.main()