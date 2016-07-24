import numpy as np
import xlrd

#functions take in a standard python list and 
#internally converts to numpy arrays when needed


#calculates the x axis range for the histogram
#and the optimal bin width using the Freedman-Diaconis rule
def setBins(data):
    
    x = np.asarray(data)
    iqr = np.subtract(*np.percentile(x, [75, 25])) #interquartile range
    h = 2.*iqr.item()*x.size**(-1./3)

    xmax = max(data)
    xmin = min(data)
    nbins = int((xmax-xmin)/h)

    return {'xmin': xmin,
            'xmax:': xmax,
            'nbins': nbins
            }


#calculates and returns the standard deviation of the dataset
def calcSD(data):
    
    x = np.asarray(data)
    r = np.std(x)
    return r.item()

#calculates and returns the mean of the dataset
def calcMean(data):
    
    x = np.asarray(data)
    r = np.mean(x)
    return r.item()

#calculates and returns the mode of the dataset
def calcMode(data):
    
    #http://stackoverflow.com/a/28129716
    return max(set(data), key=data.count)

#calculates and returns the median of the dataset
def calcMed(data):
    
    x = np.asarray(data)
    r = np.median(x)
    return r.item()



def getSheets(fname):
    xls = xlrd.open_workbook(fname, on_demand=True)
    sheets = []
    for name in xls.sheet_names():
        sheets.append(name)
    
    return sheets
    
