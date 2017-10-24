import numpy as np

f1 = open ( '../data/si.txt' , 'r')
l = np.loadtxt(f1, dtype='f', delimiter=',')
l = np.delete(l, 0, 1)
l = np.delete(l, 0, 1)
l = np.delete(l, 0, 1)
l = np.delete(l, 0, 1)

rang = int(np.prod(l.shape)/4)
z = np.zeros([rang,4])
stop = 200


for i in range (rang):
    if i % 1000 == 0:
        print(i)
    a = 0
    b = 0
    st0 = l[i,2] - stop
    op0 = l[i,2]
    st1 = l[i,2] + stop
    op1 = l[i,2]
    for j in range (rang - i - 1):
            
        if a == 0:
            z[i, 2] = z[i, 2] + 1
            if l[i + j + 1, 1] < st0:
                
                z[i, 0] = st0 - op0 - 0.0001 * l[i + j + 1, 2]
                a=1

            if l[i + j + 1, 0] > st0 + stop:
                st0 = l[i + j + 1,0] - stop


        if b == 0:
            z[i, 3] = z[i, 3] + 1
            if l[i + j + 1, 0] > st1:
                b = 2
                z[i, 1] = op1 - st1 - 0.0001 * l[i + j + 1, 2]
  
            if l[i + j + 1, 1] < st1 - stop:
                st1 = l[i + j + 1, 1] + stop

f2 = open ( '../data/sl_200_si.txt' , 'wb')
np.savetxt(f2, z,fmt='%f', delimiter=',',newline='\r\n')