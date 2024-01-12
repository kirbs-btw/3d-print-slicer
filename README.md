# 3d printing slicer - Bastian Lipka
Writing my one slicer
fundament for later use with none planar printing

# Technique
Walls:
    .stl are triangles
    slicing them with the layerheight
    Connection of points depends on the triangles
    the triangles share edges --> point loop is done 
    by connecting the same points of different edges --> like domino
    Multiple loop in one layer means multiple elements --> element hop.

Infill:
    general infillpattern:
        generating infillpatterns with the intersections
        - logic with multipe elements per line
        --> ordering the intersection points depending on the 
        dist to the origin --> picking them in pairs 
        - if the num of intersections is odd --> there is an error with the modle


# Files
.
├── demo_stl_files/
│   ├── cube.stl
│   ├── ninecube.stl
│   └── tree.stl
├── gcode_parts/
│   ├── end_gcode.gcode
│   └── top_gcode.gcode
├── Line/
│   ├── __init__.py
│   ├── intersection.py
│   └── Line.py
├── out
├── slicer_lib/
│   ├── -__init__.py
│   ├── add_infill.py
│   ├── combine_parts.py
│   ├── gcode_to_file.py
│   ├── lines_to_points.py
│   ├── plane_point_pairs.py
│   ├── points_to_gcode.py
│   └── stl_to_lines.py
├── main.py
├── README.md
└── LICENSE

# WIP
Wall thickness could be done with triangular calc
Infill with pre calc patterns and the intersection of the lines 
from the wall and the infill lines

# To do
- more infill patterns
- wall thickness
- zhop
- finding good extrusion
- filling top and bottom 