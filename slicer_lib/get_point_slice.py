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

        sup.x3 + dir.x3 * v = h
        dir.x3 * v = h - sup.x3
        v = (h / sup.x3) / dir.x3   => dir.x3 != 0
        
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

def lines_are_the_same(lineA, lineB):


    if lineA.supportV == lineB.supportV and lineA.directionV == lineB.directionV:
        return True
    elif True:
        """
        condition for lines that are the same
        """
        pass
        


    return False

def del_duplicate(lines):
    """
    deletes the duplicate lines
    stl saves points duplicate
    """

    new_lines = []

    for line in lines: 
        switch = False
        for saved_line in new_lines:
            if lines_are_the_same(saved_line, line):
                switch = True
                
        if not switch:
            new_lines.append(line)

    return new_lines

def slice_z(lines):
    """
    slices the obj by inserting the hight inside the 
    line a param and calulating the points at this hight in the model 

    optimization
    - no real problem by now, algorithm is fast enough big models lode like one second

    - could be optimized by excluding lines that are in one z plane and have no real hight
    - excluding lines with smaler upperbound than the hight we are checking 
    - deleting dublicate lines in the list --> stl files are saving sometime the same conection twice because of 
    overlapping edges 
    
    """

    points = []
    

    for layer_hight in range(40):
        layer_points = []
        layer_hight = (layer_hight / 20) - 2
        print(layer_hight)
        for line in lines:
            point = line.calcVfromH(layer_hight)
            if point != None: 
                layer_points.append(point)
        if layer_points != []:
            points.append(layer_points)
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
    # stl_file = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/tree.stl'
    cube = mesh.Mesh.from_file(stl_file)
    lines = create_line(cube)
    lines = del_duplicate(lines)
    points = slice_z(lines)
    print(points)
    show_points(points)
    


if __name__ == "__main__":
    main()
