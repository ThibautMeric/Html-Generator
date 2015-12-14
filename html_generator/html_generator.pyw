# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Thibaut MERIC"
__date__ = "$5 dec. 2015 23:17:40$"

try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import *
except:
    import Tkinter as tk
    import ttk as ttk
    from Tkinter import *
from Parameters.InitBootVersion import *
from Parameters.InitElementType import *
from Parameters.InitParameters import *
from Parameters.InitSize import *
from Parameters.InitTabSize import *
from Output.InitOutput import *

from Parameters.RefreshBootVersion import *
from Parameters.RefreshElementType import *
from Parameters.RefreshParameters import *
from Parameters.RefreshSize import *
from Parameters.RefreshTabSize import *
from Output.RefreshOutput import *
import platform


    #######################
    ##GENERAL DECLARATION##
    #######################
Version = "v0.8"
SupportedVersion = ["Bootstrap 3.xx", "Bootstrap 4.xx","General"]
Bootstrap3Type = ["Panel", "Thumbnail", "Well"]
Bootstrap4Type = ["Card"]
GeneralType = ["Header","Title","Footer","Paragraph","Image"]

TypeTable = {SupportedVersion[0]:Bootstrap3Type,
    SupportedVersion[1]:Bootstrap4Type,
    SupportedVersion[2]:GeneralType
}
WellSize = {"Small":" well-sm", "Medium":"", "Large":" well-lg"}
PanelColor = {"":" panel-default","Default":" panel-default", "Dark Blue":" panel-primary", "Green":" panel-success", "Light Blue":" panel-info", "Yellow":" panel-warning", "Red":" panel-danger"}
CardColor = {"":"","Default":"", "Dark Blue": " card-primary", "Green": " card-success", "Light Blue": " card-info", "Yellow": " card-warning", "Red": " card-danger"}
CardPack= ["Wrap","Group"]
TabSize =["One Space:     \" \"","Two Spaces:   \"  \"","Three Spaces:\"   \"","One Tab:        \"\\t\""]
Units= ["px","%","em"]
Align= {"Center":" align=\"center\"","Left":"","Right":" align=\"right\"","Justify":" align=\"justify\""}
ButtonBootstrap3={}
ButtonBootstrap4={"Blue":"btn-primary","White":"btn-secondary","Green":"btn-success","Light Blue":"btn-info","Orange":"btn-warning","Red":"btn-danger","Link":"btn-link"}
ButtonColor = {SupportedVersion[0]:ButtonBootstrap3,SupportedVersion[1]:ButtonBootstrap4}
    ##############################
    ##END OF GENERAL DECLARATION##
    ##############################

Window = Tk()
line1=[]
line2=[]
line3=[]
ActivationTable= [line1,line2,line3]

for i in range(0,8):
    Activation = StringVar()
    Activation.set(0)
    ActivationTable[0].append(Activation)
    
for i in range(0,2):
    Activation = StringVar()
    Activation.set(0)
    ActivationTable[1].append(Activation)
for i in range(0,3):
    Activation = StringVar()
    Activation.set(0)
    ActivationTable[2].append(Activation)


Window.resizable(width=False, height=False)
Window.title("Html Generator " + Version)
WindowSetting = {}

if(platform.system() == 'Windows'):
    WindowSetting["Reduce"] = 1
    WindowSetting["Enlarge"] = 1
elif(platform.system() == 'Darwin'):
    WindowSetting["Reduce"] = 0.72
    WindowSetting["Enlarge"] = 1.1
else:
    WindowSetting["Reduce"] = 0.7
    WindowSetting["Enlarge"] = 1.2


lfBootVersion = tk.LabelFrame(Window, text="Choose Bootstrap Version:")
lfBoxType = tk.LabelFrame(Window, text="Choose Box Type:")
lfParameters = tk.LabelFrame(Window, text="Select your Parameters:")
lfSize = tk.LabelFrame(Window, text="Choose Size Options:")
lfOutpout = tk.LabelFrame(Window, text="Output Code:")
lfTabSize = tk.LabelFrame(Window, text="Define Tab Size:") 

InitializeBV(lfParameters,lfBootVersion, lfSize, lfOutpout, lfBoxType, TypeTable,SupportedVersion, WellSize, PanelColor, CardColor, ActivationTable, CardPack, lfTabSize, TabSize, Units, ButtonColor,Align)
InitializeET(lfParameters,lfBootVersion, lfSize, lfOutpout, lfBoxType, TypeTable,SupportedVersion, WellSize, PanelColor, CardColor, ActivationTable, CardPack, lfTabSize, TabSize, Units, ButtonColor,Align)
InitializePM(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, Units, ButtonColor,Align)
InitializeOP(lfOutpout)
InitializeSZ(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, ButtonColor,Align)
InitializeTabSize(lfParameters, lfBoxType, lfOutpout, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, lfTabSize, TabSize, ButtonColor,Align)

RefreshBV(lfBootVersion)
RefreshET(lfBoxType)
RefreshPM(lfParameters)
RefreshOP(lfOutpout)
RefreshSZ(lfSize)
RefreshTabSize(lfTabSize)


Window.mainloop()