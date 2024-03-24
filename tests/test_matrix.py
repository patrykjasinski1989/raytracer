import unittest

from raytracer.matrix import Matrix
from raytracer.tuple import Tuple, nearly_equal


class TestMatrix(unittest.TestCase):
    identity_matrix = Matrix.identity()

    def test_4x4_matrix(self):
        M = Matrix(
            [
                [1, 2, 3, 4],
                [5.5, 6.5, 7.5, 8.5],
                [9, 10, 11, 12],
                [13.5, 14.5, 15.5, 16.5],
            ]
        )
        assert M[0, 0] == 1
        assert M[0, 3] == 4
        assert M[1, 0] == 5.5
        assert M[1, 2] == 7.5
        assert M[2, 2] == 11
        assert M[3, 0] == 13.5
        assert M[3, 2] == 15.5

    def test_2x2_matrix(self):
        M = Matrix([[-3, 5], [1, -2]])
        assert M[0, 0] == -3
        assert M[0, 1] == 5
        assert M[1, 0] == 1
        assert M[1, 1] == -2

    def test_3x3_matrix(self):
        M = Matrix([[-3, 5, 0], [1, -2, -7], [0, 1, 1]])
        assert M[0, 0] == -3
        assert M[1, 1] == -2
        assert M[2, 2] == 1

    def test_matrix_equality(self):
        A = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
        B = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
        C = Matrix([[2, 3, 4, 5], [6, 7, 8, 9], [8, 7, 6, 5], [4, 3, 2, 1]])
        assert A == B
        assert A != C

    def test_matrix_multiplication(self):
        A = Matrix(
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 8, 7, 6],
                [5, 4, 3, 2],
            ]
        )
        B = Matrix(
            [
                [-2, 1, 2, 3],
                [3, 2, 1, -1],
                [4, 3, 6, 5],
                [1, 2, 7, 8],
            ]
        )
        assert A * B == Matrix(
            [
                [20, 22, 50, 48],
                [44, 54, 114, 108],
                [40, 58, 110, 102],
                [16, 26, 46, 42],
            ]
        )

    def test_matrix_multiplied_by_tuple(self):
        A = Matrix([[1, 2, 3, 4], [2, 4, 4, 2], [8, 6, 4, 1], [0, 0, 0, 1]])
        b = Tuple(1, 2, 3, 1)
        assert A * b == Tuple(18, 24, 33, 1)

    def test_multiplying_matrix_by_identity_matrix(self):
        A = Matrix(
            [
                [0, 1, 2, 4],
                [1, 2, 4, 8],
                [2, 4, 8, 16],
                [4, 8, 16, 32],
            ]
        )
        assert A * self.identity_matrix == A

    def test_multiplying_identity_matrix_by_tuple(self):
        a = Tuple(1, 2, 3, 4)
        assert self.identity_matrix * a == a

    def test_transposing_matrix(self):
        A = Matrix(
            [
                [0, 9, 3, 0],
                [9, 8, 0, 8],
                [1, 8, 5, 3],
                [0, 0, 5, 8],
            ]
        )
        assert A.transpose() == Matrix(
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
        A = Matrix([[1, 5], [-3, 2]])
        assert A.determinant() == 17

    def test_submatrix_of_3x3_matrix_is_2x2_matrix(self):
        A = Matrix([[1, 5, 0], [-3, 2, 7], [0, 6, -3]])
        assert A.submatrix(0, 2) == Matrix([[-3, 2], [0, 6]])

    def test_submatrix_of_4x4_matrix_is_3x3_matrix(self):
        A = Matrix(
            [
                [-6, 1, 1, 6],
                [-8, 5, 8, 6],
                [-1, 0, 8, 2],
                [-7, 1, -1, 1],
            ]
        )
        assert A.submatrix(2, 1) == Matrix([[-6, 1, 6], [-8, 8, 6], [-7, -1, 1]])

    def test_calculating_minor_of_3x3_matrix(self):
        A = Matrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
        B = A.submatrix(1, 0)
        assert B.determinant() == 25
        assert A.minor(1, 0) == 25

    def test_calculating_cofactor_of_3x3_matrix(self):
        A = Matrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
        assert A.minor(0, 0) == -12
        assert A.cofactor(0, 0) == -12
        assert A.minor(1, 0) == 25
        assert A.cofactor(1, 0) == -25

    def test_calculating_determinant_of_3x3_matrix(self):
        A = Matrix([[1, 2, 6], [-5, 8, -4], [2, 6, 4]])
        assert A.cofactor(0, 0) == 56
        assert A.cofactor(0, 1) == 12
        assert A.cofactor(0, 2) == -46
        assert A.determinant() == -196

    def test_calculating_determinant_of_4x4_matrix(self):
        A = Matrix(
            [
                [-2, -8, 3, 5],
                [-3, 1, 7, 3],
                [1, 2, -9, 6],
                [-6, 7, 7, -9],
            ]
        )
        assert A.cofactor(0, 0) == 690
        assert A.cofactor(0, 1) == 447
        assert A.cofactor(0, 2) == 210
        assert A.cofactor(0, 3) == 51
        assert A.determinant() == -4071

    def test_invertible(self):
        A = Matrix(
            [
                [6, 4, 4, 4],
                [5, 5, 7, 6],
                [4, -9, 3, -7],
                [9, 1, 7, -6],
            ]
        )
        assert A.determinant() == -2120
        assert A.is_invertible()

    def test_noninvertible(self):
        A = Matrix(
            [
                [-4, 2, -2, -3],
                [9, 6, 2, 6],
                [0, -5, 1, -5],
                [0, 0, 0, 0],
            ]
        )
        assert A.determinant() == 0
        assert not A.is_invertible()

    def test_inverse_of_matrix(self):
        A = Matrix(
            [
                [-5, 2, 6, -8],
                [1, -5, 1, 8],
                [7, 7, -6, -7],
                [1, -3, 7, 4],
            ]
        )
        assert A.is_invertible()
        B = A.inverse()

        assert A.determinant() == 532
        assert A.cofactor(2, 3) == -160
        assert B.grid[3][2] == -160 / 532
        assert A.cofactor(3, 2) == 105
        assert B.grid[2][3] == 105 / 532
        assert B == Matrix(
            [
                [0.21805, 0.45113, 0.24060, -0.04511],
                [-0.80827, -1.45677, -0.44361, 0.52068],
                [-0.07895, -0.22368, -0.05263, 0.19737],
                [-0.52256, -0.81391, -0.30075, 0.30639],
            ]
        )

    def test_inverse_of_matrix_2(self):
        A = Matrix(
            [
                [8, -5, 9, 2],
                [7, 5, 6, 1],
                [-6, 0, 9, 6],
                [-3, 0, -9, -4],
            ]
        )
        assert A.inverse() == Matrix(
            [
                [-0.15385, -0.15385, -0.28205, -0.53846],
                [-0.07692, 0.12308, 0.02564, 0.03077],
                [0.35897, 0.35897, 0.43590, 0.92308],
                [-0.69231, -0.69231, -0.76923, -1.92308],
            ]
        )

    def test_inverse_of_matrix_3(self):
        A = Matrix(
            [
                [9, 3, 0, 9],
                [-5, -2, -6, -3],
                [-4, 9, 6, 4],
                [-7, 6, 6, 2],
            ]
        )
        assert A.inverse() == Matrix(
            [
                [-0.04074, -0.07778, 0.14444, -0.22222],
                [-0.07778, 0.03333, 0.36667, -0.33333],
                [-0.02901, -0.14630, -0.10926, 0.12963],
                [0.17778, 0.06667, -0.26667, 0.33333],
            ]
        )

    def test_multiplying_product_by_inverse(self):
        A = Matrix(
            [
                [3, -9, 7, 3],
                [3, -8, 2, -9],
                [-4, 4, 4, 1],
                [-6, 5, -1, 1],
            ]
        )
        B = Matrix(
            [
                [8, 2, 2, 2],
                [3, -1, 7, 0],
                [7, 0, 5, 4],
                [6, -2, 0, 5],
            ]
        )
        C = A * B
        assert C * B.inverse() == A
