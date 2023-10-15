import unittest

from raytracer.matrix import Matrix
from raytracer.tuple import Tuple, nearly_equal


class TestMatrix(unittest.TestCase):
    identity_matrix = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

    def test_4x4_matrix(self):
        m = Matrix(
            [
                [1, 2, 3, 4],
                [5.5, 6.5, 7.5, 8.5],
                [9, 10, 11, 12],
                [13.5, 14.5, 15.5, 16.5],
            ]
        )
        assert m.grid[0][0] == 1
        assert m.grid[0][3] == 4
        assert m.grid[1][0] == 5.5
        assert m.grid[1][2] == 7.5
        assert m.grid[2][2] == 11
        assert m.grid[3][0] == 13.5
        assert m.grid[3][2] == 15.5

    def test_2x2_matrix(self):
        m = Matrix([[-3, 5], [1, -2]])
        assert m.grid[0][0] == -3
        assert m.grid[0][1] == 5
        assert m.grid[1][0] == 1
        assert m.grid[1][1] == -2

    def test_3x3_matrix(self):
        m = Matrix([[-3, 5, 0], [1, -2, -7], [0, 1, 1]])
        assert m.grid[0][0] == -3
        assert m.grid[1][1] == -2
        assert m.grid[2][2] == 1

    def test_matrix_equality(self):
        m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
        m2 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
        m3 = Matrix([[2, 3, 4, 5], [6, 7, 8, 9], [8, 7, 6, 5], [4, 3, 2, 1]])
        assert m1 == m2
        assert m1 != m3

    def test_matrix_multiplication(self):
        m1 = Matrix(
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 8, 7, 6],
                [5, 4, 3, 2],
            ]
        )
        m2 = Matrix(
            [
                [-2, 1, 2, 3],
                [3, 2, 1, -1],
                [4, 3, 6, 5],
                [1, 2, 7, 8],
            ]
        )
        assert m1 * m2 == Matrix(
            [
                [20, 22, 50, 48],
                [44, 54, 114, 108],
                [40, 58, 110, 102],
                [16, 26, 46, 42],
            ]
        )

    def test_matrix_multiplied_by_tuple(self):
        m = Matrix([[1, 2, 3, 4], [2, 4, 4, 2], [8, 6, 4, 1], [0, 0, 0, 1]])
        t = Tuple(1, 2, 3, 1)
        assert m * t == Tuple(18, 24, 33, 1)

    def test_multiplying_matrix_by_identity_matrix(self):
        m = Matrix(
            [
                [0, 1, 2, 4],
                [1, 2, 4, 8],
                [2, 4, 8, 16],
                [4, 8, 16, 32],
            ]
        )
        assert m * self.identity_matrix == m

    def test_multiplying_identity_matrix_by_tuple(self):
        t = Tuple(1, 2, 3, 4)
        assert self.identity_matrix * t == t

    def test_transposing_matrix(self):
        m = Matrix(
            [
                [0, 9, 3, 0],
                [9, 8, 0, 8],
                [1, 8, 5, 3],
                [0, 0, 5, 8],
            ]
        )
        assert m.transpose() == Matrix(
            [
                [0, 9, 1, 0],
                [9, 8, 8, 0],
                [3, 0, 5, 5],
                [0, 8, 3, 8],
            ]
        )

    def test_transposing_identity_matrix(self):
        assert self.identity_matrix.transpose() == self.identity_matrix

    def test_calculating_determinant_of_2x2_matrix(self):
        m = Matrix([[1, 5], [-3, 2]])
        assert m.determinant() == 17

    def test_submatrix_of_3x3_matrix_is_2x2_matrix(self):
        m = Matrix([[1, 5, 0], [-3, 2, 7], [0, 6, -3]])
        assert m.submatrix(0, 2) == Matrix([[-3, 2], [0, 6]])

    def test_submatrix_of_4x4_matrix_is_3x3_matrix(self):
        m = Matrix(
            [
                [-6, 1, 1, 6],
                [-8, 5, 8, 6],
                [-1, 0, 8, 2],
                [-7, 1, -1, 1],
            ]
        )
        assert m.submatrix(2, 1) == Matrix([[-6, 1, 6], [-8, 8, 6], [-7, -1, 1]])

    def test_calculating_minor_of_3x3_matrix(self):
        m = Matrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
        submatrix = m.submatrix(1, 0)
        assert submatrix.determinant() == 25
        assert m.minor(1, 0) == 25

    def test_calculating_cofactor_of_3x3_matrix(self):
        m = Matrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
        assert m.minor(0, 0) == -12
        assert m.cofactor(0, 0) == -12
        assert m.minor(1, 0) == 25
        assert m.cofactor(1, 0) == -25

    def test_calculating_determinant_of_3x3_matrix(self):
        m = Matrix([[1, 2, 6], [-5, 8, -4], [2, 6, 4]])
        assert m.cofactor(0, 0) == 56
        assert m.cofactor(0, 1) == 12
        assert m.cofactor(0, 2) == -46
        assert m.determinant() == -196

    def test_calculating_determinant_of_4x4_matrix(self):
        m = Matrix(
            [
                [-2, -8, 3, 5],
                [-3, 1, 7, 3],
                [1, 2, -9, 6],
                [-6, 7, 7, -9],
            ]
        )
        assert m.cofactor(0, 0) == 690
        assert m.cofactor(0, 1) == 447
        assert m.cofactor(0, 2) == 210
        assert m.cofactor(0, 3) == 51
        assert m.determinant() == -4071

    def test_invertible(self):
        m = Matrix(
            [
                [6, 4, 4, 4],
                [5, 5, 7, 6],
                [4, -9, 3, -7],
                [9, 1, 7, -6],
            ]
        )
        assert m.determinant() == -2120
        assert m.is_invertible()

    def test_noninvertible(self):
        m = Matrix(
            [
                [-4, 2, -2, -3],
                [9, 6, 2, 6],
                [0, -5, 1, -5],
                [0, 0, 0, 0],
            ]
        )
        assert m.determinant() == 0
        assert not m.is_invertible()

    def test_inverse_of_matrix(self):
        m1 = Matrix(
            [
                [-5, 2, 6, -8],
                [1, -5, 1, 8],
                [7, 7, -6, -7],
                [1, -3, 7, 4],
            ]
        )
        assert m1.is_invertible()
        m2 = m1.inverse()

        assert m1.determinant() == 532
        assert m1.cofactor(2, 3) == -160
        assert m2.grid[3][2] == -160 / 532
        assert m1.cofactor(3, 2) == 105
        assert m2.grid[2][3] == 105 / 532
        assert m2 == Matrix(
            [
                [0.21805, 0.45113, 0.24060, -0.04511],
                [-0.80827, -1.45677, -0.44361, 0.52068],
                [-0.07895, -0.22368, -0.05263, 0.19737],
                [-0.52256, -0.81391, -0.30075, 0.30639],
            ]
        )

    def test_inverse_of_matrix_2(self):
        m = Matrix(
            [
                [8, -5, 9, 2],
                [7, 5, 6, 1],
                [-6, 0, 9, 6],
                [-3, 0, -9, -4],
            ]
        )
        assert m.inverse() == Matrix(
            [
                [-0.15385, -0.15385, -0.28205, -0.53846],
                [-0.07692, 0.12308, 0.02564, 0.03077],
                [0.35897, 0.35897, 0.43590, 0.92308],
                [-0.69231, -0.69231, -0.76923, -1.92308],
            ]
        )

    def test_inverse_of_matrix_3(self):
        m = Matrix(
            [
                [9, 3, 0, 9],
                [-5, -2, -6, -3],
                [-4, 9, 6, 4],
                [-7, 6, 6, 2],
            ]
        )
        assert m.inverse() == Matrix(
            [
                [-0.04074, -0.07778, 0.14444, -0.22222],
                [-0.07778, 0.03333, 0.36667, -0.33333],
                [-0.02901, -0.14630, -0.10926, 0.12963],
                [0.17778, 0.06667, -0.26667, 0.33333],
            ]
        )

    def test_multiplying_product_by_inverse(self):
        m1 = Matrix(
            [
                [3, -9, 7, 3],
                [3, -8, 2, -9],
                [-4, 4, 4, 1],
                [-6, 5, -1, 1],
            ]
        )
        m2 = Matrix(
            [
                [8, 2, 2, 2],
                [3, -1, 7, 0],
                [7, 0, 5, 4],
                [6, -2, 0, 5],
            ]
        )
        m3 = m1 * m2
        assert m3 * m2.inverse() == m1
