#import genetic_parameters_exe as gp
#import trend_genetic_exe as trend
import testing_genetic_random as tg

import numpy as np

numshift=8
numsim=20

result1=np.zeros(numshift)
maxdown1=np.zeros(numshift)
lowr1=np.ones(numshift)*(9999999)
highr1=np.ones(numshift)*(-9999999)
lowm1=np.ones(numshift)*(9999999)
highm1=np.ones(numshift)*(-9999999)

result2=np.zeros(numshift)
maxdown2=np.zeros(numshift)
lowr2=np.ones(numshift)*(9999999)
highr2=np.ones(numshift)*(-9999999)
lowm2=np.ones(numshift)*(9999999)
highm2=np.ones(numshift)*(-9999999)

result3=np.zeros(numshift)
maxdown3=np.zeros(numshift)
lowr3=np.ones(numshift)*(9999999)
highr3=np.ones(numshift)*(-9999999)
lowm3=np.ones(numshift)*(9999999)
highm3=np.ones(numshift)*(-9999999)

result4=np.zeros(numshift)
maxdown4=np.zeros(numshift)
lowr4=np.ones(numshift)*(9999999)
highr4=np.ones(numshift)*(-9999999)
lowm4=np.ones(numshift)*(9999999)
highm4=np.ones(numshift)*(-9999999)

result5=np.zeros(numshift)
maxdown5=np.zeros(numshift)
lowr5=np.ones(numshift)*(9999999)
highr5=np.ones(numshift)*(-9999999)
lowm5=np.ones(numshift)*(9999999)
highm5=np.ones(numshift)*(-9999999)

sh=5000
r1=400
r2=20
r3=5000

for i in range(numshift):
    shift=i*sh
    for j in range(numsim):
        print(i*numsim+j)
        #gp.main(shift,r1,r2,r3)
        #trend.main(shift,r1,r2,r3)
        result,maxdown=tg.main(shift+r3,r3)
        if result[0]<lowr1[i]:
            lowr1[i]=result[0]
        if result[0]>highr1[i]:
            highr1[i]=result[0]
        if maxdown[0]<lowm1[i]:
            lowm1[i]=maxdown[0]
        if maxdown[0]>highm1[i]:
            highm1[i]=maxdown[0]
        result1[i]=result1[i]+result[0]/numsim
        maxdown1[i]=maxdown1[i]+maxdown[0]/numsim

        #result,maxdown=tg2.main(shift+5000,r3)
        if result[1]<lowr2[i]:
            lowr2[i]=result[1]
        if result[1]>highr2[i]:
            highr2[i]=result[1]
        if maxdown[1]<lowm2[i]:
            lowm2[i]=maxdown[1]
        if maxdown[1]>highm2[i]:
            highm2[i]=maxdown[1]
        result2[i]=result2[i]+result[1]/numsim
        maxdown2[i]=maxdown2[i]+maxdown[1]/numsim

        #result,maxdown=tg3.main(shift+5000,r3)
        if result[2]<lowr3[i]:
            lowr3[i]=result[2]
        if result[2]>highr3[i]:
            highr3[i]=result[2]
        if maxdown[2]<lowm3[i]:
            lowm3[i]=maxdown[2]
        if maxdown[2]>highm3[i]:
            highm3[i]=maxdown[2]
        result3[i]=result3[i]+result[2]/numsim
        maxdown3[i]=maxdown3[i]+maxdown[2]/numsim

        #result,maxdown=tg4.main(shift+5000,r3)
        if result[3]<lowr4[i]:
            lowr4[i]=result[3]
        if result[3]>highr4[i]:
            highr4[i]=result[3]
        if maxdown[3]<lowm4[i]:
            lowm4[i]=maxdown[3]
        if maxdown[3]>highm4[i]:
            highm4[i]=maxdown[3]
        result4[i]=result4[i]+result[3]/numsim
        maxdown4[i]=maxdown4[i]+maxdown[3]/numsim

        #result,maxdown=tg5.main(shift+5000,r3)
        if result[4]<lowr5[i]:
            lowr5[i]=result[4]
        if result[4]>highr5[i]:
            highr5[i]=result[4]
        if maxdown[4]<lowm5[i]:
            lowm5[i]=maxdown[4]
        if maxdown[4]>highm5[i]:
            highm5[i]=maxdown[4]
        result5[i]=result5[i]+result[4]/numsim
        maxdown5[i]=maxdown5[i]+maxdown[4]/numsim


n1=result1
n1=np.append(n1,lowr1)
n1=np.append(n1,highr1)
n1=np.append(n1,maxdown1)
n1=np.append(n1,lowm1)
n1=np.append(n1,highm1)
n1=np.reshape(n1,(6,numshift))

n2=result2
n2=np.append(n2,lowr2)
n2=np.append(n2,highr2)
n2=np.append(n2,maxdown2)
n2=np.append(n2,lowm2)
n2=np.append(n2,highm2)
n2=np.reshape(n2,(6,numshift))

n3=result3
n3=np.append(n3,lowr3)
n3=np.append(n3,highr3)
n3=np.append(n3,maxdown3)
n3=np.append(n3,lowm3)
n3=np.append(n3,highm3)
n3=np.reshape(n3,(6,numshift))

n4=result4
n4=np.append(n4,lowr4)
n4=np.append(n4,highr4)
n4=np.append(n4,maxdown4)
n4=np.append(n4,lowm4)
n4=np.append(n4,highm4)
n4=np.reshape(n4,(6,numshift))

n5=result5
n5=np.append(n5,lowr5)
n5=np.append(n5,highr5)
n5=np.append(n5,maxdown5)
n5=np.append(n5,lowm5)
n5=np.append(n5,highm5)
n5=np.reshape(n5,(6,numshift))

f1 = open ( 'C:\\Users\\arbuzik\\codes\\docs\\random1.txt' , 'wb')
f2 = open ( 'C:\\Users\\arbuzik\\codes\\docs\\random2.txt' , 'wb')
f3 = open ( 'C:\\Users\\arbuzik\\codes\\docs\\random3.txt' , 'wb')
f4 = open ( 'C:\\Users\\arbuzik\\codes\\docs\\random4.txt' , 'wb')
f5 = open ( 'C:\\Users\\arbuzik\\codes\\docs\\random5.txt' , 'wb')
np.savetxt(f1, n1,fmt='%f', delimiter=',',newline='\r\n')
np.savetxt(f2, n2,fmt='%f', delimiter=',',newline='\r\n')
np.savetxt(f3, n3,fmt='%f', delimiter=',',newline='\r\n')
np.savetxt(f4, n4,fmt='%f', delimiter=',',newline='\r\n')
np.savetxt(f5, n5,fmt='%f', delimiter=',',newline='\r\n')