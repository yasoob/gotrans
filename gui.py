import urllib2
import wx
import goslate
from myIcon import *

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 250
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = 'Translator',
                          pos = (200,75), size = (WINDOW_WIDTH, WINDOW_HEIGHT),style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

        backP = wx.Panel(self)
        self.icon = translateicon.GetIcon()
        self.SetIcon(self.icon)
        tbicon = wx.TaskBarIcon()
        tbicon.SetIcon(self.icon, "Translator v0.1")
        
        #### Items declared ####
        transBtn = wx.Button(backP, label="Translate")
        transBtn.SetToolTipString("Clicking this button will translate the text!")

        self.textInput = wx.TextCtrl(backP,value = "Enter text to be translated!", style = wx.TE_MULTILINE)
        self.textOutput = wx.TextCtrl(backP, style = wx.TE_MULTILINE | wx.TE_READONLY)

        labelFrom = wx.StaticText(backP,label = "   From Language ? ", style = wx.ALIGN_CENTRE)
        labelTo = wx.StaticText(backP, label = "   To Language ? ", style = wx.ALIGN_CENTRE)
        self.fromLang = wx.TextCtrl(backP, value = 'en')
        self.toLang = wx.TextCtrl(backP, value = 'de')

        #### Binders ####
        transBtn.Bind(wx.EVT_BUTTON,self.translate)
        transBtn.Bind(wx.EVT_ENTER_WINDOW,self.onTransEnter)
        self.textInput.Bind(wx.EVT_ENTER_WINDOW,self.onInputEnter)
        self.textOutput.Bind(wx.EVT_ENTER_WINDOW,self.onOutputEnter)
        self.fromLang.Bind(wx.EVT_ENTER_WINDOW,self.onFromEnter)
        self.toLang.Bind(wx.EVT_ENTER_WINDOW,self.onToEnter)

        #### Horizontal Sizers ####
        horSizer = wx.BoxSizer()
        horSizer.Add(labelFrom, flag = wx.EXPAND| wx.TOP | wx.BOTTOM, proportion = 1, border = 1)
        horSizer.Add(self.fromLang, flag = wx.EXPAND, proportion = 0, border = 0)
        horSizer.Add(labelTo, flag = wx.EXPAND| wx.TOP | wx.BOTTOM, proportion = 1, border = 1)
        horSizer.Add(self.toLang, flag = wx.EXPAND | wx.LEFT | wx.RIGHT, proportion = 0, border = 3)

        #### Horizontal sizers ####
        horSizerTrans = wx.BoxSizer()
        horSizerTrans.Add(transBtn, flag = wx.EXPAND | wx.RIGHT | wx.LEFT, proportion = 1, border = 2)
        
        #### Vertical Sizers ####
        vertSizer = wx.BoxSizer(wx.VERTICAL)
        #vertSizer.AddSpacer(2)
        vertSizer.Add(self.textInput, flag = wx.EXPAND| wx.TOP | wx.LEFT | wx.RIGHT, proportion = 1, border = 3)
        vertSizer.AddSpacer(1)
        vertSizer.Add(horSizer, flag = wx.EXPAND| wx.TOP | wx.BOTTOM, proportion = 0, border = 0)
        vertSizer.Add(horSizerTrans, flag = wx.EXPAND| wx.TOP | wx.BOTTOM, proportion = 0, border = 0)
        vertSizer.AddSpacer(2)
        vertSizer.Add(self.textOutput, flag = wx.EXPAND| wx.LEFT | wx.RIGHT, proportion = 2, border = 3)
        vertSizer.AddSpacer(2)

        #### Panel sizer set ####
        backP.SetSizer(vertSizer)
        self.sb = self.CreateStatusBar()
        self.Show()


    def translate(self,event):
    	gs = goslate.Goslate()
    	text = self.textInput.GetValue()
    	froml = self.fromLang.GetValue()
    	tol = self.toLang.GetValue()
    	try:
            self.sb.SetStatusText('Translating text!')
            outputs = gs.translate(text, tol, froml)
            self.textOutput.SetValue(outputs)
            self.sb.SetStatusText('Text translated!')
        except urllib2.URLError:
            self.textOutput.SetValue('Sorry an error occured. Perhaps you should check your internet connection.')
            self.sb.SetStatusText('A network timeout error occured')
    def onTransEnter(self, e):
        self.sb.SetStatusText('Press this button to translate text!')
        e.Skip()  

    def onInputEnter(self, e):
        self.sb.SetStatusText('Enter text in this box for being translated.')
        e.Skip()  

    def onOutputEnter(self, e):
        self.sb.SetStatusText('Translated text will appear here.')
        e.Skip()  

    def onFromEnter(self, e):
        self.sb.SetStatusText('Your text will be translated from this language')
        e.Skip()  

    def onToEnter(self, e):
        self.sb.SetStatusText('Your text will be translated to this language.')
        e.Skip()
        
app = wx.App(redirect=False)
window = MainFrame()
app.MainLoop()
