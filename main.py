from stl import mesh
from slicer_lib import stl_to_lines as stltl
from slicer_lib import lines_to_points as ltp

def main():
    printer_x = 2000
    printer_y = 2000
    printer_z = 2000
    
    file_path = ''
    layer_hight = 0.2 # in mm
    obj_x_dim = 50 # in mm
    obj_y_dim = 50 # in mm
    obj_z_dim = 50 # in mm
    
    x_plate_offset = 50
    y_plate_offset = 50

    file_name = ''
    save_path = ''

    stl_obj = mesh.Mesh.from_file(file_path)
    line_triangles = stltl.get_points_from_stl(stl_obj, obj_x_dim=obj_x_dim, obj_y_dim=obj_y_dim, obj_z_dim=obj_z_dim, x_plate_offset=x_plate_offset, y_plate_offset=y_plate_offset)
    points = ltp.lines_to_points(line_triangles, layer_hight)
    
if __name__ == '__main__':
    main()