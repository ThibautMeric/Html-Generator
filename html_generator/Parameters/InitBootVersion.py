from Parameters.InitElementType import*

try:
    import tkinter as tk
    import tkinter.ttk as ttk
except:
    import Tkinter as tk
    import ttk as ttk
    from Tkinter import *
    
def InitializeBV(lfParameters,lfBootVersion, lfSize, lfOutpout, lfBoxType, TypeTable,SupportedVersion, WellSize, PanelColor, CardColor, ActivationTable, CardPack, lfTabSize, TabSize, Units, ButtonColor,Align):
    CallInitElementType = lambda event: InitializeET(lfParameters,lfBootVersion, lfSize, lfOutpout, lfBoxType, TypeTable,SupportedVersion, WellSize, PanelColor, CardColor, ActivationTable, CardPack, lfTabSize, TabSize, Units, ButtonColor,Align)
    VersionChoice = ttk.Combobox(lfBootVersion, values=SupportedVersion, state='readonly', name="versionchoice")
    VersionChoice.bind("<<ComboboxSelected>>",CallInitElementType)
    
pass