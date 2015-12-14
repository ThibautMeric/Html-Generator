try:
    import tkinter as tk
    import tkinter.ttk as ttk
except:
    import Tkinter as tk
    import ttk as ttk
    from Tkinter import *
import platform

def InitializeOP(lfOutpout):
    if(platform.system() == 'Windows'):OutputWindow = tk.Text(lfOutpout, height=30, width=90,name="outputwindow")
    else :OutputWindow = tk.Text(lfOutpout, height=36, width=90,name="outputwindow")
    OutputWindow.configure(tabs=("1c","2c"))
pass
