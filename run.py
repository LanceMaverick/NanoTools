#!/usr/bin/env python
import analyse as ana
import sys
import helpers

def main():
    
    if len(sys.argv)<3:
        print 'no data!. Usage:'
        print 'python run.py <.xsls document path> <sheet name> <no. of bins>'
        return
    
    fname = sys.argv[1]
    sname = sys.argv[2]
    
    try:
        nbins = int(sys.argv[3])
    except:
        print('\nno binning specified, using Freedman-Diaconis automatic bin optimisation\n') 
        nbins = None

    ana.analyse(fname, sname, nbins)

main()
