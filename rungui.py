from Tkinter import *
import tkMessageBox
import tkFileDialog
import xlrd
import helpers
import analyse as ana

class MainApp(Frame):
    
    def createWidgets(self):
       
        #header label
        self.label_text = StringVar()
        self.label_text.set('Import excel file and choose the sheet')
        self.label = Label(self, textvariable=self.label_text, height =2)
        self.label.grid(row=0, column = 0, columnspan=3, sticky=W)

        #import file button
        self.imp_button = Button(self, text='Import Excel File', width=20, command=self.openFile)
        self.imp_button.grid(row=1,column=0, columnspan=3,  padx=5, pady=5, sticky=W)
        
        
        #bin selection text
        self.blabel_text = StringVar()
        self.blabel_text.set('bins')
        self.blabel = Label(self, textvariable=self.blabel_text, height =2)
        self.blabel.grid(row=2,column=0, sticky=W)
       
        #manual bin specifier
        self.bentry = Entry(self, width=5)
        self.bentry.grid(row=2, column=0, sticky =W, padx=30)
        
        #automatic binning checkbox
        self.bvar = IntVar()
        self.bcheck = Checkbutton(self, text="automatic", variable=self.bvar, command=self.binCheck)
        self.bcheck.grid(row =2, column=0)
       
        #sheet box label
        self.slabel_text = StringVar()
        self.slabel_text.set('Choose sheet')
        self.slabel = Label(self, textvariable=self.slabel_text, height =1)
        self.slabel.grid(row =0, column =3, columnspan=2)
        
        #sheet list box
        self.sheetbox = Listbox(self)
        self.sheetbox.grid(row=1, column=3, columnspan=2, rowspan=2)

        #analyse button
        self.ana_button = Button(self, text='Analyse', width=20, command=self.analyse)
        self.ana_button.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        
        #output name list
        self.outstrs = ['mean:','mode:','median:','std dev:']

        #stats outputs
        self.output_text = StringVar()
        self.output_text.set('\n'.join(self.outstrs))
        self.output = Label(self, textvariable=self.output_text, height =4, justify = LEFT)
        self.output.grid(row=3, column=3, columnspan=2, rowspan=2, sticky=W, pady=10)

    #open an excel file
    def openFile(self):
        self.fname = tkFileDialog.askopenfilename(filetypes = (('excel files', '*.xlsx'), ('all files', '*.*')))
        
        #do nothing if no file is opened. Clear sheet list
        if not self.fname:
            self.sheetbox.delete(0, END)
            return

        try:
            sheets = helpers.getSheets(self.fname)
        except IOError as e:
            print e
            tkMessageBox.showwarning('File error', 'Cannot find any sheets')
            return
        except XLRDError as e:
            print e
            tkMessageBox.showwarning('File error', 'Unsupported file type!')

        #clear sheet box and load in new sheets
        self.sheetbox.delete(0, END)
            
        for sheet in sheets:
            self.sheetbox.insert(END, sheet)
    
    #handle auto binning checkbox. Disable manual entry if checked
    def binCheck(self):
        var = self.bvar.get()
        if var ==1:
            self.bentry.configure(state='disabled')
        else:
            self.bentry.configure(state='normal')

    #callback for analyse button. Return stats and print on frame
    def analyse(self):
        
        #exception handling
        try:
            fname = self.fname
            if not fname:
                raise IOError('File name is empty')
            
        except Exception as e:
            print e
            tkMessageBox.showwarning('File error', 'No file imported!')
            return

        try:
            sname = str(self.sheetbox.get(self.sheetbox.curselection()))
        except Exception as e:
            print e
            tkMessageBox.showwarning('Sheet selection', 'Please select a sheet')
            return
        
        #check binning options
        if self.bvar.get() == 1:
            nbins = None
        else:
            bin_entry = self.bentry.get()
            try:
                nbins = int(bin_entry)
            except ValueError as e:
                tkMessageBox.showwarning('Binning error', 'Please enter a valid bin number')
                return 
            except Exception as e:
                print e
                tkMessageBox.showwarning('Binning error', 'Please check your binning options')

        #analyse data and display results
        results = ana.analyse(fname, sname, nbins)
        out_text = '\n'.join('{} {}'.format(*x) for x in zip(self.outstrs, results.values()))
        self.output_text.set(out_text)


    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()
        self.pack()


#main app window
root = Tk()
root.title('Nano Tools Histogramorizer')
root.geometry('500x300+200+200')
app = MainApp(master=root)
app.mainloop()

