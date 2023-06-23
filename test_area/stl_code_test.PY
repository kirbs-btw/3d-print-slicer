import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

def main():
    stl_file = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/cube.stl'
    cube = mesh.Mesh.from_file(stl_file)
    print(cube.vectors)


if __name__ == "__main__":
    main()
