import slicer_lib
from slicer_lib import get_point_slice as sp
from slicer_lib import get_gcode_from_points as cg
from stl import mesh

def main():
    """

    
    """
    file_path = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/cube.stl'
    layer_hight = 0.2 # in mm
    x_dim = 100 
    y_dim = 100
    z_dim = 100
    plate_shift = 50

    save_path = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/save'


    stl_obj = mesh.Mesh.from_file(file_path)
    points = sp.get_points_from_stl(stl_obj)
    gcode = cg.create_gcode(points=points, save_path=save_path, x_dim=x_dim, y_dim=y_dim, z_dim=z_dim, plate_shift=plate_shift)
    


if __name__ == '__main__':
    main()