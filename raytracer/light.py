from raytracer.tuple import Color, Point


class Light:
    def __init__(self, position: Point, intensity: Color):
        self.position = position
        self.intensity = intensity
