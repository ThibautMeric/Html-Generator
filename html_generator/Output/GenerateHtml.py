try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import *
except:
    import Tkinter as tk
    import ttk as ttk
    from Tkinter import *


def GenerateHtml(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfsize, ActivationTable, CardPack, ButtonColor,Align):

    #General declaration
    Output = ""

    # Tab handler
    TAB = ""
    if(lfTabSize.children["cbtabsize"].get()==TabSize[0]):
        TAB = " "
    elif(lfTabSize.children["cbtabsize"].get()==TabSize[1]):
        TAB = "  "
    elif(lfTabSize.children["cbtabsize"].get()==TabSize[2]):
        TAB = "   "
    elif(lfTabSize.children["cbtabsize"].get()==TabSize[3]):
        TAB = "\t"

    # Size handler
    Display = ""

    if(int(ActivationTable[0][0].get()) == 1):
        Display += " col-xs-" + str (lfsize.children["sxsmall"].get())
    if(int(ActivationTable[0][1].get()) == 1):
        Display += " col-sm-" + str (lfsize.children["ssmall"].get())
    if(int(ActivationTable[0][2].get()) == 1):
        Display += " col-md-" + str (lfsize.children["smedium"].get())
    if(int(ActivationTable[0][3].get()) == 1):
        Display += " col-lg-" + str (lfsize.children["slarge"].get())

    if(int(ActivationTable[0][4].get()) == 1):
        Display += " col-xs-offset-" + str (lfsize.children["soxsmall"].get())
    if(int(ActivationTable[0][5].get()) == 1):
        Display += " col-sm-offset-" + str (lfsize.children["sosmall"].get())
    if(int(ActivationTable[0][6].get()) == 1):
        Display += " col-md-offset-" + str (lfsize.children["somedium"].get())
    if(int(ActivationTable[0][7].get()) == 1):
        Display += " col-lg-offset-" + str (lfsize.children["solarge"].get())



    #Padding handler
    try:
        Padding=""

        if(int(lfParameters.children["stop"].get())+
           int(lfParameters.children["sbottom"].get())+
           int(lfParameters.children["sleft"].get())+
           int(lfParameters.children["sright"].get())
           >0):
           Padding += " style=\""

        if(int(lfParameters.children["stop"].get())>0):
            Padding += " padding-top: " + lfParameters.children["stop"].get() + lfParameters.children["cbunit"].get() + ";"
        if(int(lfParameters.children["sbottom"].get())>0):
            Padding += " padding-bottom: " + lfParameters.children["sbottom"].get() + lfParameters.children["cbunit"].get() + ";"
        if(int(lfParameters.children["sleft"].get())>0):
            Padding += " padding-left: " + lfParameters.children["sleft"].get() + lfParameters.children["cbunit"].get() + ";"
        if(int(lfParameters.children["sright"].get())>0):
            Padding += " padding-right: " + lfParameters.children["sright"].get() + lfParameters.children["cbunit"].get() + ";"

        if(int(lfParameters.children["stop"].get())+
           int(lfParameters.children["sbottom"].get())+
           int(lfParameters.children["sleft"].get())+
           int(lfParameters.children["sright"].get())
           >0):
           Padding += "\""
    except: 1

