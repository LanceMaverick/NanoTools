import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from helpers import *

def plotData(data, nbins, name_suffix, **kwargs):
    
    print 'plotting data...'
    title = kwargs.get('title', '')
    xlabel = kwargs.get('xlabel', '')
    ylabel = kwargs.get('ylabel', '')
    
    plt.hist(np.asarray(data), nbins, facecolor='blue', alpha=0.75)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)

    plt.savefig('data_'+name_suffix.strip(' ')+'.pdf')
    plt.savefig('data_'+name_suffix.strip(' ')+'.png')
    plt.show()
    print 'plot saved as .pdf and .png'
