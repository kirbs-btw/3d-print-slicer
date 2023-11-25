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
main.py
README.md
LICENS
demo_stl_files

|--- cube.stl

|--- tree.stl

slicer_lib

# WIP
Wall thickness could be done with triangular 

# To do
- infill pattern
- wall thickness
- zhop
- finding good extrusion
