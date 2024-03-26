# Standard Library Imports
from math import sin, cos, tan
from math import atan
from math import degrees, radians
from math import pi

# Local Application Imports
from helper import *
from printable_2d import *

class Square:
    def __init__(self, side):
        self.side = side
        self.area = side ** 2
        self.perimeter = 4 * side
        self.diagonal = 2 ** 0.5 * side

    def __str__(self):
        return str_square(self.side, self.area, self.perimeter, self.diagonal)

    @classmethod
    def from_area(cls, area):
        side = area ** 0.5
        return Square(side)

    @classmethod
    def from_perimeter(cls, perimeter):
        side = perimeter / 4
        return Square(side)

    @classmethod
    def from_diagonal(cls, diagonal):
        side = diagonal / (2 ** 0.5)
        return Square(side)


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = length * breadth
        self.perimeter = 2 * (length + breadth)
        self.diagonal = (length ** 2 + breadth ** 2) ** 0.5

    def __str__(self):
        return str_rectangle(
            self.length, self.breadth, self.area, self.perimeter, self.diagonal
        )

    @classmethod
    def from_length_area(cls, length, area):
        breadth = area / length
        return Rectangle(length, breadth)

    @classmethod
    def from_breadth_area(cls, breadth, area):
        length = area / breadth
        return Rectangle(length, breadth)

    @classmethod
    def from_length_perimeter(cls, length, perimeter):
        breadth = (perimeter / 2) - length
        return Rectangle(length, breadth)

    @classmethod
    def from_breadth_perimeter(cls, breadth, perimeter):
        length = (perimeter / 2) - breadth
        return Rectangle(length, breadth)

    @classmethod
    def from_length_diagonal(cls, length, diagonal):
        breadth = (diagonal ** 2 - length ** 2) ** 0.5
        return Rectangle(length, breadth)

    @classmethod
    def from_breadth_diagonal(cls, breadth, diagonal):
        length = (diagonal ** 2 - breadth ** 2) ** 0.5
        return Rectangle(length, breadth)

    @classmethod
    def from_area_perimeter(cls, area, perimeter):  # l**2 - (l+b)*l + (l*b)
        # Using max to get the positive value
        length = max(quadratic(1, -(perimeter / 2), area))
        breadth = area / length
        return Rectangle(length, breadth)


class Parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = base * height

    def __str__(self):
        return str_parallelogram(self.base, self.height, self.area)


class RhombusDiagonals:
    def __init__(self, diagonal_1, diagonal_2):
        self.diagonal_1 = diagonal_1
        self.diagonal_2 = diagonal_2

        self.side = (((diagonal_1 / 2) ** 2) + ((diagonal_2 / 2) ** 2)) ** 0.5
        self.area = round(0.5 * diagonal_1 * diagonal_2, 14)
        self.perimeter = 4 * self.side
        self.height = round(self.area / self.side, 14)

        (
            angle_a,
            angle_b,
            angle_c,
            angle_d,
        ) = quadrilateral_interior_angles_4sides_1diagonal(
            self.side, self.side, self.side, self.side, diagonal_ac=diagonal_1
        )
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c
        self.angle_d = angle_d

    def __str__(self):
        return str_rhombus_diagonals(
            self.diagonal_1,
            self.diagonal_2,
            self.area,
            self.perimeter,
            self.side,
            self.height,
            self.angle_a,
            self.angle_b,
            self.angle_c,
            self.angle_d,
        )

    @classmethod
    def from_area_diagonal(cls, area, diagonal1):
        diagonal2 = 2 * area / diagonal1
        return RhombusDiagonals(diagonal1, diagonal2)


class RhombusBaseHeight:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = base * height
        self.perimeter = 4 * base

    def __str__(self):
        return str_rhombus_base_height(
            self.base, self.height, self.area, self.perimeter
        )


class Trapezium:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height
        self.area = 0.5 * height * (base1 + base2)

    def __str__(self):
        return str_trapezium(self.base1, self.base2, self.height, self.area)


