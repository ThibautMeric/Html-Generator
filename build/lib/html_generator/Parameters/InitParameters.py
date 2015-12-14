from html_generator.Parameters.RefreshParameters import *
from html_generator.Output.GenerateHtml import *

try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import *
except:
    import Tkinter as tk
    import ttk as ttk
    from Tkinter import *

def InitializePM(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfsize, ActivationTable, CardPack, Units, ButtonColor,Align):

    y=0
    for i in lfParameters.winfo_children():
        y+=1
        i.destroy()
        lfParameters.grid_rowconfigure(y, minsize=1)

    CallGenerateHtml = lambda event: GenerateHtml(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfsize, ActivationTable, CardPack, ButtonColor,Align)
    CallGenerateHtmlNoEvent = lambda : GenerateHtml(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfsize, ActivationTable, CardPack, ButtonColor,Align)
    CallGenerateHtmlThreeEvent = lambda event1,event2,event3: GenerateHtml(lfParameters, lfBoxType, lfOutpout, lfTabSize, TabSize, TypeTable, SupportedVersion, WellSize, PanelColor, CardColor, lfsize, ActivationTable, CardPack, ButtonColor,Align)


    if(lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[0]][0]):#if Panel

        CBTitle = tk.Label(lfParameters, text="Title:", name="cbtitle")
        TitleText = StringVar()
        ETitle = tk.Entry(lfParameters, textvariable=TitleText, name="etitle")
        TitleText.trace("w",CallGenerateHtmlThreeEvent)
        CBSize = ttk.Combobox(lfParameters, values=["","h1","h2","h3","h4","h5","h6"], state='readonly', name="cbsize",width=4)
        CBSize.set("")
        CBSize.bind("<<ComboboxSelected>>",CallGenerateHtml)

        LText = tk.Label(lfParameters, text="Text:", name="ltext")
        Text = StringVar()
        EText = tk.Entry(lfParameters, textvariable=Text, name="etext")
        Text.trace("w",CallGenerateHtmlThreeEvent)

        CBFooter = tk.Label(lfParameters, text="Footer:", name="cbfooter")
        FooterText = StringVar()
        EFooter = tk.Entry(lfParameters, textvariable=FooterText, name="efooter")
        FooterText.trace("w",CallGenerateHtmlThreeEvent)

        LColor = tk.Label(lfParameters, text="Color:", name="lcolor")
        CBColor = ttk.Combobox(lfParameters, values=list(PanelColor), state='readonly', name="cbcolor",width=17)
        CBColor.bind("<<ComboboxSelected>>",CallGenerateHtml)

        LListItem = tk.Label(lfParameters, text="Section in the box:", name="llistitem")
        SListItem = Spinbox(lfParameters, from_=1, to=15, name="slistitem",width=17,command=CallGenerateHtmlNoEvent)

        CBPicture = tk.Checkbutton(lfParameters, text="Add picture?", variable=ActivationTable[1][1], name="cbpicture",command=CallGenerateHtmlNoEvent)

        LListItem = tk.Label(lfParameters, text="Table:Row:", name="lrow")
        SRow = Spinbox(lfParameters, from_=0, to=15, name="srow",width=3,command=CallGenerateHtmlNoEvent)
        LListItem = tk.Label(lfParameters, text="    Column:", name="lcolumn")
        SColumn = Spinbox(lfParameters, from_=0, to=15, name="scolumn",width=3,command=CallGenerateHtmlNoEvent)

        LButton = tk.Label(lfParameters, text="Button:", name="lbutton")
        SButton = Spinbox(lfParameters, from_=0, to=15, name="sbutton",width=2,command=CallGenerateHtmlNoEvent)
        CBButton = ttk.Combobox(lfParameters, values=list(ButtonColor[SupportedVersion[1]]), state='readonly', name="cbbutton",width=17)
        CBButton.bind("<<ComboboxSelected>>",CallGenerateHtml)
        CBButton.set("White")


    elif(lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[0]][1]):#if Thumbnail

        1+1

    elif(lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[0]][2]):#if Well

        LText = tk.Label(lfParameters, text="                    Text:", name="ltext")
        Text = StringVar()
        EText = tk.Entry(lfParameters, textvariable=Text, name="etext")
        Text.trace("w",CallGenerateHtmlThreeEvent)

        LWellSize = tk.Label(lfParameters, text="           Well size:", name="lwellsize")
        CBWellSize = ttk.Combobox(lfParameters, values=list(WellSize),state='readonly', name="wellsize",width=17)
        CBWellSize.bind("<<ComboboxSelected>>",CallGenerateHtml)
        CBWellSize.set("Medium")

    elif(lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[1]][0]):#if Card

        CBHeader = tk.Label(lfParameters, text="Header:", name="cbheader")
        HeaderText = StringVar()
        EHeader = tk.Entry(lfParameters, textvariable=HeaderText, name="eheader")
        HeaderText.trace("w",CallGenerateHtmlThreeEvent)


        CBTitle = tk.Label(lfParameters, text="Title:", name="cbtitle")
        TitleText = StringVar()
        ETitle = tk.Entry(lfParameters, textvariable=TitleText, name="etitle")
        TitleText.trace("w",CallGenerateHtmlThreeEvent)

        CBSubTitle = tk.Label(lfParameters, text="SubTitle:", name="cbsubtitle")
        SubTitleText = StringVar()
        ETitle = tk.Entry(lfParameters, textvariable=SubTitleText, name="esubtitle")
        SubTitleText.trace("w",CallGenerateHtmlThreeEvent)

        LText = tk.Label(lfParameters, text="Text:", name="ltext")
        Text = StringVar()
        EText = tk.Entry(lfParameters, textvariable=Text, name="etext")
        Text.trace("w",CallGenerateHtmlThreeEvent)

        CBFooter = tk.Label(lfParameters, text="Footer:", name="cbfooter")
        FooterText = StringVar()
        EFooter = tk.Entry(lfParameters, textvariable=FooterText, name="efooter")
        FooterText.trace("w",CallGenerateHtmlThreeEvent)

        LColor = tk.Label(lfParameters, text="Color:", name="lcolor")
        CBColor = ttk.Combobox(lfParameters, values=list(PanelColor), state='readonly', name="cbcolor",width=17)
        CBColor.bind("<<ComboboxSelected>>",CallGenerateHtml)

        LListItem = tk.Label(lfParameters, text="Section in the box:", name="llistitem")
        SListItem = Spinbox(lfParameters, from_=0, to=15, name="slistitem",width=17,command=CallGenerateHtmlNoEvent)

        CBPicture = tk.Checkbutton(lfParameters, text="Add Picture?", variable=ActivationTable[2][0], name="cbpicture",command=CallGenerateHtmlNoEvent)

        CBPictureTop = tk.Checkbutton(lfParameters, text="Add Top Picture?", variable=ActivationTable[2][1], name="cbpicturetop",command=CallGenerateHtmlNoEvent)

        LWrap = tk.Label(lfParameters, text="Make a Set:", name="lwrap")
        CBGroupWrap = ttk.Combobox(lfParameters, values=CardPack, state='readonly', name="cbgroupwrap",width=17)
        CBGroupWrap.bind("<<ComboboxSelected>>",CallGenerateHtml)
        CBGroupWrap.set("Wrap")
        SWrap = Spinbox(lfParameters, from_=0, to=12, name="swrap",width=2,command=CallGenerateHtmlNoEvent)

        LListItem = tk.Label(lfParameters, text="Table:Row:", name="lrow")
        SRow = Spinbox(lfParameters, from_=0, to=15, name="srow",width=3,command=CallGenerateHtmlNoEvent)
        LListItem = tk.Label(lfParameters, text="    Column:", name="lcolumn")
        SColumn = Spinbox(lfParameters, from_=0, to=15, name="scolumn",width=3,command=CallGenerateHtmlNoEvent)

        LButton = tk.Label(lfParameters, text="Button:", name="lbutton")
        SButton = Spinbox(lfParameters, from_=0, to=15, name="sbutton",width=2,command=CallGenerateHtmlNoEvent)
        CBButton = ttk.Combobox(lfParameters, values=list(ButtonColor[SupportedVersion[1]]), state='readonly', name="cbbutton",width=17)
        CBButton.bind("<<ComboboxSelected>>",CallGenerateHtml)
        CBButton.set("White")

    elif(lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[2]][0]):#if Header

        CBTitle = tk.Label(lfParameters, text="Title:", name="cbtitle")
        TitleText = StringVar()
        ETitle = tk.Entry(lfParameters, textvariable=TitleText, name="etitle")
        TitleText.trace("w",CallGenerateHtmlThreeEvent)

        CBSize = ttk.Combobox(lfParameters, values=["h1","h2","h3","h4","h5","h6"], state='readonly', name="cbsize",width=4)
        CBSize.set("h1")
        CBSize.bind("<<ComboboxSelected>>",CallGenerateHtml)

        LAlign = tk.Label(lfParameters, text="Align:", name="lalign")
        CBAlign = ttk.Combobox(lfParameters, values=list(Align), state='readonly', name="cbalign",width=17)
        CBAlign.set("Left")
        CBAlign.bind("<<ComboboxSelected>>",CallGenerateHtml)

    elif(lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[2]][1]):#if Title

        CBTitle = tk.Label(lfParameters, text="Text:", name="cbtitle")
        TitleText = StringVar()
        ETitle = tk.Entry(lfParameters, textvariable=TitleText, name="etitle")
        TitleText.trace("w",CallGenerateHtmlThreeEvent)

        CBSize = ttk.Combobox(lfParameters, values=["h1","h2","h3","h4","h5","h6"], state='readonly', name="cbsize",width=4)
        CBSize.set("h1")
        CBSize.bind("<<ComboboxSelected>>",CallGenerateHtml)

        LAlign = tk.Label(lfParameters, text="Align:", name="lalign")
        CBAlign = ttk.Combobox(lfParameters, values=list(Align), state='readonly', name="cbalign",width=17)
        CBAlign.set("Left")
        CBAlign.bind("<<ComboboxSelected>>",CallGenerateHtml)

    elif(lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[2]][2]):#if Footer

        CBTitle = tk.Label(lfParameters, text="Text:", name="cbtitle")
        TitleText = StringVar()
        ETitle = tk.Entry(lfParameters, textvariable=TitleText, name="etitle")
        TitleText.trace("w",CallGenerateHtmlThreeEvent)

        CBSize = ttk.Combobox(lfParameters, values=["h1","h2","h3","h4","h5","h6"], state='readonly', name="cbsize",width=4)
        CBSize.set("h1")
        CBSize.bind("<<ComboboxSelected>>",CallGenerateHtml)

        LAlign = tk.Label(lfParameters, text="Align:", name="lalign")
        CBAlign = ttk.Combobox(lfParameters, values=list(Align), state='readonly', name="cbalign",width=17)
        CBAlign.set("Left")
        CBAlign.bind("<<ComboboxSelected>>",CallGenerateHtml)

    elif(lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[2]][3]):#if Paragraph

        CBTitle = tk.Label(lfParameters, text="Text:", name="cbtitle")
        TitleText = StringVar()
        ETitle = tk.Entry(lfParameters, textvariable=TitleText, name="etitle")
        TitleText.trace("w",CallGenerateHtmlThreeEvent)

        LAlign = tk.Label(lfParameters, text="Align:", name="lalign")
        CBAlign = ttk.Combobox(lfParameters, values=list(Align), state='readonly', name="cbalign",width=17)
        CBAlign.set("Left")
        CBAlign.bind("<<ComboboxSelected>>",CallGenerateHtml)


    elif(lfBoxType.children["elementchoice"].get() == TypeTable[SupportedVersion[2]][4]):#if Image

        1+1

    else:
        Message = tk.Label(lfParameters, text="Please select a component", name="message")

    if(len(lfBoxType.children["elementchoice"].get())>0):

        LTitle = tk.Label(lfParameters, text="Padding:", name="ltitle")
        CBUnit = ttk.Combobox(lfParameters, values=Units, state='readonly', name="cbunit",width=2)
        CBUnit.set(Units[0])
        CBUnit.bind("<<ComboboxSelected>>",CallGenerateHtml)
        LTop = tk.Label(lfParameters, text="Top:", name="ltop")
        STop = Spinbox(lfParameters, from_=0, to=1000, name="stop",width=4,command=CallGenerateHtmlNoEvent)
        LBottom = tk.Label(lfParameters, text="    Bottom:", name="lbottom")
        SBottom = Spinbox(lfParameters, from_=0, to=1000, name="sbottom",width=4,command=CallGenerateHtmlNoEvent)
        LLeft = tk.Label(lfParameters, text="Left:", name="lleft")
        SLeft = Spinbox(lfParameters, from_=0, to=1000, name="sleft",width=4,command=CallGenerateHtmlNoEvent)
        LRight = tk.Label(lfParameters, text="    Right:", name="lright")
        SRight = Spinbox(lfParameters, from_=0, to=1000, name="sright",width=4,command=CallGenerateHtmlNoEvent)



    RefreshPM(lfParameters)


pass
