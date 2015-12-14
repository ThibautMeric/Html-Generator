from html_generator.Output.GenerateHtml import*
try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import *
except:
    import Tkinter as tk
    import ttk as ttk
    from Tkinter import *

def InitializeTabSize(lfParameters, lfBoxType, lfOutpout, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfsize, ActivationTable, CardPack, lfTabSize, TabSize, ButtonColor, Align):

    CallGenerateHtml = lambda event: GenerateHtml(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfsize, ActivationTable, CardPack, ButtonColor,Align)

    CBTabSize = ttk.Combobox(lfTabSize, values=TabSize, state='readonly', name="cbtabsize",width=17)
    CBTabSize.set(TabSize[3])
    CBTabSize.bind("<<ComboboxSelected>>",CallGenerateHtml)

pass