#####################################################################################################################################
#Panel

    if(lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[0]][0]):

        Output += "<div class=\"container" + Display + "\"" +Padding +">\n"
        Output += TAB + "<div class=\"panel" + PanelColor[lfParameters.children["cbcolor"].get()] + "\">\n"

        if (len(lfParameters.children["etitle"].get()) > 0):
            if (len(lfParameters.children["cbsize"].get()) > 0):
                Output += TAB + TAB + "<div class=\"panel-heading\">" + "\n"
                Output += TAB + TAB + TAB + "<" + lfParameters.children["cbsize"].get()+ " class=\"panel-title\">" + "\n"
                Output += TAB + TAB + TAB + TAB + lfParameters.children["etitle"].get() + "\n"
                Output += TAB + TAB + TAB + "</" + lfParameters.children["cbsize"].get()+ ">"  + "\n"
                Output += TAB + TAB + "</div>" + "\n"
            else:
                Output += TAB + TAB + "<div class=\"panel-heading\">" + "\n"
                Output += TAB + TAB + TAB + "<p class=\"panel-title\">" + "\n"
                Output += TAB + TAB + TAB + TAB + lfParameters.children["etitle"].get() + "\n"
                Output += TAB + TAB + TAB + "</p>"  + "\n"
                Output += TAB + TAB + "</div>" + "\n"

        Output += TAB + TAB + "<div class=\"panel-body\">" + "\n"

        if (int(ActivationTable[1][1].get()) == 1):
            Output += TAB + TAB + TAB + "<img src=\"...\" alt=\"...\">" + "\n"

        if (len(lfParameters.children["etext"].get()) > 0):
            Output += TAB + TAB + TAB + "<p>" + lfParameters.children["etext"].get() + "</p>" + "\n"

        if(int(lfParameters.children["slistitem"].get()) > 1):
            Output += TAB + TAB + TAB + TAB + "<ul class=\"list-group\">" + "\n"
            for i in range(1, int(lfParameters.children["slistitem"].get())+1):
                    Output += TAB + TAB + TAB + TAB + TAB + "<li class=\"list-group-item\">Insert Text" + str(i) + "</li>" + "\n"
            Output += TAB + TAB + TAB + TAB + "</ul>" + "\n"

        if(int(lfParameters.children["srow"].get())*int(lfParameters.children["scolumn"].get()) > 0):
                    Output += TAB + TAB + TAB + "<table class=\"table\">" + "\n"
                    Output += TAB + TAB + TAB + TAB + "<tr>" + "\n"
                    for i in range(0,int(lfParameters.children["scolumn"].get())):
                        Output += TAB + TAB + TAB + TAB + TAB + "<th>" + "Title:[1][" + str(i) +"]</th>"  +"\n"
                    Output += TAB + TAB + TAB + TAB + "</tr>" + "\n"

                    for i in range(1,int(lfParameters.children["srow"].get())):
                        Output += TAB + TAB + TAB + TAB + "<tr>" + "\n"
                        for y in range(0,int(lfParameters.children["scolumn"].get())):
                            Output += TAB + TAB + TAB + TAB + TAB + "<td>" + "Cell:[" + str(i+1) + "]["  + str(y+1) + "]</td>" + "\n"
                        Output += TAB + TAB + TAB + TAB + "</tr>" + "\n"
                    Output += TAB + TAB + TAB + "</table>" + "\n"

        if(int(lfParameters.children["sbutton"].get())>0):
            Output +=  TAB + TAB + TAB + "<div class=\"container\">"+ "\n"
            for i in range(1,int(lfParameters.children["sbutton"].get())+1):
                Output += TAB + TAB + TAB + TAB +"<button type=\"button\" class=\" btn "+ ButtonColor[SupportedVersion[1]][lfParameters.children["cbbutton"].get()] + "\">" + "Button" + str(i) +"</button>" + "\n"
            Output +=  TAB + TAB + TAB + "</div>"+ "\n"

        Output += TAB + TAB + "</div>" + "\n"

        if (len(lfParameters.children["efooter"].get()) > 0):
            Output += TAB + TAB + "<div class=\"panel-footer\">" + lfParameters.children["efooter"].get() + "</div>" + "\n"

        Output += TAB + "</div>" + "\n"
        Output += "</div>" + "\n"


######################################################################################################################################
#Thumbnail

    elif(lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[0]][1]):
        Output += "<div class=\"row" + Display + "\"" + Padding + ">" + "\n"
        Output += TAB + "<div class=\"thumbnail\">" + "\n"
        Output += TAB + TAB + "<img src=\"...\" alt=\"...\">" + "\n"
        Output += TAB + "</div>" + "\n"
        Output += "</div>" + "\n"



######################################################################################################################################
#Well

    elif (lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[0]][2]):
        Output += "<div class=\"well" + Display + WellSize[lfParameters.children["wellsize"].get()] + "\"" + Padding + ">"

        if(len(lfParameters.children["etext"].get()) > 0):
            Output += lfParameters.children["etext"].get()
        else:
            Output += "Insert your text here"

        Output += "</div>"


