import pywavefront
from mpl_toolkits import mplot3d
from matplotlib import pyplot

cube = pywavefront.Wavefront('H:/Projekte/Projekte/Project 137/3d-print-slicer/demo_stl_files/cube.stl')
print(cube)

points = []



fig = pyplot.figure()
ax = fig.add_subplot(projection='3d')

# scatter points on graph
for i in points:    
    print(i)
    ax.scatter(i[0], i[1], i[2])

# shows the final graph
pyplot.show()