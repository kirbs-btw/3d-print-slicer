import math
import numpy as np



def calc_dist_of_points(points, factor=1) -> list:
    dist_arr = []
    for layer in points:
        dist_layer = []
        for element in layer:
            dist_element = [0]
            for point_index in range(len(element)-1):
                # appends dist of next points with a factor 
                dist_element.append(dist(element[point_index], element[point_index + 1]) * factor) 
            dist_layer.append(dist_element)
        dist_arr.append(dist_layer)

    return dist_arr


def calc_fill(dist_arr) -> list:
    fill = []
    save = 0
    for layer in dist_arr:
        fill_layer = []
        for element in layer:
            fill_element = []
            for dist in element:
                fill_element.append(dist + save)
                save += dist
            fill_layer.append(fill_element)
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


def create_moves(points, fill):
    moves = []

    for layer_index, layer in enumerate(points):
        line = "G0 Z{}\n;LAYER:{}".format(points[layer_index][0][2], (layer_index + 1))
        moves.append(line)
        for element_index, element in enumerate(layer):
            
            # line = "" # z_hop code
            # moves.append(line)
            # this could work without much more gcode because of retraction in fill 
            # but z_hops would be nice to implement further down 
            
            for point_index, point in enumerate(element):
                line = "G1 X{} Y{} E{}".format(point[0], point[1], fill[layer_index][point_index])
                moves.append(line)

    return moves
    

def create_gcode_array(moves):

    with open('F:/Projekte/Projekte/Project 137/3d-print-slicer/gcode_parts/top_gcode.txt') as f:
        top = np.array(f.readlines())

    with open('F:/Projekte/Projekte/Project 137/3d-print-slicer/gcode_parts//end_gcode.txt') as f:
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