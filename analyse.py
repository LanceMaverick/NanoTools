import xlrd
from helpers import *
import hist

def readData(fname, sname):
    #read in the book and the sheet
    book = xlrd.open_workbook(fname)
    sheet = book.sheet_by_name(sname)
    
    #get data column and lables
    data = [sheet.cell_value(r, 0) for r in range(sheet.nrows)] 
    titles = [sheet.cell_value(r, 1) for r in range(3)]
    
    return data, titles


def analyse(fname, sname, nbins):
    
    
    #get data tuple
    read = readData(fname, sname)
    data = read[0] #data vector
    labels = read[1] #plot labels

    if not nbins:    
        nbins = setBins(data)['nbins']
    
    #key word arguments for labels
    lkeys = ['title', 'xlabel', 'ylabel']
    largs = dict(zip(lkeys, labels))
    
    #print setup
    print 'label options:'
    print largs
    print 'DATA:'
    print  data

    mean = calcMean(data)
    mode = calcMode(data)
    median = calcMed(data)
    sdev = calcSD(data)

    #print statistical values
    print '\n\n'
    print 'MEAN: ',     str(mean)
    print 'MODE: ',     str(mode)
    print 'MEDIAN: ',   str(median)
    print 'STD DEV: ',  str(sdev)
    print '\n\n'

    #create histogram
    hist.plotData(data, nbins, sname, **largs)
    
    return {
            'mean': mean,
            'mode': mode,
            'median': median,
            'sdev': sdev
            }
