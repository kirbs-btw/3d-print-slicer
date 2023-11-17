from Line import *
from intersection import *

def cross_lines(obj_size_x = 10, obj_size_y = 10, obj_size_z = 10, spacing = 0.5, layer_height = 0.2,obj_offset_x = 10, obj_offset_y = 10):
    cross_lines = []
    
    line_x_count = obj_size_x / spacing
    line_y_count = obj_size_y / spacing 
    
    # creating x lines 
    for height in range(0, obj_size_z, layer_height):
        cross_layer_lines = []
        x_dir_vector = [1, 0, 0]
        y_dir_vector = [0, 1, 0]
        for x_value in range(obj_offset_x, obj_offset_x, spacing):
            support = [x_value, obj_offset_y, height]
            line = Line(support, x_dir_vector)
            cross_layer_lines.append(line)
            
        for y_value in range(obj_offset_y, obj_size_y, spacing):
            support = [obj_offset_x, y_value, height]
            line = Line(support, y_dir_vector)
            cross_layer_lines.append(line)
            
        cross_lines.append(cross_layer_lines)

    return cross_lines

def convert_obj_points_to_line(obj_wall_point_pairs):
    obj_wall_lines = []
    
    for layer in obj_wall_point_pairs:
        line_layer = []
        for element in layer:
            line_element = []
            for pair in element:
                the_line = ComplexLine(pair[0], pair[-1])
                line_element.append(the_line)
            line_layer.append(line_element)
        obj_wall_lines.append(line_layer)
    
    return obj_wall_lines

def calc_infill_points(obj_wall_lines, infill_lines):
    # looks at the intersection of an infill line with the walls of the obj
    # if line hits multiple wall lines we need to find out wich connects to wich 
    
    infill_points = []
    for layer_index, layer in enumerate(obj_wall_lines):
        infill_layer = []
        for line in infill_lines[layer_index]:
            # every line gets one element 
            infill_element = []
            # if len is 0 - ignore 
            # if len is 1 - some error with the model  
            # if len is 2 - normal line
            # if len > 2 && even multiple lines 
            # need to be sorted end split in multiple elements 
            
            for element in layer:
                for obj_line in element:
                    point = intersection(obj_line, line)
                    infill_element.append(point)
            infill_layer.append(infill_element)
        infill_points.append(infill_layer)
            
    return infill_points
    
def zip_infill_walls(obj_wall_point_pairs, infill_points):    
    """
    adding lines as new elements to the layers in there 
    """
    
    pass
    
def infill_points(obj_wall_point_pairs, infill_type="cross", obj_size_x = 10, obj_size_y = 10, obj_size_z = 10, spacing = 0.5, layer_height = 0.2,obj_offset_x = 10, obj_offset_y = 10):
    """
    calculating the infill 
    """
    obj_wall_lines = convert_obj_points_to_line(obj_wall_point_pairs)
    infill_lines = cross_lines(obj_size_x, obj_size_y, obj_size_z, spacing, layer_height, obj_offset_x, obj_offset_y)
    infill_points = calc_infill_points(obj_wall_lines, infill_lines)
    
    return infill_points
    
if __name__ == '__main__':
    pass