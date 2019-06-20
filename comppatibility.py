#!/usr/bin/env python3
import json

file = open('CompatibilityMatrix.csv', 'r') 
filehw = open('hwlist.json','w')
NX = open('NX.json','w')
NSLIST=[]
file.readline()
file.readline()
for line in file: 
	words = line.split('","') 
	
	lsthw = words[0].split(",")
	lstAOS = words[1].split(",")
	lsthy= words[2].split(",")
	for hwitem in lsthw:
		print ("hardware " + hwitem)
		NSLIST.append(str(hwitem))
		print ("teste " + str(NSLIST))
		for aositem in lstAOS:
			print ("AOS " + aositem)
			for hyitem in lsthy:
				print ("Hy " + hyitem)
				s = str(hwitem) + "," + str(aositem) + "," + str(hyitem) + "," + str(words[3]) + "\n"
				filehw.write(s)
json.dump(NSLIST,NX)	
NX.close()			
filehw.close()
