c1 = .2369268850
c2 = .4786286705
c3 = .5688888889
c4 = .4786286705
c5 = .2369268850

r1 = .9061798459
r2 = .5384693101
r3 = 0
r4 = -.5384693101
r5 = -.9061798459
 ret = 0
 
 
  for i = 1:16
    a = (i-1)*3
    b = (i-1)*3 + 3
    argum1 = ((b-a)*(r1) + (b-a))/2
    argum2 = ((b-a)*(r2) + (b-a))/2
    argum3 = ((b-a)*(r3) + (b-a))/2
    argum4 = ((b-a)*(r4) + (b-a))/2
    argum5 = ((b-a)*(r5) + (b-a))/2
    
    
    
    
    ret = ret+ ((b-a)/2)*c1*sqrt(1+(cos(argum1))**2) + ((b-a)/2)*c2*sqrt(1+(cos(argum2))**2)+ ((b-a)/2)*c3*sqrt(1+(cos(argum2))**2) +((b-a)/2)*c4*sqrt(1+(cos(argum4))**2) + ((b-a)/2)*c5*sqrt(1+(cos(argum5))**2)
    end
    
    