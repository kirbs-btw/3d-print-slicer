import math
import numpy as np

"""
issue: 
skipping 0.1mm hight 

"""

def calc_dist_of_points(points, factor=1) -> list:
    dist_arr = []
    for layer in points:
        dist_layer = [0]
        for point_index in range(len(layer)-1):
            # appends dist of next points with a factor 
            dist_layer.append(dist(layer[point_index], layer[point_index + 1]) * factor) 

        dist_arr.append(dist_layer)


    return dist_arr


def calc_fill(dist_arr) -> list:
    fill = []
    save = 0
    for layer in dist_arr:
        fill_layer = []
        for dist in layer:
            fill_layer.append(dist + save)
            save += dist
        fill.append(fill_layer)

    return fill

def calc_extrusion(points, fac = 1):
    dist_arr = calc_dist_of_points(points, factor = fac)
    extrusion = calc_fill(dist_arr)

    return extrusion

def dist(point_a, point_b) -> float:
    """
    calc dist of point_a to point_b in z plane
    """

    x0 = point_a[0] - point_b[0]
    x1 = point_a[1] - point_b[1]

    dist = math.sqrt(x0**2 + x1**2)

    return dist

def order_by_dist(points):
    """
    dist form fist point to rest finding the nearest 
    repeat from this one 
    """
    new_points = []


    for layer in points:
        new_layer = [layer[0]]
        for i in range(len(layer)-1):
            layer.remove(new_layer[i])

            nearest_dist, index_of_nearest = dist(new_layer[i], layer[0]), 0
            for index_of_point, point in enumerate(layer):
                this_dist = dist(new_layer[i], point)
                if nearest_dist > this_dist:
                    index_of_nearest = index_of_point
                    nearest_dist = this_dist

            new_layer.append(layer[index_of_nearest])
        new_points.append(new_layer)
    
    return new_points

def create_moves(points, fill):
    moves = []

    for layer_index, layer in enumerate(points):
        line = "G0 Z{}\n;LAYER:{}".format(points[layer_index][0][2], (layer_index + 1))
        moves.append(line)
        for point_index, point in enumerate(layer):
            line = "G1 X{} Y{} E{}".format(point[0], point[1], fill[layer_index][point_index])
            moves.append(line)

    return moves
    
"""
def create_moves(points, fill):
    extrusion = fill
    moves = []
    moves.append("G0 Z0")
    
    for layer_index, layer in enumerate(points):
        for point_index, point in enumerate(layer):
            
            line = "G1 X{} Y{} E{}".format(point[0], point[1], extrusion[layer_index][point_index])
            moves.append(line)
        
        if layer_index + 1 < (len(points) - 1):
            line = "G0 Z{}\n;LAYER:{}".format(points[layer_index+1][0][2], (layer_index + 1))
            moves.append(line)

    return move
"""
    

def create_gcode_array(moves):

    with open('H:/Projekte/Projekte/Project 137/3d-print-slicer/test_area/slicer_pieces/creating_gcode/top_gcode.txt') as f:
        top = np.array(f.readlines())

    with open('H:/Projekte/Projekte/Project 137/3d-print-slicer/test_area/slicer_pieces/creating_gcode/end_gcode.txt') as f:
        end = np.array(f.readlines())
    
    gcode_array = []

    for line in top:
        gcode_array.append(line)
    for line in moves:
        gcode_array.append(line)
    for line in end:
        gcode_array.append(line)

    return gcode_array


def create_gcode(points = []):
    # points = points[::-1]
    extrusion = calc_extrusion(points, fac = 0.1)
    moves = create_moves(points, extrusion)
    gcode_array = create_gcode_array(moves)

    return gcode_array