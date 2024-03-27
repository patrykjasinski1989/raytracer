from raytracer.matrix import Matrix
from raytracer.transformation_matrix import scaling_matrix, translation_matrix
from raytracer.tuple import Point, Tuple, Vector


class Ray:
    def __init__(self, origin: Point, direction: Vector):
        self.origin = origin
        self.direction = direction

    def position(self, t: float) -> Point:
        return self.origin + self.direction * t

    def translate(self, x, y, z):
        self.origin = Matrix(translation_matrix(x, y, z)) * self.origin
        return self

    def scale(self, x, y, z):
        self.origin = Matrix(scaling_matrix(x, y, z)) * self.origin
        self.direction = Matrix(scaling_matrix(x, y, z)) * self.direction
        return self

    def transform(self, matrix: Matrix):
        transformed_origin = matrix * self.origin
        transformed_direction = matrix * self.direction
        if isinstance(transformed_origin, Tuple) and isinstance(
            transformed_direction, Tuple
        ):
            self.origin = Point(
                transformed_origin.x, transformed_origin.y, transformed_origin.z
            )
            self.direction = Vector(
                transformed_direction.x,
                transformed_direction.y,
                transformed_direction.z,
            )
        else:
            raise TypeError("Unexpected type after matrix transformation")
        return self
