import unittest

from raytracer.ray import Ray
from raytracer.transformation import translation
from raytracer.tuple import Point, Vector


class TestRay(unittest.TestCase):
    def test_create_and_query_ray(self):
        origin = Point(1, 2, 3)
        direction = Vector(4, 5, 6)
        r = Ray(origin, direction)
        self.assertEqual(r.origin, origin)
        self.assertEqual(r.direction, direction)

    def test_compute_point_from_distance(self):
        r = Ray(Point(2, 3, 4), Vector(1, 0, 0))
        self.assertEqual(r.position(0), Point(2, 3, 4))
        self.assertEqual(r.position(1), Point(3, 3, 4))
        self.assertEqual(r.position(-1), Point(1, 3, 4))
        self.assertEqual(r.position(2.5), Point(4.5, 3, 4))

    def test_translate_ray(self):
        r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
        r2 = r.translate(3, 4, 5)
        self.assertEqual(r2.origin, Point(4, 6, 8))
        self.assertEqual(r2.direction, Vector(0, 1, 0))

    def test_scale_ray(self):
        r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
        r2 = r.scale(2, 3, 4)
        self.assertEqual(r2.origin, Point(2, 6, 12))
        print(r2.direction)
        self.assertEqual(r2.direction, Vector(0, 3, 0))
