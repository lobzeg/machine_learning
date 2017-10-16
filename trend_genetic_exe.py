

#import tensorflow as tf
import numpy as np
import copy

def main(shift,r1,r2,r3):
    #sess = tf.InteractiveSession()

    inp=160
    h1=240
    h2=80
    h3=20
    o=3
    stop=200
    r=90
    #r1=200
    #r2=20
    #r3=5000
    rand_runs=2
    #shift=30000

    f1 = open( '/home/creo/projects/python/test/extended_new_si.txt' , 'r')
    l = np.loadtxt(f1, dtype='f', delimiter=',')

    f2 = open( '/home/creo/projects/python/test/trend_200_si.txt' , 'r')
    m = np.loadtxt(f2, dtype='f', delimiter=',')

    
    tot= np.zeros([r,8])
    for i in range(r):
        for j in range(8):
            tot[i,j]=-99999999

    nump=8

    Ww11= np.zeros([r,int(inp*h1/64)])
    Ww12= np.zeros([r,int(inp*h1/64)])
    Ww13= np.zeros([r,int(inp*h1/64)])
    Ww14= np.zeros([r,int(inp*h1/64)])
    Ww15= np.zeros([r,int(inp*h1/64)])
    Ww16= np.zeros([r,int(inp*h1/64)])
    Ww17= np.zeros([r,int(inp*h1/64)])
    Ww18= np.zeros([r,int(inp*h1/64)])
    Ww21= np.zeros([r,int(h1*h2/64)])
    Ww22= np.zeros([r,int(h1*h2/64)])
    Ww23= np.zeros([r,int(h1*h2/64)])
    Ww24= np.zeros([r,int(h1*h2/64)])
    Ww25= np.zeros([r,int(h1*h2/64)])
    Ww26= np.zeros([r,int(h1*h2/64)])
    Ww27= np.zeros([r,int(h1*h2/64)])
    Ww28= np.zeros([r,int(h1*h2/64)])
    Ww3= np.zeros([r,h2*h3])
    Ww4= np.zeros([r,h3*o])

    bb1= np.zeros([r,h1])
    bb2= np.zeros([r,h2])
    bb3= np.zeros([r,h3])
    bb4= np.zeros([r,o])
    bparam=np.zeros([r,nump])

    #if0 = open ( 'D:\\python\\test\\GW1T.txt' , 'r')
    #if1 = open ( 'D:\\python\\test\\GW2T.txt' , 'r')
    #if2 = open ( 'D:\\python\\test\\GW3T.txt' , 'r')
    #if3 = open ( 'D:\\python\\test\\GW4T.txt' , 'r')
    #if4 = open ( 'D:\\python\\test\\Gb1T.txt' , 'r')
    #if5 = open ( 'D:\\python\\test\\Gb2T.txt' , 'r')
    #if6 = open ( 'D:\\python\\test\\Gb3T.txt' , 'r')
    #if7 = open ( 'D:\\python\\test\\Gb4T.txt' , 'r')

    #W1 = np.loadtxt(if0, dtype='f', delimiter=',')
    #W2 = np.loadtxt(if1, dtype='f', delimiter=',')
    #W3 = np.loadtxt(if2, dtype='f', delimiter=',')
    #W4 = np.loadtxt(if3, dtype='f', delimiter=',')
    #b1 = np.loadtxt(if4, dtype='f', delimiter=',')
    #b2 = np.loadtxt(if5, dtype='f', delimiter=',')
    #b3 = np.loadtxt(if6, dtype='f', delimiter=',')
    #b4 = np.loadtxt(if7, dtype='f', delimiter=',')

    flag2=0

    tot,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam=random_run(shift,nump,m,l,stop,inp,h1,h2,h3,o,tot,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,int(r1*rand_runs),r,r3)
    stagnation=0
    for i in range(r2):
        Wx11=copy.copy(Ww11)
        Wx12=copy.copy(Ww12)
        Wx13=copy.copy(Ww13)
        Wx14=copy.copy(Ww14)
        Wx21=copy.copy(Ww21)
        Wx22=copy.copy(Ww22)
        Wx23=copy.copy(Ww23)
        Wx24=copy.copy(Ww24)
        Wx15=copy.copy(Ww15)
        Wx16=copy.copy(Ww16)
        Wx17=copy.copy(Ww17)
        Wx18=copy.copy(Ww18)
        Wx25=copy.copy(Ww25)
        Wx26=copy.copy(Ww26)
        Wx27=copy.copy(Ww27)
        Wx28=copy.copy(Ww28)
        Wx3=copy.copy(Ww3)
        Wx4=copy.copy(Ww4)
        bx1=copy.copy(bb1)
        bx2=copy.copy(bb2)
        bx3=copy.copy(bb3)
        bx4=copy.copy(bb4)
        bxparam=copy.copy(bparam)
        
        
        stagnation,flag,tot,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam=gen_run(shift,nump,stagnation,m,l,stop,inp,h1,h2,h3,o,tot,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,Wx11,Wx12,Wx13,Wx14,Wx15,Wx16,Wx17,Wx18,Wx21,Wx22,Wx23,Wx24,Wx25,Wx26,Wx27,Wx28,Wx3,Wx4,bx1,bx2,bx3,bx4,bxparam,r1,r,r3)
        if flag==0:
            flag2=flag2+1
        if flag==1:
            flag2=0
        if flag2>3:
            break
        if stagnation>15:
            break
    

    A1=np.reshape(Ww11[0],(int(inp/8),int(h1/8)))
    A2=np.reshape(Ww12[0],(int(inp/8),int(h1/8)))
    A3=np.reshape(Ww13[0],(int(inp/8),int(h1/8)))
    A4=np.reshape(Ww14[0],(int(inp/8),int(h1/8)))
    A5=np.reshape(Ww15[0],(int(inp/8),int(h1/8)))
    A6=np.reshape(Ww16[0],(int(inp/8),int(h1/8)))
    A7=np.reshape(Ww17[0],(int(inp/8),int(h1/8)))
    A8=np.reshape(Ww18[0],(int(inp/8),int(h1/8)))
    W1=combine_weight(int(inp/8),int(h1/8),A1,A2,A3,A4,A5,A6,A7,A8)
    A1=np.reshape(Ww21[0],(int(h1/8),int(h2/8)))
    A2=np.reshape(Ww22[0],(int(h1/8),int(h2/8)))
    A3=np.reshape(Ww23[0],(int(h1/8),int(h2/8)))
    A4=np.reshape(Ww24[0],(int(h1/8),int(h2/8)))
    A5=np.reshape(Ww25[0],(int(h1/8),int(h2/8)))
    A6=np.reshape(Ww26[0],(int(h1/8),int(h2/8)))
    A7=np.reshape(Ww27[0],(int(h1/8),int(h2/8)))
    A8=np.reshape(Ww28[0],(int(h1/8),int(h2/8)))
    W2=combine_weight(int(h1/8),int(h2/8),A1,A2,A3,A4,A5,A6,A7,A8)
    W3=np.reshape(Ww3[0],(h2,h3))
    W4=np.reshape(Ww4[0],(h3,o))
    b1=bb1[0]
    b2=bb2[0]
    b3=bb3[0]
    b4=bb4[0]
    f3 = open ( '/home/creo/projects/python/test/GWT1.txt' , 'wb')
    np.savetxt(f3, W1,fmt='%f', delimiter=',',newline='\r\n')
    f4 = open ( '/home/creo/projects/python/test/GWT2.txt' , 'wb')
    np.savetxt(f4, W2,fmt='%f', delimiter=',',newline='\r\n')
    f5 = open ( '/home/creo/projects/python/test/GWT3.txt' , 'wb')
    np.savetxt(f5, W3,fmt='%f', delimiter=',',newline='\r\n')
    f6 = open ( '/home/creo/projects/python/test/GbT1.txt' , 'wb')
    np.savetxt(f6, b1,fmt='%f', delimiter=',',newline='\r\n')
    f7 = open ( '/home/creo/projects/python/test/GbT2.txt' , 'wb')
    np.savetxt(f7, b2,fmt='%f', delimiter=',',newline='\r\n')
    f8 = open ( '/home/creo/projects/python/test/GbT3.txt' , 'wb')
    np.savetxt(f8, b3,fmt='%f', delimiter=',',newline='\r\n')
    f9 = open ( '/home/creo/projects/python/test/GWT4.txt' , 'wb')
    np.savetxt(f9, W4,fmt='%f', delimiter=',',newline='\r\n')
    f10 = open ( '/home/creo/projects/python/test/GbT4.txt' , 'wb')
    np.savetxt(f10, b4,fmt='%f', delimiter=',',newline='\r\n')
    

    A1=np.reshape(Ww11[30],(int(inp/8),int(h1/8)))
    A2=np.reshape(Ww12[30],(int(inp/8),int(h1/8)))
    A3=np.reshape(Ww13[30],(int(inp/8),int(h1/8)))
    A4=np.reshape(Ww14[30],(int(inp/8),int(h1/8)))
    A5=np.reshape(Ww15[30],(int(inp/8),int(h1/8)))
    A6=np.reshape(Ww16[30],(int(inp/8),int(h1/8)))
    A7=np.reshape(Ww17[30],(int(inp/8),int(h1/8)))
    A8=np.reshape(Ww18[30],(int(inp/8),int(h1/8)))
    W1=combine_weight(int(inp/8),int(h1/8),A1,A2,A3,A4,A5,A6,A7,A8)
    A1=np.reshape(Ww21[30],(int(h1/8),int(h2/8)))
    A2=np.reshape(Ww22[30],(int(h1/8),int(h2/8)))
    A3=np.reshape(Ww23[30],(int(h1/8),int(h2/8)))
    A4=np.reshape(Ww24[30],(int(h1/8),int(h2/8)))
    A5=np.reshape(Ww25[30],(int(h1/8),int(h2/8)))
    A6=np.reshape(Ww26[30],(int(h1/8),int(h2/8)))
    A7=np.reshape(Ww27[30],(int(h1/8),int(h2/8)))
    A8=np.reshape(Ww28[30],(int(h1/8),int(h2/8)))
    W2=combine_weight(int(h1/8),int(h2/8),A1,A2,A3,A4,A5,A6,A7,A8)
    W3=np.reshape(Ww3[30],(h2,h3))
    W4=np.reshape(Ww4[30],(h3,o))
    b1=bb1[30]
    b2=bb2[30]
    b3=bb3[30]
    b4=bb4[30]
    f33 = open ( '/home/creo/projects/python/test/GWT11.txt' , 'wb')
    np.savetxt(f33, W1,fmt='%f', delimiter=',',newline='\r\n')
    f43 = open ( '/home/creo/projects/python/test/GWT21.txt' , 'wb')
    np.savetxt(f43, W2,fmt='%f', delimiter=',',newline='\r\n')
    f53 = open ( '/home/creo/projects/python/test/GWT31.txt' , 'wb')
    np.savetxt(f53, W3,fmt='%f', delimiter=',',newline='\r\n')
    f63 = open ( '/home/creo/projects/python/test/GbT11.txt' , 'wb')
    np.savetxt(f63, b1,fmt='%f', delimiter=',',newline='\r\n')
    f73 = open ( '/home/creo/projects/python/test/GbT21.txt' , 'wb')
    np.savetxt(f73, b2,fmt='%f', delimiter=',',newline='\r\n')
    f83 = open ( '/home/creo/projects/python/test/GbT31.txt' , 'wb')
    np.savetxt(f83, b3,fmt='%f', delimiter=',',newline='\r\n')
    f93 = open ( '/home/creo/projects/python/test/GWT41.txt' , 'wb')
    np.savetxt(f93, W4,fmt='%f', delimiter=',',newline='\r\n')
    f103 = open ( '/home/creo/projects/python/test/GbT41.txt' , 'wb')
    np.savetxt(f103, b4,fmt='%f', delimiter=',',newline='\r\n')

    A1=np.reshape(Ww11[60],(int(inp/8),int(h1/8)))
    A2=np.reshape(Ww12[60],(int(inp/8),int(h1/8)))
    A3=np.reshape(Ww13[60],(int(inp/8),int(h1/8)))
    A4=np.reshape(Ww14[60],(int(inp/8),int(h1/8)))
    A5=np.reshape(Ww15[60],(int(inp/8),int(h1/8)))
    A6=np.reshape(Ww16[60],(int(inp/8),int(h1/8)))
    A7=np.reshape(Ww17[60],(int(inp/8),int(h1/8)))
    A8=np.reshape(Ww18[60],(int(inp/8),int(h1/8)))
    W1=combine_weight(int(inp/8),int(h1/8),A1,A2,A3,A4,A5,A6,A7,A8)
    A1=np.reshape(Ww21[60],(int(h1/8),int(h2/8)))
    A2=np.reshape(Ww22[60],(int(h1/8),int(h2/8)))
    A3=np.reshape(Ww23[60],(int(h1/8),int(h2/8)))
    A4=np.reshape(Ww24[60],(int(h1/8),int(h2/8)))
    A5=np.reshape(Ww25[60],(int(h1/8),int(h2/8)))
    A6=np.reshape(Ww26[60],(int(h1/8),int(h2/8)))
    A7=np.reshape(Ww27[60],(int(h1/8),int(h2/8)))
    A8=np.reshape(Ww28[60],(int(h1/8),int(h2/8)))
    W2=combine_weight(int(h1/8),int(h2/8),A1,A2,A3,A4,A5,A6,A7,A8)
    W3=np.reshape(Ww3[60],(h2,h3))
    W4=np.reshape(Ww4[60],(h3,o))
    b1=bb1[60]
    b2=bb2[60]
    b3=bb3[60]
    b4=bb4[60]
    f35 = open ( '/home/creo/projects/python/test/GWT12.txt' , 'wb')
    np.savetxt(f35, W1,fmt='%f', delimiter=',',newline='\r\n')
    f45 = open ( '/home/creo/projects/python/test/GWT22.txt' , 'wb')
    np.savetxt(f45, W2,fmt='%f', delimiter=',',newline='\r\n')
    f55 = open ( '/home/creo/projects/python/test/GWT32.txt' , 'wb')
    np.savetxt(f55, W3,fmt='%f', delimiter=',',newline='\r\n')
    f65 = open ( '/home/creo/projects/python/test/GbT12.txt' , 'wb')
    np.savetxt(f65, b1,fmt='%f', delimiter=',',newline='\r\n')
    f75 = open ( '/home/creo/projects/python/test/GbT22.txt' , 'wb')
    np.savetxt(f75, b2,fmt='%f', delimiter=',',newline='\r\n')
    f85 = open ( '/home/creo/projects/python/test/GbT32.txt' , 'wb')
    np.savetxt(f85, b3,fmt='%f', delimiter=',',newline='\r\n')
    f95 = open ( '/home/creo/projects/python/test/GWT42.txt' , 'wb')
    np.savetxt(f95, W4,fmt='%f', delimiter=',',newline='\r\n')
    f105 = open ( '/home/creo/projects/python/test/GbT42.txt' , 'wb')
    np.savetxt(f105, b4,fmt='%f', delimiter=',',newline='\r\n')

    partot=np.zeros(nump)
    for k in range(r):
        partot=partot+bparam[k]/r
    
