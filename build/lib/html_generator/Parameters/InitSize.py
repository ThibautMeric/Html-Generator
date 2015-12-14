try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import *
except:
    import Tkinter as tk
    import ttk as ttk
    from Tkinter import *
from html_generator.Output.GenerateHtml import *
from html_generator.Parameters.RefreshSize import *
from html_generator.Parameters.ResetSizePM import *
import platform
def InitializeSZ(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, ButtonColor,Align):

    CallRefresh = lambda event: Refresh(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, ButtonColor,Align)
    CallRefreshNoEvent = lambda: Refresh(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, ButtonColor,Align)
    CallResetSizePM = lambda: ResetSizePM(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, ButtonColor,Align, Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8)
    LTitle1 = tk.Label(lfSize, text="Select Size of Component:", name="ltitle1")

    #Size xs

    CBSmall = tk.Checkbutton(lfSize, text="XSmall Mode:", name="cbxsmall", variable=ActivationTable[0][0], command=CallRefreshNoEvent)
    Value1 = DoubleVar()
    scale = tk.Scale(lfSize, variable=Value1, from_=1, to=12, orient=HORIZONTAL, name="sxsmall", command=CallRefresh)

    #Size sm

    CBSmall = tk.Checkbutton(lfSize, text="Small Mode:", name="cbsmall", variable=ActivationTable[0][1], command=CallRefreshNoEvent)
    Value2 = DoubleVar()
    scale = tk.Scale(lfSize, variable=Value2, from_=1, to=12, orient=HORIZONTAL, name="ssmall", command=CallRefresh)

    #Size md

    CBSmall = tk.Checkbutton(lfSize, text="Medium Mode:", name="cbmedium", variable=ActivationTable[0][2], command=CallRefreshNoEvent)
    Value3 = DoubleVar()
    scale = tk.Scale(lfSize, variable=Value3, from_=1, to=12, orient=HORIZONTAL, name="smedium", command=CallRefresh)

    #Size lg

    CBSmall = tk.Checkbutton(lfSize, text="Large Mode:", name="cblarge", variable=ActivationTable[0][3], command=CallRefreshNoEvent)
    Value4 = DoubleVar()
    scale = tk.Scale(lfSize, variable=Value4, from_=1, to=12, orient=HORIZONTAL, name="slarge", command=CallRefresh)




    LTitle2 = tk.Label(lfSize, text="Select Offset of Component:", name="ltitle2")

    #Size xs

    CBSmall = tk.Checkbutton(lfSize, text="XSmall Mode:", name="cboxsmall", variable=ActivationTable[0][4], command=CallRefreshNoEvent)
    Value5 = DoubleVar()
    scale = tk.Scale(lfSize, variable=Value5, from_=0, to=11, orient=HORIZONTAL, name="soxsmall", command=CallRefresh)

    #Size sm

    CBSmall = tk.Checkbutton(lfSize, text="Small Mode:", name="cbosmall", variable=ActivationTable[0][5], command=CallRefreshNoEvent)
    Value6 = DoubleVar()
    scale = tk.Scale(lfSize, variable=Value6, from_=0, to=11, orient=HORIZONTAL, name="sosmall", command=CallRefresh)

    #Size md

    CBSmall = tk.Checkbutton(lfSize, text="Medium Mode:", name="cbomedium", variable=ActivationTable[0][6], command=CallRefreshNoEvent)
    Value7 = DoubleVar()
    scale = tk.Scale(lfSize, variable=Value7, from_=0, to=11, orient=HORIZONTAL, name="somedium", command=CallRefresh)

    #Size lg

    CBSmall = tk.Checkbutton(lfSize, text="Large Mode:", name="cbolarge", variable=ActivationTable[0][7])
    Value8 = DoubleVar()
    scale = tk.Scale(lfSize, variable=Value8, from_=0, to=11, orient=HORIZONTAL, name="solarge", command=CallRefresh)



    if(platform.system() == 'Windows'):Reset = ttk.Button(lfSize, text="Reset", command=CallResetSizePM, name="breset")
    else:Reset = tk.Button(lfSize, text="Reset", command=CallResetSizePM, name="breset")
pass
def Refresh(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, ButtonColor, Align):
    GenerateHtml(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, ButtonColor, Align)
    RefreshSZ(lfSize)
pass
