import numpy as np
from Line import *

def slice_z(line_triangles, layer_height, layer_count_z):
    layer_point_pairs = []

    for layer_num in range(int(round(layer_count_z))):
        # height at wich we are slicing the current layer
        slice_height = layer_num * layer_height
        # stores the pairs of the triangle from slicing at slice_height
        layer_points = []

        for triangle in line_triangles:
            # the triangle gets sliced at the slice_hight 
            # a triangle crossing a line always has two points
            triangle_points = []
            for line in triangle:
                point = line.calcVfromZ(slice_height)
                if point != None:
                    triangle_points.append(point)
            if triangle_points != []:
                layer_points.append(triangle_points)

        # stops the slicing process when the obj ends
        # floating obj could be a problem
        if layer_points == []:
            continue
        
        # triangle point pairs at layeres unsorted
        # this process is done to later trace the right 
        # path for the print
        # the stored pairs construct the walls of the obj 
        # NO infill NO to or bottom fill
        layer_point_pairs.append(layer_points)


    return layer_point_pairs
    


def lines_to_points(line_triangles, layer_height, obj_z_height):
    layer_count = obj_z_height / layer_height

    # point pairs of obj outline 
    layer_point_pairs = slice_z(line_triangles, layer_height, layer_count)