def gen_weight_generation_old(Wx1,size,inp,h1,k,k1,k2):
    if np.random.randint(99)>k1:
        W1=np.reshape(Wx1[np.random.randint(0, size)],(inp,h1))
    elif np.random.randint(99)>k2:
        W1=np.reshape(Wx1[np.random.randint(0, size)],(inp,h1))+np.random.uniform(-k/4,k/4,size=(inp,h1))
    else:
        W1=np.random.uniform(-k,k,size=(inp,h1))
    return (W1)

def gen_bias_generation_old(bx1,size,h1,k1,k2):
    if np.random.randint(99)>k1:
        b1=bx1[np.random.randint(0, size)]
    elif np.random.randint(99)>k2:
        b1=bx1[np.random.randint(0, size)]+np.random.normal(size=h1)
    else:
        b1=np.random.normal(size=h1)
    return (b1)

def gen_weight_generation(a,b,Wx1,size,inp,h1,k,k1,k2,k3):
    if np.random.randint(9)>4:
        gen=a
    else:
        gen=b
    W1=np.reshape(Wx1[np.random.randint(int((gen%10)*20), int((gen%10)*20+int((gen/10))*20))],(inp,h1))
    if np.random.randint(99)<k1*5:
        W1=np.reshape(Wx1[np.random.randint(0, size)],(inp,h1))
    for j in range(k3):
        a=np.random.randint(0, size)
        if np.random.randint(99)<k1:
            b=np.random.randint(0, h1)
            for i in range(inp):
                W1[i,b]=Wx1[a,i*h1+b]
                    
        if np.random.randint(99)<k1:
            c=np.random.randint(0, inp)
            for i in range(h1):
                W1[c,i]=Wx1[a,c*h1+i]
                
    for i in range(2*k3):
        if np.random.randint(99)<k2:
            b=np.random.randint(0, h1)
            c=np.random.randint(0, inp)
            W1[c,b]=np.random.uniform(-k,k)     

    
    return (W1)

