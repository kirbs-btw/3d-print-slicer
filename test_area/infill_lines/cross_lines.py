import Line

def create_lines(size_x = 1000, size_y = 1000, size_z = 1000, space = 1, layer_higth = 0.2):

    dir_v = [0, 1, 0]
    lines = []
    for j in range(size_z / layer_higth):
        lines_layer = []
        hight = j * size_z
        for i in range(size_y / space):
            x_value = i * space
            support = [x_value, 0, hight]
            l = Line(support, dir_v)
            lines_layer.append(l)
        for i in range(size_y / space):
            y_value = i * space
            support = [y_value, 0, hight]
            l = Line(support, dir_v)
            lines_layer.append(l)
        lines.append(lines_layer)

def main():
    lines = create_lines()
    print(lines)

if __name__ == '__main__':
    main()