import wx
import sqlite3
from modules import func_bd


class AddWordsPanel2(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)


        self.rus_engStaticText = wx.StaticText(self, wx.ID_ANY, "Введите слово на английском")
        # self.rus_engStaticText.Wrap(300)
        bSizer1.Add(self.rus_engStaticText, 0, wx.ALIGN_CENTER | wx.LEFT, 15)

        self.engTextCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, -1))
        bSizer1.Add(self.engTextCtrl, 1, wx.ALIGN_CENTER | wx.ALL, 15)
        self.engTextCtrl.Show()

        self.rusTextCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, -1))
        bSizer1.Add(self.rusTextCtrl, 2, wx.ALIGN_CENTER | wx.ALL, 15)
        self.rusTextCtrl.Show()
        self.rusTextCtrl.Hide()




        bSizer2.Add(bSizer1, 1, wx.EXPAND, 5)

        self.textLikeStatusBar = wx.StaticText(self, wx.ID_ANY, "Здесь будет находиться текст как в статусной строке")
        self.textLikeStatusBar.Wrap(-1)
        self.textLikeStatusBar.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString))
        bSizer2.Add(self.textLikeStatusBar, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 30)

        self.SetSizer(bSizer2)
        self.Hide()
        self.Layout()

        self.engTextCtrl.Bind(wx.EVT_KEY_UP, self.onKeyUpEng)
        self.rusTextCtrl.Bind(wx.EVT_KEY_UP, self.onKeyUpRus)



    def onKeyUpEng(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_RETURN or key == wx.WXK_NUMPAD_ENTER:
            if self.engTextCtrl.GetValue() != "":
                self.engWord = self.engTextCtrl.GetValue().lower()
                self.rus_engStaticText.SetLabel("Введите слово на русском       ")
                LikeStatus = "Вы ввели слово \"" + self.engWord + "\""
                print(LikeStatus)
                self.textLikeStatusBar.SetLabel(str(LikeStatus))
                self.engTextCtrl.Hide()
                self.rusTextCtrl.Show()
                self.rusTextCtrl.SetFocus()
                # --------------------------
                si = self.GetSize()
                siz = si[0] + 1, si[1] + 1
                self.SetSize(siz)
                self.SetSize(si)



                # si = self.GetSize()
                # print(si)
                # print(si[0], si[1])
                # siz = si[0] + 1, si[1] + 1
                # print("passw", siz)
                # self.SetSize(siz)
                # self.SetSize(si)


                # self.SetSize((534, 229))
                # print(self.engWord)


    def onKeyUpRus(self, event):
        key = event.GetKeyCode()
        eng_word = self.engWord.lower()
        rus_word = self.rusTextCtrl.GetValue().lower()
        if key == wx.WXK_RETURN or key == wx.WXK_NUMPAD_ENTER:
            if self.rusTextCtrl.GetValue() != "":
                self.rusWord = self.rusTextCtrl.GetValue().lower()
                self.rus_engStaticText.SetLabel("Введите слово на английском")
                LikeStatus = "Cлова \"" + self.engWord + " - " + self.rusWord\
                                                + "\" успешно записаны в базу данных"

                try:
                    func_bd.add_new_word(eng_word, rus_word)
                    self.textLikeStatusBar.SetLabel(str(LikeStatus))
                    # self.engTextCtrl.SetValue("")
                    # self.rusTextCtrl.SetValue("")
                except:
                    asd = "Такое слово уже существует"
                    self.textLikeStatusBar.SetLabel("слово " + eng_word + " уже существует, введите другое слово")
                    print(asd)
                    dlg = wx.MessageBox("Такое слово уже существует", "Ошибка", wx.OK | wx.ICON_STOP)



                self.rusTextCtrl.Hide()
                self.engTextCtrl.Show()
                self.engTextCtrl.SetFocus()
                print(self.engWord, self.rusWord)
                self.engTextCtrl.SetValue("")
                self.rusTextCtrl.SetValue("")
                #-------------------
                si = self.GetSize()
                siz = si[0] + 1, si[1] + 1
                self.SetSize(siz)
                self.SetSize(si)


                # print(self.GetSize())
                # self.SetSize((534, 228))





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










































