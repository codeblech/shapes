# Standard Library Imports
from math import atan
from math import pi

# Local Application Imports
from helper import quadratic
from printable_3d import *


class Cube:
    def __init__(self, side):
        self.side = side
        self.volume = side ** 3
        self.diagonal = side * (3 ** 0.5)
        self.total_surface_area = 6 * (side ** 2)
        self.curved_surface_area = 4 * (side ** 2)

    @classmethod
    def from_volume(cls, volume):
        side = volume ** (1 / 3)
        return Cube(side)

    @classmethod
    def from_diagonal(cls, diagonal):
        side = diagonal / (3 ** 0.5)
        return Cube(side)

    @classmethod
    def from_total_surface_area(cls, total_surface_area):
        side = (total_surface_area / 6) ** 0.5
        return Cube(side)

    @classmethod
    def from_curved_surface_area(cls, curved_surface_area):
        side = (curved_surface_area / 4) ** 0.5
        return Cube(side)

    def __str__(self):
        return str_cube(
            self.side,
            self.volume,
            self.diagonal,
            self.total_surface_area,
            self.curved_surface_area,
        )


class Cuboid:
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.volume = length * breadth * height
        self.diagonal = (length ** 2 + breadth ** 2 + height ** 2) ** 0.5
        self.total_surface_area = 2 * (
            length * breadth + breadth * height + length * height
        )
        self.curved_surface_area = 2 * (length + breadth) * height

    @classmethod
    def from_length_breadth_volume(cls, length, breadth, volume):
        cls.length = length
        cls.breadth = breadth
        cls.volume = volume
        cls.height = volume / (length * breadth)
        return Cuboid(length, breadth, cls.height)

    @classmethod
    def from_length_height_volume(cls, length, height, volume):
        cls.length = length
        cls.height = height
        cls.volume = volume
        cls.breadth = volume / (length * height)
        return Cuboid(length, cls.breadth, height)

    @classmethod
    def from_breadth_height_volume(cls, height, breadth, volume):
        cls.breadth = breadth
        cls.height = height
        cls.volume = volume
        cls.length = volume / (breadth * height)
        return Cuboid(cls.length, breadth, height)

    def __str__(self):
        return str_cuboid(
            self.length,
            self.breadth,
            self.height,
            self.volume,
            self.diagonal,
            self.total_surface_area,
            self.curved_surface_area,
        )


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.volume = pi * radius ** 2 * height
        self.diagonal = ((height ** 2) + (4 * radius ** 2)) ** 0.5
        self.total_surface_area = 2 * pi * radius * (height + radius)
        self.curved_surface_area = 2 * pi * radius * height

    def __str__(self):
        return str_cylinder(
            self.radius,
            self.height,
            self.diagonal,
            self.volume,
            self.total_surface_area,
            self.curved_surface_area,
        )


class Sphere:
    def __init__(self, radius):
        self.radius = radius
        self.volume = (4 * pi * radius ** 3) / 3
        self.diameter = 2 * radius
        self.total_surface_area = 4 * pi * radius ** 2

    @classmethod
    def from_volume(cls, volume):
        radius = (3 * volume / (4 * pi)) ** (1 / 3)
        return Sphere(radius)

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return Sphere(radius)

    @classmethod
    def from_total_surface_area(cls, total_surface_area):
        radius = (total_surface_area / (4 * pi)) ** 0.5
        return Sphere(radius)

    def __str__(self):
        return str_sphere(
            self.radius, self.diameter, self.volume, self.total_surface_area
        )


