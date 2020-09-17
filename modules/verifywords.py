import wx


class VerifyWordsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        bsizer = wx.BoxSizer(wx.VERTICAL)
        self.verifyText = wx.StaticText(self, wx.ID_ANY, "Введите перевод слова <destiny>")
        bsizer.Add(self.verifyText, 0, flag=wx.ALL, border=10)

        self.verifyCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, -1))
        bsizer.Add(self.verifyCtrl, 1, flag=wx.ALL, border=19)

        self.logList = wx.ScrolledWindow(self, wx.ID_ANY, wx.VSCROLL)
        self.logList.SetScrollRate(5, 5)
        bsizer.Add(self.logList, 2, flag=wx.ALL | wx.EXPAND, border=12)



        self.SetSizer(bsizer)
        self.Hide()
        self.Layout()











        # gbSizer = wx.GridBagSizer(3, 2)
        # self.engStaticText1 = wx.StaticText(self, wx.ID_ANY, "Englsdfish: ")
        # self.engStaticText2 = wx.StaticText(self, wx.ID_ANY, "Englifdssh: ")
        # self.engStaticText3 = wx.StaticText(self, wx.ID_ANY, "Engladasish: ")
        # self.engStaticText4 = wx.StaticText(self, wx.ID_ANY, "Englgfaadfgish: ")
        # gbSizer.Add(self.engStaticText1, pos=(0, 0), flag=wx.ALL, border=30)
        # gbSizer.Add(self.engStaticText2, pos=(1, 2), flag=wx.ALL, border=30)
        # gbSizer.Add(self.engStaticText3, pos=(1, 0), flag=wx.ALL, border=30)
        # gbSizer.Add(self.engStaticText4, pos=(0, 3), flag=wx.ALL, border=30)
        #
        # self.SetSizer(gbSizer)

        self.Hide()
        self.Layout()
