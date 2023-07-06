from demopoints import test_points
import math

def gcode(points):
    for layer in points:
        for point in layer:
            pass

def calc_dist_of_points(points):
    dist_arr = []
    for i, layer in enumerate(points):
        layer_dist = []
        for j in range(len(layer)-2):
            dist_var = dist(points[i][j], points[i][j+1])
            layer_dist.append(dist_var)
        layer_dist.append(dist(points[i][-1], points[i][0]))
        dist_arr.append(layer_dist)
    return dist_arr


def dist(point_a, point_b):
    x0 = point_a[0] - point_b[0]
    x1 = point_a[1] - point_b[1]
    x2 = point_a[2] - point_b[2]

    dist = math.sqrt(x0**2 + x1**2 + x2**2)
    return dist

def print_points(points):
    for i in points:
        print(i)

def main():
    points = test_points.cube_points
    print_points(calc_dist_of_points(points))
    gcode(points)
    """
    order points - are orderd 
    order by nearest points
    
    """


if __name__ == '__main__':
    main()


