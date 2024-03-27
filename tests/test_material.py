from math import sqrt
import unittest

from raytracer.light import Light
from raytracer.material import Material
from raytracer.sphere import Sphere
from raytracer.tuple import Color, Point, Vector


class TestMaterial(unittest.TestCase):
    def test_default_material(self):
        m = Material()
        self.assertEqual(m.color, Color(1, 1, 1))
        self.assertEqual(m.ambient, 0.1)
        self.assertEqual(m.diffuse, 0.9)
        self.assertEqual(m.specular, 0.9)
        self.assertEqual(m.shininess, 200.0)

    def test_lightning_with_eye_between_light_and_surface(self):
        m = Material()
        position = Point(0, 0, 0)
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 0, -10), Color(1, 1, 1))
        result = m.lighting(light, position, eyev, normalv)
        self.assertEqual(result, Color(1.9, 1.9, 1.9))

    def test_lighting_with_eye_between_light_and_surface_eye_offset_45_degrees(self):
        m = Material()
        position = Point(0, 0, 0)
        eyev = Vector(0, sqrt(2) / 2, -sqrt(2) / 2)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 0, -10), Color(1, 1, 1))
        result = m.lighting(light, position, eyev, normalv)
        print("Expected:", Color(1.0, 1.0, 1.0))
        print("Actual:", result)
        self.assertEqual(result, Color(1.0, 1.0, 1.0))

    def test_lighting_with_eye_opposite_surface_light_offset_45_degrees(self):
        m = Material()
        position = Point(0, 0, 0)
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 10, -10), Color(1, 1, 1))
        result = m.lighting(light, position, eyev, normalv)
        print("Expected:", Color(1.0, 1.0, 1.0))
        print("Actual:", result)
        self.assertEqual(result, Color(0.7364, 0.7364, 0.7364))

    def test_lighting_with_eye_in_path_of_reflection_vector(self):
        m = Material()
        position = Point(0, 0, 0)
        eyev = Vector(0, -sqrt(2) / 2, -sqrt(2) / 2)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 10, -10), Color(1, 1, 1))
        result = m.lighting(light, position, eyev, normalv)
        print("Expected:", Color(1.0, 1.0, 1.0))
        print("Actual:", result)
        self.assertEqual(result, Color(1.6364, 1.6364, 1.6364))

    def test_lighting_with_light_behind_surface(self):
        m = Material()
        position = Point(0, 0, 0)
        eyev = Vector(0, 0, -1)
        normalv = Vector(0, 0, -1)
        light = Light(Point(0, 0, 10), Color(1, 1, 1))
        result = m.lighting(light, position, eyev, normalv)
        print("Expected:", Color(1.0, 1.0, 1.0))
        print("Actual:", result)
        self.assertEqual(result, Color(0.1, 0.1, 0.1))
