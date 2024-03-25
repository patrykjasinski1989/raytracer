from math import pi
from raytracer.canvas import Canvas
from raytracer.intersection import hit
from raytracer.ray import Ray
from raytracer.sphere import Sphere
from raytracer.transformation import rotation_y
from raytracer.tuple import Color, Point, Tuple, point


class Projectile:
    def __init__(self, position: Tuple, velocity: Tuple) -> None:
        self.position = position
        self.velocity = velocity


class Environment:
    def __init__(self, gravity: Tuple, wind: Tuple) -> None:
        self.gravity = gravity
        self.wind = wind


def tick(env: Environment, proj: Projectile) -> Projectile:
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)


if __name__ == "__main__":
    # start the ray at z = -5
    ray_origin = Point(0, 0, -5)
    # put the wall at z = 10
    wall_z = 10
    wall_size = 7.0
    canvas_pixels = 100
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2
    canvas = Canvas(canvas_pixels, canvas_pixels)
    color = Color(1, 0, 0)  # red
    shape = Sphere()

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
            if hit(xs):
                canvas.write_pixel(x, y, color)

    with open("circle.ppm", "w") as f:
        f.write(canvas.to_ppm())
