import wx
import sqlite3
from modules import func_bd


class AddWordsPanel2(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)


        self.rus_engStaticText = wx.StaticText(self, wx.ID_ANY, "Введите слово на русском")
        self.rus_engStaticText.Wrap(-1)
        bSizer1.Add(self.rus_engStaticText, 0, wx.ALIGN_CENTER | wx.LEFT, 15)

        self.rusTextCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, -1))
        bSizer1.Add(self.rusTextCtrl, 1, wx.ALIGN_CENTER | wx.ALL, 15)
        self.rusTextCtrl.Show()

        self.engTextCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, -1))
        bSizer1.Add(self.engTextCtrl, 1, wx.ALIGN_CENTER | wx.ALL, 15)
        self.engTextCtrl.Hide()

        bSizer2.Add(bSizer1, 1, wx.EXPAND, 5)

        self.textLikeStatusBar = wx.StaticText(self, wx.ID_ANY, "Здесь будет находиться текст как в статусной строке")
        self.textLikeStatusBar.Wrap(-1)
        self.textLikeStatusBar.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        bSizer2.Add(self.textLikeStatusBar, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 30)

        self.SetSizer(bSizer2)
        self.Hide()
        self.Layout()





        self.rusTextCtrl.Bind(wx.EVT_KEY_UP, self.onKeyUp)




    def onKeyUp(self, event):
        if True:
            pass
        print("Hello")


        # rus_engString = ""
        #
        # self.rus_engStaticText = wx.StaticText(self, wx.ID_ANY, rus_engString, )
        # self.rus_engStaticText.SetLabel("Введите слово на русском")
        # self.rus_engTextCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, -1))
        #
        # gbSizer = wx.GridBagSizer(1, 1)
        #
        #
        #
        #
        #
        #




































    #     gbSizer = wx.GridBagSizer(3, 2)
    #     self.engStaticText = wx.StaticText(self, wx.ID_ANY, "English222: ")
    #     self.rusStaticText = wx.StaticText(self, wx.ID_ANY, "Russian222: ")
    #     self.engCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, -1))
    #     self.rusCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, -1))
    #     self.writeWordsBTN = wx.Button(self, wx.ID_ANY, label="Записать слово222", size=(100, -1))
    #
    #     gbSizer.Add(self.engStaticText, pos=(0, 0), flag=wx.ALL, border=10)
    #     gbSizer.Add(self.engCtrl, pos=(0, 1), flag=wx.ALL, border=10)
    #     gbSizer.Add(self.rusStaticText, pos=(1, 0), flag=wx.ALL, border=10)
    #     gbSizer.Add(self.rusCtrl, pos=(1, 1), flag=wx.ALL, border=10)
    #     gbSizer.Add(self.writeWordsBTN, pos=(2, 0), span=(1, 2), flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=10)
    #     self.SetSizer(gbSizer)
    #     self.Hide()
    #     self.Layout()
    #
    #     self.writeWordsBTN.Bind(wx.EVT_BUTTON, self.onWriteWords, self.writeWordsBTN)
    #
    #     # self.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
    #     # self.Bind(wx.EVT_KEY_UP, self.onKeyUp)
    #
    #     self.rusCtrl.Bind(wx.EVT_KEY_UP, self.onKeyUp)
    #     self.engCtrl.Bind(wx.EVT_KEY_UP, self.onKeyUp)
    #
    #
    # def onKeyUp(self, event):
    #     key = event.GetKeyCode()
    #     if key == wx.WXK_RETURN or key == wx.WXK_NUMPAD_ENTER:
    #         print("Вы выполняете функцию")
    #         self.writeWordsBTN.Bind(wx.EVT_BUTTON, self.onWriteWords, self.writeWordsBTN)
    #     else:
    #         print("Вы нажали кнопку", key, "Загаданная клавиша ", wx.WXK_RETURN, " и ", wx.WXK_NUMPAD_ENTER)
    #
    # def onKeyDown(self, event):
    #     key = event.GetKeyCode()
    #     print("Вы отпустили кнопку", key)
    #
    # def onWriteWords(self, event):
    #     eng_word = self.engCtrl.GetValue().lower()
    #     rus_word = self.rusCtrl.GetValue().lower()
    #
    #     # func_bd.add_new_word(eng_word, rus_word)
    #
    #     self.engCtrl.SetFocus()
    #
    #     if eng_word == "" or rus_word == "":
    #         print("Вы пытаетесь записать пустое слово")
    #     else:
    #         print(eng_word, " - ", rus_word)










































