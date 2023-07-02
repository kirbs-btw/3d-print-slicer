from demopoints import test_points
import math

def gcode(points):
    for point in points:
        if point == "layer shift":
            # do layershift stuff
            pass
        else: 
            pass
            # do point print

def dist(point_a, point_b):
    x0 = point_a[0] - point_b[0]
    x1 = point_a[1] - point_b[1]
    x2 = point_a[2] - point_b[2]

    dist = math.sqrt(x0**2 + x1**2 + x2**2)
    return dist


def main():
    points = test_points.cube_points
    gcode(points)
    """
    order points - are orderd 
    order by nearest points
    
    """


if __name__ == '__main__':
    main()


