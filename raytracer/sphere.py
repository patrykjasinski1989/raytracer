from typing import List
from raytracer.intersection import Intersection
from raytracer.matrix import Matrix
from raytracer.ray import Ray
from raytracer.transformation_matrices import scaling_matrix
from raytracer.tuple import Point


class Sphere:
    def __init__(self):
        self.origin = Point(0, 0, 0)
        self.radius = 1
        self.transform = Matrix.identity()

    def intersect(self, ray: Ray) -> List[Intersection]:
        ray2 = ray.transform(self.transform.inverse())
        sphere_to_ray = ray2.origin - self.origin
        a = ray2.direction.dot(ray2.direction)
        b = 2 * ray2.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return []
        t1 = (-b - discriminant ** 0.5) / (2 * a)
        t2 = (-b + discriminant ** 0.5) / (2 * a)
        return [Intersection(t1, self), Intersection(t2, self)]
