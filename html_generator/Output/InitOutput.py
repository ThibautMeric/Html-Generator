try:
    import tkinter as tk
    import tkinter.ttk as ttk
except:
    import Tkinter as tk
    import ttk as ttk
    from Tkinter import *
    
def InitializeOP(lfOutpout):
    OutputWindow = tk.Text(lfOutpout, height=30, width=90,name="outputwindow")
    OutputWindow.configure(tabs=("1c","2c"))
pass