class TriangleBaseHeight:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.area = 0.5 * base * height

        # The following attributes can only bs defined if Triangle is Isosceles:
        self.side_a = None
        self.side_b = None
        self.side_c = None
        self.angle_a = None
        self.angle_b = None
        self.angle_c = None
        self.perimeter = None
        self.height_for_side_a = None
        self.height_for_side_b = None
        self.height_for_side_c = None

    def isosceles(self):
        # If Triangle is Isosceles:
        self.side_a = self.base
        self.side_b = ((self.base / 2) ** 2 + (self.height ** 2)) ** 0.5
        self.side_c = self.side_b

        angle_a, angle_b, angle_c = triangle_interior_angles_3sides(
            self.side_a, self.side_b, self.side_c
        )
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c

        self.side_type = "Isosceles"
        self.angle_type = "Acute"
        self.perimeter = self.side_a + self.side_b + self.side_c

        (
            height_for_side_a,
            height_for_side_b,
            height_for_side_c,
        ) = triangle_respective_heights(
            self.area, self.side_a, self.side_b, self.side_c
        )
        self.height_for_side_a = height_for_side_a
        self.height_for_side_b = height_for_side_b
        self.height_for_side_c = height_for_side_c

    def is_isosceles(self):
        return True if self.side_a is not None else False

    def __str__(self):
        if self.is_isosceles():
            return str_triangle_everything(
                self.area,
                self.perimeter,
                self.side_type,
                self.angle_type,
                self.side_a,
                self.side_b,
                self.side_c,
                self.angle_a,
                self.angle_b,
                self.angle_c,
                self.height_for_side_a,
                self.height_for_side_b,
                self.height_for_side_c,
            )
        else:
            return str_triangle_base_height(self.base, self.height, self.area)


class TriangleSAS:
    def __init__(self, side_a, side_b, angle_c):
        self.side_a = side_a
        self.side_b = side_b
        # Using Law of Cosines-> c^2 = a^2 + b^2 - 2ab.cosC:
        self.side_c = (
            side_a ** 2 + side_b ** 2 - 2 * side_a * side_b * (cos(radians(angle_c)))
        ) ** 0.5

        angle_a, angle_b, angle_c = triangle_interior_angles_3sides(
            self.side_a, self.side_b, self.side_c
        )
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c

        # Area = (a * b * sinC) / 2
        self.area = (side_a * side_b * sin(radians(angle_c))) / 2
        self.perimeter = self.side_a + self.side_b + self.side_c

        (
            height_for_side_a,
            height_for_side_b,
            height_for_side_c,
        ) = triangle_respective_heights(
            self.area, self.side_a, self.side_b, self.side_c
        )
        self.height_for_side_a = height_for_side_a
        self.height_for_side_b = height_for_side_b
        self.height_for_side_c = height_for_side_c

        self.side_type = triangle_side_type(self.side_a, self.side_b, self.side_c)
        self.angle_type = triangle_angle_type(self.angle_a, self.angle_b, self.angle_c)

    def __str__(self):
        return str_triangle_everything(
            self.area,
            self.perimeter,
            self.side_type,
            self.angle_type,
            self.side_a,
            self.side_b,
            self.side_c,
            self.angle_a,
            self.angle_b,
            self.angle_c,
            self.height_for_side_a,
            self.height_for_side_b,
            self.height_for_side_c,
        )


class TriangleEquilateral:
    def __init__(self, side):
        self.side = side
        self.area = (3 ** 0.5 / 4) * side ** 2
        self.perimeter = 3 * side
        self.angle_a = self.angle_b = self.angle_c = 60
        self.height = 2 * self.area / self.side

    def __str__(self):
        return str_triangle_equilateral(
            self.side, self.area, self.perimeter, self.height
        )


class TriangleHerons:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.perimeter = side_a + side_b + side_c

        s = (side_a + side_b + side_c) / 2  # SemiPerimeter
        self.area = (s * (s - side_a) * (s - side_b) * (s - side_c)) ** 0.5

        angle_a, angle_b, angle_c = triangle_interior_angles_3sides(
            self.side_a, self.side_b, self.side_c
        )
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c

        (
            height_for_side_a,
            height_for_side_b,
            height_for_side_c,
        ) = triangle_respective_heights(
            self.area, self.side_a, self.side_b, self.side_c
        )
        self.height_for_side_a = height_for_side_a
        self.height_for_side_b = height_for_side_b
        self.height_for_side_c = height_for_side_c

        self.side_type = triangle_side_type(self.side_a, self.side_b, self.side_c)
        self.angle_type = triangle_angle_type(self.angle_a, self.angle_b, self.angle_c)

    def __str__(self):
        return str_triangle_everything(
            self.area,
            self.perimeter,
            self.side_type,
            self.angle_type,
            self.side_a,
            self.side_b,
            self.side_c,
            self.angle_a,
            self.angle_b,
            self.angle_c,
            self.height_for_side_a,
            self.height_for_side_b,
            self.height_for_side_c,
        )


