import wx
app=wx.App()
# win=wx.Frame(None)
windowSize=[410,335]
win=wx.Frame(None,title='Simple Editor',size=windowSize)
loadBtn=wx.Button(win,label='Open',pos=(225,5),size=(80,25))
saveBtn=wx.Button(win,label='Save',pos=(315,5),size=(80,25))
fileName=wx.TextCtrl(win,pos=(5,5),size=(210,25))
contents=wx.TextCtrl(win,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)
# btn=wx.Button(win)
win.Show()
app.MainLoop()