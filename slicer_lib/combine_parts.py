
# points form is points = [layer[element[point[]]]]
# combining the elements of the other array to the new one
# combination issue ?


def combine_pairs(obj_points, infill_points):
    new_points = []
    for idx, layer in enumerate(obj_points):
        new_layer = []
        for element in layer:
            new_layer.append(element)
        for element in infill_points[idx]:
            new_layer.append(element)
        new_points.append(new_layer)
    return new_points


"""

def combine_pairs(*args):
    # defines the first arg as a scaffold to append the other elements in 
    obj_point_pairs = args[0]
    
    # iterates through all but the first one
    for arg in args[1:]:
        for layer_index, layer in enumerate(arg):
            
            for element in layer: 
                # skipping the empty arrays
                if element == []:
                    continue
                obj_point_pairs[layer_index].append(element)
    
    return obj_point_pairs
"""