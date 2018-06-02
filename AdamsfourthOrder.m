function AdamsfourthOrder(a,b,f, N, alph)
  h = (b-a)/N
  t = a
  w = alph
  wVect = zeros(4)
  for i = 1:3
    k1 = *h*f(t,w)
    k2 = h*f(t+h/2, w+k1/2)
    k3 = h*f(t+h/2,w+k2/2)
    k4 = h*f(t+h/2,w+k3)
    t = t +i*h
    w = w + (k1+k2+k3+k4)/6
    wVect[i] = w 
    
  end
  
  