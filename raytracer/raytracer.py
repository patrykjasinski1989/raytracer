from math import pi
from raytracer.canvas import Canvas
from raytracer.intersection import hit
from raytracer.light import Light
from raytracer.material import Material
from raytracer.ray import Ray
from raytracer.sphere import Sphere
from raytracer.transformation import rotation_y
from raytracer.tuple import Color, Point, Tuple, point


if __name__ == "__main__":
    # start the ray at z = -5
    ray_origin = Point(0, 0, -5)
    # put the wall at z = 10
    wall_z = 10
    wall_size = 7.0
    canvas_pixels = 512
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2
    canvas = Canvas(canvas_pixels, canvas_pixels)
    color = Color(1, 0, 0)  # red

    shape = Sphere()
    shape.material = Material()
    shape.material.color = Color(1, 0.2, 1)

    light_position = Point(-10, 10, -10)
    light_color = Color(1, 1, 1)
    light = Light(light_position, light_color)

    # for each row of pixels in the canvas
    for y in range(canvas_pixels):
        # compute the world y coordinate (top = +half, bottom = -half)
        world_y = half - pixel_size * y
        # for each pixel in the row
        for x in range(canvas_pixels):
            # compute the world x coordinate (left = -half, right = half)
            world_x = -half + pixel_size * x
            # describe the point on the wall that the ray will target
            position = Point(world_x, world_y, wall_z)
            r = Ray(ray_origin, (position - ray_origin).normalize())  # type: ignore
            xs = shape.intersect(r)
            _hit = hit(xs)
            if _hit:
                point = r.position(_hit.t)
                normal = _hit.object.normal_at(point)
                eye = -r.direction
                color = _hit.object.material.lighting(light, point, eye, normal)
                canvas.write_pixel(x, y, color)

    with open("sphere.ppm", "w") as f:
        f.write(canvas.to_ppm())
