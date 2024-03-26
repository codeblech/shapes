from math import asin, acos, atan
from math import sin, cos, tan
from math import degrees, radians
from math import pi


def quadratic(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    helperer = (-b + discriminant ** 0.5) / (2 * a)
    sol2 = (-b - discriminant ** 0.5) / (2 * a)
    return helperer, sol2


def distance(x1, y1, x2, y2):
    distance_ = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance_


def triangle_respective_heights(area, side_a, side_b, side_c):
    height_for_side_a = 2 * area / side_a
    height_for_side_b = 2 * area / side_b
    height_for_side_c = 2 * area / side_c
    return height_for_side_a, height_for_side_b, height_for_side_c


def triangle_interior_angles_3sides(side_a, side_b, side_c):
    angle_a = round(degrees(acos((side_b ** 2 + side_c ** 2 - side_a ** 2) / (2 * side_b * side_c))), 13)
    angle_b = round(degrees(acos((side_a ** 2 + side_c ** 2 - side_b ** 2) / (2 * side_a * side_c))), 13)
    angle_c = 180 - (angle_a + angle_b)

    return angle_a, angle_b, angle_c


def triangle_side_type(side_a, side_b, side_c):
    # Check for Triangle Type based on Sides
    if side_a == side_b == side_c:
        side_type = 'Equilateral'

    elif (side_a == side_b) or (side_b == side_c) or (side_a == side_c):
        side_type = 'Isosceles'

    else:
        side_type = 'Scalene'

    return side_type


def triangle_angle_type(angle_a, angle_b, angle_c):
    # Check for Triangle Type based on Angles
    if angle_a < 90 and angle_b < 90 and angle_c < 90:
        angle_type = 'Acute'

    elif angle_a == 90 or angle_b == 90 or angle_b == 90:
        angle_type = 'Right'

    elif angle_a == 180 or angle_b == 180 or angle_c == 180:
        angle_type = 'StraightLine'

    else:
        angle_type = 'Obtuse'

    return angle_type


def quadrilateral_type(side_ab, side_bc, side_cd, side_da, diagonal_ac, diagonal_bd, area_1, area_2):
    if (side_ab == side_cd) and (side_bc == side_da):
        quad_type = "Parallelogram"

        if diagonal_ac == diagonal_bd:
            quad_type = "Rectangle"

        if (side_ab == side_bc) == (side_cd == side_da):
            quad_type = "Rhombus"

            if diagonal_ac == diagonal_bd:
                quad_type = "Square"

    elif (side_ab == side_bc and side_cd == side_da) or (side_bc == side_cd and side_da == side_ab):
        quad_type = "Kite"

    else:

        if area_1 == 0 or area_2 == 0:
            quad_type = "Not Quadrilateral"

        else:
            quad_type = "Simple Quadrilateral"

    return quad_type


def quadrilateral_interior_angles_4sides_1diagonal(side_ab, side_bc, side_cd, side_da, diagonal_ac=None,
                                                   diagonal_bd=None):
    # Diagonal divides the quadrilateral in two triangles. Law of Cosines can be applied on both triangles.
    if diagonal_ac is not None:
        triangle_1_angle_c1, triangle_1_angle_a1, triangle_1_angle_b = triangle_interior_angles_3sides(side_ab, side_bc,
                                                                                                       diagonal_ac)

        triangle_2_angle_a2, triangle_2_angle_c2, triangle_2_angle_d = triangle_interior_angles_3sides(side_cd, side_da,
                                                                                                       diagonal_ac)

        angle_a = round(triangle_1_angle_a1 + triangle_2_angle_a2, 13)
        angle_b = round(triangle_1_angle_b, 13)
        angle_c = round(triangle_1_angle_c1 + triangle_2_angle_c2, 13)
        angle_d = 360 - (angle_a + angle_b + angle_c)

    elif diagonal_bd is not None:
        triangle_1_angle_b1, triangle_1_angle_d1, triangle_1_angle_a = triangle_interior_angles_3sides(side_da, side_ab,
                                                                                                       diagonal_bd)

        triangle_2_angle_d2, triangle_2_angle_b2, triangle_2_angle_c = triangle_interior_angles_3sides(side_bc, side_cd,
                                                                                                       diagonal_bd)

        angle_a = round(triangle_1_angle_a, 13)
        angle_b = round(triangle_1_angle_b1 + triangle_2_angle_b2, 13)
        angle_c = round(triangle_2_angle_c, 13)
        angle_d = 360 - (angle_a + angle_b + angle_c)
    else:
        angle_a = None
        angle_b = None
        angle_c = None
        angle_d = None

    return angle_a, angle_b, angle_c, angle_d


# def circular_segment_radius():



def circular_segment_chord_length(radius=None, angle=None, apothem=None, sagitta=None, chord_length=None):
    if chord_length != None:
        return chord_length
    try:
        chord_length = 2 * apothem * round(tan(radians(angle / 2)))
    except TypeError:
        try:
            chord_length = 2 * (radius ** 2 - apothem ** 2) ** 0.5
        except TypeError:
            try:
                chord_length = 2 * radius * round(sin(radians(angle / 2)))
            except TypeError:
                chord_length = 2 * (sagitta * (2 * radius - sagitta)) ** 0.5

    return chord_length


def circular_segment_arc_length(radius, angle, arc_length=None):
    if arc_length != None:
        return arc_length
    arc_length = 2 * pi * radius * (angle / 360)

    return arc_length

# r-> apothem, h-> apothem

def circular_segment_apothem(radius=None, angle=None, chord_length=None, apothem=None):
    if apothem != None:
        return apothem
    try:
        apothem = radius * round(cos(radians(angle / 2)))
    except TypeError:
        try:
            apothem = 0.5 * chord_length / round(tan(radians(angle / 2)), 14)
        except TypeError:
            apothem = 0.5 * (4 * radius ** 2 - chord_length ** 2) ** 0.5

    return apothem


def circular_segment_angle(radius=None, arc_length=None, apothem=None, chord_length=None, angle=None):
    if angle != None:
        return angle
    try:
        angle = degrees(arc_length / radius)
    except TypeError:
        try:
            angle = degrees(2 * round(acos(apothem / radius)))
        except TypeError:
            try:
                angle = degrees(2 * round(atan(chord_length / (2 * apothem))))
            except TypeError:
                angle = degrees(2 * round(asin(chord_length / (2 * radius))))

    return angle


def circular_segment_area(radius, angle=None, arc_length=None, chord_length=None, apothem=None, sagitta=None, area=None):
    if area != None:
        return area
    try:
        area = pi * radius ** 2 * (angle / 360)
    except TypeError:
        try:
            area = 0.5 * (radius * arc_length - chord_length * apothem)
        except TypeError:
            try:
                area = radius ** 2 * round(acos(apothem / radius) - apothem * (radius ** 2 - apothem ** 2) ** 0.5)
            except:
                area = radius ** 2 * round(acos((radius - sagitta) / radius) - (radius - sagitta) * (2 * radius * sagitta - sagitta ** 2) ** 0.5)

    return area


def circular_segment_sagitta(radius=None, angle=None, chord_length=None, apothem=None, sagitta=None):
    if sagitta != None:
        return sagitta
    try:
        sagitta = radius - apothem
    except TypeError:
        try:
            sagitta = max(quadratic(apothem ** 2, -2 * radius, (chord_length / 2) ** 2))
        except TypeError:
            sagitta = radius - (radius ** 2 - (chord_length / 2) ** 2) ** 0.5


def circular_segment_initialiser(radius=None, angle=None, arc_length=None, apothem=None, sagitta=None, chord_length=None, area=None):
    non_none_attributes = {}
    for i in range(10):
        try:
            diamter = 2 * radius
        except TypeError:
            angle = circular_segment_angle(radius, arc_length, apothem, chord_length, angle)
        except TypeError:
            area = circular_segment_area(radius, angle, arc_length, chord_length, apothem, sagitta, area)
        except TypeError:
            arc_length = circular_segment_arc_length(radius, angle, arc_length)
        except TypeError:
            apothem = circular_segment_apothem(radius, angle, chord_length, apothem)
        except TypeError:
            chord_length = circular_segment_chord_length(radius, angle, apothem, sagitta, chord_length)
        except TypeError:
            sagitta = circular_segment_sagitta(radius, angle, chord_length, apothem, sagitta)
        except TypeError:
            attributes = [radius, diamter, angle, area, arc_length, apothem, chord_length, sagitta]


            for attribute in attributes:
                if attribute is not None:
                    non_none_attributes[str(attribute)] = attribute
                    attributes.remove(attribute)
    return non_none_attributes
    # for i in range(10):
    #     try:
    #         radius = radius
    #         diamter = 2 * radius
    #         angle = circular_segment_angle(radius, arc_length, apothem, chord_length, angle)
    #         area = circular_segment_area(radius, angle, arc_length, chord_length, apothem, sagitta, area)
    #         arc_length = circular_segment_arc_length(radius, angle, arc_length)
    #         apothem = circular_segment_apothem(radius, angle, chord_length, apothem)
    #         chord_length = circular_segment_chord_length(radius, angle, apothem, sagitta, chord_length)
    #         sagitta = circular_segment_sagitta(radius, angle, chord_length, apothem, sagitta)
    #     except TypeError as error:
    #         return error


    #         attributes = [radius, diamter, angle, area, arc_length, apothem, chord_length, sagitta]
    #         non_none_attributes = {}
    #         for attribute in attributes:
    #             if attribute is not None:
    #                 non_none_attributes[str(attribute)] = attribute
    #                 attributes.remove(attribute)
    #     except TypeError:
    #         continue
    # return non_none_attributes
# {'radius': radius, 'diameter': diamter, 'angle': angle, 'area': area, 'arc_length': arc_length,
#            'apothem': apothem, 'chord_length': chord_length, 'sagitta': sagitta}

def circular_sector_chord_length():
    pass


def circular_sector_arc_length():
    pass


def circular_sector_apothem():
    pass


def circular_sector_angle():
    pass


def circular_sector_area():
    pass
