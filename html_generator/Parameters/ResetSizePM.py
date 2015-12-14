from Parameters.RefreshSize import*
from Output.GenerateHtml import *
def ResetSizePM(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, ButtonColor, Align, Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8):
    for i in range(0,len(ActivationTable[0])):
        ActivationTable[0][i].set(0)
    
    Value1.set(0)
    Value2.set(0)
    Value3.set(0)
    Value4.set(0)
    Value5.set(0)
    Value6.set(0)
    Value7.set(0)
    Value8.set(0)

    RefreshSZ(lfSize)
    GenerateHtml(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfSize, ActivationTable, CardPack, ButtonColor, Align)
pass