from stl import mesh
from slicer_lib import stl_to_lines as stltl
from slicer_lib import lines_to_points as ltp
from slicer_lib import plane_point_pairs as ppp
from slicer_lib import add_infill as adi
from slicer_lib import combine_parts as cop
from slicer_lib import points_to_gcode as ptg
from slicer_lib import gcode_to_file as gtf

def main():
    printer_x = 2000
    printer_y = 2000
    printer_z = 2000
    
    file_path = 'H:/Projekte/Projekte/Project 137/slicer_2/demo_stl_files/cube.stl'
    layer_height = 0.2 # in mm
    obj_x_dim = 50 # in mm
    obj_y_dim = 50 # in mm
    obj_z_dim = 50 # in mm
    
    x_plate_offset = 50
    y_plate_offset = 50

    file_name = 'test.gcode'
    save_path = 'H:/Projekte/Projekte/Project 137/slicer_2/out/'

    stl_obj = mesh.Mesh.from_file(file_path)
    line_triangles = stltl.get_points_from_stl(stl_obj, obj_x_dim=obj_x_dim, obj_y_dim=obj_y_dim, obj_z_dim=obj_z_dim, x_plate_offset=x_plate_offset, y_plate_offset=y_plate_offset)
    
    # wall points
    # format: new format is:[points[layer[element[pair[points]]]]]
    obj_layer_point_pairs = ltp.lines_to_points(line_triangles, layer_height, obj_z_dim)
    
    # infill_point in pair form
    infill_point_pairs = adi.infill_points(obj_layer_point_pairs, "cross", obj_x_dim, obj_y_dim, obj_z_dim, spacing=0.5, layer_height=layer_height, obj_offset_x=x_plate_offset, obj_offset_y=y_plate_offset)
    print(infill_point_pairs)

    # fill bottom and top

    # combine points
    obj_point_pairs = cop.combine_pairs(obj_layer_point_pairs, infill_point_pairs)
    
    # reformate the point pairs to points 
    # format: new format is:[points[layer[element[points]]]]
    # obj_points = ppp.plane_pairs(obj_layer_point_pairs)
    obj_points = ppp.plane_pairs(obj_point_pairs)
    
    # slicing to gcode 
    
    gcode = ptg.create_gcode(obj_points)
    
    gtf.gcode_to_file(gcode, file_name, save_path)
    
   
    # without the infill the code works fine 
    # searching the infill issue 
    
if __name__ == '__main__':
    main()
    
    
"""
Bug report 

layer lines and infill lines dont start at the same hight 
--> out of sync --> no lines intersect 
--> shifted by 0.2
    
"""