def gen_bias_generation(a,b,bx1,size,h1,k1,k2,k3):
    if np.random.randint(9)>4:
        gen=a
    else:
        gen=b
    b1=bx1[np.random.randint(int((gen%10)*20), int((gen%10)*20+int((gen/10))*20))]
    if np.random.randint(99)<k1*5:
        b1=bx1[np.random.randint(0, size)]
    for i in range(h1):
        if np.random.randint(99)>k2:
            b1[i]=bx1[np.random.randint(0, size),i]
        if np.random.randint(99)>k2:
            b1[i]=b1[i]+np.random.normal()
        if np.random.randint(99)>k1:
            b1[i]=np.random.normal()
    return (b1)


def separated_gen_weight_generation_old(Wx1,size,inp,h1,k,k1,k2,g1,f,bparam,nn):
    if g1==0:
        W1=np.zeros([inp,h1])
    else:
        g=np.random.randint(0, size)
        zed=bparam[g]
        if zed[nn]==1:
            if np.random.randint(99)>k1:
                W1=np.reshape(Wx1[g],(inp,h1))
            elif np.random.randint(99)>k2:
                W1=np.reshape(Wx1[g],(inp,h1))+np.random.uniform(-k/4,k/4,size=(inp,h1))
            else:
                W1=np.random.uniform(-k,k,size=(inp,h1))
        else:
            if np.random.randint(99)>k1:
                W1=np.reshape(Wx1[f],(inp,h1))
            elif np.random.randint(99)>k2:
                W1=np.reshape(Wx1[f],(inp,h1))+np.random.uniform(-k/4,k/4,size=(inp,h1))
            else:
                W1=np.random.uniform(-k,k,size=(inp,h1))
    return (W1)

