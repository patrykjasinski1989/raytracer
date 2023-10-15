import math
import unittest
from raytracer.tuple import Color, Tuple, nearly_equal, point, vector


class TestTuple(unittest.TestCase):
    def test_tuple_point(self):
        a = Tuple(4.3, -4.2, 3.1, 1.0)
        assert a.x == 4.3
        assert a.y == -4.2
        assert a.z == 3.1
        assert a.w == 1.0
        assert a.is_point()
        assert not a.is_vector()

    def test_tuple_vector(self):
        a = Tuple(4.3, -4.2, 3.1, 0.0)
        assert a.x == 4.3
        assert a.y == -4.2
        assert a.z == 3.1
        assert a.w == 0.0
        assert not a.is_point()
        assert a.is_vector()

    def test_factory_functions(self):
        p = point(4, -4, 3)
        assert p == Tuple(4, -4, 3, 1)

        v = vector(4, -4, 3)
        assert v == Tuple(4, -4, 3, 0)

    def test_adding_tuples(self):
        a1 = Tuple(3, -2, 5, 1)
        a2 = Tuple(-2, 3, 1, 0)
        assert a1 + a2 == Tuple(1, 1, 6, 1)

    def test_subtracting_points(self):
        p1 = point(3, 2, 1)
        p2 = point(5, 6, 7)
        assert p1 - p2 == vector(-2, -4, -6)

    def test_subtracting_vector_from_point(self):
        p = point(3, 2, 1)
        v = vector(5, 6, 7)
        assert p - v == point(-2, -4, -6)

    def test_subtracting_vectors(self):
        v1 = vector(3, 2, 1)
        v2 = vector(5, 6, 7)
        assert v1 - v2 == vector(-2, -4, -6)

    def test_subtracting_vector_from_zero_vector(self):
        zero = vector(0, 0, 0)
        v = vector(1, -2, 3)
        assert zero - v == vector(-1, 2, -3)

    def test_negating_tuple(self):
        a = Tuple(1, -2, 3, -4)
        assert -a == Tuple(-1, 2, -3, 4)

    def test_multiplying_tuple_by_scalar(self):
        a = Tuple(1, -2, 3, -4)
        assert a * 3.5 == Tuple(3.5, -7, 10.5, -14)

    def test_multiplying_tuple_by_fraction(self):
        a = Tuple(1, -2, 3, -4)
        assert a * 0.5 == Tuple(0.5, -1, 1.5, -2)

    def test_dividing_tuple_by_scalar(self):
        a = Tuple(1, -2, 3, -4)
        assert a / 2 == Tuple(0.5, -1, 1.5, -2)

    def test_magnitude(self):
        v1 = vector(1, 0, 0)
        assert v1.magnitude() == 1
        v2 = vector(0, 1, 0)
        assert v2.magnitude() == 1
        v3 = vector(0, 0, 1)
        assert v3.magnitude() == 1
        v4 = vector(1, 2, 3)
        assert v4.magnitude() == math.sqrt(14)
        v5 = vector(-1, -2, -3)
        assert v5.magnitude() == math.sqrt(14)

    def test_normalize(self):
        v1 = vector(4, 0, 0)
        assert v1.normalize() == vector(1, 0, 0)
        v2 = vector(1, 2, 3)
        assert v2.normalize() == vector(
            1 / math.sqrt(14), 2 / math.sqrt(14), 3 / math.sqrt(14)
        )
        v3 = vector(1, 2, 3)
        assert v3.normalize().magnitude() == 1

    def test_dot_product(self):
        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        assert a.dot(b) == 20

    def test_cross_product(self):
        a = vector(1, 2, 3)
        b = vector(2, 3, 4)
        assert a.cross(b) == vector(-1, 2, -1)
        assert b.cross(a) == vector(1, -2, 1)


class TestColor(unittest.TestCase):
    def test_colors_are_rgb_tuples(self):
        c = Color(-0.5, 0.4, 1.7)
        assert nearly_equal(c.red, -0.5)
        assert nearly_equal(c.green, 0.4)
        assert nearly_equal(c.blue, 1.7)

    def test_adding_colors(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        assert c1 + c2 == Color(1.6, 0.7, 1.0)

    def test_subtracting_colors(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)
        assert c1 - c2 == Color(0.2, 0.5, 0.5)

    def test_multiplying_color_by_scalar(self):
        c = Color(0.2, 0.3, 0.4)
        assert c * 2 == Color(0.4, 0.6, 0.8)

    def test_multiplying_colors(self):
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)
        assert c1 * c2 == Color(0.9, 0.2, 0.04)