######################################################################################################################################
#Card

    elif (lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[1]][0]):

        if(int(lfParameters.children["swrap"].get())>1):
            Output += "<div class=\"container" + Display + "\"" + Padding + ">" + "\n"
            if (lfParameters.children["cbgroupwrap"].get()==CardPack[0]):

                Output += TAB +"<div class=\"card-deck-wrapper\""+ ">" + "\n"
                Output += TAB + TAB +"<div class=\"card-deck"+ Display +"\">" + "\n"
            else:
                Output += TAB + TAB +"<div class=\"card-group\">" + "\n"
            for i in range(0,int(lfParameters.children["swrap"].get())):
                Output += TAB + TAB + TAB +"<div class=\"card\">" + "\n"
                if (int(ActivationTable[2][1].get()) == 1):# if top picture
                    Output += TAB + TAB + TAB + TAB +"<img class=\"card-img-top\" data-src=\"...\" alt=\"...\">" + "\n"

                if (len(lfParameters.children["eheader"].get()) > 0):# if header
                    Output += TAB + TAB + TAB + TAB +"<div class=\"card-header"+ CardColor[lfParameters.children["cbcolor"].get()] + "\">" + lfParameters.children["eheader"].get() + "</div>" + "\n"

                Output += TAB + TAB + TAB + TAB +"<div class=\"card-block"
                if(len(lfParameters.children["eheader"].get())==0):
                    Output += CardColor[lfParameters.children["cbcolor"].get()]
                Output +=  "\">" + "\n"

                if (len(lfParameters.children["etitle"].get()) > 0):# if title
                    Output += TAB + TAB + TAB +TAB + TAB +"<h4 class=\"card-title\">" + lfParameters.children["etitle"].get() + "</h4>" + "\n"

                if (len(lfParameters.children["esubtitle"].get()) > 0):# if subtitlte
                    Output += TAB + TAB + TAB +TAB + TAB +"<h6 class=\"card-subtitle text-muted\">" + lfParameters.children["esubtitle"].get() + "</h6>" + "\n"

                if (len(lfParameters.children["etext"].get()) > 0):#if text
                    Output += TAB + TAB + TAB +TAB + TAB +"<p class=\"card-text\">"+ lfParameters.children["etext"].get() +"</p>" + "\n"

                if (int(ActivationTable[2][0].get()) == 1):#if picture
                        Output += TAB + TAB + TAB + TAB + TAB +"<img src=\"...\" alt=\"...\">"+ "\n"

                if(int(lfParameters.children["slistitem"].get()) > 0):#if list
                    Output += TAB + TAB + TAB + TAB + TAB +"<ul class=\"list-group list-group-flush\">" + "\n"
                    for i in range(1, int(lfParameters.children["slistitem"].get())+1):
                        Output += TAB + TAB + TAB + TAB + TAB + TAB +"<li class=\"list-group-item\">Insert Text" + str(i) + "</li>" + "\n"
                    Output += TAB + TAB + TAB + TAB + TAB +"</ul>" + "\n"

                if(int(lfParameters.children["srow"].get())*int(lfParameters.children["scolumn"].get()) > 0):
                    Output += TAB + TAB + TAB + TAB + TAB +"<table class=\"table\">" + "\n"
                    Output += TAB + TAB + TAB + TAB + TAB + TAB +"<tr>" + "\n"
                    for i in range(0,int(lfParameters.children["scolumn"].get())):
                        Output += TAB + TAB + TAB + TAB + TAB + TAB + TAB +"<th>" + "Title:[1][" + str(i) +"]</th>"  +"\n"
                    Output += TAB + TAB + TAB + TAB + TAB + TAB +"</tr>" + "\n"

                    for i in range(1,int(lfParameters.children["srow"].get())):
                        Output += TAB + TAB + TAB + TAB + TAB + TAB +"<tr>" + "\n"
                        for y in range(0,int(lfParameters.children["scolumn"].get())):
                            Output += TAB + TAB + TAB + TAB + TAB + TAB + TAB +"<td>" + "Cell:[" + str(i+1) + "]["  + str(y+1) + "]</td>" + "\n"
                        Output += TAB + TAB + TAB + TAB + TAB + TAB +"</tr>" + "\n"
                    Output += TAB + TAB + TAB + TAB + TAB +"</table>" + "\n"

                if(int(lfParameters.children["sbutton"].get())>0):
                    Output += TAB + TAB + TAB + TAB + TAB +"<div class=\"container\">"+ "\n"
                    for i in range(1,int(lfParameters.children["sbutton"].get())+1):
                        Output += TAB + TAB + TAB + TAB + TAB + TAB +"<button type=\"button\" class=\" btn "+ ButtonColor[SupportedVersion[1]][lfParameters.children["cbbutton"].get()] + "\">" + "Button" + str(i) +"</button>" + "\n"
                    Output += TAB + TAB + TAB + TAB + TAB +"</div>"+ "\n"

                Output += TAB + TAB + TAB + TAB +"</div>" + "\n"

                if (len(lfParameters.children["efooter"].get()) > 0):#if footer
                    Output +=  TAB + TAB + TAB +"<div class=\"card-footer text-muted\">" + lfParameters.children["efooter"].get() + "</div>" + "\n"
                Output +=  TAB + TAB + TAB +"</div>" + "\n"
            Output +=  TAB + TAB +"</div>" + "\n"
            if (lfParameters.children["cbgroupwrap"].get()==CardPack[0]): Output += TAB +"</div>" + "\n"
            Output += "</div>" + "\n"

        else:
            Output += "<div class=\"container" + Display + "\"" + Padding + ">" + "\n"
            Output += TAB + "<div class=\"card\">" + "\n"
            if (int(ActivationTable[2][1].get()) == 1):# if top picture
                Output += TAB + TAB + "<img class=\"card-img-top\" data-src=\"...\" alt=\"...\">" + "\n"

            if (len(lfParameters.children["eheader"].get()) > 0):# if header
                Output += TAB + TAB + "<div class=\"card-header"+ CardColor[lfParameters.children["cbcolor"].get()] + "\">" + lfParameters.children["eheader"].get() + "</div>" + "\n"

            Output += TAB + TAB + "<div class=\"card-block"
            if(len(lfParameters.children["eheader"].get())==0):
                Output += CardColor[lfParameters.children["cbcolor"].get()]
            Output +=  "\">" + "\n"

            if (len(lfParameters.children["etitle"].get()) > 0):# if title
                Output += TAB + TAB + TAB +"<h4 class=\"card-title\">" + lfParameters.children["etitle"].get() + "</h4>" + "\n"

            if (len(lfParameters.children["esubtitle"].get()) > 0):# if subtitlte
                Output += TAB + TAB + TAB +"<h6 class=\"card-subtitle text-muted\">" + lfParameters.children["esubtitle"].get() + "</h6>" + "\n"

            if (len(lfParameters.children["etext"].get()) > 0):#if text
                Output += TAB + TAB + TAB +"<p class=\"card-text\">"+ lfParameters.children["etext"].get() +"</p>" + "\n"

            if (int(ActivationTable[2][0].get()) == 1):#if picture
                    Output += TAB + TAB + TAB + "<img src=\"...\" alt=\"...\">"+ "\n"

            if(int(lfParameters.children["slistitem"].get()) > 0):#if list
                Output += TAB + TAB + TAB + "<ul class=\"list-group list-group-flush\">" + "\n"
                for i in range(1, int(lfParameters.children["slistitem"].get())+1):
                    Output += TAB + TAB + TAB + TAB + "<li class=\"list-group-item\">Insert Text" + str(i) + "</li>" + "\n"
                Output += TAB + TAB + TAB + "</ul>" + "\n"

            if(int(lfParameters.children["srow"].get())*int(lfParameters.children["scolumn"].get()) > 0):
                    Output += TAB + TAB + TAB + "<table class=\"table\">" + "\n"
                    Output += TAB + TAB + TAB + TAB + "<tr>" + "\n"
                    for i in range(0,int(lfParameters.children["scolumn"].get())):
                        Output += TAB + TAB + TAB + TAB + TAB + "<th>" + "Title:[1][" + str(i) +"]</th>"  +"\n"
                    Output += TAB + TAB + TAB + TAB + "</tr>" + "\n"

                    for i in range(1,int(lfParameters.children["srow"].get())):
                        Output += TAB + TAB + TAB + TAB + "<tr>" + "\n"
                        for y in range(0,int(lfParameters.children["scolumn"].get())):
                            Output += TAB + TAB + TAB + TAB + TAB + "<td>" + "Cell:[" + str(i+1) + "]["  + str(y+1) + "]</td>" + "\n"
                        Output += TAB + TAB + TAB + TAB + "</tr>" + "\n"
                    Output += TAB + TAB + TAB + "</table>" + "\n"

            if(int(lfParameters.children["sbutton"].get())>0):
                Output += TAB + TAB + TAB +"<div class=\"container\">"+ "\n"
                for i in range(1,int(lfParameters.children["sbutton"].get())+1):
                    Output += TAB + TAB + TAB + TAB +"<button type=\"button\" class=\" btn "+ ButtonColor[SupportedVersion[1]][lfParameters.children["cbbutton"].get()] + "\">" + "Button" + str(i) +"</button>" + "\n"
                Output += TAB + TAB + TAB +"</div>"+ "\n"


            Output += TAB + TAB + "</div>" + "\n"

            if (len(lfParameters.children["efooter"].get()) > 0):#if footer
                Output += TAB + TAB +"<div class=\"card-footer text-muted\">" + lfParameters.children["efooter"].get() + "</div>" + "\n"
            Output += TAB + "</div>" + "\n"
            Output += "</div>" + "\n"

