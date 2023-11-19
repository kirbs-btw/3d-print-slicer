def plane_pairs(pair_arr):
    """
    new format is:
    [points
        [layer
            [element
                [points]
            ]
        ]
    ]
    """
    new_arr = []
    for layer in pair_arr:
        new_layer = []
        for element in layer:
            new_element = []
            for pair in element:
                for point in pair:
                    new_element.append(point)
            new_layer.append(new_element)
        new_arr.append(new_layer)
    return new_arr