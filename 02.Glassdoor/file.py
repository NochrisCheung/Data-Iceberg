import os

mydir = os.path.dirname(os.path.realpath(__file__))
file = open(mydir+'path.txt','w')
file.write(mydir)
file.close()