class TriangleCoordinates:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.side_a = distance(x2, y2, x3, y3)
        self.side_b = distance(x1, y1, x3, y3)
        self.side_c = distance(x1, y1, x2, y2)

        s = (self.side_a + self.side_b + self.side_c) / 2  # SemiPerimeter
        self.area = (
            s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)
        ) ** 0.5
        self.perimeter = self.side_a + self.side_b + self.side_c

        angle_a, angle_b, angle_c = triangle_interior_angles_3sides(
            self.side_a, self.side_b, self.side_c
        )
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c

        (
            height_for_side_a,
            height_for_side_b,
            height_for_side_c,
        ) = triangle_respective_heights(
            self.area, self.side_a, self.side_b, self.side_c
        )
        self.height_for_side_a = height_for_side_a
        self.height_for_side_b = height_for_side_b
        self.height_for_side_c = height_for_side_c

        self.side_type = triangle_side_type(self.side_a, self.side_b, self.side_c)
        self.angle_type = triangle_angle_type(self.angle_a, self.angle_b, self.angle_c)

    def __str__(self):
        return str_triangle_everything(
            self.area,
            self.perimeter,
            self.side_type,
            self.angle_type,
            self.side_a,
            self.side_b,
            self.side_c,
            self.angle_a,
            self.angle_b,
            self.angle_c,
            self.height_for_side_a,
            self.height_for_side_b,
            self.height_for_side_c,
        )


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = 2 * radius
        self.area = pi * radius ** 2
        self.circumference = 2 * pi * radius

    @classmethod
    def from_circumeference(cls, circumference):
        radius = circumference / (2 * pi)
        return Circle(radius)

    @classmethod
    def from_area(cls, area):
        radius = (area / pi) ** 0.5
        return Circle(radius)


class CircularSegment:
    def __init__(
        self,
        radius=None,
        angle=None,
        arc_length=None,
        apothem=None,
        sagitta=None,
        chord_length=None,
        area=None,
    ):
        self.radius = radius
        self.diamter = 2 * self.radius
        self.arc_length = circular_segment_arc_length(self.radius, angle, arc_length)
        self.angle = circular_segment_angle(
            self.radius, self.arc_length, apothem, chord_length, angle
        )
        self.area = circular_segment_area(
            self.radius,
            self.angle,
            self.arc_length,
            chord_length,
            apothem,
            sagitta,
            area,
        )
        self.apothem = circular_segment_apothem(
            self.radius, self.angle, chord_length, apothem
        )
        self.chord_length = circular_segment_chord_length(
            self.radius, self.angle, self.apothem, sagitta, chord_length
        )
        self.sagitta = circular_segment_sagitta(
            radius, self.angle, self.chord_length, self.apothem, sagitta
        )


# class CircularSector:

#     def __init__(self, radius=None, angle=None, arc_length=None, apothem=None, apothem=None, chord_length=None, area=None)
#         self.radius = radius
#         self.apothem = apothem
#         self.angle = circular_segment_angle(radius, arc_length, apothem, chord_length, angle)
#         self.area = circular_segment_area(radius, angle, arc_length, chord_length, apothem, apothem, area)
#         self.arc_length = circular_segment_arc_length(radius, angle, arc_length)
#         self.apothem = circular_segment_apothem(radius, angle, chord_length, apothem)
#         self.chord_length = circular_segment_chord_length(radius, angle, apothem, apothem, chord_length)


class KiteDiagonals:
    # Diagonal_1 is vertical Diagonal
    # Diagonal_2 is horizontal Diagonal

    def __init__(self, diagonal_1, diagonal_2):
        self.diagonal_1 = diagonal_1
        self.diagonal_2 = diagonal_2
        self.area = 0.5 * diagonal_1 * diagonal_2

    def __str__(self):
        return str_kite_diagonals(self.diagonal_1, self.diagonal_2, self.area)


