import wx
import sqlite3
from modules import func_bd
# text

class AddWordsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        gbSizer = wx.GridBagSizer(3, 2)
        self.engStaticText = wx.StaticText(self, wx.ID_ANY, "English: ")
        self.rusStaticText = wx.StaticText(self, wx.ID_ANY, "Russian: ")
        self.engCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, -1))
        self.rusCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, -1))
        self.writeWordsBTN = wx.Button(self, wx.ID_ANY, label="Записать слово", size=(100, -1))

        gbSizer.Add(self.engStaticText, pos=(0, 0), flag=wx.ALL, border=10)
        gbSizer.Add(self.engCtrl, pos=(0, 1), flag=wx.ALL, border=10)
        gbSizer.Add(self.rusStaticText, pos=(1, 0), flag=wx.ALL, border=10)
        gbSizer.Add(self.rusCtrl, pos=(1, 1), flag=wx.ALL, border=10)
        gbSizer.Add(self.writeWordsBTN, pos=(2, 0), span=(1, 2), flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=10)
        self.SetSizer(gbSizer)
        self.Hide()
        self.Layout()

        self.writeWordsBTN.Bind(wx.EVT_BUTTON, self.onWriteWords, self.writeWordsBTN)

        # self.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
        # self.Bind(wx.EVT_KEY_UP, self.onKeyUp)

        self.rusCtrl.Bind(wx.EVT_KEY_UP, self.onKeyUpRus)
        self.engCtrl.Bind(wx.EVT_KEY_UP, self.onKeyUpEng)

    def onKeyUpEng(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_RETURN or key == wx.WXK_NUMPAD_ENTER:
            self.rusCtrl.SetFocus()
            print("Вы выполняете переход к новой строке")

    def onKeyUpRus(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_RETURN or key == wx.WXK_NUMPAD_ENTER:
            self.onWriteWords(wx.EVT_BUTTON)
            print("Вы выполняете функцию добавления слова")




    # def onKeyDown(self, event):
    #     key = event.GetKeyCode()
    #     print("Вы отпустили кнопку", key)

    def onWriteWords(self, event):
        eng_word = self.engCtrl.GetValue().lower()
        rus_word = self.rusCtrl.GetValue().lower()

        if eng_word == "":
            print("Вы пытаетесь записать пустое слово")
            self.engCtrl.SetFocus()
        elif rus_word == "":
            print("Вы пытаетесь записать пустое слово")
            self.rusCtrl.SetFocus()
        else:
            print(eng_word, " - ", rus_word, "успешно записаны в базу данных")
            func_bd.add_new_word(eng_word, rus_word)
            self.rusCtrl.SetValue("")
            self.engCtrl.SetValue("")
            self.engCtrl.SetFocus()











































