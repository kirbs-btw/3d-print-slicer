import numpy as np 
from stl import mesh
import pyvista as pv

class line:
    def __init__(self, v1, v2):
        self.supportV = [0, 0, 0]
        self.directionV = [0, 0, 0]
        self.lower_z_bound = 0
        self.upper_z_bound = 0
        self.pointA = v1
        self.pointB = v2
        self.calcV(v1, v2)
        
    def print(self):
        print("sV: \n{}".format(self.supportV))
        print("dV: \n{}".format(self.directionV))
        print("lb: \n{}".format(self.lower_z_bound))
        print("ub: \n{}".format(self.upper_z_bound))
        print("pA: \n{}".format(self.pointA))
        print("pB \n{}".format(self.pointB))
 

    def calcV(self, v1, v2):
        """
        calculates support 
        and directional vector for the line

        also determins the upper and lower bound of the 
        line to see if pointis is bewtween those
        """

        lower_x = v1[0]
        upper_x = v2[0]

        if lower_x > upper_x: 
            lower_x, upper_x = upper_x, lower_x

        lower_y = v1[1]
        upper_y = v2[1]

        if lower_y > upper_y: 
            lower_y, upper_y = upper_y, lower_y

        lower_z = v1[2]
        upper_z = v2[2]

        if lower_z > upper_z: 
            lower_z, upper_z = upper_z, lower_z
            v1, v2 = v2, v1

        x = v2[0] - v1[0]
        y = v2[1] - v1[1]
        z = v2[2] - v1[2]

        dirV = [x, y, z]
        supportV = v1
        self.supportV = supportV
        self.directionV = dirV
        self.lower_x_bound = lower_x
        self.upper_x_bound = upper_x
        self.lower_y_bound = lower_y
        self.upper_y_bound = upper_y
        self.lower_z_bound = lower_z
        self.upper_z_bound = upper_z
        
    
    def calcVfromH(self, h):
        """
        calculation be like

        sup.x3 + dir.x3 * v = h
        dir.x3 * v = h - sup.x3
        v = (h - sup.x3) / dir.x3   => dir.x3 != 0
        
        """
        if self.directionV[2] == 0:
            return None

        v = (h - self.supportV[2]) / self.directionV[2] 

        """
        placing v in equation
        """
        x3 = self.supportV[2] + self.directionV[2] * v

        # check if point is in between the original points 
        if not x3 > self.lower_z_bound or not x3 < self.upper_z_bound:
            return None
        
        x1 = self.supportV[0] + self.directionV[0] * v
        x2 = self.supportV[1] + self.directionV[1] * v
        
        return [x1, x2, x3]

def add_dim(stl_obj, x_dim, y_dim, z_dim):
    x_dim /= 2
    y_dim /= 2
    z_dim /= 2


    new_triangles = []

    for triangle in stl_obj.vectors:
        v1 = [triangle[0][0]*x_dim, triangle[0][1]*y_dim, triangle[0][2]*z_dim]
        v2 = [triangle[1][0]*x_dim, triangle[1][1]*y_dim, triangle[1][2]*z_dim]
        v3 = [triangle[2][0]*x_dim, triangle[2][1]*y_dim, triangle[2][2]*z_dim]
        new_triangles.append([v1, v2, v3])

    return new_triangles

def find_lower_value(points):
    x = points[0][0][0]
    y = points[0][0][1]
    z = points[0][0][2]

    for triangle in points:

        for vector in triangle:
            if x > vector[0]:
                x = vector[0]
            if y > vector[1]:
                y = vector[1]
            if z > vector[2]:
                z = vector[2]

    return x, y, z

def adding_lower_bound(points, x, y, z, offset=100):
    new_triangles = []

    for triangle in points:
        v1 = [triangle[0][0] - x + offset, triangle[0][1] - y + offset, triangle[0][2] - z]
        v2 = [triangle[1][0] - x + offset, triangle[1][1] - y + offset, triangle[1][2] - z]
        v3 = [triangle[2][0] - x + offset, triangle[2][1] - y + offset, triangle[2][2] - z]
        new_triangles.append([v1, v2, v3])

    return new_triangles

def nrml_points(points, offset):
    x, y, z = find_lower_value(points)
    points = adding_lower_bound(points, x, y, z, offset)

    return points

