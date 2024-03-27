import unittest

from raytracer.light import Light
from raytracer.tuple import Color, Point


class TestLight(unittest.TestCase):
    def test_point_light_has_position_and_intensity(self):
        intensity = Color(1, 1, 1)
        position = Point(0, 0, 0)
        light = Light(position, intensity)
        self.assertEqual(light.position, position)
        self.assertEqual(light.intensity, intensity)
