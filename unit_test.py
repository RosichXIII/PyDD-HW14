import unittest
from matrix import Matrix

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
matrix_3 = Matrix([[12, 11, 10], [9, 8, 7], [6, 5, 4], [3, 2, 1]])
matrix_4 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

class TestMatrix(unittest.TestCase):
        
    def test_equal_success(self):        
        self.assertEqual(matrix_1, matrix_2)
        self.assertNotEqual(matrix_1, matrix_4)
        
    def test_not_equal_success(self):
        self.assertFalse(matrix_1 != matrix_2)
        self.assertTrue(matrix_1 != matrix_4)
        
    def test_add_success(self):
        self.assertTrue(matrix_1 + matrix_3 == Matrix([[13, 13, 13], [13, 13, 13], [13, 13, 13], [13, 13, 13]]))

    def test_matrix_mult_success(self):
        self.assertTrue(matrix_4 * 5 == Matrix([[5, 10, 15, 20], [25, 30, 35, 40], [45, 50, 55, 60]]))

if __name__ == '__main__':
     unittest.main(verbosity=2)