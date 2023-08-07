import slicer_lib
from slicer_lib import get_point_slice as sp
from stl import mesh

def main():
    """

    
    """
    file_path = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/cube.stl'
    layer_hight = 0.2 # in mm
    x_dim = 100 
    y_dim = 100
    z_dim = 100
    
    save_place = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/save'

    stl_obj = mesh.Mesh.from_file(file_path)
    points = sp.get_points_from_stl(stl_obj)
    
    


if __name__ == '__main__':
    main()