def str_cube(side, volume, diagonal, total_surface_area, curved_surface_area):
    return f"""Side: {side}
Volume: {volume}
Diagonal: {diagonal}
Total Surface Area: {total_surface_area}
Curved Surface Area: {curved_surface_area}"""


def str_cuboid(
    length, breadth, height, volume, diagonal, total_surface_area, curved_surface_area
):
    return f"""Length: {length}
Breadth: {breadth}
Height: {height}
Volume:{volume}
Diagonal: {diagonal}
Total Surface Area: {total_surface_area}
Curved Surface Area: {curved_surface_area}"""


def str_cylinder(
    radius, height, diagonal, volume, total_surface_area, curved_surface_area
):
    return f"""Radius: {radius}
Height: {height}
Diagonal: {diagonal}
Volume: {volume}
Total Surface Area: {total_surface_area}
Curved Surface Area: {curved_surface_area}"""


def str_sphere(radius, diameter, volume, total_surface_area):
    return f"""Radius: {radius}
Diameter: {diameter}
Volume: {volume}
Total Surface Area: {total_surface_area}"""


def str_hemisphere(radius, diameter, volume, total_surface_area, curved_surface_area):
    return f"""Radius: {radius}
Diameter: {diameter}
Volume: {volume}
Total Surface Area: {total_surface_area}
Curved Surface Area: {curved_surface_area}"""


def str_cone(
    radius,
    diameter,
    height,
    slant_height,
    base_angle,
    vertical_angle,
    volume,
    total_surface_area,
    curved_surface_area,
):
    return f"""Radius: {radius}
Diameter: {diameter}
Height: {height}
Slant Height: {slant_height}
Base Angle: {base_angle}
Vertical Angle: {vertical_angle}
Volume: {volume}
Total Surface Area: {total_surface_area}
Curved Surface Area: {curved_surface_area}"""


def str_cone_frustum(
    lower_radius,
    upper_radius,
    lower_diameter,
    upper_diameter,
    height,
    slant_height,
    volume,
    total_surface_area,
    curved_surface_area,
):
    return f"""Lower Radius: {lower_radius}
Upper Radius: {upper_radius}
Lower Diameter: {lower_diameter}
Upper Diameter: {upper_diameter}
Height: {height}
Slant Height: {slant_height}
Volume: {volume}
Total Surface Area: {total_surface_area}
Curved Surface Area: {curved_surface_area}"""
