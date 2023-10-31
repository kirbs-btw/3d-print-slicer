from stl import mesh

def main():
    file_path = ''
    layer_hight = 0.2 # in mm
    obj_x_dim = 50 # in mm
    obj_y_dim = 50 # in mm
    obj_z_dim = 50 # in mm
    
    x_plate_offset = 50
    y_plate_offset = 50

    file_name = ''
    save_path = ''

    stl_obj = mesh.Mesh.from_file(file_path)
    

if __name__ == '__main__':
    main()