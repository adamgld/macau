import unittest
import macau
import scipy.sparse

class TestBPMF(unittest.TestCase):
    def test_one(self):
        self.assertTrue( macau.test() > 0 )
    def test_bpmf(self):
        X = scipy.sparse.rand(15, 10, 0.2)
        macau.bpmf(rows = X.row, cols = X.col, values = X.data, num_latent = 10)

if __name__ == '__main__':
    unittest.main()
