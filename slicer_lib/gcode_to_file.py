def gcode_to_file(gcode, filename, path):
    full_path = str(filename) + str(path)
    f = open(full_path, "r+")
    for line in gcode:
        f.writelines(line)
    f.close()