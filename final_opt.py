import os
import sys
import fileinput

x=1
a=1
itr=1

for itr in range(0,4):
    for x in xrange(1,11):
        y = format (float(x/float(10)),'.1f')
	z = 2**itr
        txtfile = open ("commands.txt","a")
        txtfile.write("./sim -f /home/jay/final/inputs/islip_itr_"+str(z)+"_"+str(y)+" -l 500000 -t2 -s1 -e2 > /home/jay/final/outputs/opt_islip_itr_"+str(z)+"_"+str(y)+".txt")
        txtfile.write("\n")
        txtfile.write("./sim -f /home/jay/final/inputs/pim_itr_"+str(z)+"_"+str(y)+" -l 500000 -t2 -s1 -e2 > /home/jay/final/outputs/opt_pim_itr_"+str(z)+"_"+str(y)+".txt")
        txtfile.write("\n")
txtfile.close()


for a in xrange(1,11):
    b = format (float(a/float(10)),'.1f')
    
    txtfile = open ("commands.txt","a")
    txtfile.write("./sim -f /home/jay/final/inputs/max_size_"+str(b)+" -l 500000 -t2 -s1 -e2 > /home/jay/final/outputs/opt_max_size_"+str(b)+".txt")
    txtfile.write("\n")
    txtfile.write("./sim -f /home/jay/final/inputs/lqf_"+str(b)+" -l 500000 -t2 -s1 -e2 > /home/jay/final/outputs/opt_lqf_"+str(b)+".txt")
    txtfile.write("\n")

txtfile.close()
