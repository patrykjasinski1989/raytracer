from math import pi, sqrt
import unittest

from raytracer.matrix import Matrix
from raytracer.transformation import (
    translation,
    scaling,
    rotation_x,
    rotation_y,
    rotation_z,
    shearing,
)
from raytracer.tuple import point, vector


class TestTransformation(unittest.TestCase):
    def test_multiplying_by_translation_matrix(self):
        transform = translation(5, -3, 2)
        p = point(-3, 4, 5)
        assert transform * p == point(2, 1, 7)

    def test_multiplying_by_inverse_of_translation_matrix(self):
        transform = translation(5, -3, 2)
        inv = transform.inverse()
        p = point(-3, 4, 5)
        assert inv * p == point(-8, 7, 3)

    def test_translation_does_not_affect_vectors(self):
        transform = translation(5, -3, 2)
        v = vector(-3, 4, 5)
        assert transform * v == v

    def test_scaling_matrix_applied_to_point(self):
        transform = scaling(2, 3, 4)
        p = point(-4, 6, 8)
        assert transform * p == point(-8, 18, 32)

    def test_scaling_matrix_applied_to_vector(self):
        transform = scaling(2, 3, 4)
        v = vector(-4, 6, 8)
        assert transform * v == vector(-8, 18, 32)

    def test_multiplying_by_inverse_of_scaling_matrix(self):
        transform = scaling(2, 3, 4)
        inv = transform.inverse()
        v = vector(-4, 6, 8)
        assert inv * v == vector(-2, 2, 2)

    def test_reflection_is_scaling_by_negative_value(self):
        transform = scaling(-1, 1, 1)
        p = point(2, 3, 4)
        assert transform * p == point(-2, 3, 4)

    def test_rotating_point_around_x_axis(self):
        p = point(0, 1, 0)
        half_quarter = rotation_x(pi / 4)
        full_quarter = rotation_x(pi / 2)
        assert half_quarter * p == point(0, sqrt(2) / 2, sqrt(2) / 2)
        assert full_quarter * p == point(0, 0, 1)

    def test_inverse_of_x_rotation_rotates_in_opposite_direction(self):
        p = point(0, 1, 0)
        half_quarter = rotation_x(pi / 4)
        inv = half_quarter.inverse()
        assert inv * p == point(0, sqrt(2) / 2, -sqrt(2) / 2)

    def test_rotating_point_around_y_axis(self):
        p = point(0, 0, 1)
        half_quarter = rotation_y(pi / 4)
        full_quarter = rotation_y(pi / 2)
        assert half_quarter * p == point(sqrt(2) / 2, 0, sqrt(2) / 2)
        assert full_quarter * p == point(1, 0, 0)

    def test_rotating_point_around_z_axis(self):
        p = point(0, 1, 0)
        half_quarter = rotation_z(pi / 4)
        full_quarter = rotation_z(pi / 2)
        assert half_quarter * p == point(-sqrt(2) / 2, sqrt(2) / 2, 0)
        assert full_quarter * p == point(-1, 0, 0)

    def test_shearing_transformation_moves_x_in_proportion_to_y(self):
        transform = shearing(1, 0, 0, 0, 0, 0)
        p = point(2, 3, 4)
        assert transform * p == point(5, 3, 4)

    def test_shearing_transformation_moves_x_in_proportion_to_z(self):
        transform = shearing(0, 1, 0, 0, 0, 0)
        p = point(2, 3, 4)
        assert transform * p == point(6, 3, 4)

    def test_shearing_transformation_moves_y_in_proportion_to_x(self):
        transform = shearing(0, 0, 1, 0, 0, 0)
        p = point(2, 3, 4)
        assert transform * p == point(2, 5, 4)

    def test_shearing_transformation_moves_y_in_proportion_to_z(self):
        transform = shearing(0, 0, 0, 1, 0, 0)
        p = point(2, 3, 4)
        assert transform * p == point(2, 7, 4)

    def test_shearing_transformation_moves_z_in_proportion_to_x(self):
        transform = shearing(0, 0, 0, 0, 1, 0)
        p = point(2, 3, 4)
        assert transform * p == point(2, 3, 6)

    def test_shearing_transformation_moves_z_in_proportion_to_y(self):
        transform = shearing(0, 0, 0, 0, 0, 1)
        p = point(2, 3, 4)
        assert transform * p == point(2, 3, 7)

    def test_individual_transformations_applied_in_sequence(self):
        p = point(1, 0, 1)
        A = rotation_x(pi / 2)
        B = scaling(5, 5, 5)
        C = translation(10, 5, 7)
        p2 = A * p
        assert p2 == point(1, -1, 0)
        p3 = B * p2
        assert p3 == point(5, -5, 0)
        p4 = C * p3
        assert p4 == point(15, 0, 7)

    def test_chained_transformations_applied_in_reverse_order(self):
        p = point(1, 0, 1)
        A = rotation_x(pi / 2)
        B = scaling(5, 5, 5)
        C = translation(10, 5, 7)
        T = C * B * A
        assert T * p == point(15, 0, 7)

    def test_fluent_interface(self):
        p = point(1, 0, 1)
        T = Matrix.identity().rotate_x(pi / 2).scale(5, 5, 5).translate(10, 5, 7)
        assert T * p == point(15, 0, 7)
