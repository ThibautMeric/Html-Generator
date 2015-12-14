def RefreshSZ(lfsize):
    line=0
    
    lfsize.children["ltitle1"].grid(row=line, column=1,columnspan=2,sticky="w",pady=5)
    line+=1
    
    lfsize.children["cbxsmall"].grid(row=line, column=1,sticky="ws")
    lfsize.children["sxsmall"].grid(row=line, column=2,sticky="s")
    line+=1
    
    lfsize.children["cbsmall"].grid(row=line, column=1,sticky="ws")
    lfsize.children["ssmall"].grid(row=line, column=2,sticky="s")
    line+=1
    
    lfsize.children["cbmedium"].grid(row=line, column=1,sticky="ws")
    lfsize.children["smedium"].grid(row=line, column=2,sticky="s")
    line+=1
    
    lfsize.children["cblarge"].grid(row=line, column=1,sticky="ws")
    lfsize.children["slarge"].grid(row=line, column=2,sticky="s")
    line+=1
    
    lfsize.children["ltitle2"].grid(row=line, column=1,columnspan=2,sticky="w",pady=5)
    line+=1
    
    lfsize.children["cboxsmall"].grid(row=line, column=1,sticky="ws")
    lfsize.children["soxsmall"].grid(row=line, column=2,sticky="s")
    lfsize.children["soxsmall"].configure(from_=0,to=12-lfsize.children["sxsmall"].get())
    line+=1
    
    lfsize.children["cbosmall"].grid(row=line, column=1,sticky="ws")
    lfsize.children["sosmall"].grid(row=line, column=2,sticky="s")
    lfsize.children["sosmall"].configure(from_=0,to=12-lfsize.children["ssmall"].get())
    line+=1
    
    lfsize.children["cbomedium"].grid(row=line, column=1,sticky="ws")
    lfsize.children["somedium"].grid(row=line, column=2,sticky="s")
    lfsize.children["somedium"].configure(from_=0,to=12-lfsize.children["smedium"].get())
    line+=1
    
    lfsize.children["cbolarge"].grid(row=line, column=1,sticky="ws")
    lfsize.children["solarge"].grid(row=line, column=2,sticky="s")
    lfsize.children["solarge"].configure(from_=0,to=12-lfsize.children["slarge"].get())
    line+=1
    
    lfsize.children["breset"].grid(row=line, column=1,columnspan=2,pady=25)
    
    
    
    lfsize.grid(row=1, column=3,rowspan=100, sticky="n s")