import math
    
def unit_v(v):
    return math.sqrt(v[0]**2 + v[1] ** 2 + v[2] ** 2)

def unit_v(v):
    length = unit_v(v)
    x1 = v[0] / length
    x2 = v[1] / length
    x3 = v[2] / length 

    unit_v = [x1, x2, x3]

    return unit_v 

def vector_is_equal(v1, v2):
    if v1[0] == v2[0] and v1[1] == v2[1] and v1[2] == v2[2]:
        return True
    return False

def compare_dir_v(dir_a, dir_b):
    """
    copares two vectors if they are equal 
    equal means == or * -1 == 
    """
    if vector_is_equal(dir_a, dir_b): return True
    if vector_is_equal(dir_a, [dir_b[0]*(-1), dir_b[1]*(-1), dir_b[2]*(-1)]): return True
    return False

def intersection(g1, g2):
    """
    equal 
    put one point of line a in line b to check if it is on it 
    --> equal - infinit points 
    --> no mathc - no points 

    cross / windswept 
    set equal 

    if no match 
    windsewpt: no points 

    if mach 
    cross: points 
    """

    # compare dir v 
    # could be inverted by -1 so check both cases 
    dir_v_is_equal = compare_dir_v(g1.dV, g2.dV)
    
    if dir_v_is_equal:
        """
        there could be further calc but if there are infinite solutions 
        or none is the same for the result
        """
        return None 

    # I     ax1 + s * bx1 = cx1 + k * dx1
    # II    ax2 + s * bx2 = cx2 + k * dx2
    # III   ax3 + s * bx3 = cx3 + k * dx3

    # setting up the variables for calculation
    ax1 = g1.sV[0]
    ax2 = g1.sV[1]
    ax3 = g1.sV[2]
    bx1 = g1.dV[0]
    bx2 = g1.dV[1]
    bx3 = g1.dV[2]
    cx1 = g2.sV[0]
    cx2 = g2.sV[1]
    cx3 = g2.sV[2]
    dx1 = g2.dV[0]
    dx2 = g2.dV[1]
    dx3 = g2.dV[2]

    # check for edgecases before
    # writing more calculations for the edgecases
    
    # lines:
    """
    print()
    print("{} + s*{} = {} + k*{}".format(ax1, bx1, cx1, dx1))
    print("{} + s*{} = {} + k*{}".format(ax2, bx2, cx2, dx2))
    print("{} + s*{} = {} + k*{}".format(ax3, bx3, cx3, dx3))
    """
    
    if bx1 == 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 != 0 and dx3 != 0:
        k = (ax1 - cx1)/dx1
        s = (cx2+(dx2*k)-ax2)/bx2
    elif bx2 == 0 and bx3 != 0 and dx2 != 0 and dx3 != 0: 
        k = (ax2-cx2)/dx2
        s = (cx3+(dx3*k)-ax3)/bx3
    elif bx3 == 0 and bx2 != 0 and dx2 != 0 and dx3 != 0:
        k = (ax3 - cx3) / dx3
        s = (cx2 - ax2 + (((ax3 * dx2) - (cx3 * dx2))/dx3))/bx2
    elif dx1 == 0 and bx1 != 0 and dx2 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 + (bx2 * s) - cx2)/dx2 
    elif dx2 == 0 and bx2 != 0 and dx1 != 0: 
        s = (cx2-ax2) / bx2
        k = (ax1 + (bx1 * s) - cx1) / dx1
    elif dx3 == 0 and bx1 != 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 != 0: 
        s = (cx3 - ax3) / bx3
        k = (ax2 - cx2 + (((cx3 * bx2) - (ax3 * bx2))/bx3)) / dx2
    elif bx3 == 0 and dx3 == 0 and bx1 == 0 and dx1 != 0 and dx2 != 0:
        s = (ax1 - cx1) / dx1
        k = (ax2 + (bx2 * s) - cx2) / dx2
    elif bx3 == 0 and dx3 == 0 and bx2 == 0 and dx1 != 0 and dx2 != 0:
        s = (ax2 - cx2) / dx2
        k = (ax1 + (bx1*s) - cx1) / dx1
    elif bx3 == 0 and dx3 == 0 and dx1 == 0 and bx1 != 0 and dx2 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 + (bx2*s) - cx2) / dx2
    elif bx3 == 0 and dx3 == 0 and dx2 == 0 and bx2 != 0 and dx1 != 0:
        s = (cx2-ax2) / bx2
        k = (ax1 + (bx1*s) - cx1) / dx1
    elif bx3 == 0 and dx3 == 0 and bx1 == 0 and dx2 == 0 and bx2 != 0 and dx1 != 0:
        s = (cx2 - ax2) / bx2
        k = (ax1 - cx1) / dx1
    elif bx3 == 0 and dx3 == 0 and bx2 == 0 and dx1 == 0 and bx1 != 0 and dx2 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 - cx2) / dx2
    elif dx3 == 0 and bx3 == 0 and ax3 == cx3 and bx1 != 0 and bx2 != 0 and dx1 != 0 and dx2 != 0:
        k = ((ax2/dx2)-(cx2/dx2)+((bx2*cx1)/(dx2*bx1))-((bx2*ax1)/(dx2*bx1)))/(1-((bx2*dx1)/(dx2*dx1)))#
        s = (cx1-ax1+(dx1*k))/bx1
    elif bx1 == 0 and dx1 == 0 and  ax1 != cx1:
        return None
    elif bx2 == 0 and dx2 == 0 and  ax2 != cx2:
        return None
    elif dx3 == 0 and bx3 == 0 and ax3 != cx3:
        return None
    elif bx1 == 0 and cx1 == 0 and dx2 == 0 and cx3 == 0 and dx3 == 0 and bx2 != 0:
        k = ax1 
        s = (cx2 - ax2) / bx2
    elif bx2 == 0 and dx2 == 0 and ax2 == cx2 and dx3 == 0:
        s = (cx3 - ax3) / bx3
        k = ax1 + s*bx1 
    elif dx1 == 0 and bx2 == 0 and dx3 == 0:
        k = (ax2 - cx2) / dx2
        s = (cx1 - ax1) / bx1
    elif dx1 == 0 and bx2 == 0 and dx3 == 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 - cx2) / dx2
    elif bx1 == 0 and dx1 == 0 and dx3 == 0 and bx3 != 0:
        s = (cx3 - ax3) / bx3
        k = ax2 + s*bx2 - cx2
    
    # if none is equal to 0
    elif dx2 != 0 and dx1 != 0 and (bx2 * dx1) / (dx2 * dx1) != 1:
        k = ((ax2/dx2)-(cx2/dx2)+((bx2*cx1)/(dx2*bx1))-((bx2*ax1)/(dx2*bx1)))/(1-((bx2*dx1)/(dx2*dx1)))
        s = (cx3 + (dx3 * k) - ax3) / bx3

    
    
    # comparing if s and k fit in the equation 
    if math.isnan(k) or math.isnan(s): return None
    if k == math.inf or k == -math.inf or s == math.inf or s == -math.inf: return None
    
    test_point_a = g1.point(s)
    test_point_b = g2.point(k)

    # s and k don't fit the lines don't cross 
    if vector_is_equal(test_point_a, test_point_b):
        print(test_point_a)
        return test_point_a
    return None


"""
the intersection of two points is a hell 
you can go and check for all edge cases of calculations 

--> 6 variables that can be 0 or a other value
--> 2^6 --> 64 differen calcuations to be checked

--> im not finding a general solution to the issue 
--> could wirte all 64 edge cases and what the output would be 
    --> many have no solution or infinite 

- there is one solution with intense math and code i don't understand quite 
https://paulbourke.net/geometry/pointlineplane/L3D.py
     
- thinking about writing the 64 solutions to have a working script 
--> if someone reads this please leave a comment about the topic <3
    
"""