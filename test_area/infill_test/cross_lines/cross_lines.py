
def line_points():
    len_x = 100
    len_y = 100
    num_lines = 10
    layer_count = 50
    layer_hight = 0.1

    spacing = len_y / (num_lines - 1)

    lines = []
    for layer_num in range(layer_count):
        hight = layer_num / (1/layer_hight)
        for i in range(num_lines):
            current_space = round(spacing * i, 3)
            lines.append([[0, current_space, hight], [len_x, current_space, hight]])
        for i in range(num_lines):
            current_space = round(spacing * i, 3)
            lines.append([[current_space, 0, hight], [current_space, len_y, hight]])

    return lines

def main():
    points = line_points()
    for i in points:
        print(i)

if __name__ == '__main__':
    main()