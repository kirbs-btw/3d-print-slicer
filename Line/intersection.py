import math
from Line import ComplexLine
 
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
    
    if bx1 == 0 and bx2 == 0 and bx3 == 0 and dx1 == 0 and dx2 == 0 and dx3 == 0:
        return None
    elif bx1 == 0 and bx2 == 0 and bx3 == 0 and dx1 == 0 and dx2 == 0 and dx3 != 0:
        return None
    elif bx1 == 0 and bx2 == 0 and bx3 == 0 and dx1 == 0 and dx2 != 0 and dx3 == 0:
        return None
    elif bx1 == 0 and bx2 == 0 and bx3 == 0 and dx1 == 0 and dx2 != 0 and dx3 != 0:
        return None
    elif bx1 == 0 and bx2 == 0 and bx3 == 0 and dx1 != 0 and dx2 == 0 and dx3 == 0:
        return None
    elif bx1 == 0 and bx2 == 0 and bx3 == 0 and dx1 != 0 and dx2 == 0 and dx3 != 0:
        return None
    elif bx1 == 0 and bx2 == 0 and bx3 == 0 and dx1 != 0 and dx2 != 0 and dx3 == 0:
        return None
    elif bx1 == 0 and bx2 == 0 and bx3 == 0 and dx1 != 0 and dx2 != 0 and dx3 != 0:
        return None
    elif bx1 == 0 and bx2 == 0 and bx3 != 0 and dx1 == 0 and dx2 == 0 and dx3 == 0:
        return None
    elif bx1 == 0 and bx2 == 0 and bx3 != 0 and dx1 == 0 and dx2 == 0 and dx3 != 0:
        return None
    elif bx1 == 0 and bx2 == 0 and bx3 != 0 and dx1 == 0 and dx2 != 0 and dx3 == 0:
        s = (cx3 - ax3) / bx3
        k = (ax2 - cx2) / dx2
    elif bx1 == 0 and bx2 == 0 and bx3 != 0 and dx1 == 0 and dx2 != 0 and dx3 == 0:
        k = (ax2 - cx2) / dx2
        s = (cx3 + dx3*k - ax3) / bx3
    elif bx1 == 0 and bx2 == 0 and bx3 != 0 and dx1 != 0 and dx2 == 0 and dx3 != 0:
        s = (cx3 - ax3) / bx3
        k = (ax1 - cx1) / dx1
    elif bx1 == 0 and bx2 == 0 and bx3 != 0 and dx1 != 0 and dx2 != 0 and dx3 == 0:
        k = (ax1 - cx1) / dx1
        s = (cx3 - ax3) / bx3
    elif bx1 == 0 and bx2 == 0 and bx3 != 0 and dx1 != 0 and dx2 != 0 and dx3 != 0:
        k = (ax1 - cx1) / dx1
        s = (cx3 + dx3*k - ax3) / bx3
    elif bx1 == 0 and bx2 != 0 and bx3 == 0 and dx1 == 0 and dx2 == 0 and dx3 == 0:
        return None
    elif bx1 == 0 and bx2 != 0 and bx3 == 0 and dx1 == 0 and dx2 == 0 and dx3 != 0:
        k = (ax3 - cx3) / dx3
        s = (cx2 - ax2) / bx2
    elif bx1 == 0 and bx2 != 0 and bx3 == 0 and dx1 == 0 and dx2 != 0 and dx3 == 0:
        return None
    elif bx1 == 0 and bx2 != 0 and bx3 == 0 and dx1 == 0 and dx2 != 0 and dx3 != 0:
        k = (ax3 - cx3) / dx3
        s = (cx2 + dx2*k - ax2) / bx2
    elif bx1 == 0 and bx2 != 0 and bx3 == 0 and dx1 != 0 and dx2 == 0 and dx3 == 0:
        k = (ax1 - cx1) / dx1
        s = (cx2 - ax2) / bx2
    elif bx1 == 0 and bx2 != 0 and bx3 == 0 and dx1 != 0 and dx2 == 0 and dx3 != 0:
        k = (ax1 - cx1) / dx1
        s = (cx2 - ax2) / bx2
    elif bx1 == 0 and bx2 != 0 and bx3 == 0 and dx1 != 0 and dx2 != 0 and dx3 == 0:
        k = (ax1 - cx1) / dx1
        s = (cx2 + dx2*k - ax2) / bx2
    elif bx1 == 0 and bx2 != 0 and bx3 == 0 and dx1 != 0 and dx2 != 0 and dx3 != 0:
        k = (ax1 - cx1) / dx1
        s = (cx2 + dx2*k - ax2) / bx2
    elif bx1 == 0 and bx2 != 0 and bx3 != 0 and dx1 == 0 and dx2 == 0 and dx3 == 0:
        return None
    elif bx1 == 0 and bx2 != 0 and bx3 != 0 and dx1 == 0 and dx2 == 0 and dx3 != 0:
        s = (cx2 - ax2) / bx2
        k = (ax3 + s*bx3 - cx3) / dx3
    elif bx1 == 0 and bx2 != 0 and bx3 != 0 and dx1 == 0 and dx2 != 0 and dx3 == 0:
        s = (cx3 - ax3) / bx3
        k = (ax2 + s*bx2 - cx2) / dx2
    elif bx1 == 0 and bx2 != 0 and bx3 != 0 and dx1 == 0 and dx2 != 0 and dx3 != 0 and dx3*bx2 != bx3*dx2:
        k = (bx2*ax3 + bx3*cx2 - bx3*ax2 - cx3*bx2)/(dx3*bx2 - bx3*dx2)
        s = (cx2 + dx2*k - ax2) / bx2
    elif bx1 == 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 == 0 and dx3 == 0:
        s = (cx2 - ax2) / bx2
        k = (ax1 - cx1) / dx1
    elif bx1 == 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 == 0 and dx3 != 0:
        s = (cx2 - ax2) / bx2
        k = (ax1 - cx1) / dx1
    elif bx1 == 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 != 0 and dx3 == 0:
        s = (cx3 - ax3) / bx3
        k = (ax1 - cx1) / dx1
    elif bx1 == 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 != 0 and dx3 != 0:
        k = (ax1 - cx1) / dx1
        s = (cx2 + dx2*k - ax2) / bx2
    elif bx1 != 0 and bx2 == 0 and bx3 == 0 and dx1 == 0 and dx2 == 0 and dx3 == 0:
        return None
    elif bx1 != 0 and bx2 == 0 and bx3 == 0 and dx1 == 0 and dx2 == 0 and dx3 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax3 - cx3) / dx3
    elif bx1 != 0 and bx2 == 0 and bx3 == 0 and dx1 == 0 and dx2 != 0 and dx3 == 0:
        print("hello")
        s = (cx1 - ax1) / bx1
        k = (ax2 - cx2) / dx2
    elif bx1 != 0 and bx2 == 0 and bx3 == 0 and dx1 == 0 and dx2 != 0 and dx3 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 - cx2) / dx2
    elif bx1 != 0 and bx2 == 0 and bx3 == 0 and dx1 != 0 and dx2 == 0 and dx3 == 0:
        return None
    elif bx1 != 0 and bx2 == 0 and bx3 == 0 and dx1 != 0 and dx2 == 0 and dx3 != 0:
        k = (ax3 - cx3) / dx3
        s = (cx1 + dx1*k - ax1) / bx1
    elif bx1 != 0 and bx2 == 0 and bx3 == 0 and dx1 != 0 and dx2 != 0 and dx3 == 0:
        k = (ax2 - cx2) / dx2
        s = (cx1 + dx1*k - ax1) / bx1
    elif bx1 != 0 and bx2 == 0 and bx3 == 0 and dx1 != 0 and dx2 != 0 and dx3 != 0:
        k = (ax2 - cx2) / dx2
        s = (cx1 + dx1*k - ax1) / bx1
    elif bx1 != 0 and bx2 == 0 and bx3 != 0 and dx1 == 0 and dx2 == 0 and dx3 == 0:
        return None
    elif bx1 != 0 and bx2 == 0 and bx3 != 0 and dx1 == 0 and dx2 == 0 and dx3 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax3 + s*bx3 - cx3) / dx3
    elif bx1 != 0 and bx2 == 0 and bx3 != 0 and dx1 == 0 and dx2 != 0 and dx3 == 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 - cx2) / dx2
    elif bx1 != 0 and bx2 == 0 and bx3 != 0 and dx1 == 0 and dx2 != 0 and dx3 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 - cx2) / dx2
    elif bx1 != 0 and bx2 == 0 and bx3 != 0 and dx1 != 0 and dx2 == 0 and dx3 == 0:
        s = (cx3 - ax3) / bx3
        k = (ax1 + s*bx1 - cx1) / dx1
    elif bx1 != 0 and bx2 == 0 and bx3 != 0 and dx1 != 0 and dx2 == 0 and dx3 != 0 and dx3*bx1 != bx3*dx1:
        k = (bx1*ax3 + bx3*cx1 - bx3*ax1 - cx3*bx1)/(dx3*bx1 - bx3*dx1)
        s = (cx1 + dx1*k - ax1) / bx1
    elif bx1 != 0 and bx2 == 0 and bx3 != 0 and dx1 != 0 and dx2 != 0 and dx3 == 0:
        k = (ax2 - cx2) / dx2
        s = (cx3 - ax3) / bx3
    elif bx1 != 0 and bx2 == 0 and bx3 != 0 and dx1 != 0 and dx2 != 0 and dx3 != 0 and dx3*bx1 != bx3*dx1:
        k = (bx1*ax3 + bx3*cx1 - bx3*ax1 - cx3*bx1)/(dx3*bx1 - bx3*dx1)
        s = (cx1 + dx1*k - ax1) / bx1
    elif bx1 != 0 and bx2 != 0 and bx3 == 0 and dx1 == 0 and dx2 == 0 and dx3 == 0:
        return None
    elif bx1 != 0 and bx2 != 0 and bx3 == 0 and dx1 == 0 and dx2 == 0 and dx3 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax3 - cx3) / dx3
    elif bx1 != 0 and bx2 != 0 and bx3 == 0 and dx1 == 0 and dx2 != 0 and dx3 == 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 + s*bx2 - cx2) / dx2
    elif bx1 != 0 and bx2 != 0 and bx3 == 0 and dx1 == 0 and dx2 != 0 and dx3 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 + s*bx2 - cx2) / dx2
    elif bx1 != 0 and bx2 != 0 and bx3 == 0 and dx1 != 0 and dx2 == 0 and dx3 == 0:
        s = (cx2 - ax2) / bx2
        k = (ax1 + s*bx1 - cx1) / dx1
    elif bx1 != 0 and bx2 != 0 and bx3 == 0 and dx1 != 0 and dx2 == 0 and dx3 != 0:
        s = (cx2 - ax2) / bx2
        k = (ax1 + s*bx1 - cx1) / dx1
    elif bx1 != 0 and bx2 != 0 and bx3 == 0 and dx1 != 0 and dx2 != 0 and dx3 == 0 and dx2*bx1 != bx2*dx1:
        k = (bx1*ax2 + bx2*cx1 - bx2*ax1 - cx2*bx1)/(dx2*bx1 - bx2*dx1)
        s = (cx1 + dx1*k - ax1) / bx1
    elif bx1 != 0 and bx2 != 0 and bx3 == 0 and dx1 != 0 and dx2 != 0 and dx3 != 0 and dx2*bx1 != bx2*dx1:
        k = (bx1*ax2 + bx2*cx1 - bx2*ax1 - cx2*bx1)/(dx2*bx1 - bx2*dx1)
        s = (cx1 + dx1*k - ax1) / bx1
    elif bx1 != 0 and bx2 != 0 and bx3 != 0 and dx1 == 0 and dx2 == 0 and dx3 == 0:
        return None
    elif bx1 != 0 and bx2 != 0 and bx3 != 0 and dx1 == 0 and dx2 == 0 and dx3 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax3 + s*bx3 - cx3) / dx3
    elif bx1 != 0 and bx2 != 0 and bx3 != 0 and dx1 == 0 and dx2 != 0 and dx3 == 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 + s*bx2 - cx2) / dx2
    elif bx1 != 0 and bx2 != 0 and bx3 != 0 and dx1 == 0 and dx2 != 0 and dx3 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 + s*bx2 - cx2) / dx2
    elif bx1 != 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 == 0 and dx3 == 0:
        s = (cx2 - ax2) / bx2
        k = (ax1 + s*bx1 - cx1) / dx1
    elif bx1 != 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 == 0 and dx3 != 0:
        s = (cx2 - ax2) / bx2
        k = (ax1 + s*bx1 - cx1) / dx1
    elif bx1 != 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 != 0 and dx3 == 0:
        s = (cx3 - ax3) / bx3
        k = (ax1 + s*bx1 - cx1) / dx1
    elif bx1 != 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 != 0 and dx3 != 0 and dx2*bx1 != bx2*dx1:
        k = (bx1*ax2 + bx2*cx1 - bx2*ax1 - cx2*bx1)/(dx2*bx1 - bx2*dx1)
        s = (cx1 + dx1*k - ax1) / bx1
    else: 
        return None
    
    print(s, k)
    
    test_point_a = g1.point(s)
    test_point_b = g2.point(k)
    print(test_point_a)
    print(test_point_b)
    
    # s and k don't fit the lines don't cross 
    if vector_is_equal(test_point_a, test_point_b):
        return test_point_a
    return None

