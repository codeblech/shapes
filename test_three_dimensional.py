from three_dimensional import *
from random import randrange


def test():
    try:
        cube = Cube(randrange(0, 10))
    except ValueError as error:
        print(error, "Try changing your input values.")
    except ZeroDivisionError as error:
        print(error, "Try changing your input values.")
    try:
        cuboid = Cuboid(randrange(0, 10), randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, "Try changing your input values.")
    except ZeroDivisionError as error:
        print(error, "Try changing your input values.")
    try:
        cyl = Cylinder(randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, "Try changing your input values.")
    except ZeroDivisionError as error:
        print(error, "Try changing your input values.")
    try:
        cone = Cone(3, 4, 5)
    except ValueError as error:
        print(error, "Try changing your input values.")
    except ZeroDivisionError as error:
        print(error, "Try changing your input values.")
    try:
        frus = ConeFrustum(4, 12, 6, 10)
    except ValueError as error:
        print(error, "Try changing your input values.")
    except ZeroDivisionError as error:
        print(error, "Try changing your input values.")
    try:
        sphere = Sphere(randrange(0, 10))
    except ValueError as error:
        print(error, "Try changing your input values.")
    except ZeroDivisionError as error:
        print(error, "Try changing your input values.")
    try:
        hemi = Hemisphere(randrange(0, 10))
    except ValueError as error:
        print(error, "Try changing your input values.")
    except ZeroDivisionError as error:
        print(error, "Try changing your input values.")

    try:
        print(
            cube.diagonal,
            cube.volume,
            cube.total_surface_area,
            cube.curved_surface_area,
        )
    except NameError as error:
        print(error, "Try changing your input values.")
    print("\n")
    try:
        print(
            cuboid.volume,
            cuboid.diagonal,
            cuboid.total_surface_area,
            cuboid.curved_surface_area,
        )
    except NameError as error:
        print(error, "Try changing your input values.")
    print("\n")
    try:
        print(cyl.volume, cyl.diagonal, cyl.total_surface_area, cyl.curved_surface_area)
    except NameError as error:
        print(error, "Try changing your input values.")
    print("\n")
    try:
        print(
            cone.volume,
            cone.base_angle,
            cone.vertical_angle,
            cone.total_surface_area,
            cone.curved_surface_area,
        )
    except NameError as error:
        print(error, "Try changing your input values.")
    except AttributeError as error:
        print(error, "Try changing your input values.")
    print("\n")
    try:
        print(frus.volume, frus.total_surface_area, frus.curved_surface_area)
    except NameError as error:
        print(error, "Try changing your input values.")
    print("\n")
    try:
        print(sphere.volume, sphere.total_surface_area)
    except NameError as error:
        print(error, "Try changing your input values.")
        print("\n")
    try:
        print(hemi.volume, hemi.curved_surface_area, hemi.total_surface_area)
    except NameError as error:
        print(error, "Try changing your input values.")
    print("\n")


for i in range(100):
    test()