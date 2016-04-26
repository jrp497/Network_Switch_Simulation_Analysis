import os
import sys
import fileinput

a=1
x=1
itr=1

for itr in range(0,4):
    for x in xrange(1,11):
        y = format (float(x/float(10)),'.1f')
        z = 2**itr
    
        f1 = open('ref','r')
        filedata = f1.read()
	newdata1 = filedata.replace('0.1',''+str(y))
	newdata2 = newdata1.replace('pim -n 1','pim -n '+str(z))
        g = open('pim_itr_'+str(z)+'_'+str(y),'w')
	g.write(newdata2)
        g.close()
        f1.close()

        f2 = open('ref','r')
        filedata = f2.read()
	newdata3 = filedata.replace('0.1',''+str(y))
	newdata4 = newdata3.replace('pim -n 1','islip -n '+str(z))
        s = open('islip_itr_'+str(z)+'_'+str(y),'w')
	s.write(newdata4)
        s.close()
        f2.close()
       
        x+=1
    itr+=1


for a in range(1,11):
    c = format (float(a/float(10)),'.1f')
    
    b1 = open('ref','r')
    filedatamax = b1.read()
    newdatamax1 = filedatamax.replace('0.1',''+str(c))
    newdatamax2 = newdatamax1.replace('pim -n 1','maxsize')
    e = open('lqf_'+str(c),'w')
    e.write(newdatalqf2)
    e.close()
    b1.close()

    b2 = open('ref','r')
    filedatamax = b2.read()
    newdatalqf1 = filedatamax.replace('0.1',''+str(c))
    newdatalqf2 = newdatalqf1.replace('pim -n 1','lqf')
    d = open('max_size_'+str(c),'w')
    d.write(newdatamax2)
    d.close()
    b2.close()
    a+=1
   