def main():
    # test of the things
    
    v1g1 = [2, 2, -3]
    v2g1 = [2, 3, 2]
    
    v1g2 = [3, 0, -1]
    v2g2 = [1, -2, 2] 
    
    a = ComplexLine(v1g1, v2g1)
    b = ComplexLine(v1g2, v2g2)
    
    print(intersection(a, b))
    
if __name__ == '__main__':
    main()

"""
simple lines are beeing correctly calc 
but complex lines have some issues
- wip 

"""

"""  
- thinking about writing the 64 solutions to have a working script 
1: bx1 2: bx2 3: bx3 4:dx1 5:dx2 6: dx3
000 000 - 
000 001 -
000 010 -
000 011 -
000 100 -
000 101 -
000 110 - 
000 111 -
001 000 -
001 001 - 
001 010 - 
001 011 - 
001 100 - 
001 101 -
001 110 - 
001 111 - 
010 000 - 
010 001 -
010 010 - 
010 011 -
010 100 -
010 101 -
010 110 -
010 111 -
011 000 -
011 001 -
011 010 - 
011 011 -
011 100 - 
011 101 - 
011 110 -
011 111 - 
100 000 - 
100 001 -
100 010 - 
100 011 - 
100 100 - 
100 101 - 
100 110 - 
100 111 - 
101 000 - 
101 001 -
101 010 - 
101 011 - 
101 100 - 
101 101 - 
101 110 - 
101 111 - 
110 000 - 
110 001 - 
110 010 -
110 011 - 
110 100 - 
110 101 - 
110 110 - 
110 111 - 
111 000 -
111 001 -
111 010 -
111 011 -
111 100 -
111 101 -
111 110 -
111 111 -


 
"""