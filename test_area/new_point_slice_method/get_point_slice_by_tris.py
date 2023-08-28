import numpy as np 
from stl import mesh
import pyvista as pv

class line:
    def __init__(self, v1, v2):
        self.supportV, self.directionV, self.lower_bound, self.upper_bound = self.calcV(v1, v2)
        

    def calcV(self, v1, v2):
        """
        calculates support 
        and directional vector for the line

        also determins the upper and lower bound of the 
        line to see if pointis is bewtween those
        
        """
        lower = v1[2]
        upper = v2[2]

        if lower > upper: 
            lower, upper = upper, lower
            v1, v2 = v2, v1

        x = v2[0] - v1[0]
        y = v2[1] - v1[1]
        z = v2[2] - v1[2]

        dirV = [x, y, z]
        supportV = v1
        return supportV, dirV, lower, upper
    
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
        if not x3 > self.lower_bound or not x3 < self.upper_bound:
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
                    layer_points.append(tris_points)
            if tris_points != []:
                layer_points.append(tris_points)
        points.append(layer_points)
        
    return points

def points_are_equal(point_a, point_b):
    """
    checks is points are equal 
    function exists to match up lines in sort_pairs()
    """

    if point_a[0] == point_b[0]:
        return False
    if point_a[1] == point_b[1]:
        return False
    
    """
    not needed because we check only points that are on the same layer

    if point_a[2] == point_b[2]:
        return False
    """

    return True

def sort_pairs(point_pairs):
    """
    compart/match logic

    exp.:
        [24, 12]
        [3, 24]
        [3, 12]

        -> 24, 12, 12, 3, 3, 24
    
    if there is only one loop and not multiple elements
    for layer in point_pairs:
        new_layer_points = [layer[0]]
        while layer != []:
            checking_element = new_layer_points[-1] 
            for every pair (exept used ones) in layer:
                check for equal part in pair
                    new_layer_points.append(pair)

        reformating new_layer_points to normal plane list of points 

    """



    points = []
    for layer in point_pairs:
        pass



def get_points_from_stl(stl_obj, layer_hight=0.1, x_dim=1, y_dim=1, z_dim=1, offset=100):
    layer_count = z_dim / layer_hight

    triangles = add_dim(stl_obj, x_dim, y_dim, z_dim)
    triangles = nrml_points(triangles, offset)
    triangle_lines = create_lines(triangles)
    point_pairs = slice_z(triangle_lines, layer_hight, layer_count)
    points = sort_pairs(point_pairs)
    return points
  
def show_points(points):
    point_list = []
    for i in points:
        for j in i:
            point_list.append(j)

    point_cloud = pv.PolyData(point_list)
    point_cloud.plot(eye_dome_lighting=True)

def main():
    stl_file = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/cube.stl'
    obj = mesh.Mesh.from_file(stl_file)

    points = get_points_from_stl(obj, x_dim=100, y_dim=100, z_dim=100)
    print("the points{}".format(points))
    show_points(points)


if __name__ == '__main__':
    main()