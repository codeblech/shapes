from two_dimensional import *
from random import randrange


def test():
    try:
        s = Square(randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        r = Rectangle(randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        p = Parallelogram(randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        rd = RhombusDiagonals(randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        rbh = RhombusBaseHeight(randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        tp = Trapezium(randrange(0, 10), randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        tbh = TriangleBaseHeight(0, 0)
        tbh.isosceles()
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        tsas = TriangleSAS(randrange(0, 10), randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        teq = TriangleEquilateral(randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        th = TriangleHerons(randrange(0, 10), randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        tc = TriangleCoordinates(randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10),
                                 randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        c = Circle(randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        kd = KiteDiagonals(randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        kcs = KiteConsecutiveSides(randrange(0, 10), randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        qc = QuadrilateralCoordinates(randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10),
                                      randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')
    try:
        qdp = QuadrilateralDiagonalPerpendicular(randrange(0, 10), randrange(0, 10), randrange(0, 10), randrange(0, 10))
    except ValueError as error:
        print(error, 'Try changing your input values.')
    except ZeroDivisionError as error:
        print(error, 'Try changing your input values.')










    try:
        print(s.area, s.perimeter, s.diagonal)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(r.area, r.diagonal, r.perimeter)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(p.area)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(rd.area, rd.perimeter, rd.height, rd.angle_a, rd.angle_b, rd.angle_c, rd.angle_d)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(rbh.area, rbh.perimeter)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(tp.area)
    except NameError as error:
        print(error, 'Try changing your input values.')
        print("\n")
    try:
        print(tbh.side_a, tbh.side_b, tbh.side_c, tbh.angle_a, tbh.angle_b, tbh.angle_c)
    except NameError as error:
        print(error, 'Try changing your input values.')

    try:
        print(tbh.angle_a, tbh.angle_b, tbh.angle_c, tbh.height_for_side_a, tbh.height_for_side_b, tbh.height_for_side_c,
              tbh.area, tbh.perimeter)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(tsas.angle_a, tsas.angle_b, tsas.angle_c, tsas.height_for_side_a, tsas.height_for_side_b, tsas.height_for_side_c,
              tsas.area, tsas.perimeter, tsas.angle_type, tsas.side_type)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(teq.area, teq.perimeter, teq.height)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(th.angle_a, th.angle_b, th.angle_c, th.height_for_side_a, th.height_for_side_b, th.height_for_side_c,
              th.area, th.perimeter, th.angle_type, th.side_type)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(c.area, c.circumference)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(kd.area)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(kcs.area, kcs.perimeter, kcs.angle_a, kcs.angle_b, kcs.angle_c, kcs.diagonal_1, kcs.diagonal_2)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(qc.area, qc.perimeter, qc.angle_a, qc.angle_b, qc.angle_c, qc.angle_d, qc.diagonal_bd, qc.diagonal_ac, qc.quad_type)
    except NameError as error:
        print(error, 'Try changing your input values.')
    print("\n")
    try:
        print(qdp.area)
    except NameError as error:
        print(error, 'Try changing your input values.')


for i in range(1000):
    test()