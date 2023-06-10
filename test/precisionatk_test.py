import decimal
import os
import sys

# add your project directory to the sys.path
project_home = os.getcwd()
if project_home not in sys.path:
    sys.path.insert(0, project_home)
os.chdir(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'prs_project.settings'
from evaluator.algorithm_evaluator import PrecisionAtK

import unittest

class TestPrecisionAtK(unittest.TestCase):

    def test_recall_at_k_no_actual(self):
        pak = PrecisionAtK(5, None)
        recs = [(1, ''),
                (2, ''),
                (3, '')]
        actual = []
        result = pak.recall_at_k(recs, actual)
        self.assertEqual(result, 0)

    def test_recall_at_k_perfect(self):
        pak = PrecisionAtK(5, None)
        recs = [(1, ''),
                (2, ''),
                (3, '')]
        actual = [1,2,3]
        result = pak.recall_at_k(recs, actual)
        self.assertEqual(result, 1)

    def test_recall_at_k_good_top(self):
        pak = PrecisionAtK(5, None)
        recs = [(1, ''),
                (2, ''),
                (3, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (4, '')]
        actual = [1,2,3]
        result = pak.recall_at_k(recs, actual)
        self.assertEqual(result, 1)

    def test_recall_at_k_good_bottom(self):
        pak = PrecisionAtK(5, None)
        recs = [(4, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (4, ''),
                (1, ''),
                (2, ''),
                (3, '')]
        actual = [1,2,3]
        result = pak.recall_at_k(recs, actual)
        self.assertEqual(result, 1)

    def test_precision_at_k_perfect(self):
        pak = PrecisionAtK(5, None)
        recs = [(1, ''),
                (2, ''),
                (3, '')]
        actual = [1, 2, 3]
        result = pak.average_precision_k(recs, actual)
        self.assertEqual(result, 1)

    def test_precision_at_k_worst(self):
        pak = PrecisionAtK(5, None)
        recs = [(1, ''),
                (2, ''),
                (3, '')]
        actual = []
        result = pak.average_precision_k(recs, actual)
        self.assertEqual(result, 0)

    def test_precision_at_k_worst2(self):
        pak = PrecisionAtK(5, None)
        recs = [(1, ''),
                (2, ''),
                (3, '')]
        actual = [4,5,6,7]
        result = pak.average_precision_k(recs, actual)
        self.assertEqual(result, 0)

    def test_precision_at_k_not_so_good(self):
        pak = PrecisionAtK(5, None)
        recs = [(1, ''),
                (2, ''),
                (3, '')]
        actual = [1, 5, 6, 7]

        result = pak.average_precision_k(recs, actual)
        self.assertAlmostEqual(result, decimal.Decimal(11/18))

if __name__ == '__main__':
    unittest.main()