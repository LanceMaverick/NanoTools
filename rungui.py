from Tkinter import *
import tkMessageBox
import tkFileDialog
import xlrd
import helpers
import analyse as ana

class MainApp(Frame):
    
    def createWidgets(self):
        
        self.label_text = StringVar()
        self.label_text.set('Import excel file and choose the sheet')
        self.label = Label(self, textvariable=self.label_text, height =2)
        self.label.pack()

        #import file button
        self.imp_button = Button(self, text='Import Excel File', width=20, command=self.openFile)
        self.imp_button.pack(side='top', padx=15, pady=15)
        
        #analyse button
        self.ana_button = Button(self, text='Analyse', width=20, command=self.analyse)
        self.ana_button.pack(side='bottom', padx=15, pady=15)
        
        
        
        #bin selection
        self.blabel_text = StringVar()
        self.blabel_text.set('Specify binning')
        self.blabel = Label(self, textvariable=self.blabel_text, height =2)
        self.blabel.pack(side = 'left')
        
        self.bentry = Entry(self, width=5)
        self.bentry.pack(side = 'left')
        
        self.bvar = IntVar()
        self.bcheck = Checkbutton(self, text="automatic", variable=self.bvar, command=self.binCheck)
        self.bcheck.pack(side = 'left')
        
        #sheet list
        self.scrollbar = Scrollbar(root, orient="vertical")
        
        self.sheetbox = Listbox(self, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.sheetbox.yview)
        #self.scrollbar.pack(side="right", fill="y")
        self.sheetbox.pack(side = 'left')
        
#        self.slabel_text = StringVar()
#        self.slabel_text.set('Choose sheet')
 #       self.slabel = Label(self, textvariable=self.slabel_text, height =1)
#        self.slabel.pack(side = 'top')

       

    def openFile(self):
        self.fname = tkFileDialog.askopenfilename(filetypes = (('excel files', '*.xlsx'), ('all files', '*.*')))
        sheets = helpers.getSheets(self.fname)
        self.sheetbox.delete(0, END)

        for sheet in sheets:
            self.sheetbox.insert(END, sheet)

    def binCheck(self):
        var = self.bvar.get()
        if var ==1:
            self.bentry.configure(state='disabled')
        else:
            self.bentry.configure(state='normal')

    def analyse(self):
        try:
            fname = self.fname 
        except:
            tkMessageBox.showwarning('File error', 'No file imported!')
            return

        try:
            sname = str(self.sheetbox.get(self.sheetbox.curselection()))
        except:
            tkMessageBox.showwarning('Sheet selection', 'Please select a sheet')
            return
        
        if self.bvar.get() == 1:
            nbins = None
        else:
            bin_entry = self.bentry.get()
            try:
                nbins = int(bin_entry)
            except:
                tkMessageBox.showwarning('Binning effor', 'Please enter a valid bin number')
                return 
        
        ana.analyse(fname, sname, nbins)

    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()
        self.pack()


#main app window
root = Tk()
root.title('Nano Tools Histogramorizer')
root.geometry('500x400+200+200')
app = MainApp(master=root)
app.mainloop()

