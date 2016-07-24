# NanoTools
Simple, private tool for the analysing of nanoparticle data

Current features are very basic. It can read in an excel spread sheet and plot a histogram from a column of data, 
calculating statistical quantities.

##Requirements
- python 2.7
- xlrd
- matplotlib
- numpy
- tkinter

##Installation
Requirements can be installed with
`pip install -r requirements.txt`
or for each missing requirement,
`pip install xlrd`,
etc. Using a python `virtualenv` is recommended, however this may cause plots to not be shown after the data
has been analysed. They will still be saved, as `data_<sheet_name>.pdf/.png`

##Running
Either the command line or gui versions can be used:

###Command line version
This is run in the folliwing way 

```
python run.py <path to .xlsx file> <name of sheet> <optional bin number>
```

If a binning is not specified it is set automatically using the Freedman-Diaconis rule 
to optimise the number of bins and is determined by the statistical spread of your data, and the range. 

The gui version is run simply with:
```
python rungui.py
```
and its use should be self explanatory


##.xlsx formatting
The sheet to be analysed should have the following style of formatting:

Column A:

    A vertical list of your data

    
Column B

    B1: Plot title
    B2: x axis title
    B3: y axis title
        
    Any or all of these can be left blank, and in this case that particular
    title or label will not be drawn





