import math

class line:
    def __init__(self, v1, v2):
        self.supportV = [0, 0, 0]
        self.directionV = [0, 0, 0]
        self.lower_z_bound = 0
        self.upper_z_bound = 0
        self.pointA = v1
        self.pointB = v2
        self.calcV(v1, v2)
        
    def print(self):
        print("sV: \n{}".format(self.supportV))
        print("dV: \n{}".format(self.directionV))
        print("lb: \n{}".format(self.lower_z_bound))
        print("ub: \n{}".format(self.upper_z_bound))
        print("pA: \n{}".format(self.pointA))
        print("pB \n{}".format(self.pointB))
 
    def point(self, k):
        x1 = self.supportV[0] + self.directionV[0] * k
        x2 = self.supportV[1] + self.directionV[1] * k
        x3 = self.supportV[2] + self.directionV[2] * k

        return [x1, x2, x3]

    def calcV(self, v1, v2):
        """
        calculates support 
        and directional vector for the line

        also determins the upper and lower bound of the 
        line to see if pointis is bewtween those
        """

        # print("\n\n\nv1 = {}\n\n\n".format(v1))
        lower_x = v1[0]
        upper_x = v2[0]

        if lower_x > upper_x: 
            lower_x, upper_x = upper_x, lower_x

        lower_y = v1[1]
        upper_y = v2[1]

        if lower_y > upper_y: 
            lower_y, upper_y = upper_y, lower_y

        lower_z = v1[2]
        upper_z = v2[2]

        if lower_z > upper_z: 
            lower_z, upper_z = upper_z, lower_z
            v1, v2 = v2, v1

        x = v2[0] - v1[0]
        y = v2[1] - v1[1]
        z = v2[2] - v1[2]

        dirV = [x, y, z]
        supportV = v1
        self.supportV = supportV
        self.directionV = dirV
        self.lower_x_bound = lower_x
        self.upper_x_bound = upper_x
        self.lower_y_bound = lower_y
        self.upper_y_bound = upper_y
        self.lower_z_bound = lower_z
        self.upper_z_bound = upper_z

    

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
    three ways:

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

    # could be more difficult
    
    finde a matching variable 

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
    
    # if none is equal to 0
    k = ((ax2/dx2)-(cx2/dx2)+((bx2*cx1)/(dx2*bx1))-((bx2*ax1)/(dx2*bx1)))/(1-((bx2*dx1)/(dx2*dx1)))
    s = (cx3 + (dx3 * k) - ax3) / bx3

    # if only bx3 is equal to 0 dx3 != 0
    k = (ax3 - cx3) / dx3
    s = (cx2 - ax2 + (((ax3 * dx2) - (cx3 * dx2))/dx3))/bx2
    
    # if only dx3 == 0 and bx3 != 0
    s = (cx3 - ax3) / bx3
    k = (ax2 - cx2 + (((cx3 * bx2) - (ax3 * bx2))/bx3)) / dx2

    # if dx3 and bx3 == 0 
    # interesting because we use it the most for the infill calcuations
    # ax3 == cx3 --> otherwise no solution
    k = ((ax2/dx2)-(cx2/dx2)+((bx2*cx1)/(dx2*bx1))-((bx2*ax1)/(dx2*bx1)))/(1-((bx2*dx1)/(dx2*dx1)))
    


    """
    now setting these inside the lines and if 
    the points are equal there is a intersection 

    think about the edge cases with div by 0 
    cases:

    bx1 != 0
    bx2 != 0
    bx3 != 0
    dx1 != 0
    dx2 != 0 

    (bx2 * dx1) / (dx2 * dx1) != 1
    """

    # comparing if s and k fit in the equation 
    test_point_a = g1.point(s)
    test_point_b = g2.point(k)

    # s and k don't fit the lines don't cross 
    if not vector_is_equal(test_point_a, test_point_b):
        return False

    # points are equal 
    return test_point_a
