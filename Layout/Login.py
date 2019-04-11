#!/usr/bin/python
# -*- coding: UTF-8 -*-
import wx


class Layout(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, -1, "登录系统", size = (300,200))
		self.InitUI()		
		self.Centre()
		self.SetBackgroundColour(wx.Colour(235,237,239))
		self.Show()


	def InitUI(self):
		panel = wx.Panel(self)
		wx.StaticText(panel, -1, "小名", pos = (33, 25))
		wx.StaticText(panel, -1, "代理线", pos = (20, 65))

		name = wx.TextCtrl(panel, -1, pos = (60, 22), size = (200, 22))
		agent = wx.TextCtrl(panel, -1, pos = (60, 62), size = (200, 22))

		btn_login = wx.Button(panel, -1, "登录", pos = (59, 98), size = (202, 26))
		panel.Bind(wx.EVT_BUTTON, self.OnLogin, btn_login)


	# 登录
	def OnLogin(self, event):
		wx.MessageBox("Hello")