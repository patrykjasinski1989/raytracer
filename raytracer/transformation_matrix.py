from math import cos, sin


def translation_matrix(x, y, z):
    return [[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]]


def scaling_matrix(x, y, z):
    return [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]]


def rotation_x_matrix(r):
    return [
        [1, 0, 0, 0],
        [0, cos(r), -sin(r), 0],
        [0, sin(r), cos(r), 0],
        [0, 0, 0, 1],
    ]


def rotation_y_matrix(r):
    return [
        [cos(r), 0, sin(r), 0],
        [0, 1, 0, 0],
        [-sin(r), 0, cos(r), 0],
        [0, 0, 0, 1],
    ]


def rotation_z_matrix(r):
    return [
        [cos(r), -sin(r), 0, 0],
        [sin(r), cos(r), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]


def shearing_matrix(xy, xz, yx, yz, zx, zy):
    return [
        [1, xy, xz, 0],
        [yx, 1, yz, 0],
        [zx, zy, 1, 0],
        [0, 0, 0, 1],
    ]
