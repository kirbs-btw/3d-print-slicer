# 3d printing slicer - Bastian Lipka
Writing my one slicer
ifundament for later use with none planar printing

# Technique
.stl mesh is converted to triangle lines. The lines get sliced
certain hights to create layers.
The order of the points in the layer is determined by the conection of the triangles 
every tris shares an edge --> are conected by algorithm like domino.
Multiple loop in one layer means multiple elements --> element hop.

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
- infill pattern
- wall thickness
- zhop
- finding good extrusion