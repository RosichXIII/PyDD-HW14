import pytest
from matrix import Matrix

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
matrix_3 = Matrix([[12, 11, 10], [9, 8, 7], [6, 5, 4], [3, 2, 1]])
matrix_4 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

@pytest.mark.parametrize('expected_value, actual_value', [
    (matrix_1, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]),
    (matrix_4, [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), ])
def test_check_success(expected_value, actual_value):
    assert (expected_value == Matrix(actual_value))
    assert (id(expected_value) != id(Matrix(actual_value)))
    
@pytest.mark.parametrize('matrix_first, matrix_second, expected_value', [
    (matrix_2, matrix_3, Matrix([[13, 13, 13], [13, 13, 13], [13, 13, 13], [13, 13, 13]]))
])
def test_add_success(matrix_first, matrix_second, expected_value):
    assert ((temp := matrix_first + matrix_second) == expected_value)
    assert (id(temp) != id(expected_value))

@pytest.mark.parametrize('matrix_first, number, expected_value', [
    (matrix_3, 5, Matrix([[60, 55, 50], [45, 40, 35], [30, 25, 20], [15, 10, 5]]))
])
def test_mult_success(matrix_first, number, expected_value):
    assert (matrix_first * number == expected_value)

if __name__ == '__main__':
    pytest.main(['-v'])