import unittest
from raytracer.canvas import Canvas
from raytracer.tuple import Color


class TestCanvas(unittest.TestCase):
    def test_canvas_creation(self):
        c = Canvas(10, 20)
        assert c.width == 10
        assert c.height == 20
        assert all(pixel == Color(0, 0, 0) for row in c.grid for pixel in row)

    def test_write_pixel(self):
        c = Canvas(10, 20)
        red = Color(1, 0, 0)
        c.write_pixel(2, 3, red)
        assert c.pixel_at(2, 3) == red

    def test_constructing_ppm_header(self):
        c = Canvas(5, 3)
        ppm = c.to_ppm()
        lines = ppm.splitlines()
        assert lines[0] == "P3"
        assert lines[1] == "5 3"
        assert lines[2] == "255"

    def test_constructing_ppm_pixel_data(self):
        c = Canvas(5, 3)
        c1 = Color(1.5, 0, 0)
        c2 = Color(0, 0.5, 0)
        c3 = Color(-0.5, 0, 1)
        c.write_pixel(0, 0, c1)
        c.write_pixel(2, 1, c2)
        c.write_pixel(4, 2, c3)
        ppm = c.to_ppm()
        lines = ppm.splitlines()
        assert lines[3] == "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
        assert lines[4] == "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0"
        assert lines[5] == "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"

    def test_splitting_long_lines(self):
        c = Canvas(10, 2)
        for x in range(10):
            for y in range(2):
                c.write_pixel(x, y, Color(1, 0.8, 0.6))
        ppm = c.to_ppm()
        lines = ppm.splitlines()
        assert (
            lines[3]
            == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204"
        )
        assert lines[4] == "153 255 204 153 255 204 153 255 204 153 255 204 153"
        assert (
            lines[5]
            == "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204"
        )
        assert lines[6] == "153 255 204 153 255 204 153 255 204 153 255 204 153"

    def test_ppm_ends_with_newline(self):
        c = Canvas(5, 3)
        ppm = c.to_ppm()
        assert ppm.endswith("\n")
