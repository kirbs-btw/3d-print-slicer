import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# point cloud graphing
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

        h
        sup.x3 + dir.x3 * v = h
        dir.x3 * v = h - sup.x3
        v = (h / sup.x3) / dir.x3 => dir.x3 != 0
        
        """
        if self.directionV[2] == 0:
            return None


        v = (h / self.supportV[2]) / self.directionV[2] 

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

def create_line(mesh):
    # array to hold all conections between triangles
    lines = []

    # creates the conecting lines between the triangles of the mesh
    for triangle in mesh.vectors:
        lineOne = line(triangle[0], triangle[1])
        lineTwo = line(triangle[0], triangle[2])
        lineThree = line(triangle[1], triangle[2])
        lines.append(lineOne)
        lines.append(lineTwo)
        lines.append(lineThree)

    return lines

def slice_z(lines):
    points = []


    for layer_hight in range(10):
        layer_hight = (layer_hight / 10)
        print(layer_hight)
        for line in lines:
            point = line.calcVfromH(layer_hight)
            if point != None: 
                points.append(point)
    
    return points


def show_points(points):
    print("GRAPHING POINTS...")
    point_cloud = pv.PolyData(points)
    point_cloud.plot(eye_dome_lighting=True)
    
# way to slow 
"""
def graph_points(points):
    print("GRAPHING POINTS...")
    fig = pyplot.figure()
    ax = fig.add_subplot(projection='3d')

    for i in points:    
        ax.scatter(i[0], i[1], i[2])

    pyplot.show()
"""

def main():
    # stl_file = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/cube.stl'
    stl_file = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/tree.stl'
    cube = mesh.Mesh.from_file(stl_file)
    lines = create_line(cube)
    points = slice_z(lines)
    show_points(points)
    """
    missing the optimisation 
    """


if __name__ == "__main__":
    main()
