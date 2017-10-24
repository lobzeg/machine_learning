import numpy as np

f = open ( '../data/si.txt' , 'r')
l = np.loadtxt(f, dtype='f', delimiter=',')
f1 = open ( '../data/exp_ma_20_si.txt' , 'r')
l1 = np.loadtxt(f1, dtype='f', delimiter=',')
f2 = open ( '../data/exp_ma_100_si.txt' , 'r')
l2 = np.loadtxt(f2, dtype='f', delimiter=',')
f3 = open ( '../data/price-exp_ma_20_si.txt' , 'r')
l3 = np.loadtxt(f3, dtype='f', delimiter=',')
f4 = open ( '../data/price-exp_ma_100_si.txt' , 'r')
l4 = np.loadtxt(f4, dtype='f', delimiter=',')

s = 20
size = int((np.prod(l.shape) / 8) - s)

l = np.delete(l, 0, 1)
l = np.delete(l, 0, 1)
l = np.delete(l, 0, 1)
l = np.delete(l, 0, 1)

k = np.zeros([size, 8 * s])
for j in range(1, size + 1):
    for i in range(0, s):
        k[j - 1, i] = l[j + i, 0] - l[j + i - 1, 0]
        k[j - 1, s + i] = l[j + i, 1] - l[j + i - 1, 1]
        k[j - 1, 2 * s + i] = l[j + i,2] - l[j + i - 1 ,2]
        k[j - 1, 3 * s + i] = l[j + i,3] / 1000
        k[j - 1, 4 * s + i] = l1[j + i]
        k[j - 1, 5 * s + i] = l2[j + i]
        k[j - 1, 6 * s + i] = l3[j + i]
        k[j - 1, 7 * s + i] = l4[j + i]

f5 = open ( '../data/extended_new_si.txt' , 'wb')
np.savetxt(f5, k,fmt='%f', delimiter=',', newline='\r\n')
