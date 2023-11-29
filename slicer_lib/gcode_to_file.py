def gcode_to_file(gcode, filename, path):
    full_path =  str(path) + str(filename)
    f = open(full_path, "w+")
    for line in gcode:
        line_txt = "{}\n".format(line)
        f.writelines(line_txt)
    f.close()