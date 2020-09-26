import wx
from modules.func_bd import rand_word, add_new_word

# temp_while = 0

class VerifyWordsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        bsizer = wx.BoxSizer(wx.VERTICAL)

        self.rand = rand_word()
        try:
            self.eng = self.rand[0]
            self.rus = self.rand[1]
        except:
            add_new_word("eng_word", "rus_word")
            self.rand = rand_word()
            self.eng = self.rand[0]
            self.rus = self.rand[1]
            i = 0
            while self.eng == "eng_word" or i >= 10:
                # global temp_while
                # temp_while += 1
                self.rand = rand_word()
                self.eng = self.rand[0]
                self.rus = self.rand[1]
                i += 1
                if i == 10:
                    dlg = wx.MessageBox("Your dictionary is empty - Ваш словарь пуст\n "
                                        "Добавьте новое слово в режиме 'Добавить слово'", "Ошибка",
                                        wx.OK | wx.ICON_STOP)
                    break


        self.verifyText = wx.StaticText(self, wx.ID_ANY, "")
        if self.eng == "eng_word":
            self.verifyText.SetLabel("Your dictionary is empty - Ваш словарь пуст")
        else:
            self.verifyText.SetLabel("Введите перевод слова: " + self.eng)
        bsizer.Add(self.verifyText, 0, flag=wx.ALL, border=10)

        self.verifyCtrl = wx.TextCtrl(self, wx.ID_ANY, size=(200, 23))
        self.verifyCtrl.SetMaxSize((200, 23))
        bsizer.Add(self.verifyCtrl, 1, flag=wx.ALL, border=19)

        self.logList = wx.TextCtrl(self, wx.ID_ANY, value="Приветствуем!\n", style=wx.TE_MULTILINE | wx.TE_READONLY\
                                   | wx.TE_RICH | wx.VSCROLL)
        bsizer.Add(self.logList, 2, flag=wx.ALL | wx.EXPAND, border=12)



        # print(rand_word())

        self.SetSizer(bsizer)
        self.Hide()
        self.Layout()

        self.verifyCtrl.Bind(wx.EVT_KEY_UP, self.onKeyUp)


    def onKeyUp(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_RETURN or key == wx.WXK_NUMPAD_ENTER:
            loglist = self.logList.GetValue()
            word = self.verifyCtrl.GetValue()

            if self.eng == "eng_word":
                self.logList.SetValue("Your dictionary is empty - Ваш словарь пуст")
            elif word == self.rus:
                self.logList.SetValue("Вы ввели правильное слово, Молодец\n"+loglist)
                self.verifyCtrl.SetValue("")
            else:
                self.logList.SetValue("Не правильно, это было слово " + self.rus + "\n"+loglist)
                self.verifyCtrl.SetValue("")

            self.rand = rand_word()
            self.eng = self.rand[0]
            self.rus = self.rand[1]
            i=0
            while self.eng == "eng_word" or i >= 10:
                # global temp_while
                # temp_while += 1
                self.rand = rand_word()
                self.eng = self.rand[0]
                print(self.eng)
                self.rus = self.rand[1]
                i += 1
                if i == 10:
                    dlg = wx.MessageBox("Your dictionary is empty - Ваш словарь пуст", "Ошибка", wx.OK | wx.ICON_STOP)
                    break
            # print(temp_while)
            self.verifyText.SetLabel("Введите перевод слова: " + self.eng)







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

        # self.Hide()
        # self.Layout()
