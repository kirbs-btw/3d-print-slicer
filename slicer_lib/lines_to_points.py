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

def points_are_equal(point_a, point_b):
    """
    checks is points are equal 
    function exists to match up lines in sort_pairs()
    """

    if point_a[0] != point_b[0]:
        return False
    if point_a[1] != point_b[1]:
        return False
    
    """
    not needed because we check only points that are on the same layer

    if point_a[2] == point_b[2]:
        return False
    """

    return True

def point_is_equal_nrml(pair_a, pair_b):
    return points_are_equal(pair_a[-1], pair_b[0])

def point_is_equal_swap(pair_a, pair_b):    
    return points_are_equal(pair_a[-1], pair_b[-1])

def find_fitting_pair(checking_pair, pair_list):
    for index, pair in enumerate(pair_list):
        if pair == [] or checking_pair == []:
            continue
        if point_is_equal_nrml(checking_pair, pair):
            return [pair, index]
        if point_is_equal_swap(checking_pair, pair):
            new_pair = [pair[1], pair[0]]
            return [new_pair, index]

def sort_layer_pairs(layer_pairs):
    layer_sorted = []

    layer_pairs_save = layer_pairs # saves unsorted state of layer_pairs to be changes later
    while layer_pairs_save != []: 
        run_time = len(layer_pairs_save)
        sorted_element = [layer_pairs_save[0]] # sorted pairs
        layer_pairs_save.remove(sorted_element[0])
        for _ in range(run_time):
            fitting = find_fitting_pair(sorted_element[-1], layer_pairs_save)
            if fitting == None:
                continue
            fitting_pair = fitting[0]
            index_of_fitting_pair = fitting[1]
            sorted_element.append(fitting_pair)
            layer_pairs_save.remove(layer_pairs_save[index_of_fitting_pair])
        layer_sorted.append(sorted_element)

    return layer_sorted

def sort_point_pairs(layer_point_pairs):
    point_pairs_sorted = []
    
    for layer in layer_point_pairs:
        point_pairs_sorted.append(sort_layer_pairs(layer))
    
    return point_pairs_sorted



def lines_to_points(line_triangles, layer_height, obj_z_height):
    layer_count = obj_z_height / layer_height

    # point pairs of obj outline 
    layer_point_pairs = slice_z(line_triangles, layer_height, layer_count)

