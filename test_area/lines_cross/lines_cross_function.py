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

def compare_dir_v(dir_a, dir_b):
    """
    copares two vectors if they are equal 
    equal means == or * -1 == 
    """

    if dir_a[0] == dir_b[0] and dir_a[1] == dir_b[1] and dir_a[2] == dir_b[2]:
        return True
    elif (dir_a[0] * (-1)) == dir_b[0] and (dir_a[1] * (-1)) == dir_b[1] and (dir_a[2] * (-1)) == dir_b[2]:
        return True
    else: 
        return False 

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

    



