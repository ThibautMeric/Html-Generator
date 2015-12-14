def RefreshPM(lfParameters):
    
    
    for i in range(0,100):
        lfParameters.grid_rowconfigure(i, minsize=0)
    
    line=0
    lfParameters.grid_columnconfigure(1, minsize=100)
    lfParameters.grid_columnconfigure(2, minsize=100)
    
    try:
        lfParameters.children["message"].pack(fill="y")
        line+=1
    except:1
    
    
    try:
        lfParameters.children["cbheader"].grid(row=line, column=1,sticky="en")
    except:1
    try:
        lfParameters.children["eheader"].grid(row=line, column=2,sticky="n")
        lfParameters.grid_rowconfigure(line, minsize=24)
        line+=1
    except:1

    
    try:
        lfParameters.children["cbtitle"].grid(row=line, column=1,sticky="en")
    except:1
    try:
        lfParameters.children["cbsize"].grid(row=line, column=1,sticky="wn")
    except:1
    
    try:
        lfParameters.children["etitle"].grid(row=line, column=2,sticky="n")
        lfParameters.grid_rowconfigure(line, minsize=24)
        line+=1
    except:1
    
    try:
        lfParameters.children["lalign"].grid(row=line, column=1,sticky="en")
    except:1   
    try:
        lfParameters.children["cbalign"].grid(row=line, column=2,sticky="n")
        lfParameters.grid_rowconfigure(line, minsize=24)
        line+=1
    except:1
    
    try:
        lfParameters.children["cbsubtitle"].grid(row=line, column=1,sticky="en")
    except:1
    try:
        lfParameters.children["esubtitle"].grid(row=line, column=2,sticky="n")
        lfParameters.grid_rowconfigure(line, minsize=24)
        line+=1
    except:1
    
    
    try:
        lfParameters.children["ltext"].grid(row=line, column=1,sticky="en")
    except:1
    try:
        lfParameters.children["etext"].grid(row=line, column=2,sticky="n")
        lfParameters.grid_rowconfigure(line, minsize=24)
        line+=1
    except:1


    try:
        lfParameters.children["cbfooter"].grid(row=line, column=1,sticky="en")
    except:1
    try:
        lfParameters.children["efooter"].grid(row=line, column=2,sticky="n")
        lfParameters.grid_rowconfigure(line, minsize=24)
        line+=1
    except:1   

 
    try:
        lfParameters.children["lcolor"].grid(row=line, column=1,sticky="en")
    except:1
    try:
        lfParameters.children["cbcolor"].grid(row=line, column=2,sticky="n")
        lfParameters.grid_rowconfigure(line, minsize=24)
        line+=1
    except:1
    
    
    try:
        lfParameters.children["lwellsize"].grid(row=line, column=1,sticky="n")
    except:1
    try:
        lfParameters.children["wellsize"].grid(row=line, column=2,sticky="n")
        lfParameters.grid_rowconfigure(line, minsize=24)
        line+=1
    except:1
    
    
    try:
        lfParameters.children["llistitem"].grid(row=line, column=1, columnspan=2, sticky="wn")
    except:1
    try:
        lfParameters.children["slistitem"].grid(row=line, column=2,sticky="n")
        line+=1
    except:1
    
    try:
        lfParameters.children["cbpicturetop"].grid(row=line, column=2, columnspan=2,sticky="wn")
    except:1 
    try:
        lfParameters.children["cbpicture"].grid(row=line, column=1,sticky="wn")
        line+=1
    except:1
    
    try:
        lfParameters.children["lwrap"].grid(row=line, column=1, sticky="wn")
    except:1
    try:
        lfParameters.children["cbgroupwrap"].grid(row=line, column=2, sticky="wn")
    except:1
    try:
        lfParameters.children["swrap"].grid(row=line, column=1,sticky="en")
        lfParameters.grid_rowconfigure(line, minsize=24)
        line+=1
    except:1
    
    
    try:
        lfParameters.children["lrow"].grid(row=line, column=1,sticky="wn")
        lfParameters.grid_rowconfigure(line, minsize=24)
    except:1
    try:
        lfParameters.children["srow"].grid(row=line, column=1,sticky="en")
    except:1
    try:
        lfParameters.children["lcolumn"].grid(row=line, column=2,sticky="wn")
    except:1
    try:
        lfParameters.children["scolumn"].grid(row=line, column=2,sticky="en")
        line+=1
    except:1
    
    try:
        lfParameters.children["ltitle"].grid(row=line, column=1,sticky="wn")
        lfParameters.grid_rowconfigure(line, minsize=24)
    except:1
    try:
        lfParameters.children["cbunit"].grid(row=line, column=1,sticky="en")
        line+=1
    except:1
    try:
        lfParameters.children["ltop"].grid(row=line, column=1,sticky="wn")
    except:1
    try:
        lfParameters.children["stop"].grid(row=line, column=1,sticky="en")
    except:1
    try:
        lfParameters.children["lbottom"].grid(row=line, column=2,sticky="wn")
    except:1
    try:
        lfParameters.children["sbottom"].grid(row=line, column=2,sticky="en")
        line+=1
    except:1
    try:
        lfParameters.children["lleft"].grid(row=line, column=1,sticky="wn")
    except:1
    try:
        lfParameters.children["sleft"].grid(row=line, column=1,sticky="en")
    except:1
    try:
        lfParameters.children["lright"].grid(row=line, column=2,sticky="wn")
    except:1
    try:
        lfParameters.children["sright"].grid(row=line, column=2,sticky="en")
        line+=1
    except:1
    
    
    try:
        lfParameters.children["lbutton"].grid(row=line, column=1,sticky="ws")
        lfParameters.grid_rowconfigure(line, minsize=24)
    except:1
    try:
        lfParameters.children["sbutton"].grid(row=line, column=1,sticky="es")
    except:1
    try:
        lfParameters.children["cbbutton"].grid(row=line, column=2,sticky="ws")
        line+=1
    except:1

    lfParameters.grid(row=3, column=1, rowspan=96, sticky= "news")

pass