def separated_gen_weight_generation(a,b,Wx1,size,inp,h1,k,k1,k2,k3,f,g,bparam,nn):
    if f==0:
        W1=np.zeros([inp,h1])
    else:
        if np.random.randint(9)>4:
            gen=a
        else:
            gen=b
        g2=np.random.randint(int((gen%10)*20), int((gen%10)*20+int((gen/10))*20))
        zed=bparam[g2]
        if zed[nn]==1:
            W1=np.reshape(Wx1[g2],(inp,h1))
        else:
            W1=np.reshape(Wx1[g],(inp,h1))
        if np.random.randint(99)<k1*5:
            W1=np.reshape(Wx1[np.random.randint(0, size)],(inp,h1))
        for j in range(k3):
            a=np.random.randint(0, size)
            if np.random.randint(99)<k1:
                b=np.random.randint(0, h1)
                for i in range(inp):
                    W1[i,b]=Wx1[a,i*h1+b]
                        
            if np.random.randint(99)<k1:
                c=np.random.randint(0, inp)
                for i in range(h1):
                    W1[c,i]=Wx1[a,c*h1+i]
                    
        for i in range(2*k3):
            if np.random.randint(99)<k2:
                b=np.random.randint(0, h1)
                c=np.random.randint(0, inp)
                W1[c,b]=np.random.uniform(-k,k) 

    return (W1)




