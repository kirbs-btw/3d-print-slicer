from Line import *
import numpy as np

def add_dimensions(triangles, obj_x_dim, obj_y_dim, obj_z_dim):
    
    new_triangles = []

    for triangle in triangles:
        v1 = [triangle[0][0]*obj_x_dim, triangle[0][1]*obj_y_dim, triangle[0][2]*obj_z_dim]
        v2 = [triangle[1][0]*obj_x_dim, triangle[1][1]*obj_y_dim, triangle[1][2]*obj_z_dim]
        v3 = [triangle[2][0]*obj_x_dim, triangle[2][1]*obj_y_dim, triangle[2][2]*obj_z_dim]
        new_triangles.append([v1, v2, v3])
    
    return new_triangles

def shift_triangles(triangles, x_offset, y_offset):
    new_triangles = []

    for triangle in triangles:
        v1 = [triangle[0][0] + x_offset, triangle[0][1] + y_offset, triangle[0][2]]
        v2 = [triangle[1][0] + x_offset, triangle[1][1] + y_offset, triangle[1][2]]
        v3 = [triangle[2][0] + x_offset, triangle[2][1] + y_offset, triangle[2][2]]
        new_triangles.append([v1, v2, v3])

    return new_triangles

def triangles_to_lines(triangles):
    line_triangles = []
    for triangle in triangles:
        line_a = ComplexLine(triangle[0], triangle[1])
        line_b = ComplexLine(triangle[0], triangle[2])
        line_c = ComplexLine(triangle[1], triangle[2])
    line_triangles.append([line_a, line_b, line_c])

    return line_triangles

def find_min_xyz(triangles):
    x = triangles[0][0][0]
    y = triangles[0][0][1]
    z = triangles[0][0][2]
    
    for triangle in triangles:
        if triangle[0] < x: x = triangle[0]
        if triangle[1] < y: y = triangle[1]
        if triangle[2] < z: z = triangle[2]
        
    return x, y, z

def normal_points(triangles):
    x, y, z = find_min_xyz(triangles)
    new_triangles = []
    for triangle in triangles:
        new_triangle = []
        for vector in triangle:
            new_v = [vector[0]-x, vector[1]-y, vector[2]-y]
            new_triangle.append(new_v)
        new_triangles.append(new_triangle)

    return new_triangles

def get_points_from_stl(stl_obj, obj_x_dim = 10, obj_y_dim = 10, obj_z_dim = 10, x_plate_offset = 10, y_plate_offset = 10):
    # stl obj stores sets of 3 point that form a triangle
    point_triangles = stl_obj.vectors
    # normal points - pushing the points into positiv space
    point_triangles = normal_points(point_triangles)
    # adding dimensions to the stl_points
    point_triangles = add_dimensions(point_triangles, obj_x_dim, obj_y_dim, obj_z_dim)
    # shifting the points on the x and y axis 
    point_triangles = shift_triangles(point_triangles, x_plate_offset, y_plate_offset)
    # converting the three points to three lines to draw the triangle
    line_triangles = triangles_to_lines(point_triangles)

    return line_triangles