from typing import List, Union

import numpy as np

from raytracer.transformation_matrix import (
    rotation_x_matrix,
    rotation_y_matrix,
    rotation_z_matrix,
    scaling_matrix,
    shearing_matrix,
    translation_matrix,
)
from raytracer.tuple import Tuple, nearly_equal


class Matrix:
    @classmethod
    def zeros(cls, rows: int, cols: int) -> "Matrix":
        return cls([[0.0 for _ in range(cols)] for _ in range(rows)])

    @classmethod
    def identity(cls) -> "Matrix":
        return cls([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

    def __init__(self, grid: List[List[float]]):
        self.grid = grid
        self.rows: int = len(grid)
        self.cols: int = len(grid[0])

    def __getitem__(self, index: tuple) -> float:
        return self.grid[index[0]][index[1]]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Matrix):
            return NotImplemented

        for row in range(self.rows):
            for col in range(self.cols):
                if not nearly_equal(self.grid[row][col], other.grid[row][col]):
                    return False
        return True

    def __mul__(self, other: Union[Tuple, "Matrix"]) -> Union[Tuple, "Matrix"]:
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Matrix dimensions do not match!")
            result_matrix = Matrix.zeros(self.rows, other.cols)
            for row in range(self.rows):
                for col in range(other.cols):
                    for i in range(other.rows):
                        result_matrix.grid[row][col] += (
                            self.grid[row][i] * other.grid[i][col]
                        )
            return result_matrix

        elif isinstance(other, Tuple):
            if self.cols != 4:
                raise ValueError("Matrix dimensions do not match!")
            result_tuple: List[float] = [0.0, 0.0, 0.0, 0.0]
            for row in range(self.rows):
                row_values = self.grid[row]
                result_tuple[row] = (
                    row_values[0] * other.x
                    + row_values[1] * other.y
                    + row_values[2] * other.z
                    + row_values[3] * other.w
                )
            return Tuple(
                result_tuple[0], result_tuple[1], result_tuple[2], result_tuple[3]
            )

        else:
            return NotImplemented

    def __str__(self) -> str:
        return "\n".join(
            [" ".join([f"{value:.2f}" for value in row]) for row in self.grid]
        )

    def transpose(self) -> "Matrix":
        return Matrix(
            [[self.grid[j][i] for j in range(self.rows)] for i in range(self.cols)]
        )

    def determinant(self) -> float:
        return np.linalg.det(self.grid)

    def submatrix(self, row: int, col: int) -> "Matrix":
        return Matrix(
            [
                [self.grid[i][j] for j in range(self.cols) if j != col]
                for i in range(self.rows)
                if i != row
            ]
        )

    def minor(self, row: int, col: int) -> float:
        return self.submatrix(row, col).determinant()

    def cofactor(self, row: int, col: int) -> float:
        minor = self.minor(row, col)
        return minor if (row + col) % 2 == 0 else -minor

    def is_invertible(self) -> bool:
        return self.determinant() != 0

    def inverse(self) -> "Matrix":
        if not self.is_invertible():
            raise ValueError("Matrix is not invertible!")

        m2 = Matrix.zeros(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                m2.grid[col][row] = self.cofactor(row, col) / self.determinant()
        return m2

    def translate(self, x, y, z):
        self = Matrix(translation_matrix(x, y, z)) * self
        return self

    def scale(self, x, y, z):
        self = Matrix(scaling_matrix(x, y, z)) * self
        return self

    def rotate_x(self, r):
        self = Matrix(rotation_x_matrix(r)) * self
        return self

    def rotate_y(self, r):
        self = Matrix(rotation_y_matrix(r)) * self
        return self

    def rotate_z(self, r):
        self = Matrix(rotation_z_matrix(r)) * self
        return self

    def shear(self, xy, xz, yx, yz, zx, zy):
        self = Matrix(shearing_matrix(xy, xz, yx, yz, zx, zy)) * self
        return self
