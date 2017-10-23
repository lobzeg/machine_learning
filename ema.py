
import numpy as np

f = open ( './data/si.txt' , 'r')
l = np.loadtxt(f, dtype='f', delimiter=',')
s=20


print (s)
size=np.prod(l.shape)/8

size = int (size)
print(size)

l=np.delete(l, 0, 1)
l=np.delete(l, 0, 1)
l=np.delete(l, 0, 1)
l=np.delete(l, 0, 1)

print(np.prod(l.shape)/4)



#size=size-s
size = int (size)
k=np.zeros([size])
k[0]=l[0,2]
a=2/(s+1)
for j in range(1,size):
    k[j]=(1-a)*k[j-1]+a*l[j,2]
       
m=np.zeros([size])
n=np.zeros([size])
for j in range(1,size):
    m[j]=k[j]-k[j-1]
    n[j]=l[j,2]-k[j]
print(np.prod(m.shape))
print(np.prod(n.shape))
f2 = open ( './data/exp_ma_20_si.txt' , 'wb')
np.savetxt(f2, m,fmt='%f', delimiter=',',newline='\r\n')
f3 = open ( './data/price-exp_ma_20_si.txt' , 'wb')
np.savetxt(f3, n,fmt='%f', delimiter=',',newline='\r\n')
