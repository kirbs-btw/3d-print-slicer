# 3d printing slicer - Bastian Lipka
Writing my one slicer
fundament for later use with none planar printing

# how to use
- dowload the repo
- put your .stl files in the stl folder
- add your paths and names in the main.py
- you can test the gcode with your printer or look at it in a normal slicer like cura
- for sizing and other params change the x,y and z values in the main.py 



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
