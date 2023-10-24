import math

"""
new line class only for easy lines
"""

class Line:
    def __init__(self, support, dir):
        self.supportV = support
        self.directionV = dir
 
    def point(self, k):
        x1 = self.supportV[0] + self.directionV[0] * k
        x2 = self.supportV[1] + self.directionV[1] * k
        x3 = self.supportV[2] + self.directionV[2] * k

        return [x1, x2, x3]

    def calcVfromX(self, x_value):
        if self.directionV[0] == 0:
            return None

        v = (x_value - self.supportV[0]) / self.directionV[0] 

        """
        placing v in equation
        """
        x1 = self.supportV[0] + self.directionV[0] * v

        # check if point is in between the original points 
        if not x1 > self.lower_x_bound or not x1 < self.upper_x_bound:
            return None
        
        x2 = self.supportV[1] + self.directionV[1] * v
        x3 = self.supportV[2] + self.directionV[2] * v
        
        return [x1, x2, x3]

    def calcVfromY(self, y_value):
        if self.directionV[1] == 0:
            return None

        v = (y_value - self.supportV[1]) / self.directionV[1] 

        """
        placing v in equation
        """
        x2 = self.supportV[1] + self.directionV[1] * v

        # check if point is in between the original points 
        if not x2 > self.lower_y_bound or not x2 < self.upper_y_bound:
            return None
        
        x1 = self.supportV[0] + self.directionV[0] * v
        x3 = self.supportV[2] + self.directionV[2] * v
        
        return [x1, x2, x3]

    
    def calcVfromH(self, h):
        """
        calculation be like

        sup.x3 + dir.x3 * v = h
        dir.x3 * v = h - sup.x3
        v = (h - sup.x3) / dir.x3   => dir.x3 != 0
        
        """
        if self.directionV[2] == 0:
            return None

        v = (h - self.supportV[2]) / self.directionV[2] 

        """
        placing v in equation
        """
        x3 = self.supportV[2] + self.directionV[2] * v

        # check if point is in between the original points 
        if not x3 > self.lower_z_bound or not x3 < self.upper_z_bound:
            return None
        
        x1 = self.supportV[0] + self.directionV[0] * v
        x2 = self.supportV[1] + self.directionV[1] * v
        
        return [x1, x2, x3]
    
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
    is_equal = False
    is_equal = vector_is_equal(dir_a, dir_b)
    is_equal = vector_is_equal(dir_a, [dir_b[0]*(-1), dir_b[1]*(-1), dir_b[2]*(-1)])
    return is_equal

def line_cross(g1, g2):
    """
    four ways:
    - parallel - no point
    - cross    - point
    - windswept- no point 
    - equal    - infinite points 
    parallel 
    dir vector = multiple of the other dirv
    solution: 
    could normal the dir v to len 1 
    
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
    dir_v_is_equal = compare_dir_v(g1.directionV, g2.directionV)
    
    if dir_v_is_equal:
        """
        there could be further calc but if there are infinite solutions 
        or none is the same for the result
        """
        return None 

    # I     g1.sV.x1 + s * g1.dV.x1 = g2.sV.x1 + k * g2.dV.x1
    # II    g1.sV.x2 + s * g1.dV.x2 = g2.sV.x2 + k * g2.dV.x2
    # III   g1.sV.x3 + s * g1.dV.x3 = g2.sV.x3 + k * g2.dV.x3

    # setting up the variables for calculation
    ax1 = g1.supportV[0]
    ax2 = g1.supportV[1]
    ax3 = g1.supportV[2]
    bx1 = g1.directionV[0]
    bx2 = g1.directionV[1]
    bx3 = g1.directionV[2]
    cx1 = g2.supportV[0]
    cx2 = g2.supportV[1]
    cx3 = g2.supportV[2]
    dx1 = g2.directionV[0]
    dx2 = g2.directionV[1]
    dx3 = g2.directionV[2]

    # check for edgecases before
    # writing more calculations for the edgecases
    
    if bx1 == 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 != 0 and dx3 != 0: 
        k = (ax1 - cx1)/dx1
        s = (cx2+(dx2*k)-ax2)/bx2
    if bx2 == 0 and bx3 != 0 and dx2 != 0 and dx3 != 0: 
        k = (ax2-cx2)/dx2
        s = (cx3+(dx3*k)-ax3)/bx3
    if bx3 == 0 and bx2 != 0 and dx2 != 0 and dx3 != 0:
        k = (ax3 - cx3) / dx3
        s = (cx2 - ax2 + (((ax3 * dx2) - (cx3 * dx2))/dx3))/bx2
    if dx1 == 0 and bx1 != 0 and dx2 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 + (bx2 * s) - cx2)/dx2 
    if dx2 == 0 and bx2 != 0 and dx1 != 0: 
        s = (cx2-ax2) / bx2
        k = (ax1 + (bx1 * s) - cx1) / dx1
    if dx3 == 0 and bx1 != 0 and bx2 != 0 and bx3 != 0 and dx1 != 0 and dx2 != 0: 
        s = (cx3 - ax3) / bx3
        k = (ax2 - cx2 + (((cx3 * bx2) - (ax3 * bx2))/bx3)) / dx2
    if bx3 == 0 and dx3 == 0 and bx1 == 0 and dx1 != 0 and dx2 != 0:
        s = (ax1 - cx1) / dx1
        k = (ax2 + (bx2 * s) - cx2) / dx2
    if bx3 == 0 and dx3 == 0 and bx2 == 0 and dx1 != 0 and dx2 != 0:
        s = (ax2 - cx2) / dx2
        k = (ax1 + (bx1*s) - cx1) / dx1
    if bx3 == 0 and dx3 == 0 and dx1 == 0 and bx1 != 0 and dx2 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 + (bx2*s) - cx2) / dx2
    if bx3 == 0 and dx3 == 0 and dx2 == 0:
        s = (cx2-ax2) / bx2
        k = (ax1 + (bx1*s) - cx1) / dx1
    if bx3 == 0 and dx3 == 0 and bx1 == 0 and dx2 == 0 and bx2 != 0 and dx1 != 0:
        s = (cx2 - ax2) / bx2
        k = (ax1 - cx1) / dx1
    if bx3 == 0 and dx3 == 0 and bx2 == 0 and dx1 == 0 and bx1 != 0 and dx2 != 0:
        s = (cx1 - ax1) / bx1
        k = (ax2 - cx2) / dx2
    if dx3 == 0 and bx3 == 0 and ax3 == cx3 and bx1 != 0 and bx2 != 0 and dx1 != 0 and dx2 != 0:
        k = ((ax2/dx2)-(cx2/dx2)+((bx2*cx1)/(dx2*bx1))-((bx2*ax1)/(dx2*bx1)))/(1-((bx2*dx1)/(dx2*dx1)))#
        s = (cx1-ax1+(dx1*k))/bx1
    if dx3 == 0 and bx3 == 0 and ax3 != cx3:
        return None
    
    # if none is equal to 0
    if (bx2 * dx1) / (dx2 * dx1) != 1:
        k = ((ax2/dx2)-(cx2/dx2)+((bx2*cx1)/(dx2*bx1))-((bx2*ax1)/(dx2*bx1)))/(1-((bx2*dx1)/(dx2*dx1)))
        s = (cx3 + (dx3 * k) - ax3) / bx3

    # comparing if s and k fit in the equation 
    test_point_a = g1.point(s)
    test_point_b = g2.point(k)

    # s and k don't fit the lines don't cross 
    if not vector_is_equal(test_point_a, test_point_b):
        return False

    # points are equal 
    return test_point_a
