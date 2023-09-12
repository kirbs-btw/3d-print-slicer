import slicer_lib
from slicer_lib import get_point_slice as sp
from slicer_lib import get_gcode_from_points as cg
from stl import mesh

def save_gcode(gcode, save_path="", file_name="unnamend"):
    file = open('{}{}.gcode'.format(save_path, file_name), 'w+')
    for line in gcode:
        file.write('\n{}'.format(line))

def main():

    file_path = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/tree.stl'
    layer_hight = 0.2 # in mm
    x_dim = 50
    y_dim = 50
    z_dim = 50
    plate_shift = 30

    file_name = 'tree'
    save_path = 'H:/Projekte/Projekte/Project 137/3d-print-slicer/save/'
    
    stl_obj = mesh.Mesh.from_file(file_path)
    points = sp.get_points_from_stl(stl_obj, layer_hight=layer_hight, x_dim=x_dim, y_dim=y_dim, z_dim=z_dim, offset=plate_shift)
    gcode = cg.create_gcode(points=points)
    save_gcode(gcode, save_path=save_path, file_name=file_name)

if __name__ == '__main__':
    main()