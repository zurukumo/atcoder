import unittest

from libs import bisect_find


class TestBisectFind(unittest.TestCase):
    def test_find(self):
        target = [1, 3]
        self.assertEqual(bisect_find.find_lt(target, 0), None)
        self.assertEqual(bisect_find.find_le(target, 0), None)
        self.assertEqual(bisect_find.find_gt(target, 0), 1)
        self.assertEqual(bisect_find.find_ge(target, 0), 1)
        self.assertEqual(bisect_find.find_lt(target, 1), None)
        self.assertEqual(bisect_find.find_le(target, 1), 1)
        self.assertEqual(bisect_find.find_gt(target, 1), 3)
        self.assertEqual(bisect_find.find_ge(target, 1), 1)
        self.assertEqual(bisect_find.find_lt(target, 2), 1)
        self.assertEqual(bisect_find.find_le(target, 2), 1)
        self.assertEqual(bisect_find.find_gt(target, 2), 3)
        self.assertEqual(bisect_find.find_ge(target, 2), 3)
        self.assertEqual(bisect_find.find_lt(target, 3), 1)
        self.assertEqual(bisect_find.find_le(target, 3), 3)
        self.assertEqual(bisect_find.find_gt(target, 3), None)
        self.assertEqual(bisect_find.find_ge(target, 3), 3)
        self.assertEqual(bisect_find.find_lt(target, 4), 3)
        self.assertEqual(bisect_find.find_le(target, 4), 3)
        self.assertEqual(bisect_find.find_gt(target, 4), None)
        self.assertEqual(bisect_find.find_ge(target, 4), None)