def selection(r1,r2,i,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,param,inp,h1,h2,h3,o):
    #stagnation=stagnation+1
    for j in range(r2):
        k=j+r1
        if total[i]==tot[k,i]:
            break
        if total[i]>tot[k,i]:
            flag=1
            
            if k==0:
                stagnation= max([0,stagnation-2])
            a1=copy.copy(tot[k])
            a21=copy.copy(Ww11[k])
            a22=copy.copy(Ww12[k])
            a23=copy.copy(Ww13[k])
            a24=copy.copy(Ww14[k])
            a31=copy.copy(Ww21[k])
            a32=copy.copy(Ww22[k])
            a33=copy.copy(Ww23[k])
            a34=copy.copy(Ww24[k])
            a25=copy.copy(Ww15[k])
            a26=copy.copy(Ww16[k])
            a27=copy.copy(Ww17[k])
            a28=copy.copy(Ww18[k])
            a35=copy.copy(Ww25[k])
            a36=copy.copy(Ww26[k])
            a37=copy.copy(Ww27[k])
            a38=copy.copy(Ww28[k])
            a4=copy.copy(Ww3[k])
            a41=copy.copy(Ww4[k])
            a7=copy.copy(bb3[k])
            a71=copy.copy(bb4[k])

            a5=copy.copy(bb1[k])
            a6=copy.copy(bb2[k])
            a8=copy.copy(bparam[k])
            
            tot[k]=copy.copy(total)
            
            (A1,A2,A3,A4,A5,A6,A7,A8)=break_weight(int(inp/8),int(h1/8),W1)
            Ww11[k]=copy.copy(np.ndarray.flatten(A1))
            Ww12[k]=copy.copy(np.ndarray.flatten(A2))
            Ww13[k]=copy.copy(np.ndarray.flatten(A3))
            Ww14[k]=copy.copy(np.ndarray.flatten(A4))
            Ww15[k]=copy.copy(np.ndarray.flatten(A5))
            Ww16[k]=copy.copy(np.ndarray.flatten(A6))
            Ww17[k]=copy.copy(np.ndarray.flatten(A7))
            Ww18[k]=copy.copy(np.ndarray.flatten(A8))

            (A1,A2,A3,A4,A5,A6,A7,A8)=break_weight(int(h1/8),int(h2/8),W2)
            Ww21[k]=copy.copy(np.ndarray.flatten(A1))
            Ww22[k]=copy.copy(np.ndarray.flatten(A2))
            Ww23[k]=copy.copy(np.ndarray.flatten(A3))
            Ww24[k]=copy.copy(np.ndarray.flatten(A4))
            Ww25[k]=copy.copy(np.ndarray.flatten(A5))
            Ww26[k]=copy.copy(np.ndarray.flatten(A6))
            Ww27[k]=copy.copy(np.ndarray.flatten(A7))
            Ww28[k]=copy.copy(np.ndarray.flatten(A8))
            Ww3[k]=copy.copy(np.ndarray.flatten(W3))
            Ww4[k]=copy.copy(np.ndarray.flatten(W4))
            bb3[k]=copy.copy(b3)
            bb4[k]=copy.copy(b4)
            
            
            bb1[k]=copy.copy(b1)
            bb2[k]=copy.copy(b2)
            bparam[k]=copy.copy(param)
            #c1=np.zeros(5)
            for h in range(1,r2-j):
                c1=copy.copy(tot[k+h])
                c21=copy.copy(Ww11[k+h])
                c22=copy.copy(Ww12[k+h])
                c23=copy.copy(Ww13[k+h])
                c24=copy.copy(Ww14[k+h])
                c31=copy.copy(Ww21[k+h])
                c32=copy.copy(Ww22[k+h])
                c33=copy.copy(Ww23[k+h])
                c34=copy.copy(Ww24[k+h])
                c25=copy.copy(Ww15[k+h])
                c26=copy.copy(Ww16[k+h])
                c27=copy.copy(Ww17[k+h])
                c28=copy.copy(Ww18[k+h])
                c35=copy.copy(Ww25[k+h])
                c36=copy.copy(Ww26[k+h])
                c37=copy.copy(Ww27[k+h])
                c38=copy.copy(Ww28[k+h])

                c4=copy.copy(Ww3[k+h])
                c41=copy.copy(Ww4[k+h])
                c7=copy.copy(bb3[k+h])
                c71=copy.copy(bb4[k+h])
                
                c5=copy.copy(bb1[k+h])
                c6=copy.copy(bb2[k+h])
                c8=copy.copy(bparam[k+h])
                
                tot[k+h]=copy.copy(a1)
                Ww11[k+h]=copy.copy(a21)
                Ww12[k+h]=copy.copy(a22)
                Ww13[k+h]=copy.copy(a23)
                Ww14[k+h]=copy.copy(a24)
                Ww21[k+h]=copy.copy(a31)
                Ww22[k+h]=copy.copy(a32)
                Ww23[k+h]=copy.copy(a33)
                Ww24[k+h]=copy.copy(a34)
                Ww15[k+h]=copy.copy(a25)
                Ww16[k+h]=copy.copy(a26)
                Ww17[k+h]=copy.copy(a27)
                Ww18[k+h]=copy.copy(a28)
                Ww25[k+h]=copy.copy(a35)
                Ww26[k+h]=copy.copy(a36)
                Ww27[k+h]=copy.copy(a37)
                Ww28[k+h]=copy.copy(a38)

                Ww3[k+h]=copy.copy(a4)
                Ww4[k+h]=copy.copy(a41)
                bb1[k+h]=copy.copy(a5)
                bb2[k+h]=copy.copy(a6)
                bb3[k+h]=copy.copy(a7)
                bb4[k+h]=copy.copy(a71)
                
                bb1[k+h]=copy.copy(a5)
                bb2[k+h]=copy.copy(a6)
                bparam[k+h]=copy.copy(a8)
                a1=copy.copy(c1)
                a21=copy.copy(c21)
                a22=copy.copy(c22)
                a23=copy.copy(c23)
                a24=copy.copy(c24)
                a31=copy.copy(c31)
                a32=copy.copy(c32)
                a33=copy.copy(c33)
                a34=copy.copy(c34)
                a25=copy.copy(c25)
                a26=copy.copy(c26)
                a27=copy.copy(c27)
                a28=copy.copy(c28)
                a35=copy.copy(c35)
                a36=copy.copy(c36)
                a37=copy.copy(c37)
                a38=copy.copy(c38)

                a4=copy.copy(c4)
                a41=copy.copy(c41)
                a5=copy.copy(c5)
                a6=copy.copy(c6)
                a7=copy.copy(c7)  
                a71=copy.copy(c71) 
                
                a5=copy.copy(c5)
                a6=copy.copy(c6)
                a8=copy.copy(c8)
                                    
            break
    return(flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot)