######################################################################################################################################
#Header

    elif (lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[2]][0]):
        Output += "<header"
        if (len(Display) > 0):
            Output += " class=\"row" + Display +"\""
        if (len(Padding) > 0):
            Output += Padding
        Output += ">\n"
        Output += TAB + "<" + lfParameters.children["cbsize"].get() + Align[lfParameters.children["cbalign"].get()] + ">"
        if(len(lfParameters.children["etitle"].get())>0):
            Output += lfParameters.children["etitle"].get() + "</" + lfParameters.children["cbsize"].get() + ">" + "\n"
        else:
            Output += "Insert text here" + "</" + lfParameters.children["cbsize"].get() + ">" + "\n"
        Output += "</header>" + "\n"

######################################################################################################################################
#Title

    elif (lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[2]][1]):
        Output += "<" + lfParameters.children["cbsize"].get()+ Align[lfParameters.children["cbalign"].get()]
        if (len(Display) > 0):
            Output += " class=\"row" + Display + "\""
        if (len(Padding) > 0):
            Output += Padding
        Output += ">"

        if(len(lfParameters.children["etitle"].get())>0):
            Output += lfParameters.children["etitle"].get() + "</" + lfParameters.children["cbsize"].get() + ">" + "\n"
        else:
            Output += "Insert text here" + "</" + lfParameters.children["cbsize"].get() + ">" + "\n"

