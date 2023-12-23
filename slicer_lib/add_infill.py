from Line import Line
from Line import intersection
import math

def cross_lines(obj_size_x = 10, obj_size_y = 10, obj_size_z = 10, spacing = 0.5, layer_height = 0.2,obj_offset_x = 10, obj_offset_y = 10):
    cross_lines = []
    
    start_point_x = obj_offset_x
    end_point_x = obj_offset_x + obj_size_x
    x_count = int(math.ceil((end_point_x - start_point_x) / spacing))
     
    start_point_y = obj_offset_y
    end_point_y = obj_offset_y + obj_size_y
    y_count = int(math.ceil((end_point_y - start_point_y) / spacing))
    
    layer_count = int(math.ceil(obj_size_z / layer_height))
    
    xVdir = [0, 1, 0]
    yVdir = [1, 0, 0]
        
    for layer in range(layer_count):
        line_layer = []
        current_z = layer * layer_height
        for pos in range(x_count):
            pos_space = pos * spacing
            supportV = [pos_space + start_point_x, 0, current_z]
            this_line = Line.Line(supportV, xVdir)
            line_layer.append(this_line)
        for pos in range(y_count):
            pos_space = pos * spacing
            supportV = [0, pos_space + start_point_x, current_z]
            this_line = Line.Line(supportV, yVdir)
            line_layer.append(this_line)
        cross_lines.append(line_layer)    
    return cross_lines

def test_pattern(layer_height=0.2):
    lines = []

    layer_count = math.ceil(100 / layer_height)
    for count in range(layer_count):
        layer = []
        current_height = count * layer_height
        line = Line.Line([0.5, 0, current_height], [1, 1, 0])
        layer.append(line)
        lines.append(layer)
    return lines


def convert_obj_points_to_line(obj_wall_point_pairs):
    obj_wall_lines = []
    # starts with 0.2 why ? 
    
    for layer in obj_wall_point_pairs:
        line_layer = []
        for element in layer:
            line_element = []
            for pair in element:
                # converting because of float ppe
                # janky fix
                pair[0][2] = round(pair[0][2] * 1000000) / 1000000
                pair[-1][2] = round(pair[-1][2] * 1000000) / 1000000

                print(pair[0])
                print(pair[-1])
                the_line = Line.ComplexLine(pair[0], pair[-1])
                line_element.append(the_line)
            line_layer.append(line_element)
        obj_wall_lines.append(line_layer)
    
    return obj_wall_lines

def calc_infill_points(obj_wall_lines, infill_lines):
    # looks at the intersection of an infill line with the walls of the obj
    # if line hits multiple wall lines we need to find out wich connects to wich 
    
    infill_points = []
    
    # print(obj_wall_lines[0][0][0].sV[2])
    # print(infill_lines[0][0].sV[2])
    
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
                    """
                    print("element")
                    print(obj_line.sV[2])
                    print("infill")
                    print(line.sV[2])
                    """
                    # obj_line.info()
                    # line.info()


                    point = intersection.intersection(obj_line, line)
                    if point != None:
                    # if point != None and obj_line.pointInsideLine(point):
                        print(point)
                        infill_element.append(point)
            if infill_element != []:
                infill_layer.append(infill_element)
        if infill_layer != []:
            infill_points.append(infill_layer)
            
    return infill_points
       
def infill_points(obj_wall_point_pairs, infill_type="cross", obj_size_x = 10, obj_size_y = 10, obj_size_z = 10, spacing = 0.5, layer_height = 0.2,obj_offset_x = 10, obj_offset_y = 10):
    """
    calculating the infill 
    """
    # converted wall lines of obj to line obj
    obj_wall_lines = convert_obj_points_to_line(obj_wall_point_pairs)
    # generating infill lines "cross pattern"
    # infill_lines = cross_lines(obj_size_x, obj_size_y, obj_size_z, spacing, layer_height, obj_offset_x, obj_offset_y)
    infill_lines = test_pattern()
    # finding the infill lines inside the obj 
    infill_points = calc_infill_points(obj_wall_lines, infill_lines)
    
    return infill_points
    
if __name__ == '__main__':
    pass


# could be an issues with the rounding of the numbers 
# the point pairs are line going up and down so every one is skew to the other
# 49.800000000000004 goes to 49.8
# the dirV z coord is -0.000000000000004
# instead of 0...