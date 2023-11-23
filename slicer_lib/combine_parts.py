def combine_pairs(*args):
    # defines the first arg as a scaffold to append the other elements in 
    obj_point_pairs = args[0]
    
    # iterates through all but the first one
    for arg in args[1:]:
        for layer_index, layer in enumerate(arg):
            for element in layer: 
                obj_point_pairs[layer_index].append(element)
    
    return obj_point_pairs
    