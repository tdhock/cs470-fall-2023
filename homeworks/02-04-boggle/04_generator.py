__author__ = 'Eck'

##  VITAL:  MUST be run using Python 3.6 or better...else random.choices fails. New in 3.6
import sys, string, random
'''
Utility script.  creates a random boggle board of given size.  Two commands line args:
N = the size of board desired
outFile = name of desired output file
'''

script_py, N_str, outFile = sys.argv
N=int(N_str)
out = open(outFile,'w')


charlist= string.ascii_uppercase

for z in range(0,N):
    line = ' '.join(random.choices(charlist,k=N))
    out.write((line+"\n"))

out.close()

print("tada!")

