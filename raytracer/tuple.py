EPSILON: float = 1e-5


def nearly_equal(a: float, b: float) -> bool:
    return abs(a - b) < EPSILON


class Tuple:
    def __init__(self, x, y, z, w):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def __str__(self) -> str:
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f}, {self.w:.2f})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tuple):
            return NotImplemented
        return (
            nearly_equal(self.x, other.x)
            and nearly_equal(self.y, other.y)
            and nearly_equal(self.z, other.z)
            and nearly_equal(self.w, other.w)
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
        magnitude = self.magnitude()
        if magnitude == 0:
            return self
        return self / magnitude

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

    def reflect(self, normal: "Tuple") -> "Tuple":
        return self - normal * 2 * self.dot(normal)


class Point(Tuple):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 1.0)

    def __add__(self, other: "Tuple") -> "Point":
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Point")
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)


class Vector(Tuple):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z, 0.0)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    __rmul__ = __mul__


def point(x: float, y: float, z: float) -> Point:
    return Point(x, y, z)


def vector(x: float, y: float, z: float) -> Vector:
    return Vector(x, y, z)


class Color(Tuple):
    def __init__(self, red, green, blue):
        super().__init__(red, green, blue, 0.0)
        self.red = self.x
        self.green = self.y
        self.blue = self.z

    def hadamard_product(self, other):
        return Color(
            self.red * other.red, self.green * other.green, self.blue * other.blue
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Color(self.red * other, self.green * other, self.blue * other)
        elif isinstance(other, Color):
            return self.hadamard_product(other)
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Color):
            return Color(
                self.red + other.red, self.green + other.green, self.blue + other.blue
            )
        else:
            return NotImplemented
