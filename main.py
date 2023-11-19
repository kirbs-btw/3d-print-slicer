from stl import mesh
from slicer_lib import stl_to_lines as stltl
from slicer_lib import lines_to_points as ltp
from slicer_lib import plane_point_pairs as ppp
from slicer_lib import add_infill as adi

def main():
    printer_x = 2000
    printer_y = 2000
    printer_z = 2000
    
    file_path = ''
    layer_height = 0.2 # in mm
    obj_x_dim = 50 # in mm
    obj_y_dim = 50 # in mm
    obj_z_dim = 50 # in mm
    
    x_plate_offset = 50
    y_plate_offset = 50

    file_name = ''
    save_path = ''

    stl_obj = mesh.Mesh.from_file(file_path)
    line_triangles = stltl.get_points_from_stl(stl_obj, obj_x_dim=obj_x_dim, obj_y_dim=obj_y_dim, obj_z_dim=obj_z_dim, x_plate_offset=x_plate_offset, y_plate_offset=y_plate_offset)
    
    # wall points
    # format: new format is:[points[layer[element[pair[points]]]]]
    obj_layer_point_pairs = ltp.lines_to_points(line_triangles, layer_height)
    
    
    
    # infill_point in pair form
    infill_points = adi.infill_points(obj_layer_point_pairs, "cross", obj_x_dim, obj_y_dim, obj_z_dim, spacing=0.5, layer_height=layer_height, obj_offset_x=x_plate_offset, obj_offset_y=y_plate_offset)
    
    # combine points
    
    
    
    
    
    # reformate the point pairs to points 
    # reformat
    # format: new format is:[points[layer[element[points]]]]
    obj__points = ppp.plane_pairs(obj_layer_point_pairs)
    
    
if __name__ == '__main__':
    main()