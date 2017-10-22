import numpy as np
#import copy




f12 = open ( './data/si.txt' , 'r')
l = np.loadtxt(f12, dtype='f', delimiter=',')
l=np.delete(l, 0, 1)
l=np.delete(l, 0, 1)
l=np.delete(l, 0, 1)
l=np.delete(l, 0, 1)



rang=int(np.prod(l.shape)/4)
z=np.zeros([rang,4])



stop=200

fl=np.zeros(6)

for i in range (rang):
    if i % 1000 == 0:
        print(i)
        print(fl)
    a=0
    b=0
    st0=l[i,2]-stop
    op0=l[i,2]
    st1=l[i,2]+stop
    op1=l[i,2]
    for j in range (rang-i-1):
            
        if a==0:
            z[i,2]=z[i,2]+1
            if l[i+j+1,1]<st0:
                
                z[i,0]=st0-op0-0.0001*l[i+j+1,2]
                a=1

            '''if (c1>c0 and c1>c2 and a==0):
                a=2
                total=total+st-op-0.0001*l[i+j+1,2]
                print(total)'''

            if l[i+j+1,0]>st0+stop:
                st0=l[i+j+1,0]-stop

            '''if l[i+j+1,0]>op+stop*2.5:
                a=2
                total=total+stop*2.5-0.0001*l[i+j+1,2]
                print(total)'''

            

        if b==0:
            z[i,3]=z[i,3]+1
            if l[i+j+1,0]>st1:
                b=2
                z[i,1]=op1-st1-0.0001*l[i+j+1,2]
          
            '''if (c0>c1 and c0>c2 and a==1):
                a=2
                total=total-st+op-0.0001*l[i+j+1,2]
                print(total)'''

            if l[i+j+1,1]<st1-stop:
                st1=l[i+j+1,1]+stop

            '''if l[i+j+1,1]<op-stop*2.5:
                a=2
                total=total+stop*2.5-0.0001*l[i+j+1,2]
                print(total)'''

        if a>0 and b>0:
            if z[i,1]>200 and z[i,2]<20:
                fl[0]=fl[0]+1
            if z[i,1]>200 and z[i,2]<40:
                fl[1]=fl[1]+1
            if z[i,1]>200 and z[i,2]<60:
                fl[2]=fl[2]+1
            if z[i,0]>200 and z[i,3]<20:
                fl[3]=fl[3]+1
            if z[i,0]>200 and z[i,3]<40:
                fl[4]=fl[4]+1
            if z[i,0]>200 and z[i,3]<60:
                fl[5]=fl[5]+1
            break
print(fl)
f2 = open ( './data/trend_200_si.txt' , 'wb')
np.savetxt(f2, z,fmt='%f', delimiter=',',newline='\r\n')