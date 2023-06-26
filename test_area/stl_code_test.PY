import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

class striaght:
    def __init__(self, v1, v2):
        self.supportV, self.directionV, self.bounds = self.calcV(v1, v2)
        

    def clacV(self, v1, v2):
        """
        calculates support 
        and directional vector for the straight

        also determins the upper and lower bound of the 
        straight to see if pointis is bewtween those



        
        """
        upper = v1[2]
        lower = v2[2]

        if lower > upper: lower, upper = upper, lower

        x = v2[0] - v1[0]
        y = v2[1] - v1[1]
        z = v2[2] - v1[3]

        dirV = [x, y, z]
        supportV = v1
        return supportV, dirV, [lower, upper]
    
    def calcVfromH(self, h):
        """
        calculation be like

        h
        sup.x3 + dir.x3 * v = h
        dir.x3 * v = h - sup.x3
        v = (h / sup.x3) / dir.x3 => dir.x3 != 0
        
        """
        if dir.x3 == 0:
            return None
        
        v = (h / self.supportV[2]) / self.dirV[2] 

        """
        placing v in equation
        
        x1 = sup.x1 + dir.x1 * v
        x2 = sup.x2 + dir.x2 * v
        x3 = sup.x3 + dir.x3 * v

        """

        x1 = self.supportV[0] + self.directionV[0] * v
        x2 = self.supportV[1] + self.directionV[1] * v
        x3 = self.supportV[2] + self.directionV[2] * v

        return [x1, x2, x3]



def main():
    stl_file = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/cube.stl'
    cube = mesh.Mesh.from_file(stl_file)
    print(cube.vectors)

    # thinking how to slice

    """ 
        straight obj
        create straight from points

        clac x,y with a z value
        use fance math to fine point on that hight 

        iteration through ervery hight

    
    
    
    """


if __name__ == "__main__":
    main()