def create_lines(triangles):
    triangle_lines = []

    for triangle in triangles:
        face_lines = []
        lineOne = line(triangle[0], triangle[1])
        lineTwo = line(triangle[0], triangle[2])
        lineThree = line(triangle[1], triangle[2])
        face_lines.append(lineOne)
        face_lines.append(lineTwo)
        face_lines.append(lineThree)
        triangle_lines.append(face_lines)
    
    return triangle_lines

def slice_z(triangle_lines, layer_hight = 0.1, layer_count = 0):
    
    """
    slices the obj by inserting the hight inside the 
    line a param and calulating the points at this hight in the model

    issue:
        -edge case 
        if layer hits corner of tris there are 3 points from wich are two the same
        del the equal point   
    """
    points = []
    

    for layer_count in range(int(round(layer_count))):
        slice_hight = layer_count / (1 / layer_hight) # layerhight factor
        layer_points = []


        for tris in triangle_lines:
            tris_points = []
            for line in tris:
                point = line.calcVfromH(slice_hight)
                if point != None:
                    tris_points.append(point)
            
            if tris_points != []:
                layer_points.append(tris_points)
        
        if layer_points != []:
            points.append(layer_points)

    return points

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

"""
def sort_layer_pairs(layer_pairs):
    run_time = len(layer_pairs)
    layer_pairs_save = layer_pairs # saves unsorted state of layer_pairs to be changes later
    layer_sorted = [layer_pairs_save[0]] # sorted pairs
    layer_pairs_save.remove(layer_sorted[0])
    for _ in range(run_time):
        fitting = find_fitting_pair(layer_sorted[-1], layer_pairs_save)
        if fitting == None:
            continue
        fitting_pair = fitting[0]
        index_of_fitting_pair = fitting[1]
        layer_sorted.append(fitting_pair)
        layer_pairs_save.remove(layer_pairs_save[index_of_fitting_pair])

    return layer_sorted
"""

def sort_point_pairs(point_pairs):
    point_pairs_sorted = []
    
    for layer in point_pairs:
        point_pairs_sorted.append(sort_layer_pairs(layer))
    
    return point_pairs_sorted

def plane_pairs(pair_arr):
    new_arr = []
    for layer in pair_arr:
        new_layer = []
        for element in layer:
            new_element = []
            for pair in element:
                for point in pair:
                    new_element.append(point)
            new_layer.append(new_element)
        new_arr.append(new_layer)
    return new_arr


# Testing around with infill slicing 
def slice_infill(infill_points, point_pairs_sorted, layer_num):
    # create lines for wall at layer_num 
    layer_lines = []
    #structure will be [element[linesof element]] 
    
    for element in point_pairs_sorted[layer_num]:
        element_lines = []
        for pair in element: 
            element_lines.append(line(pair[0], pair[-1])
        layer_lines.append(element_lines)
    # slicing lines 
    # slicing with the x/y value of the wall line to get the point 
    
    # no creation of lines for infill 
    # using the points to slice in the wall lines 
    # --> new finding pos method in line class
    # 
    # only a solution for line that are inside the grid and not for lines that have an angle or are 
    # curves or honey comb
    


    


def get_points_from_stl(stl_obj, layer_hight=0.1, x_dim=1, y_dim=1, z_dim=1, offset=100):
    layer_count = z_dim / layer_hight

    triangles = add_dim(stl_obj, x_dim, y_dim, z_dim)
    triangles = nrml_points(triangles, offset)
    triangle_lines = create_lines(triangles)
    point_pairs = slice_z(triangle_lines, layer_hight, layer_count) # slice z returns only []
    point_pairs = sort_point_pairs(point_pairs)
    points = plane_pairs(point_pairs) # needs to be changes for multiple elements in one layer
    return points

def show_points(points):
    point_list = []
    for i in points:
        for j in i:
            point_list.append(j)

    point_cloud = pv.PolyData(point_list)
    point_cloud.plot(eye_dome_lighting=True)

def main():
    stl_file = 'F:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/cube.stl'
    # stl_file = 'F:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/tree.stl'
    obj = mesh.Mesh.from_file(stl_file)

    points = get_points_from_stl(obj, x_dim=100, y_dim=100, z_dim=100)
    show_points(points)


if __name__ == '__main__':
    main()
