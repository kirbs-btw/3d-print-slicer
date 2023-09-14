# 3d printing slicer - Bastian Lipka
This repo is for writing my own slicer from scratch. 

# Technique
Slicing the mesh in to points at layers with vector math
defining lines and slicing with them the layers

To track wich line goes where, slicing by triangle is used. after that the lines can be sorted together by machting ends like with domino. 
when there are multiple loops there are multiple elements in one layer --> zhop 

# Files
Still work in progress sorted work will be comming soon 

# WIP
wall thickness could be done by triangular calc 



# To do
- infill pattern
- wall thickness
- zhop
- finding good extrusion 
