import math

class Line:
    def __init__(self, support, direction):
        self.sV = support
        self.dV = direction
    
    def lenV(self, v):
        return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    
    def unitV(self, v):
        x1 = v[0] / self.lenV(v)
        x2 = v[1] / self.lenV(v)
        x3 = v[2] / self.lenV(v)  
        return [x1, x2, x3]

    def print(self):
        print('---class Line---')
        print('sV: {}'.format(self.sV))
        print('sD: {}'.format(self.sD))
        print('----------------')
    
    def point(self, s):
        x1 = self.dV[0] + self.sV[0] * s
        x2 = self.dV[1] + self.sV[1] * s
        x3 = self.dV[2] + self.sV[2] * s
        return [x1, x2, x3]

    def info(self):
        print(type(self))
        print("Support V: {}".format(self.sV))
        print("Direction V: {}".format(self.dV))
        


class ComplexLine:
    def __init__(self, v1, v2):
        self.a = v1
        self.b = v2
        self.sV = [0, 0, 0]
        self.dV = [0, 0, 0]
        self.lower_x_bound = 0
        self.higher_x_bound = 0
        self.lower_y_bound = 0
        self.higher_y_bound = 0
        self.lower_z_bound = 0
        self.higher_z_bound = 0
        
        
        self.calcVar(v1, v2)
        
    def calcVar(self, v1, v2):
        """Calculates missing values

        Args:
            v1 (list): 3d vector
            v2 (list): 3d vector
        """
        xa1 = v1[0]
        xb1 = v2[0]
        xa2 = v1[1]
        xb2 = v2[1]
        xa3 = v1[2]
        xb3 = v2[2]
        
        if xa1 > xb1: 
            self.higher_x_bound = xa1
            self.lower_x_bound = xb1
        else: 
            self.higher_x_bound = xb1
            self.lower_x_bound = xa1
        if xa2 > xb2: 
            self.higher_y_bound = xa2
            self.lower_y_bound = xb2
        else: 
            self.higher_y_bound = xb2
            self.lower_y_bound = xa2
        if xa3 > xb3: 
            self.higher_z_bound = xa3
            self.lower_z_bound = xb3
        else: 
            self.higher_z_bound = xb3
            self.lower_z_bound = xa3
        
        x = v2[0] - v1[0]
        y = v2[1] - v1[1]
        z = v2[2] - v1[2]
        dirV = [x, y, z]
        supportV = v1
        
        self.sV = supportV
        self.dV = dirV                
    
    def calcVfromX(self, x_value):
        if self.directionV[0] == 0:
            return None

        v = (x_value - self.sV[0]) / self.dV[0] 
        x1 = self.sV[0] + self.dV[0] * v

        # check if point is in between the original points 

        if not x1 >= self.lower_x_bound or not x1 <= self.higher_x_bound:
            return None
        
        x2 = self.sV[1] + self.dV[1] * v
        x3 = self.sV[2] + self.dV[2] * v
        
        return [x1, x2, x3]

    def calcVfromY(self, y_value):
        if self.dV[1] == 0:
            return None

        v = (y_value - self.sV[1]) / self.dV[1] 
        x2 = self.sV[1] + self.dV[1] * v

        # check if point is in between the original points 
        if not x2 >= self.lower_y_bound or not x2 <= self.higher_y_bound:
            return None
        
        x1 = self.sV[0] + self.dV[0] * v
        x3 = self.sV[2] + self.dV[2] * v
        
        return [x1, x2, x3]

    def calcVfromZ(self, z_value):
        if self.dV[2] == 0:
            return None

        v = (z_value - self.sV[2]) / self.dV[2] 
        x3 = self.sV[2] + self.dV[2] * v

        # check if point is in between the original points 
        if not x3 >= self.lower_z_bound or not x3 <= self.higher_z_bound:
            return None
        
        x1 = self.sV[0] + self.dV[0] * v
        x2 = self.sV[1] + self.dV[1] * v
        
        return [x1, x2, x3]
    
    def lenV(self, v):
        return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    
    def unitV(self, v):
        x1 = v[0] / self.lenV(v)
        x2 = v[1] / self.lenV(v)
        x3 = v[2] / self.lenV(v)  
        return [x1, x2, x3]

    def point(self, s):
        x1 = self.sV[0] + self.dV[0] * s
        x2 = self.sV[1] + self.dV[1] * s
        x3 = self.sV[2] + self.dV[2] * s
        return [x1, x2, x3]
    
    def pointInsideLine(self, point):
        """
        checks if the given point is inside the bounds of the line
        give point has to be first calculated to be on the line
        here is the check if it is in bounds of the dimensions of the line
        """
        if point[0] < self.lower_x_bound or point[0] > self.higher_x_bound:
            return False
        if point[1] < self.lower_y_bound or point[1] > self.higher_y_bound:
            return False
        if point[2] < self.lower_z_bound or point[2] > self.higher_z_bound:
            return False
        return True
        

    def print(self):
        print('---ComplexLine---')
        print('sV: {}'.format(self.sV))
        print('dV: {}'.format(self.dV))
        print('a: {}'.format(self.a))
        print('b: {}'.format(self.b))
        print('hx: {}'.format(self.higher_x_bound))
        print('lx: {}'.format(self.lower_x_bound))
        print('hy: {}'.format(self.higher_y_bound))
        print('ly: {}'.format(self.lower_y_bound))
        print('hz: {}'.format(self.higher_z_bound))
        print('lz: {}'.format(self.lower_z_bound))
        print('------')

    def info(self):
        print(type(self))
        print("Support V: {}".format(self.sV))
        print("Direction V: {}".format(self.dV))