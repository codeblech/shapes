def str_square(side, area, perimeter, diagonal):
    return f"""Side: {side}
Area: {area}
Perimeter: {perimeter}
Diagonal: {diagonal}"""


def str_rectangle(length, breadth, area, perimeter, diagonal):
    return f"""Length: {length}
Breadth: {breadth}
Area: {area}
Perimeter: {perimeter}
Diagonal: {diagonal}"""


def str_parallelogram(base, height, area):
    return f"""Base: {base}
Height: {height}
Area: {area}"""


def str_rhombus_diagonals(diagonal_1, diagonal_2, area, perimeter, side, height, angle_a, angle_b, angle_c, angle_d):
    return f"""Diagonal1: {diagonal_1}
Diagonal2: {diagonal_2}
Area: {area}
Perimeter: {perimeter}
Side: {side}
Height: {height}
Interior Angles: ∠A: {angle_a}°   ∠B: {angle_b}°   ∠C: {angle_c}°   ∠D: {angle_d}°"""


def str_rhombus_base_height(base, height, area, perimeter):
    return f"""Side: {base}
Height: {height}
Area: {area}
Perimeter: {perimeter}"""


def str_trapezium(base1, base2, height, perimeter):
    return f"""Base1: {base1}
Base2: {base2}
Height: {height}
Perimeter: {perimeter}"""


def str_triangle_everything(area, perimeter, side_type, angle_type,
                            side_a, side_b, side_c,
                            angle_a, angle_b, angle_c,
                            height_for_side_a, height_for_side_b, height_for_side_c):

    return f"""
Area: {area}
Perimeter: {perimeter}
Type of Triangle(based on sides): {side_type}
Type of Triangle(based on angle): {angle_type}
Side a: {side_a}
Side b: {side_b}
Side c: {side_c}
Height For Side a: {height_for_side_a}
Height For Side b: {height_for_side_b}
Height For Side c: {height_for_side_c}
Interior Angles: ∠A: {angle_a}°   ∠B: {angle_b}°   ∠C: {angle_c}°"""


def str_triangle_base_height(base, height, area):
    return f"""Base: {base}
Height: {height}
Area: {area}"""


def str_triangle_equilateral(side, area, perimeter, height):
    return f"""Side: {side}
Area: {area}
Perimeter: {perimeter}
Heights: {height}
Interior Angles: 60°"""


def str_circle(radius, circumference, area):
    return f'''Radius: {radius}
Area(a): {area}
Circumference(c): {circumference}'''


def str_kite_diagonals(diagonal_1, diagonal_2, area):
    return f"""Diagonal1: {diagonal_1}
Diagonal2: {diagonal_2}
Area: {area}"""


def str_kite_consecutive_sides(side_a, side_b, area, perimeter, diagonal_1, diagonal_2, angle_a, angle_b, angle_c, angle_d):
    return f"""Side a: {side_a}
Side b: {side_b}
Side c: {side_b}
Side d: {side_a}
Area: {area}
Perimeter: {perimeter}
Diagonal1: {diagonal_1}
Diagonal2: {diagonal_2}
Interior Angles: ∠A: {angle_a}°   ∠B: {angle_b}°   ∠C: {angle_c}°   ∠D: {angle_d}°"""


def str_quadrilateral_coordinates(side_ab, side_bc, side_cd, side_da, area, perimeter, diagonal_ac, diagonal_bd, angle_a, angle_b, angle_c, angle_d, quad_type):
    return f"""Side AB: {side_ab}
Side BC: {side_bc}
Side CD: {side_cd}
Side DA: {side_da}
Area: {area}
Perimeter: {perimeter}
Diagonal AC: {diagonal_ac}
Diagonal BD: {diagonal_bd}
Interior Angles: ∠A: {angle_a}°   ∠B: {angle_b}°   ∠C: {angle_c}°   ∠D: {angle_d}°
Type Of Quadrilateral: {quad_type}"""


def str_quadrilateral_diagonal_perpendicular(diagonal_1, diagonal_2, perpendicular_1, perpendicular_2, area):
    return f"""Diagonal1: {diagonal_1}
Diagonal2: {diagonal_2}
Perpendicular1: {perpendicular_1}
Perpendicular2: {perpendicular_2}
Area: {area}"""
