from Line import Line
from Line import intersection
import math

def x_lines(obj_size_x = 10, obj_size_y = 10, obj_size_z = 10, spacing = 0.5, layer_height = 0.2,obj_offset_x = 10, obj_offset_y = 10):
    x_lines = []

    dirV = [1, 0, 0]

    layer_count = int(math.ceil(obj_size_z / layer_height))
    line_in_layer_count = int(math.ceil(obj_size_x/spacing)) * 2

    for layer_count_num in range(layer_count):
        infill_layer = []
        current_layer_height = layer_count_num * layer_height
        for x_pos in range(line_in_layer_count):
            current_x_pos = x_pos * spacing + obj_offset_x
            supV = [0, current_x_pos, current_layer_height]
            infill_layer.append(Line.Line(supV, dirV))
        x_lines.append(infill_layer)
        # inserting horrizontal lines to check the easy calc 
    return x_lines

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
        current_height = round(current_height * 1000000) / 1000000
        line = Line.Line([0.5, 0, current_height], [1, 1, 0])
        # line.info()
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
                # not pretty but works 
                pair[0][2] = round(pair[0][2] * 1000000) / 1000000
                pair[-1][2] = round(pair[-1][2] * 1000000) / 1000000

                # print(pair[0])
                # print(pair[-1])
                the_line = Line.ComplexLine(pair[0], pair[-1])
                line_element.append(the_line)
            line_layer.append(line_element)
        obj_wall_lines.append(line_layer)
    
    return obj_wall_lines

def point_len_opt(point):
    return ((point[0] ** 2) + (point[1] ** 2) + (point[2] ** 2))


def bubbleSortDouble(arr, childArr):
    n = len(arr)
    swapped = False
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                childArr[j], childArr[j + 1] = childArr[j + 1], childArr[j]
         
        if not swapped:
            return

def sort_intersection_cross_points(points):
    # optimizing by not taking the sqrt 
    # sorting them with depending on the distance to the 
    # [0, 0, 0] point --> taking the len of the point (no sqrt)
    if len(points) % 2 != 0:
        print("something is wrong with the model")
        return
    


    pointLenArr = []
    for point in points:
        pointLenArr.append(point_len_opt(point))
    
    # parallel sorting of the points to its distances 
    bubbleSortDouble(pointLenArr, points)

    # seperating points into pairs
    







    pass 

def calc_infill_points(obj_wall_lines, infill_lines):
    # looks at the intersection of an infill line with the walls of the obj
    # if line hits multiple wall lines we need to find out wich connects to wich 
    
    infill_points = []
    
    # print(obj_wall_lines[0][0][0].sV[2])
    # print(infill_lines[0][0].sV[2])
    
    for layer_index, layer in enumerate(obj_wall_lines):
        infill_layer = []
        for line in infill_lines[layer_index]:
            line_intersection_points = []
            for element in layer:
                for obj_line in element:
                    point = intersection.intersection(obj_line, line)

                    # checks if the point exists and is on the line
                    if point != None and obj_line.pointInsideLine(point):
                        line_intersection_points.append(point)
            
            # sorting the point out
            # r: if there are two points they belong together 
            # if there are four we need to find the two pairs

            # format holdingArr[elements[pointpairs[point[], point[]]]]            
            sorted_layer = sort_intersection_cross_points(line_intersection_points)
            
                        
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
    infill_lines = x_lines(obj_size_x, obj_size_y, obj_size_z, 5, layer_height, obj_offset_x, obj_offset_y)
    
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

# fixed the fppe 
# no good fix because of just rounding the num 
# the lines still dont form intersections
# 