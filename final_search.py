import os
import sys
import fileinput

x=1
itr=1
textfile = open("latency.txt","a")
for itr in range(0,4):
    textfile.write("******** SLIP iteration " + str(2**itr)+"***********\n")
    for x in xrange(1,11):
        y = format (float(x/float(10)),'.1f')
	z = 2**itr
        searchfile = open ("opt_slip_itr_"+str(z)+"_"+str(y)+".txt","r")

        for line in searchfile:
            if "Total Latency over all cells:" in line: textfile.write(line)

searchfile.close

x1=1
itr1=1

for itr1 in range(0,4):
    textfile.write("********** PIM iteration " + str(2**itr)+"***********\n")
    for x1 in xrange(1,11):
        y1 = format (float(x1/float(10)),'.1f')
	z1 = 2**itr1
        searchfile = open ("opt_itr_"+str(z1)+"_"+str(y1)+".txt","r")

        for line in searchfile:
            if "Total Latency over all cells:" in line: textfile.write(line)

searchfile.close


x3=1

textfile.write("********** maxsize iteration ***********\n")
for x3 in xrange(1,11):
    y3 = format (float(x3/float(10)),'.1f')
	
    searchfile = open ("opt_max_size_"+str(y3)+".txt","r")

    for line in searchfile:
        if "Total Latency over all cells:" in line: textfile.write(line)

searchfile.close

x4=1

textfile.write("********** LQF iteration ***********\n")
for x4 in xrange(1,11):
    y4 = format (float(x4/float(10)),'.1f')
	
    searchfile = open ("opt_lqf_"+str(y4)+".txt","r")

    for line in searchfile:
        if "Total Latency over all cells:" in line: textfile.write(line)

searchfile.close


textfile.close







