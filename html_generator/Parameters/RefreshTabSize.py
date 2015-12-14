def RefreshTabSize(lfTabSize):
    
    lfTabSize.children["cbtabsize"].grid(row=1, column=1,sticky="news")
    lfTabSize.grid_columnconfigure(1, minsize=215)
    
    lfTabSize.grid(row=100, column=1,sticky="news")
pass