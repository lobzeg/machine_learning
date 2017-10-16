

import numpy as np
import copy


def main(shift,rang):

    f0 = open ( '/home/creo/projects/python/test/GW1.txt' , 'r')
    f1 = open ( '/home/creo/projects/python/test/GW2.txt' , 'r')
    f2 = open ( '/home/creo/projects/python/test/GW3.txt' , 'r')
    f3 = open ( '/home/creo/projects/python/test/GW4.txt' , 'r')
    f4 = open ( '/home/creo/projects/python/test/Gb1.txt' , 'r')
    f5 = open ( '/home/creo/projects/python/test/Gb2.txt' , 'r')
    f6 = open ( '/home/creo/projects/python/test/Gb3.txt' , 'r')
    f7 = open ( '/home/creo/projects/python/test/Gb4.txt' , 'r')

    W1 = np.loadtxt(f0, dtype='f', delimiter=',')
    W2 = np.loadtxt(f1, dtype='f', delimiter=',')
    W3 = np.loadtxt(f2, dtype='f', delimiter=',')
    W4 = np.loadtxt(f3, dtype='f', delimiter=',')
    b1 = np.loadtxt(f4, dtype='f', delimiter=',')
    b2 = np.loadtxt(f5, dtype='f', delimiter=',')
    b3 = np.loadtxt(f6, dtype='f', delimiter=',')
    b4 = np.loadtxt(f7, dtype='f', delimiter=',')


    f01 = open ( '/home/creo/projects/python/test/GW11.txt' , 'r')
    f11 = open ( '/home/creo/projects/python/test/GW21.txt' , 'r')
    f21 = open ( '/home/creo/projects/python/test/GW31.txt' , 'r')
    f31 = open ( '/home/creo/projects/python/test/GW41.txt' , 'r')
    f41 = open ( '/home/creo/projects/python/test/Gb11.txt' , 'r')
    f51 = open ( '/home/creo/projects/python/test/Gb21.txt' , 'r')
    f61 = open ( '/home/creo/projects/python/test/Gb31.txt' , 'r')
    f71 = open ( '/home/creo/projects/python/test/Gb41.txt' , 'r')

    W11 = np.loadtxt(f01, dtype='f', delimiter=',')
    W21 = np.loadtxt(f11, dtype='f', delimiter=',')
    W31 = np.loadtxt(f21, dtype='f', delimiter=',')
    W41 = np.loadtxt(f31, dtype='f', delimiter=',')
    b11 = np.loadtxt(f41, dtype='f', delimiter=',')
    b21 = np.loadtxt(f51, dtype='f', delimiter=',')
    b31 = np.loadtxt(f61, dtype='f', delimiter=',')
    b41 = np.loadtxt(f71, dtype='f', delimiter=',')


    f02 = open ( '/home/creo/projects/python/test/GW12.txt' , 'r')
    f12 = open ( '/home/creo/projects/python/test/GW22.txt' , 'r')
    f22 = open ( '/home/creo/projects/python/test/GW32.txt' , 'r')
    f32 = open ( '/home/creo/projects/python/test/GW42.txt' , 'r')
    f42 = open ( '/home/creo/projects/python/test/Gb12.txt' , 'r')
    f52 = open ( '/home/creo/projects/python/test/Gb22.txt' , 'r')
    f62 = open ( '/home/creo/projects/python/test/Gb32.txt' , 'r')
    f72 = open ( '/home/creo/projects/python/test/Gb42.txt' , 'r')

    W12 = np.loadtxt(f02, dtype='f', delimiter=',')
    W22 = np.loadtxt(f12, dtype='f', delimiter=',')
    W32 = np.loadtxt(f22, dtype='f', delimiter=',')
    W42 = np.loadtxt(f32, dtype='f', delimiter=',')
    b12 = np.loadtxt(f42, dtype='f', delimiter=',')
    b22 = np.loadtxt(f52, dtype='f', delimiter=',')
    b32 = np.loadtxt(f62, dtype='f', delimiter=',')
    b42 = np.loadtxt(f72, dtype='f', delimiter=',')


    ft0 = open ( '/home/creo/projects/python/test/GWT1.txt' , 'r')
    ft1 = open ( '/home/creo/projects/python/test/GWT2.txt' , 'r')
    ft2 = open ( '/home/creo/projects/python/test/GWT3.txt' , 'r')
    ft3 = open ( '/home/creo/projects/python/test/GWT4.txt' , 'r')
    ft4 = open ( '/home/creo/projects/python/test/GbT1.txt' , 'r')
    ft5 = open ( '/home/creo/projects/python/test/GbT2.txt' , 'r')
    ft6 = open ( '/home/creo/projects/python/test/GbT3.txt' , 'r')
    ft7 = open ( '/home/creo/projects/python/test/GbT4.txt' , 'r')

    Wt1 = np.loadtxt(ft0, dtype='f', delimiter=',')
    Wt2 = np.loadtxt(ft1, dtype='f', delimiter=',')
    Wt3 = np.loadtxt(ft2, dtype='f', delimiter=',')
    Wt4 = np.loadtxt(ft3, dtype='f', delimiter=',')
    bt1 = np.loadtxt(ft4, dtype='f', delimiter=',')
    bt2 = np.loadtxt(ft5, dtype='f', delimiter=',')
    bt3 = np.loadtxt(ft6, dtype='f', delimiter=',')
    bt4 = np.loadtxt(ft7, dtype='f', delimiter=',')


    ft01 = open ( '/home/creo/projects/python/test/GWT11.txt' , 'r')
    ft11 = open ( '/home/creo/projects/python/test/GWT21.txt' , 'r')
    ft21 = open ( '/home/creo/projects/python/test/GWT31.txt' , 'r')
    ft31 = open ( '/home/creo/projects/python/test/GWT41.txt' , 'r')
    ft41 = open ( '/home/creo/projects/python/test/GbT11.txt' , 'r')
    ft51 = open ( '/home/creo/projects/python/test/GbT21.txt' , 'r')
    ft61 = open ( '/home/creo/projects/python/test/GbT31.txt' , 'r')
    ft71 = open ( '/home/creo/projects/python/test/GbT41.txt' , 'r')

    Wt11 = np.loadtxt(ft01, dtype='f', delimiter=',')
    Wt21 = np.loadtxt(ft11, dtype='f', delimiter=',')
    Wt31 = np.loadtxt(ft21, dtype='f', delimiter=',')
    Wt41 = np.loadtxt(ft31, dtype='f', delimiter=',')
    bt11 = np.loadtxt(ft41, dtype='f', delimiter=',')
    bt21 = np.loadtxt(ft51, dtype='f', delimiter=',')
    bt31 = np.loadtxt(ft61, dtype='f', delimiter=',')
    bt41 = np.loadtxt(ft71, dtype='f', delimiter=',')


    ft02 = open ( '/home/creo/projects/python/test/GWT12.txt' , 'r')
    ft12 = open ( '/home/creo/projects/python/test/GWT22.txt' , 'r')
    ft22 = open ( '/home/creo/projects/python/test/GWT32.txt' , 'r')
    ft32 = open ( '/home/creo/projects/python/test/GWT42.txt' , 'r')
    ft42 = open ( '/home/creo/projects/python/test/GbT12.txt' , 'r')
    ft52 = open ( '/home/creo/projects/python/test/GbT22.txt' , 'r')
    ft62 = open ( '/home/creo/projects/python/test/GbT32.txt' , 'r')
    ft72 = open ( '/home/creo/projects/python/test/GbT42.txt' , 'r')

    Wt12 = np.loadtxt(ft02, dtype='f', delimiter=',')
    Wt22 = np.loadtxt(ft12, dtype='f', delimiter=',')
    Wt32 = np.loadtxt(ft22, dtype='f', delimiter=',')
    Wt42 = np.loadtxt(ft32, dtype='f', delimiter=',')
    bt12 = np.loadtxt(ft42, dtype='f', delimiter=',')
    bt22 = np.loadtxt(ft52, dtype='f', delimiter=',')
    bt32 = np.loadtxt(ft62, dtype='f', delimiter=',')
    bt42 = np.loadtxt(ft72, dtype='f', delimiter=',')


    

    f111 = open ( '/home/creo/projects/python/test/alt_new_si.txt' , 'r')
    f112 = open ( '/home/creo/projects/python/test/trend_200_si.txt' , 'r')
    f113 = open( '/home/creo/projects/python/test/extended_new_si.txt' , 'r')
    m = np.loadtxt(f113, dtype='f', delimiter=',')
    k = np.loadtxt(f111, dtype='f', delimiter=',')
    l = np.loadtxt(f112, dtype='f', delimiter=',')
    

    s=20
    #s1=20





    a=2
    total=np.zeros(5)
    #rang=10000
    totalmax=np.zeros(5)
    maxdown=np.zeros(5)
    #shift=35000
    stop=200

    i=int(0) 
    while i < rang:
        #if i % 1000 == 0:
            #print(i)
        x=k[i]
        z=m[i]
        
        y1 = np.matmul(x,W1) + b1
        y2 = np.matmul(y1,W2) + b2
        y21 = np.matmul(y2,W3) + b3
        y3 = np.matmul(y21,W4) + b4
        d=max(y3)
        #print(y3)
        y3[0]=y3[0]-d
        y3[1]=y3[1]-d
        y3[2]=y3[2]-d
        scoreMatExp = np.exp(np.asarray(y3))
        y4 = scoreMatExp / scoreMatExp.sum(0)
        c=copy.copy(y4)


        #print(c)
        #c0=c[0]
        #c1=c[1]
        #c2=c[2]
        if c[0]>c[1] and c[0]>c[2]:
            total[0]=total[0]+l[shift+i+19,0]
            i=i+int(l[shift+i+19,2]-1)
            if totalmax[0]-total[0]>maxdown[0]:
                maxdown[0]=copy.copy(totalmax[0]-total[0])
            if total[0]>totalmax[0]:
                totalmax[0]=copy.copy(total[0])
        if c[1]>c[0] and c[1]>c[2]:
            total[0]=total[0]+l[shift+i+19,1]
            i=i+int(l[shift+i+19,3]-1)
            if totalmax[0]-total[0]>maxdown[0]:
                maxdown[0]=copy.copy(totalmax[0]-total[0])
            if total[0]>totalmax[0]:
                totalmax[0]=copy.copy(total[0])
        i+=1

    i=int(0) 
    while i < rang:
        #if i % 1000 == 0:
            #print(i)
        x=k[i]
        z=m[i]
        
        y1 = np.matmul(x,W1) + b1
        y2 = np.matmul(y1,W2) + b2
        y21 = np.matmul(y2,W3) + b3
        y3 = np.matmul(y21,W4) + b4
        d=max(y3)
        #print(y3)
        y3[0]=y3[0]-d
        y3[1]=y3[1]-d
        y3[2]=y3[2]-d
        scoreMatExp = np.exp(np.asarray(y3))
        y4 = scoreMatExp / scoreMatExp.sum(0)
        c=copy.copy(y4)

        yt1 = np.matmul(z,Wt1) + bt1
        yt2 = np.matmul(yt1,Wt2) + bt2
        yt21 = np.matmul(yt2,Wt3) + bt3
        yt3 = np.matmul(yt21,Wt4) + bt4
        d=max(yt3)
        yt3[0]=yt3[0]-d
        yt3[1]=yt3[1]-d
        yt3[2]=yt3[2]-d
        scoreMatExp = np.exp(np.asarray(yt3))
        yt4 = scoreMatExp / scoreMatExp.sum(0)
        ct=copy.copy(yt4)


        if c[0]>c[1] and c[0]>c[2] and ct[0]>ct[1] and ct[0]>ct[2]:
            total[1]=total[1]+l[shift+i+19,0]
            i=i+int(l[shift+i+19,2]-1)
            if totalmax[1]-total[1]>maxdown[1]:
                maxdown[1]=copy.copy(totalmax[1]-total[1])
            if total[1]>totalmax[1]:
                totalmax[1]=copy.copy(total[1])
        if c[1]>c[0] and c[1]>c[2] and ct[1]>ct[0] and ct[1]>ct[2]:
            total[1]=total[1]+l[shift+i+19,1]
            i=i+int(l[shift+i+19,3]-1)
            if totalmax[1]-total[1]>maxdown[1]:
                maxdown[1]=copy.copy(totalmax[1]-total[1])
            if total[1]>totalmax[1]:
                totalmax[1]=copy.copy(total[1])
        i+=1

    i=int(0) 
    while i < rang:
        #if i % 1000 == 0:
            #print(i)
        x=k[i]
        z=m[i]
        
        y1 = np.matmul(x,W1) + b1
        y2 = np.matmul(y1,W2) + b2
        y21 = np.matmul(y2,W3) + b3
        y3 = np.matmul(y21,W4) + b4
        d=max(y3)
        #print(y3)
        y3[0]=y3[0]-d
        y3[1]=y3[1]-d
        y3[2]=y3[2]-d
        scoreMatExp = np.exp(np.asarray(y3))
        y4 = scoreMatExp / scoreMatExp.sum(0)
        c=copy.copy(y4)


        yt1 = np.matmul(z,Wt11) + bt11
        yt2 = np.matmul(yt1,Wt21) + bt21
        yt21 = np.matmul(yt2,Wt31) + bt31
        yt3 = np.matmul(yt21,Wt41) + bt41
        d=max(yt3)
        yt3[0]=yt3[0]-d
        yt3[1]=yt3[1]-d
        yt3[2]=yt3[2]-d
        scoreMatExp = np.exp(np.asarray(yt3))
        yt4 = scoreMatExp / scoreMatExp.sum(0)
        ct1=copy.copy(yt4)

        yt1 = np.matmul(z,Wt12) + bt12
        yt2 = np.matmul(yt1,Wt22) + bt22
        yt21 = np.matmul(yt2,Wt32) + bt32
        yt3 = np.matmul(yt21,Wt42) + bt42
        d=max(yt3)
        yt3[0]=yt3[0]-d
        yt3[1]=yt3[1]-d
        yt3[2]=yt3[2]-d
        scoreMatExp = np.exp(np.asarray(yt3))
        yt4 = scoreMatExp / scoreMatExp.sum(0)
        ct2=copy.copy(yt4)


        if c[0]>c[1] and c[0]>c[2] and ct1[0]>ct1[1] and ct1[0]>ct1[2]:
            total[2]=total[2]+l[shift+i+19,0]
            i=i+int(l[shift+i+19,2]-1)
            if totalmax[2]-total[2]>maxdown[2]:
                maxdown[2]=copy.copy(totalmax[2]-total[2])
            if total[2]>totalmax[2]:
                totalmax[2]=copy.copy(total[2])
        if c[1]>c[0] and c[1]>c[2] and ct2[1]>ct2[0] and ct2[1]>ct2[2]:
            total[2]=total[2]+l[shift+i+19,1]
            i=i+int(l[shift+i+19,3]-1)
            if totalmax[2]-total[2]>maxdown[2]:
                maxdown[2]=copy.copy(totalmax[2]-total[2])
            if total[2]>totalmax[2]:
                totalmax[2]=copy.copy(total[2])
        i+=1

    i=int(0) 
    while i < rang:
        #if i % 1000 == 0:
            #print(i)
        x=k[i]
        z=m[i]
        
        y1 = np.matmul(x,W11) + b11
        y2 = np.matmul(y1,W21) + b21
        y21 = np.matmul(y2,W31) + b31
        y3 = np.matmul(y21,W41) + b41
        d=max(y3)
        #print(y3)
        y3[0]=y3[0]-d
        y3[1]=y3[1]-d
        y3[2]=y3[2]-d
        scoreMatExp = np.exp(np.asarray(y3))
        y4 = scoreMatExp / scoreMatExp.sum(0)
        c1=copy.copy(y4)

        y1 = np.matmul(x,W12) + b12
        y2 = np.matmul(y1,W22) + b22
        y21 = np.matmul(y2,W32) + b32
        y3 = np.matmul(y21,W42) + b42
        d=max(y3)
        #print(y3)
        y3[0]=y3[0]-d
        y3[1]=y3[1]-d
        y3[2]=y3[2]-d
        scoreMatExp = np.exp(np.asarray(y3))
        y4 = scoreMatExp / scoreMatExp.sum(0)
        c2=copy.copy(y4)

        yt1 = np.matmul(z,Wt1) + bt1
        yt2 = np.matmul(yt1,Wt2) + bt2
        yt21 = np.matmul(yt2,Wt3) + bt3
        yt3 = np.matmul(yt21,Wt4) + bt4
        d=max(yt3)
        yt3[0]=yt3[0]-d
        yt3[1]=yt3[1]-d
        yt3[2]=yt3[2]-d
        scoreMatExp = np.exp(np.asarray(yt3))
        yt4 = scoreMatExp / scoreMatExp.sum(0)
        ct=copy.copy(yt4)


        if c1[0]>c1[1] and c1[0]>c1[2] and ct[0]>ct[1] and ct[0]>ct[2]:
            total[3]=total[3]+l[shift+i+19,0]
            i=i+int(l[shift+i+19,2]-1)
            if totalmax[3]-total[3]>maxdown[3]:
                maxdown[3]=copy.copy(totalmax[3]-total[3])
            if total[3]>totalmax[3]:
                totalmax[3]=copy.copy(total[3])
        if c2[1]>c2[0] and c2[1]>c2[2] and ct[1]>ct[0] and ct[1]>ct[2]:
            total[3]=total[3]+l[shift+i+19,1]
            i=i+int(l[shift+i+19,3]-1)
            if totalmax[3]-total[3]>maxdown[3]:
                maxdown[3]=copy.copy(totalmax[3]-total[3])
            if total[3]>totalmax[3]:
                totalmax[3]=copy.copy(total[3])
        i+=1

    i=int(0) 
    while i < rang:
        #if i % 1000 == 0:
            #print(i)
        x=k[i]
        z=m[i]

        y1 = np.matmul(x,W11) + b11
        y2 = np.matmul(y1,W21) + b21
        y21 = np.matmul(y2,W31) + b31
        y3 = np.matmul(y21,W41) + b41
        d=max(y3)
        #print(y3)
        y3[0]=y3[0]-d
        y3[1]=y3[1]-d
        y3[2]=y3[2]-d
        scoreMatExp = np.exp(np.asarray(y3))
        y4 = scoreMatExp / scoreMatExp.sum(0)
        c1=copy.copy(y4)

        y1 = np.matmul(x,W12) + b12
        y2 = np.matmul(y1,W22) + b22
        y21 = np.matmul(y2,W32) + b32
        y3 = np.matmul(y21,W42) + b42
        d=max(y3)
        #print(y3)
        y3[0]=y3[0]-d
        y3[1]=y3[1]-d
        y3[2]=y3[2]-d
        scoreMatExp = np.exp(np.asarray(y3))
        y4 = scoreMatExp / scoreMatExp.sum(0)
        c2=copy.copy(y4)


        yt1 = np.matmul(z,Wt11) + bt11
        yt2 = np.matmul(yt1,Wt21) + bt21
        yt21 = np.matmul(yt2,Wt31) + bt31
        yt3 = np.matmul(yt21,Wt41) + bt41
        d=max(yt3)
        yt3[0]=yt3[0]-d
        yt3[1]=yt3[1]-d
        yt3[2]=yt3[2]-d
        scoreMatExp = np.exp(np.asarray(yt3))
        yt4 = scoreMatExp / scoreMatExp.sum(0)
        ct1=copy.copy(yt4)

        yt1 = np.matmul(z,Wt12) + bt12
        yt2 = np.matmul(yt1,Wt22) + bt22
        yt21 = np.matmul(yt2,Wt32) + bt32
        yt3 = np.matmul(yt21,Wt42) + bt42
        d=max(yt3)
        yt3[0]=yt3[0]-d
        yt3[1]=yt3[1]-d
        yt3[2]=yt3[2]-d
        scoreMatExp = np.exp(np.asarray(yt3))
        yt4 = scoreMatExp / scoreMatExp.sum(0)
        ct2=copy.copy(yt4)

        if c1[0]>c1[1] and c1[0]>c1[2] and ct1[0]>ct1[1] and ct1[0]>ct1[2]:
            total[4]=total[4]+l[shift+i+19,0]
            i=i+int(l[shift+i+19,2]-1)
            if totalmax[4]-total[4]>maxdown[4]:
                maxdown[4]=copy.copy(totalmax[4]-total[4])
            if total[4]>totalmax[4]:
                totalmax[4]=copy.copy(total[4])
        if c1[1]>c1[0] and c1[1]>c1[2] and ct2[1]>ct2[0] and ct2[1]>ct2[2]:
            total[4]=total[4]+l[shift+i+19,1]
            i=i+int(l[shift+i+19,3]-1)
            if totalmax[4]-total[4]>maxdown[4]:
                maxdown[4]=copy.copy(totalmax[4]-total[4])
            if total[4]>totalmax[4]:
                totalmax[4]=copy.copy(total[4])
        i+=1

    return (total,maxdown)
