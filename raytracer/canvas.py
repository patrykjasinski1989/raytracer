from math import ceil
from typing import List
from raytracer.tuple import Color


class Canvas:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.grid: List[List[Color]] = [
            [Color(0, 0, 0) for _ in range(height)] for _ in range(width)
        ]

    def write_pixel(self, x: int, y: int, color: Color):
        self.grid[x][y] = color

    def pixel_at(self, x: int, y: int) -> Color:
        return self.grid[x][y]

    def to_ppm(self) -> str:
        max_line_length: int = 70
        ppm: str = f"P3\n{self.width} {self.height}\n255\n"
        clamp = lambda x: min(255, max(0, ceil(x * 255)))

        for y in range(self.height):
            line: str = ""
            for x in range(self.width):
                pixel = self.pixel_at(x, y)
                rgb_values = [clamp(pixel.red), clamp(pixel.green), clamp(pixel.blue)]
                for value in rgb_values:
                    value_str: str = str(value)
                    if len(line) + len(value_str) > max_line_length:
                        ppm += line.rstrip() + "\n"
                        line = ""
                    line += value_str + " "

            ppm += line.rstrip() + "\n"

        return ppm
