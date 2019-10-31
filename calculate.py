import numpy as np


class Nutrients:
    # Attribute

    # Method
    def Calculate(self,val, n):
        call = int(val)
        a = np.asarray(n)
        Total = (a*call)/100
        return Total

    def Energy(self, a, b, c):
        Total = a.sum()+b.sum()+c.sum()
        return Total

    def Total_Calculate(self, n):
        a = np.asanyarray(n)
        b = np.array([4, 4, 9], dtype=int)
        Total = a*b
        return Total


Call = Nutrients()