class Hemisphere:
    def __init__(self, radius):
        self.radius = radius
        self.volume = (2 * pi * radius ** 3) / 3
        self.diameter = 2 * radius
        self.total_surface_area = 3 * pi * radius ** 2
        self.curved_surface_area = 2 * pi * radius ** 2

    @classmethod
    def from_volume(cls, volume):
        radius = (3 * volume / (2 * pi)) ** (1 / 3)
        return Hemisphere(radius)

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return Hemisphere(radius)

    @classmethod
    def from_total_surface_area(cls, total_surface_area):
        radius = (total_surface_area / (4 * pi)) ** 0.5
        return Hemisphere(radius)

    @classmethod
    def from_curved_surface_area(cls, curved_surface_area):
        radius = (curved_surface_area / (2 * pi)) ** 0.5
        return Hemisphere(radius)

    def __str__(self):
        return str_hemisphere(
            self.radius,
            self.diameter,
            self.volume,
            self.total_surface_area,
            self.curved_surface_area,
        )


class Cone:
    def __init__(self, radius=None, height=None, slant_height=None):
        if radius == None:
            radius = (slant_height ** 2 - height ** 2) ** 0.5
        elif height == None:
            height = (slant_height ** 2 - radius ** 2) ** 0.5
        elif slant_height == None:
            slant_height = (height ** 2 + radius ** 2) ** 0.5
        if slant_height ** 2 == radius ** 2 + height ** 2:
            self.radius = radius
            self.diameter = 2 * radius
            self.height = height
            self.slant_height = slant_height
            self.volume = 1 / 3 * (pi * (radius ** 2) * height)
            self.base_angle = atan(height / radius)
            self.vertical_angle = 180 - 2 * self.base_angle
            self.total_surface_area = pi * radius * (slant_height + radius)
            self.curved_surface_area = pi * radius * slant_height
        else:
            raise ValueError("The input values do not correspond to any single cone.")

    def __str__(self):
        return str_cone(
            self.radius,
            self.diameter,
            self.height,
            self.slant_height,
            self.base_angle,
            self.vertical_angle,
            self.volume,
            self.total_surface_area,
            self.curved_surface_area,
        )


class ConeFrustum:
    def __init__(
        self, lower_radius=None, upper_radius=None, height=None, slant_height=None
    ):
        if height == None:
            height = (slant_height ** 2 - (lower_radius - upper_radius) ** 2) ** 0.5

        elif slant_height == None:
            slant_height = (height ** 2 + (lower_radius - upper_radius) ** 2) ** 0.5

        elif lower_radius == None:
            lower_radius = max(
                quadratic(
                    1,
                    -2 * upper_radius,
                    -(slant_height ** 2) + height ** 2 + upper_radius ** 2,
                )
            )

        elif upper_radius == None:
            upper_radius = max(
                quadratic(
                    1,
                    -2 * lower_radius,
                    -(slant_height ** 2) + height ** 2 + lower_radius ** 2,
                )
            )

        if slant_height == ((lower_radius - upper_radius) ** 2 + height ** 2) ** 0.5:
            self.lower_radius = lower_radius
            self.upper_radius = upper_radius
            self.height = height
            self.slant_height = slant_height
            self.lower_diameter = 2 * lower_radius
            self.upper_diameter = 2 * upper_radius
            self.volume = ((pi * height) / 3) * (
                upper_radius ** 2 + upper_radius ** 2 + upper_radius * upper_radius
            )
            self.curved_surface_area = pi * (upper_radius + upper_radius) * slant_height
            self.total_surface_area = (
                self.curved_surface_area
                + (pi * upper_radius ** 2)
                + (pi * upper_radius ** 2)
            )
        else:
            raise ValueError(
                "The input values do not correspond to any single Frustum of Cone."
            )

    def __str__(self):
        return str_cone_frustum(
            self.lower_radius,
            self.upper_radius,
            self.lower_diameter,
            self.upper_diameter,
            self.height,
            self.slant_height,
            self.volume,
            self.total_surface_area,
            self.curved_surface_area,
        )


# c1 = Cube(2)
# c2 = Cuboid(2, 2, 2)
# c3 = Cylinder(6, 10)
# s = Sphere(4)
# h = Hemisphere(4)
# c = Cone(3, 4)
# f = ConeFrustum(7, 3, 3, 5)
# print(c1, c2, c3, s, h, c, f, sep='\n\n')