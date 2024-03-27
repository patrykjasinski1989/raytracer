from math import pi, sqrt
import unittest

from raytracer.material import Material
from raytracer.matrix import Matrix
from raytracer.ray import Ray
from raytracer.sphere import Sphere
from raytracer.transformation import rotation_z, scaling, translation
from raytracer.tuple import Point, Vector


class TestRay(unittest.TestCase):
    def test_ray_intersects_sphere_at_two_points(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 4.0)
        self.assertEqual(xs[1].t, 6.0)

    def test_ray_intersects_sphere_at_tangent(self):
        r = Ray(Point(0, 1, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, 5.0)
        self.assertEqual(xs[1].t, 5.0)

    def test_ray_misses_sphere(self):
        r = Ray(Point(0, 2, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 0)

    def test_ray_originates_inside_sphere(self):
        r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -1.0)
        self.assertEqual(xs[1].t, 1.0)

    def test_sphere_behind_ray(self):
        r = Ray(Point(0, 0, 5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].t, -6.0)
        self.assertEqual(xs[1].t, -4.0)

    def test_intersect_sets_object_on_intersection(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertEqual(xs[0].object, s)
        self.assertEqual(xs[1].object, s)

    def test_sphere_default_transformation(self):
        s = Sphere()
        self.assertEqual(s.transform, Matrix.identity())

    def test_changing_sphere_transformation(self):
        s = Sphere()
        t = translation(2, 3, 4)
        s.transform = t
        self.assertEqual(s.transform, t)

    def test_intersecting_scaled_sphere_with_ray(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        s.transform = scaling(2, 2, 2)
        xs = s.intersect(r)
        self.assertEqual(len(xs), 2)
        self.assertAlmostEqual(xs[0].t, 3)
        self.assertAlmostEqual(xs[1].t, 7)

    def test_intersecting_translated_sphere_with_ray(self):
        r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
        s = Sphere()
        s.transform = translation(5, 0, 0)
        xs = s.intersect(r)
        self.assertEqual(len(xs), 0)

    def test_normal_on_sphere_at_point_on_x_axis(self):
        s = Sphere()
        n = s.normal_at(Point(1, 0, 0))
        self.assertEqual(n, Vector(1, 0, 0))

    def test_normal_on_sphere_at_point_on_y_axis(self):
        s = Sphere()
        n = s.normal_at(Point(0, 1, 0))
        self.assertEqual(n, Vector(0, 1, 0))

    def test_normal_on_sphere_at_point_on_z_axis(self):
        s = Sphere()
        n = s.normal_at(Point(0, 0, 1))
        self.assertEqual(n, Vector(0, 0, 1))

    def test_normal_is_normalized_vector(self):
        s = Sphere()
        n = s.normal_at(Point(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))
        self.assertEqual(n, Vector(sqrt(3) / 3, sqrt(3) / 3, sqrt(3) / 3))

    def test_computing_normal_on_translated_sphere(self):
        s = Sphere()
        s.transform = translation(0, 1, 0)
        n = s.normal_at(Point(0, 1.70711, -0.70711))
        self.assertEqual(n, Vector(0, 0.70711, -0.70711))

    def test_computing_normal_on_transformed_sphere(self):
        s = Sphere()
        m = scaling(1, 0.5, 1) * rotation_z(pi / 5)
        s.transform = m
        n = s.normal_at(Point(0, sqrt(2) / 2, -sqrt(2) / 2))
        self.assertEqual(n, Vector(0, 0.97014, -0.24254))

    def test_sphere_has_default_material(self):
        s = Sphere()
        m = s.material
        self.assertEqual(m, Material())

    def test_sphere_may_be_assigned_material(self):
        s = Sphere()
        m = Material()
        m.ambient = 1
        s.material = m
        self.assertEqual(s.material, m)
