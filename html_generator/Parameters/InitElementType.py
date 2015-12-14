from Parameters.InitParameters import*

try:
    import tkinter as tk
    import tkinter.ttk as ttk
except:
    import Tkinter as tk
    import ttk as ttk
    from Tkinter import *
    
def InitializeET(lfParameters,lfBootVersion, lfSize, lfOutpout, lfBoxType, TypeTable,SupportedVersion, WellSize, PanelColor, CardColor, ActivationTable, CardPack, lfTabSize, TabSize, Units, ButtonColor,Align):
    
    for i in lfBoxType.winfo_children():
        i.destroy()
    
    ElementChoice = ttk.Combobox(lfBoxType, state='disabled', name="elementchoice")
    
    if ((lfBootVersion.children["versionchoice"].get())==(SupportedVersion[0])):
        ElementChoice.configure(values=TypeTable[SupportedVersion[0]], state="readonly")
        ElementChoice.pack(padx=40,pady=5)
    if ((lfBootVersion.children["versionchoice"].get())==(SupportedVersion[1])):
        ElementChoice.configure(values=TypeTable[SupportedVersion[1]], state="readonly")
        ElementChoice.pack(padx=40,pady=5)
    if ((lfBootVersion.children["versionchoice"].get())==(SupportedVersion[2])):
        ElementChoice.configure(values=TypeTable[SupportedVersion[2]], state="readonly")
        ElementChoice.pack(padx=40,pady=5)
    else:
        ElementChoice.pack(padx=40,pady=5)
    
        
    CallIRefresh = lambda event: Refresh(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, Units, ButtonColor,Align)
    ElementChoice.bind("<<ComboboxSelected>>",CallIRefresh)
    InitializePM(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, Units, ButtonColor,Align)
pass
def Refresh(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, Units, ButtonColor,Align):
    InitializePM(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, Units, ButtonColor,Align)
    GenerateHtml(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, ButtonColor,Align)
pass