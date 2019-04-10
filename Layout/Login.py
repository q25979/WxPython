#!/usr/bin/python
# -*- coding: UTF-8 -*-
import wx


class Layout(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, -1, "登录系统", size = (300,200))
		self.InitUI()		
		self.Centre()
		self.Show()


	def InitUI(self):
		panel = wx.Panel(self)
		wx.StaticText(panel, -1, "账号", pos = (20, 25))