import wx
from modules.addwords import AddWordsPanel
from modules.verifywords import VerifyWordsPanel
from modules.addwords2 import AddWordsPanel2


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Это тестовая версия словаря", size=(550, 310))
        # self.m_statusBar1 = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)

        self.sb = self.CreateStatusBar()
        self.sb.SetStatusText("Статусная строка запущена")

        # ico = wx.Icon('img/free bsd.ico', wx.BITMAP_TYPE_ICO)
        # self.SetIcon(ico)

        self.add_words_panel = AddWordsPanel(self)
        self.add_words_panel2 = AddWordsPanel2(self)
        self.verify_words_panel = VerifyWordsPanel(self)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        # -----------------------------------------------------------------------------------------------------------
        # self.m_statusBar1 = self.CreateStatusBar(1, wx.BoxSizer, wx.ID_ANY)
        # self.statusBar1 = wx.CreateStatusBar(1, wx.BoxSizer, wx.ID_ANY)
        # self.Centre(wx.BOTH)

        self.panel = wx.Panel(self)
        bxSizer = wx.BoxSizer(wx.VERTICAL)

        myfir = wx.StaticText(self.panel, wx.ID_ANY, "Приветствуем в программе Собственного Словаря"
                             "Здесь вы можете добавлять собственное слово с переводом в режиме добавления слова,"
                             "Также вы можете проверять эти слова для укрепления знаний в режиме проверки слов, "
                             "Эта программа расчитана на добросовестное использование для Саморазвития",
                              style=wx.ALIGN_CENTRE_HORIZONTAL)

        bxSizer.Add(myfir, 1, flag=wx.ALL | wx.EXPAND, border=24)

        self.panel.Layout()

        self.panel.SetSizer(bxSizer)



        # -----------------------------------------------------------------------------------------------------------
        self.sizer.Add(self.add_words_panel, 1, wx.EXPAND)
        self.sizer.Add(self.verify_words_panel, 1, wx.EXPAND)
        self.sizer.Add(self.add_words_panel2, 1, wx.EXPAND)
        self.sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Layout()

        menubar = wx.MenuBar()
        mainmenu = wx.Menu()
        # menuitem = wx.Menu()

        main_menu_item = mainmenu.Append(wx.ID_ANY, "Главная\tCtrl+M")
        # main_menu_item.SetBitmap(wx.Bitmap("img/Home.png"))
        add_word_menu_item = mainmenu.Append(wx.ID_ANY, "Добавить слово\tCtrl+Q")
        # add_word_menu_item.SetBitmap(wx.Bitmap("img/Add.png"))
        add_word_menu_item2 = mainmenu.Append(wx.ID_ANY, "Добавить слово 2(тест)")
        # add_word_menu_item2.SetBitmap(wx.Bitmap("img/Create.png"))
        verify_words_menu_item = mainmenu.Append(wx.ID_ANY, "Проверка слов\tCtrl+W")
        # verify_words_menu_item.SetBitmap(wx.Bitmap("img/Apply.png"))

        self.Bind(wx.EVT_MENU, self.onMainMenu, main_menu_item)
        self.Bind(wx.EVT_MENU, self.onAddWord, add_word_menu_item)
        self.Bind(wx.EVT_MENU, self.onAddWord2, add_word_menu_item2)
        self.Bind(wx.EVT_MENU, self.onVerifyWords, verify_words_menu_item)

        # menuitem.Append(wx.ID_ABOUT, "О нас")
        menubar.Append(mainmenu, "Menu")
        # menubar.Append(menuitem, "About Us")
        self.SetMenuBar(menubar)





    #     self.add_words_panel.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
    #     self.add_words_panel.Bind(wx.EVT_KEY_UP, self.onKeyUp)
    #
    # def onKeyUp(self, event):
    #     key = event.GetKeyCode()
    #     print("Вы нажали кнопку", key)
    #
    # def onKeyDown(self, event):
    #     key = event.GetKeyCode()
    #     print("Вы отпустили кнопку", key)






    def onMainMenu(self, event):
        self.sb.SetStatusText("Главная")
        self.add_words_panel2.Disable()
        self.add_words_panel2.Hide()
        self.add_words_panel.Disable()
        self.add_words_panel.Hide()
        self.verify_words_panel.Disable()
        self.verify_words_panel.Hide()
        self.panel.Show()
        self.Show()
        self.Layout()

    def onAddWord(self, event):
        self.sb.SetStatusText("Режим добавления слов")
        self.panel.Hide()
        self.verify_words_panel.Disable()
        self.verify_words_panel.Hide()
        self.add_words_panel2.Disable()
        self.add_words_panel2.Hide()
        self.add_words_panel.Enable()
        self.add_words_panel.Show()
        self.add_words_panel.SetFocus()
        self.Layout()

    def onVerifyWords(self, event):
        self.sb.SetStatusText("Режим проверки слов")
        self.panel.Hide()
        self.add_words_panel2.Disable()
        self.add_words_panel2.Hide()
        self.add_words_panel.Disable()
        self.add_words_panel.Hide()
        self.verify_words_panel.Enable()
        self.verify_words_panel.Show()
        self.verify_words_panel.SetFocus()
        self.Layout()

    def onAddWord2(self, event):
        self.sb.SetStatusText("Режим добавления слов 2")
        self.panel.Hide()
        self.verify_words_panel.Hide()
        self.verify_words_panel.Disable()
        self.add_words_panel.Disable()
        self.add_words_panel.Hide()
        self.add_words_panel2.Enable()
        self.add_words_panel2.Show()
        self.add_words_panel2.SetFocus()
        self.Layout()



























    #     menubar = wx.MenuBar()
    #     fileMenu = wx.Menu()
    #     switch_panels_menu_item = fileMenu.Append(
    #         wx.ID_ANY,
    #         "Switch Panels",
    #         "Some text")
    #     self.Bind(wx.EVT_MENU, self.onSwitchPanels,
    #               switch_panels_menu_item)
    #     menubar.Append(fileMenu, '&File')
    #     self.SetMenuBar(menubar)
    #
    #     self.verify_words_panel = VerifyWordsPanel(self)
    #     self.add_words_panel = AddWordsPanel(self)
    #     self.add_words_panel.Hide()
    #     # self.verify_words_panel.Hide()
    #
    #     self.sizer = wx.BoxSizer(wx.VERTICAL)
    #     self.sizer.Add(self.add_words_panel, 1, wx.EXPAND)
    #     self.sizer.Add(self.verify_words_panel, 1, wx.EXPAND)
    #     self.SetSizer(self.sizer)
    #
    # def onSwitchPanels(self, event):
    #     if self.verify_words_panel.IsShown():
    #         self.SetTitle("Панель добавления слова")
    #         self.verify_words_panel.Hide()
    #         self.add_words_panel.Show()
    #     else:
    #         self.SetTitle("Панель проверки слова")
    #         self.verify_words_panel.Show()
    #         self.add_words_panel.Hide()
    #     self.Layout()


















if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