######################################################################################################################################
#Footer
    elif (lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[2]][2]):
        Output += "<footer"
        if (len(Display) > 0):
            Output += " class=\"row" + Display + "\""
        if (len(Padding) > 0):
            Output += Padding
        Output += ">\n"
        Output += TAB + "<" + lfParameters.children["cbsize"].get() + Align[lfParameters.children["cbalign"].get()] + ">"
        if(len(lfParameters.children["etitle"].get())>0):
            Output += lfParameters.children["etitle"].get() + "</" + lfParameters.children["cbsize"].get() + ">" + "\n"
        else:
            Output += "Insert text here" + "</" + lfParameters.children["cbsize"].get() + ">" + "\n"
        Output += "</footer>" + "\n"

######################################################################################################################################
#Paragraph
    elif (lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[2]][3]):
        Output += "<p" + Align[lfParameters.children["cbalign"].get()]
        if (len(Display) > 0):
            Output += " class=\"row" + Display + "\""
        if (len(Padding) > 0):
            Output += Padding

        Output += ">"
        if(len(lfParameters.children["etitle"].get())>0):
            Output += lfParameters.children["etitle"].get()
        else:
            Output += "Insert text here"
        Output += "</p>" + "\n"
######################################################################################################################################
#Image
    elif (lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[2]][4]):
        Output += "<img"
        if (len(Display) > 0):
            Output += " class=\"row" + Display + "\""
        if (len(Padding) > 0):
            Output += Padding
        Output += " src=\"...\" alt=\"...\">" + "\n"


######################################################################################################################################
#Empty

    else:
        Output += "<!DOCTYPE html>" + "\n"
        Output += "<html lang=\"en\">" + "\n"
        Output += TAB + "<head>" + "\n"
        Output += TAB + TAB + "<meta charset=\"utf-8\">" + "\n"
        Output += TAB + TAB + "<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">" + "\n"
        Output += TAB + TAB + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">" + "\n"
        Output += TAB + TAB + "<!-- Title displayed on the Web Browser tab -->" + "\n"
        Output += TAB + TAB + "<title>title</title>" + "\n"
        Output += TAB + TAB + "<!-- Bootstrap + Custom CSS-->" + "\n"
        Output += TAB + TAB + "<link rel=\"stylesheet\" href=\"yourcsspath.css\">" + "\n"
        Output += TAB + TAB + "<!-- Javascript-->" + "\n"
        Output += TAB + TAB + "<script src=\"yourscriptfile.js\"></script>" + "\n"
        Output += TAB + "</head>" + "\n"
        Output += TAB + "<body>" + "\n"
        Output += TAB + TAB + "<!-- page content -->" + "\n"
        Output += TAB + "</body>" + "\n"
        Output += "</html>" + "\n"




    lfOutpout.children["outputwindow"].delete(1.0, END)
    lfOutpout.children["outputwindow"].insert(END, Output)
    pass
