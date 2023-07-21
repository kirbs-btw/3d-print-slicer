from demopoints import test_points
import math


def calc_dist_of_points(points):
    dist_arr = []
    for i, layer in enumerate(points):
        layer_dist = []
        for j in range(len(layer)-2):
            dist_var = dist(points[i][j], points[i][j+1])
            layer_dist.append(round(dist_var, 5))
        layer_dist.append(dist(points[i][-1], points[i][0]))
        dist_arr.append(layer_dist)
    return dist_arr

def find_lower_value(points):
    x, y, z = points[0][0][0], points[0][0][1], points[0][0][2]
    for layer in points:
        for point in layer:
            if point[0] < x:
                x = point[0]
            if point[1] < y:
                y = point[1]
            if point[2] < z:
                z = point[2]
 

    return x, y, z

def adding_lower_bound(points, x, y, z):
    new_points = []
    for layer in points:
        new_layer = []
        for point in layer:
            x1 = point[0] - x
            x2 = point[1] - y
            x3 = point[2] - z
            

            new_point = [x1, x2, x3]
            new_layer.append(new_point)

        new_points.append(new_layer)
    
    return new_points

def nrml_points(points):
    points = []

    x, y, z = find_lower_value(points)
    adding_lower_bound(points, x, y, z)



    new_points = []

    return new_points


def dist(point_a, point_b):
    x0 = point_a[0] - point_b[0]
    x1 = point_a[1] - point_b[1]
    x2 = point_a[2] - point_b[2]

    dist = math.sqrt(x0**2 + x1**2 + x2**2)

    return dist

def create_moves(points, fill):
    extrusion = fill
    moves = []
    moves.append("G0 Z0")
    
    for layer_index, layer in enumerate(points):
        for point_index, point in enumerate(layer):
            line = "G1 X{} Y{} E{}".format(point[0], point[1], extrusion[0][0])
            # list index out of range bug 
            
            # line = "G1 X{} Y{} E{}".format(point[0], point[1], extrusion[layer_index][point_index])
            moves.append(line)
        
        if layer_index + 1 < (len(points) - 1):
            line = "G0 Z{}\n;LAYER:{}".format(points[layer_index+1][0][2], (layer_index + 1))
            moves.append(line)

    return moves

def create_file(moves):

    with open('F:/Projekte/Projekte/Project 137/3d-print-slicer/test_area/slicer_pieces/creating_gcode/top_gcode.txt') as f:
        top = f.readlines()

    with open('F:/Projekte/Projekte/Project 137/3d-print-slicer/test_area/slicer_pieces/creating_gcode/end_gcode.txt') as f:
        end = f.readlines()

    file = open('F:/Projekte/Projekte/Project 137/3d-print-slicer/test_area/slicer_pieces/creating_gcode/gcode.gcode', 'w+')

    for char in top:
        file.write(char)

    for char in moves:
        file.write('\n{}'.format(char))

    for char in end:
        file.write(char)


def main():
    points = test_points.cube_points
    x, y, z = find_lower_value(points)
    points = adding_lower_bound(points, x, y, z)

    fill = calc_dist_of_points(points)

    moves = create_moves(points, fill)
    
    # generates gcode
    create_file(moves)



if __name__ == '__main__':
    main()