def gen_run(shift,nump,stagnation,m,l,stop,inp,h1,h2,h3,o,tot,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,Wx11,Wx12,Wx13,Wx14,Wx15,Wx16,Wx17,Wx18,Wx21,Wx22,Wx23,Wx24,Wx25,Wx26,Wx27,Wx28,Wx3,Wx4,bx1,bx2,bx3,bx4,bxparam,rang,r,r3):
    flag=0
    k1=max([5+stagnation*2,70])
    k2=max([1+stagnation*3,80])
    k3=max([1+stagnation*0.2,5])
    k4=max([1+stagnation,10])
    stagnation=stagnation+3
    f=np.zeros(nump)
    for j in range (rang):
        nonzp=0
        if np.random.randint(9)>4:
            sel=np.random.randint(99)
            if sel>79:
                a=11
                b=12
            elif sel>59:
                a=11
                b=11
            elif sel>39:
                a=12
                b=12
            else:
                a=30
                b=30
            
            for h in range(nump):
                if np.random.randint(9)>4:
                    gen=a
                else:
                    gen=b
                g=np.random.randint(int((gen%10)*r/3), int((gen%10)*r/3+int((gen/10))*r/3))
                g1=bxparam[g]
                f[h]=g1[h]
                nonzp=nonzp+f[h]
            if nonzp==0:
                f[np.random.randint(nump)]=1
            A1=separated_gen_weight_generation(a,b,Wx11,r,int(inp/8),int(h1/8),k3,k1,k2,k4,f[0],g,bxparam,0)
            A2=separated_gen_weight_generation(a,b,Wx12,r,int(inp/8),int(h1/8),k3,k1,k2,k4,f[1],g,bxparam,1)
            A3=separated_gen_weight_generation(a,b,Wx13,r,int(inp/8),int(h1/8),k3,k1,k2,k4,f[2],g,bxparam,2)
            A4=separated_gen_weight_generation(a,b,Wx14,r,int(inp/8),int(h1/8),k3,k1,k2,k4,f[3],g,bxparam,3)
            A5=separated_gen_weight_generation(a,b,Wx15,r,int(inp/8),int(h1/8),k3,k1,k2,k4,f[0],g,bxparam,4)
            A6=separated_gen_weight_generation(a,b,Wx16,r,int(inp/8),int(h1/8),k3,k1,k2,k4,f[1],g,bxparam,5)
            A7=separated_gen_weight_generation(a,b,Wx17,r,int(inp/8),int(h1/8),k3,k1,k2,k4,f[2],g,bxparam,6)
            A8=separated_gen_weight_generation(a,b,Wx18,r,int(inp/8),int(h1/8),k3,k1,k2,k4,f[3],g,bxparam,7)
            W1=combine_weight(int(inp/8),int(h1/8),A1,A2,A3,A4,A5,A6,A7,A8)

            A1=separated_gen_weight_generation(a,b,Wx21,r,int(h1/8),int(h2/8),k3,k1,k2,k4,f[0],g,bxparam,0)
            A2=separated_gen_weight_generation(a,b,Wx22,r,int(h1/8),int(h2/8),k3,k1,k2,k4,f[1],g,bxparam,1)
            A3=separated_gen_weight_generation(a,b,Wx23,r,int(h1/8),int(h2/8),k3,k1,k2,k4,f[2],g,bxparam,2)
            A4=separated_gen_weight_generation(a,b,Wx24,r,int(h1/8),int(h2/8),k3,k1,k2,k4,f[3],g,bxparam,3)
            A5=separated_gen_weight_generation(a,b,Wx25,r,int(h1/8),int(h2/8),k3,k1,k2,k4,f[0],g,bxparam,4)
            A6=separated_gen_weight_generation(a,b,Wx26,r,int(h1/8),int(h2/8),k3,k1,k2,k4,f[1],g,bxparam,5)
            A7=separated_gen_weight_generation(a,b,Wx27,r,int(h1/8),int(h2/8),k3,k1,k2,k4,f[2],g,bxparam,6)
            A8=separated_gen_weight_generation(a,b,Wx28,r,int(h1/8),int(h2/8),k3,k1,k2,k4,f[3],g,bxparam,7)
            W2=combine_weight(int(h1/8),int(h2/8),A1,A2,A3,A4,A5,A6,A7,A8)

            W3=gen_weight_generation(a,b,Wx3,r,h2,h3,k3,k1,k2,k4)
            W4=gen_weight_generation(a,b,Wx4,r,h3,o,k3,k1,k2,k4)
            
            b1=gen_bias_generation(a,b,bx1,r,h1,k1,k2,k4)
            b2=gen_bias_generation(a,b,bx2,r,h2,k1,k2,k4)
            b3=gen_bias_generation(a,b,bx3,r,h3,k1,k2,k4)
            b4=gen_bias_generation(a,b,bx4,r,o,k1,k2,k4)

        else:
            for h in range(nump):
                g=np.random.randint(r)
                g1=bxparam[g]
                f[h]=g1[h]
                nonzp=nonzp+f[h]
            if nonzp==0:
                f[np.random.randint(nump)]=1
            A1=separated_gen_weight_generation_old(Wx11,r,int(inp/8),int(h1/8),k3,k1,k2,f[0],g,bxparam,0)
            A2=separated_gen_weight_generation_old(Wx12,r,int(inp/8),int(h1/8),k3,k1,k2,f[1],g,bxparam,1)
            A3=separated_gen_weight_generation_old(Wx13,r,int(inp/8),int(h1/8),k3,k1,k2,f[2],g,bxparam,2)
            A4=separated_gen_weight_generation_old(Wx14,r,int(inp/8),int(h1/8),k3,k1,k2,f[3],g,bxparam,3)
            A5=separated_gen_weight_generation_old(Wx15,r,int(inp/8),int(h1/8),k3,k1,k2,f[0],g,bxparam,4)
            A6=separated_gen_weight_generation_old(Wx16,r,int(inp/8),int(h1/8),k3,k1,k2,f[1],g,bxparam,5)
            A7=separated_gen_weight_generation_old(Wx17,r,int(inp/8),int(h1/8),k3,k1,k2,f[2],g,bxparam,6)
            A8=separated_gen_weight_generation_old(Wx18,r,int(inp/8),int(h1/8),k3,k1,k2,f[3],g,bxparam,7)
            W1=combine_weight(int(inp/8),int(h1/8),A1,A2,A3,A4,A5,A6,A7,A8)

            A1=separated_gen_weight_generation_old(Wx21,r,int(h1/8),int(h2/8),k3,k1,k2,f[0],g,bxparam,0)
            A2=separated_gen_weight_generation_old(Wx22,r,int(h1/8),int(h2/8),k3,k1,k2,f[1],g,bxparam,1)
            A3=separated_gen_weight_generation_old(Wx23,r,int(h1/8),int(h2/8),k3,k1,k2,f[2],g,bxparam,2)
            A4=separated_gen_weight_generation_old(Wx24,r,int(h1/8),int(h2/8),k3,k1,k2,f[3],g,bxparam,3)
            A5=separated_gen_weight_generation_old(Wx25,r,int(h1/8),int(h2/8),k3,k1,k2,f[0],g,bxparam,4)
            A6=separated_gen_weight_generation_old(Wx26,r,int(h1/8),int(h2/8),k3,k1,k2,f[1],g,bxparam,5)
            A7=separated_gen_weight_generation_old(Wx27,r,int(h1/8),int(h2/8),k3,k1,k2,f[2],g,bxparam,6)
            A8=separated_gen_weight_generation_old(Wx28,r,int(h1/8),int(h2/8),k3,k1,k2,f[3],g,bxparam,7)
            W2=combine_weight(int(h1/8),int(h2/8),A1,A2,A3,A4,A5,A6,A7,A8)

            W3=gen_weight_generation_old(Wx3,r,h2,h3,k3,k1,k2)
            W4=gen_weight_generation_old(Wx4,r,h3,o,k3,k1,k2)
            
            b1=gen_bias_generation_old(bx1,r,h1,k1,k2)
            b2=gen_bias_generation_old(bx2,r,h2,k1,k2)
            b3=gen_bias_generation_old(bx3,r,h3,k1,k2)
            b4=gen_bias_generation_old(bx4,r,o,k1,k2)

        total=single_run(shift,m,l,stop,W1,W2,W3,W4,b1,b2,b3,b4,r3)

        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(0,20,0,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,f,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(20,10,7,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,f,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(30,10,1,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,f,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(40,10,2,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,f,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(50,10,3,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,f,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(60,10,4,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,f,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(70,10,5,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,f,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(80,10,6,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,f,inp,h1,h2,h3,o)
        
        
    return (stagnation,flag,tot,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam)

def combine_weight(s1,s2,A1,A2,A3,A4,A5,A6,A7,A8):
    W=np.zeros([s1*8,s2*8])
    W[0:s1,0:s2]=A1
    W[s1:2*s1,s2:2*s2]=A2
    W[2*s1:3*s1,2*s2:3*s2]=A3
    W[3*s1:4*s1,3*s2:4*s2]=A4
    W[4*s1:5*s1,4*s2:5*s2]=A5
    W[5*s1:6*s1,5*s2:6*s2]=A6
    W[6*s1:7*s1,6*s2:7*s2]=A7
    W[7*s1:8*s1,7*s2:8*s2]=A8
    return (W)

def break_weight(s1,s2,W):
    A1=W[0:s1,0:s2]
    A2=W[s1:2*s1,s2:2*s2]
    A3=W[2*s1:3*s1,2*s2:3*s2]
    A4=W[3*s1:4*s1,3*s2:4*s2]
    A5=W[4*s1:5*s1,4*s2:5*s2]
    A6=W[5*s1:6*s1,5*s2:6*s2]
    A7=W[6*s1:7*s1,6*s2:7*s2]
    A8=W[7*s1:8*s1,7*s2:8*s2]
    return (A1,A2,A3,A4,A5,A6,A7,A8)

def separated_weight(param,s1,s2):
    if param[0]==1:
        A1=np.random.uniform(-1,1,size=(s1,s2))
    else:
        A1=np.zeros([s1,s2])
    if param[1]==1:
        A2=np.random.uniform(-1,1,size=(s1,s2))
    else:
        A2=np.zeros([s1,s2])
    if param[2]==1:
        A3=np.random.uniform(-1,1,size=(s1,s2))
    else:
        A3=np.zeros([s1,s2])
    if param[3]==1:
        A4=np.random.uniform(-1,1,size=(s1,s2))
    else:
        A4=np.zeros([s1,s2])
    if param[4]==1:
        A5=np.random.uniform(-1,1,size=(s1,s2))
    else:
        A5=np.zeros([s1,s2])
    if param[5]==1:
        A6=np.random.uniform(-1,1,size=(s1,s2))
    else:
        A6=np.zeros([s1,s2])
    if param[6]==1:
        A7=np.random.uniform(-1,1,size=(s1,s2))
    else:
        A7=np.zeros([s1,s2])
    if param[7]==1:
        A8=np.random.uniform(-1,1,size=(s1,s2))
    else:
        A8=np.zeros([s1,s2])
    return (A1,A2,A3,A4,A5,A6,A7,A8)



def random_run(shift,nump,m,l,stop,inp,h1,h2,h3,o,tot,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,rang,r,r3):
    for j in range (rang):
        nonzp=0
        param=np.zeros(nump)
        for j1 in range (nump):
            if np.random.randint(9)>4:
                param[j1]=1
                nonzp=1
        if nonzp==0:
                param[np.random.randint(nump)]=1  
        
        (A1,A2,A3,A4,A5,A6,A7,A8)=separated_weight(param,int(inp/8),int(h1/8))
        W1=combine_weight(int(inp/8),int(h1/8),A1,A2,A3,A4,A5,A6,A7,A8)
        (A1,A2,A3,A4,A5,A6,A7,A8)=separated_weight(param,int(h1/8),int(h2/8))
        W2=combine_weight(int(h1/8),int(h2/8),A1,A2,A3,A4,A5,A6,A7,A8)
        
        W3= np.random.uniform(-1,1,size=(h2,h3))
        W4= np.random.uniform(-1,1,size=(h3,o))

        b1= np.random.normal(size=h1)
        b2= np.random.normal(size=h2)
        b3= np.random.normal(size=h3)
        b4= np.random.normal(size=o)

        total=single_run(shift,m,l,stop,W1,W2,W3,W4,b1,b2,b3,b4,r3)
        flag=0
        stagnation=0
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(0,20,0,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,param,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(20,10,7,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,param,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(30,10,1,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,param,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(40,10,2,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,param,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(50,10,3,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,param,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(60,10,4,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,param,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(70,10,5,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,param,inp,h1,h2,h3,o)
        flag,stagnation,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,tot=selection(80,10,6,flag,stagnation,W1,W2,W3,W4,b1,b2,b3,b4,tot,total,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam,param,inp,h1,h2,h3,o)
        
    return (tot,Ww11,Ww12,Ww13,Ww14,Ww15,Ww16,Ww17,Ww18,Ww21,Ww22,Ww23,Ww24,Ww25,Ww26,Ww27,Ww28,Ww3,Ww4,bb1,bb2,bb3,bb4,bparam)


def single_run(shift,m,l,stop,W1,W2,W3,W4,b1,b2,b3,b4,rang):
    #a=np.zeros(3)
    total=np.zeros(8)
    #shift=30000
    s=20
    
    numdeals1=0
    numdeals2=0
    for i in range (rang):
        
        x=l[i]
        
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
        
        c=y4
        #print(c)
        c0=c[0]
        c1=c[1]
        c2=c[2]
        
        if c0>c1 and c0>c2:
            if m[i+19,0]>200 and m[i+19,3]<10:
                numdeals1=1
                total[1]=total[1]+m[i+19,0]/100
                total[2]=total[2]+m[i+19,0]/20
                total[3]=total[3]+m[i+19,0]/400
            if m[i+19,0]<0:
                total[1]=total[1]+min([m[i+19,0]/200,-0.5])
                total[2]=total[2]+m[i+19,0]/400
                total[3]=total[3]+m[i+19,0]/100
        elif m[i+19,0]>200 and m[i+19,3]<10:
            total[1]=total[1]-0.3
            

        if c1>c0 and c1>c2:
            if m[i+19,1]>200 and m[i+19,2]<10:
                numdeals2=1
                total[4]=total[4]+m[i+19,1]/100
                total[5]=total[5]+m[i+19,1]/20
                total[6]=total[6]+m[i+19,1]/400
            if m[i+19,1]<0:
                total[4]=total[4]+min([m[i+19,1]/200,-0.5])
                total[5]=total[5]+m[i+19,1]/400
                total[6]=total[6]+m[i+19,1]/100
        elif m[i+19,0]>200 and m[i+19,2]<10:
            total[4]=total[4]-0.3
            

        if c2>c0 and c2>c1:
            if m[i+19,0]<200 and m[i+19,1]<200:
                total[7]=total[7]+1
            else:
                total[7]=total[7]-0.8
        
    if total[1]==0:
        total[1]=-9999999
    if total[4]==0:
        total[4]=-9999999
    if numdeals1==0:
        total[1]=-9999999
    if numdeals2==0:
        total[4]=-9999999
    total[0]=total[1]+total[4]
    return total



if __name__ == "__main__":
    main()