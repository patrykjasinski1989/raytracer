from dataclasses import dataclass, field


@dataclass
class Tuple:
    x: float
    y: float
    z: float
    w: float

    EPSILON: float = field(default=1e-9, init=False, repr=False)

    @staticmethod
    def nearly_equal(a: float, b: float) -> bool:
        return abs(a - b) < Tuple.EPSILON

    def __repr__(self) -> str:
        return f"Tuple({self.x}, {self.y}, {self.z}, {self.w})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tuple):
            return NotImplemented
        return (
            self.nearly_equal(self.x, other.x)
            and self.nearly_equal(self.y, other.y)
            and self.nearly_equal(self.z, other.z)
            and self.nearly_equal(self.w, other.w)
        )

    def __add__(self, other: "Tuple") -> "Tuple":
        return Tuple(
            self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w
        )

    def __sub__(self, other: "Tuple") -> "Tuple":
        return Tuple(
            self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w
        )

    def __neg__(self) -> "Tuple":
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, scalar: float) -> "Tuple":
        return Tuple(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)

    __rmul__ = __mul__

    def __truediv__(self, scalar: float) -> "Tuple":
        return Tuple(self.x / scalar, self.y / scalar, self.z / scalar, self.w / scalar)

    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2) ** 0.5

    def normalize(self) -> "Tuple":
        return self / self.magnitude()

    def dot(self, other: "Tuple") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def cross(self, other: "Tuple") -> "Tuple":
        return vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def is_point(self) -> bool:
        return self.w == 1.0

    def is_vector(self) -> bool:
        return self.w == 0.0


def point(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 1.0)


def vector(x: float, y: float, z: float) -> Tuple:
    return Tuple(x, y, z, 0.0)


if __name__ == "__main__":

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

    p = Projectile(10 * point(0, 1, 0), vector(1, 1, 0).normalize())
    e = Environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))

    tick_count = 0
    while p.position.y > 0:
        print(p.position)
        p = tick(e, p)
        tick_count += 1
    print(f"The projectile hit the ground after {tick_count} ticks.")
