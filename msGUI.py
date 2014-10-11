#/usr/bin/python
#coding=utf-8
import wx
class ms(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'×ÊÁÏÂ¼Èë')
        panel=wx.Panel(self)
        
if __name__=='__main__':
    myapp=wx.PySimpleApp()
    myframe=ms()
    myframe.Show()
    myapp.MainLoop()


