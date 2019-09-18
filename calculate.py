class Nutrients:
    #Method
    def Protein(self,cal,p,c,f):
        a = (float(cal)*p)/100
        b = (float(cal)*c)/100
        c = (float(cal)*f)/100
        result = []
        result.insert(0,a)
        result.insert(1,b)
        result.insert(2,c)
        return result

    def Carbohydrate(self,cal,p,c,f):
        a = (float(cal)*p)/100
        b = (float(cal)*c)/100
        c = (float(cal)*f)/100
        result = []
        result.insert(0,a)
        result.insert(1,b)
        result.insert(2,c)
        return result
    
    def Fat(self,cal,p,c,f):
        a = (float(cal)*p)/100
        b = (float(cal)*c)/100
        c = (float(cal)*f)/100
        result = []
        result.insert(0,a)
        result.insert(1,b)
        result.insert(2,c)
        return result
    
    def Energy(self,a,b,c):
        Total = a+b+c
        return Total

    def Calculate(self,n):
        Total = []
        Total.insert(0,(4*n[0])+(4*n[1])+(9*n[2]))
        return Total.pop()

Call = Nutrients()