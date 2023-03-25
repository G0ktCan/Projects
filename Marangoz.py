class App:
    def cal(self,weight,height,matareil,alan,f):
        weight = self.weight
        height = self.height
        mat = self.matareil
        alan = weight  * height
        f = self.f
        if(mat == 'çam'):
            f = alan * 10
        elif(mat == 'meşe'):
            f = alan  * 15
            
cal(int(input),int(input),int(input)        
      