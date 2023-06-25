import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

class striaght:
    def __init__(self, v1, v2):
        self.supportV, self.directionV = self.calcV(v1, v2)

    def clacV(self, v1, v2):
        x = v2[0] - v1[0]
        y = v2[1] - v1[1]
        z = v2[2] - v1[3]

        dirV = [x, y, z]
        supportV = v1
        return supportV, dirV




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
