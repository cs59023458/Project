import numpy as np
class Nutrients:
    #Method
    def Calculate(self,cal,p,c,f):
        a = np.array([p,c,f])
        a = (a*cal)/100
        result = []
        result.insert(0,a)
        result.insert(1,b)
        result.insert(2,c)
        return result
    
    def Energy(self,a,b,c):
        Total = a+b+c
        return Total

    def Total_Calculate(self,n):
        Total = []
        Total.insert(0,(4*n[0])+(9*n[1])+(9*n[2]))
        return Total.pop()

Call = Nutrients()
