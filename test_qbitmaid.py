import unittest
from qlist import is_preme,is_cat_ignored,is_tracker_blank,is_protected_tracker,is_not_protected_tracker,is_tag_blank,is_ignored_tag
from qprocess import is_downloading,is_protected_under_ratio,is_old_tor,is_protected_over_ratio,is_not_protected_tor

class TestQbitmaid(unittest.TestCase):
    def test_ispreme_sanity(self):
        self.assertTrue(is_preme(1,1))
        self.assertTrue(is_preme(1,2))
        self.assertFalse(is_preme(2,1))
    
    def test_ispreme(self):
        pass

    def test_iscatignored_sanity(self):
        self.assertTrue(is_cat_ignored('a', ['a','b','c']))
        self.assertTrue(is_cat_ignored('b', ['a','b','c']))
        self.assertTrue(is_cat_ignored('c', ['a','b','c']))
        self.assertFalse(is_cat_ignored('d', ['a','b','c']))
        self.assertFalse(is_cat_ignored(1, ['a','b','d']))
        self.assertFalse(is_cat_ignored(1.0000000, ['a','b','c']))

    def test_iscatignored(self):
        pass

    def test_istrackerblank_sanity(self):
        self.assertTrue(is_tracker_blank(''))
        self.assertFalse(is_tracker_blank('a'))
        self.assertFalse(is_tracker_blank(1))
        self.assertFalse(is_tracker_blank(1.00000000))

    def test_istrackerblank(self):
        pass

    def test_isprotectedtracker_sanity(self):
        self.assertTrue(is_protected_tracker('https://a.com/',['a.com','b.me','c.io']))
        self.assertFalse(is_protected_tracker('https://google.com/',['a.com','b.me','c.io']))
        self.assertFalse(is_protected_tracker('https://d.com',['a.com','b.me','c.io']))

    def test_isprotectedtracker(self):
        pass

    def test_isnotprotectedtracker_sanity(self):
        self.assertFalse(is_not_protected_tracker('https://a.com/',['a.com','b.me','c.io']))
        self.assertTrue(is_not_protected_tracker('https://google.com/',['a.com','b.me','c.io']))
        self.assertTrue(is_not_protected_tracker('https://d.com',['a.com','b.me','c.io']))

    def test_isnotprotectedtracker(self):
        pass

    def test_istagblank(self):
        self.assertTrue(is_tag_blank(''))
        self.assertFalse(is_tag_blank('a'))
        self.assertFalse(is_tag_blank(1))
        self.assertFalse(is_tag_blank(1.0001))
        self.assertFalse(is_tag_blank(False))
        self.assertFalse(is_tag_blank(True))

    def test_isdownloading_sanity(self):
        self.assertTrue(is_downloading('downloading'))
    
    def test_isdownloading(self):
        self.assertFalse(is_downloading('DOWNLOADING'))
        self.assertFalse(is_downloading('dOwNlOaDiNg'))

    def test_isprotectedunderratio_sanity(self):
        self.assertTrue(is_protected_under_ratio(0.5,1,'a','a,b,c'))

    def test_isprotectedunderratio(self):
        pass

    def test_isoldtor_sanity(self):
        self.assertFalse(is_old_tor(1,2))

    def test_isoldtor(self):
        self.assertTrue(is_old_tor(1,1))
        self.assertTrue(is_old_tor(2,1))
        self.assertFalse(is_old_tor(1,2))

    def test_isprotectedoverratio_sanity(self):
        self.assertTrue(is_protected_over_ratio(2,1,'a','a,b,c'))

    def test_isprotectedoverratio(self):
        pass

    def test_isnonprotectedtor_sanity(self):
        self.assertTrue(is_not_protected_tor('a','a,b,c'))

    def test_isnonprotectedtor(self):
        pass

    def test_isignoredtag_sanity(self):
        self.assertTrue(is_ignored_tag(['a','b','c'], 'first,second,third,a'))
    
    def test_isignoredtag(self):
        self.assertTrue(is_ignored_tag(['save'], 'save,public,ipt'))

    # def test__sanity(self):
    #     pass

    # def test_(self):
    #     pass
        
if __name__ == '__main__':
    unittest.main()