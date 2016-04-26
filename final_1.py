import os
import sys
import fileinput

a=1
x=1
l=4
m=3
n=2
o=1
p=100
itr=1

for itr in range(0,4):
    for x in xrange(1,11):
        
        y1 = format (float(x/float(10)),'.1f')
	
	
	u1= format(float(x*l/float(p)),'.3f')
	u2= format(float(x*m/float(p)),'.3f')	
	u3= format(float(x*n/float(p)),'.3f')
	u4= format(float(x*o/float(p)),'.3f')
	
        z = 2**itr
    
        f1 = open('ref','r')
        filedata = f1.read()
	newdata1 = filedata.replace('0.1',''+str(u1)+' '+str(u2)+' '+str(u3)+' '+str(u4))
	newdata2 = newdata1.replace('pim -n 1','pim -n '+str(z))
        g = open('pim_itr_'+str(z)+'_'+str(y1),'w')
	g.write(newdata2)
        g.close()
        f1.close()

        f2 = open('ref','r')
        filedata = f2.read()
	newdata3 = filedata.replace('0.1',''+str(u1)+' '+str(u2)+' '+str(u3)+' '+str(u4))
	newdata4 = newdata3.replace('pim -n 1','islip -n '+str(z))
        s = open('islip_itr_'+str(z)+'_'+str(y1),'w')
	s.write(newdata4)
        s.close()
        f2.close()
       
        x+=1
    itr+=1


for a in range(1,11):
    c = format (float(a/float(p)),'.1f')
    c1 = format (float(a/float(10)),'.1f')

    u5= format(float(a*l/float(p)),'.3f')
    u6= format(float(a*m/float(p)),'.3f')	
    u7= format(float(a*n/float(p)),'.3f')
    u8= format(float(a*o/float(p)),'.3f')
	
    
    b1 = open('ref','r')
    filedatamax = b1.read()
    newdatamax1 = filedatamax.replace('0.1',''+str(u5)+' '+str(u6)+' '+str(u7)+' '+str(u8))
    newdatamax2 = newdatamax1.replace('pim -n 1','maxsize')
    d = open('max_size_'+str(c1),'w')
    d.write(newdatamax2)
    d.close()
    b1.close()

    b2 = open('ref','r')
    filedatamax = b2.read()
    newdatalqf1 = filedatamax.replace('0.1',''+str(u5)+' '+str(u6)+' '+str(u7)+' '+str(u8))
    newdatalqf2 = newdatalqf1.replace('pim -n 1','lqf')
    e = open('lqf_'+str(c1),'w')
    e.write(newdatalqf2)
    e.close()
    
    b2.close()
    a+=1
   