class KiteConsecutiveSides:
    def __init__(self, side_a, side_b, angle_consecutive):
        self.side_a = side_a
        self.side_b = side_b

        self.area = side_a * side_b * sin(radians(angle_consecutive))
        self.perimeter = 2 * (side_a + side_b)
        self.diagonal_1 = (
            side_a ** 2
            + side_b ** 2
            - 2 * side_a * side_b * (cos(radians(angle_consecutive)))
        ) ** 0.5
        self.diagonal_2 = 2 * self.area / self.diagonal_1

        angle_c1, angle_a1, angle_d = triangle_interior_angles_3sides(
            self.side_a, self.side_b, self.diagonal_1
        )
        self.angle_a = angle_a1 * 2
        self.angle_b = angle_consecutive
        self.angle_c = angle_c1 * 2
        self.angle_d = angle_d

    def __str__(self):
        return str_kite_consecutive_sides(
            self.side_a,
            self.side_b,
            self.area,
            self.perimeter,
            self.diagonal_1,
            self.diagonal_2,
            self.angle_a,
            self.angle_b,
            self.angle_c,
            self.angle_d,
        )


class QuadrilateralCoordinates:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.side_ab = distance(x1, y1, x2, y2)
        self.side_bc = distance(x2, y2, x3, y3)
        self.side_cd = distance(x3, y3, x4, y4)
        self.side_da = distance(x4, y4, x1, y1)

        self.diagonal_ac = distance(x1, y1, x3, y3)
        self.diagonal_bd = distance(x2, y2, x4, y4)

        s_1 = (self.side_ab + self.side_bc + self.diagonal_ac) / 2  # SemiPerimeter_1
        area_1 = (
            s_1 * (s_1 - self.side_ab) * (s_1 - self.side_bc) * (s_1 - self.diagonal_ac)
        ) ** 0.5

        s_2 = (self.side_cd + self.side_da + self.diagonal_bd) / 2  # SemiPerimeter_2
        area_2 = (
            s_2 * (s_2 - self.side_cd) * (s_2 - self.side_da) * (s_2 - self.diagonal_bd)
        ) ** 0.5

        self.perimeter = self.side_ab + self.side_bc + self.side_cd + self.side_da
        self.area = area_1 + area_2

        (
            angle_a,
            angle_b,
            angle_c,
            angle_d,
        ) = quadrilateral_interior_angles_4sides_1diagonal(
            self.side_ab,
            self.side_bc,
            self.side_cd,
            self.side_da,
            self.diagonal_ac,
            self.diagonal_bd,
        )
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c
        self.angle_d = angle_d

        self.quad_type = quadrilateral_type(
            self.side_ab,
            self.side_bc,
            self.side_cd,
            self.side_da,
            self.diagonal_ac,
            self.diagonal_bd,
            area_1,
            area_2,
        )

    def __str__(self):
        return str_quadrilateral_coordinates(
            self.side_ab,
            self.side_bc,
            self.side_cd,
            self.side_da,
            self.area,
            self.perimeter,
            self.diagonal_ac,
            self.diagonal_bd,
            self.angle_a,
            self.angle_b,
            self.angle_c,
            self.angle_d,
            self.quad_type,
        )


class QuadrilateralDiagonalPerpendicular:
    def __init__(self, diagonal_1, diagonal_2, perpendicular_1, perpendicular_2):
        self.diagonal_1 = diagonal_1
        self.diagonal_2 = diagonal_2
        self.perpendicular_1 = perpendicular_1
        self.perpendicular_2 = perpendicular_2
        self.area = 0.5 * (diagonal_1 * perpendicular_1 + diagonal_2 * perpendicular_2)

    def __str__(self):
        return str_quadrilateral_diagonal_perpendicular(
            self.diagonal_1,
            self.diagonal_2,
            self.perpendicular_1,
            self.perpendicular_2,
            self.area,
        )


# c = CircularSegment(radius=5, arc_length=5*pi)
# print(c.angle)
# print(c.chord_length)
# print(c.apothem)
# print(c.sagitta)
# print(c.chord_length)
# k1 = KiteDiagonals(1, 2)
# k2 = KiteConsecutiveSides(3, 4, 90)
# q1 = QuadrilateralCoordinates(0, 0, 5, 0, 5, 5, 5, 0)
# q2 = QuadrilateralDiagonalPerpendicular(8, 8, 3, 3)
# print(k1, k2, q1, q2, sep='\n')

# TriangleASA
# class Hexagon:
#     def __init__(self):
#         self.area=1
#         self.perimeter

square = Square(5)
print(square.area)
