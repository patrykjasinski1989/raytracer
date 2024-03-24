from raytracer.transformation_matrices import (
    translation_matrix,
    scaling_matrix,
    rotation_x_matrix,
    rotation_y_matrix,
    rotation_z_matrix,
    shearing_matrix,
)
from raytracer.matrix import Matrix


def translation(x, y, z):
    return Matrix(translation_matrix(x, y, z))


def scaling(x, y, z):
    return Matrix(scaling_matrix(x, y, z))


def rotation_x(r):
    return Matrix(rotation_x_matrix(r))


def rotation_y(r):
    return Matrix(rotation_y_matrix(r))


def rotation_z(r):
    return Matrix(rotation_z_matrix(r))


def shearing(xy, xz, yx, yz, zx, zy):
    return Matrix(shearing_matrix(xy, xz, yx, yz, zx, zy))
