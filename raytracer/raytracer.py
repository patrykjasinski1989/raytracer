from raytracer.canvas import Canvas
from raytracer.tuple import Color, Tuple, point, vector


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


start = point(0, 1, 0)
velocity = vector(1, 1.8, 0).normalize() * 11.25
p = Projectile(start, velocity)

gravity = vector(0, -0.1, 0)
wind = vector(-0.01, 0, 0)
e = Environment(gravity, wind)

c = Canvas(900, 550)
color = Color(1, 0, 0)

tick_count = 0
while p.position.y > 0:
    x = int(p.position.x)
    y = c.height - int(p.position.y)
    if 0 <= x < c.width and 0 <= y < c.height:
        c.write_pixel(x, y, color)
    p = tick(e, p)
with open("projectile_path.ppm", "w") as f:
        f.write(c.to_ppm())
