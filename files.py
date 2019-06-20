#!/usr/bin/env python3
import time
import os


def main():

	opt = int(input("numero de files ?"))
	start = time.time()
	startmaster = start
	
	for n in range(1,min(opt,1000)):
		f= open("file" + str(n) + ".txt","w+")
		for i in range(1000):
			f.write("first batch "+str(i+1) + " of file " + str(n) + "\r\n")	
		f.close() 
	done = time.time()
	elapsed = done - start
	print("files created " +str(elapsed))
	
	for n in range(1,min(opt,1000)):
		f= open("file" + str(n) + ".txt","a")
		for i in range(1000):
			f.write("second batch"+str(i+1) + " of file " + str(n) + "\r\n")	
		f.close() 
	done = time.time()
	elapsed = done - start
	print("files updated " +str(elapsed))
	
	for n in range(1,min(opt,1000)):
		os.remove("file" + str(n) + ".txt")
			
	done = time.time()
	elapsed = done - start
	print("files deleted " +str(elapsed))

	done = time.time()
	elapsed = done - startmaster
	print("total time " +str(elapsed))


if __name__ == "__main__":
  main()