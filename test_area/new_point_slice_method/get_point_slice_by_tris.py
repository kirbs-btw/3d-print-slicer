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

def get_points_from_stl(stl_obj, layer_hight=0.1, x_dim=1, y_dim=1, z_dim=1, offset=100):
    layer_count = z_dim / layer_hight

    triangles = add_dim(stl_obj, x_dim, y_dim, z_dim)
    triangles = nrml_points(triangles, offset)
    
    """
    lines = create_line(triangles)
    lines = del_redundant(lines)
    points = slice_z(lines, layer_hight, layer_count)

    return points
    """
  
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