import math
from raytracer.tuple import Tuple, point, vector


def test_tuple_point():
    t = Tuple(4.3, -4.2, 3.1, 1.0)
    assert t.x == 4.3
    assert t.y == -4.2
    assert t.z == 3.1
    assert t.w == 1.0
    assert t.is_point()
    assert not t.is_vector()


def test_tuple_vector():
    t = Tuple(4.3, -4.2, 3.1, 0.0)
    assert t.x == 4.3
    assert t.y == -4.2
    assert t.z == 3.1
    assert t.w == 0.0
    assert not t.is_point()
    assert t.is_vector()


def test_factory_functions():
    p = point(4, -4, 3)
    assert p == Tuple(4, -4, 3, 1)

    v = vector(4, -4, 3)
    assert v == Tuple(4, -4, 3, 0)


def test_adding_tuples():
    t1 = Tuple(3, -2, 5, 1)
    t2 = Tuple(-2, 3, 1, 0)
    assert t1 + t2 == Tuple(1, 1, 6, 1)


def test_subtracting_points():
    p1 = point(3, 2, 1)
    p2 = point(5, 6, 7)
    assert p1 - p2 == vector(-2, -4, -6)


def test_subtracting_vector_from_point():
    p = point(3, 2, 1)
    v = vector(5, 6, 7)
    assert p - v == point(-2, -4, -6)


def test_subtracting_vectors():
    v1 = vector(3, 2, 1)
    v2 = vector(5, 6, 7)
    assert v1 - v2 == vector(-2, -4, -6)


def test_subtracting_vector_from_zero_vector():
    zero = vector(0, 0, 0)
    v = vector(1, -2, 3)
    assert zero - v == vector(-1, 2, -3)


def test_negating_tuple():
    t = Tuple(1, -2, 3, -4)
    assert -t == Tuple(-1, 2, -3, 4)


def test_multiplying_tuple_by_scalar():
    t = Tuple(1, -2, 3, -4)
    assert t * 3.5 == Tuple(3.5, -7, 10.5, -14)


def test_multiplying_tuple_by_fraction():
    t = Tuple(1, -2, 3, -4)
    assert t * 0.5 == Tuple(0.5, -1, 1.5, -2)


def test_dividing_tuple_by_scalar():
    t = Tuple(1, -2, 3, -4)
    assert t / 2 == Tuple(0.5, -1, 1.5, -2)


def test_magnitude():
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


def test_normalize():
    v1 = vector(4, 0, 0)
    assert v1.normalize() == vector(1, 0, 0)
    v2 = vector(1, 2, 3)
    assert v2.normalize() == vector(
        1 / math.sqrt(14), 2 / math.sqrt(14), 3 / math.sqrt(14)
    )
    v3 = vector(1, 2, 3)
    assert v3.normalize().magnitude() == 1


def test_dot_product():
    a = vector(1, 2, 3)
    b = vector(2, 3, 4)
    assert a.dot(b) == 20


def test_cross_product():
    a = vector(1, 2, 3)
    b = vector(2, 3, 4)
    assert a.cross(b) == vector(-1, 2, -1)
    assert b.cross(a) == vector(1, -2, 1)
