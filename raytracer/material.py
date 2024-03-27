from raytracer.light import Light
from raytracer.tuple import Color, Point, Vector


class Material:
    def __init__(self):
        self.color = Color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Material):
            return NotImplemented
        return (
            self.color == other.color
            and self.ambient == other.ambient
            and self.diffuse == other.diffuse
            and self.specular == other.specular
            and self.shininess == other.shininess
        )

    def lighting(
        self, light: Light, point: Point, eyev: Vector, normalv: Vector
    ) -> Color:
        effective_color = self.color * light.intensity
        lightv = (light.position - point).normalize()
        ambient = effective_color * self.ambient
        light_dot_normal = lightv.dot(normalv)
        if light_dot_normal < 0:
            diffuse = Color(0, 0, 0)
            specular = Color(0, 0, 0)
        else:
            diffuse = effective_color * self.diffuse * light_dot_normal
            reflectv = -lightv.reflect(normalv)
            reflect_dot_eye = reflectv.dot(eyev)
            if reflect_dot_eye <= 0:
                specular = Color(0, 0, 0)
            else:
                factor = reflect_dot_eye ** self.shininess
                specular = light.intensity * self.specular * factor
        return ambient + diffuse + specular
