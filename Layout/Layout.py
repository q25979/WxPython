#!/usr/bin/python
# -*- coding: UTF-8 -*-
import wx
import Login


"""
公司报表统计软件
主页布局
"""
class Layout(wx.Frame):
	def __init__(self, parent, title):
		super(Layout, self).__init__(parent, title = title, size = (330,450))
		self.InitUI()
		self.Centre()
		self.Show()


	def InitUI(self):
		self.MenuList()		# 菜单栏
		self.NotebookList()	# 选项卡


	# 选项卡
	def NotebookList(self):
		nb = wx.Notebook(self)
		nb.AddPage(PageUpWork(nb), "上班报表")
		nb.AddPage(PageDownWork(nb), "下班报表")


	# 创建菜单选项
	def MenuList(self):
		menu_bar = wx.MenuBar()	# 创建一个菜单栏
		menu = wx.Menu()		# 创建一个菜单
		login = menu.Append(-1, "登录")
		exit  = menu.Append(-1, "退出")

		help_menu = wx.Menu()
		help = help_menu.Append(-1, "指南")
		about = help_menu.Append(-1, "关于")

		self.Bind(wx.EVT_MENU, self.OnLogin, login)
		self.Bind(wx.EVT_MENU, self.OnExit, exit)

		self.Bind(wx.EVT_MENU, self.OnHelp, help)
		self.Bind(wx.EVT_MENU, self.OnAbout, about)

		menu_bar.Append(menu, "菜单")
		menu_bar.Append(help_menu, "帮助")
		self.SetMenuBar(menu_bar)


	# 登录按钮响应事件
	def OnLogin(self, event):
		Login.Layout(self)


	# 退出按钮响应事件
	def OnExit(self, event):
		self.Close()


	# 指南按钮响应事件
	def OnHelp(self, event):
		pass


	# 关于按钮响应事件
	def OnAbout(self, event):
		pass


"""
上班报表布局
"""
class PageUpWork(wx.Panel):
	def __init__(self, parent):
		super(PageUpWork, self).__init__(parent, size = (0, 0))
		panel = wx.Panel(self)

		leftvolue = 22
		tx_amount_recharge = wx.StaticText(self, -1, "充值总金额", pos = (10, 10))
		tx_amount_drawing  = wx.StaticText(self, -1, "提款总金额", pos = (10, 40))
		tx_flow_volume  = wx.StaticText(self, -1, "总打码量", pos = (leftvolue, 70))
		tx_number_cnter = wx.StaticText(self, -1, "引流人数", pos = (leftvolue, 100))
		tx_number_register = wx.StaticText(self, -1, "注册人数", pos = (leftvolue, 130))
		tx_number_recharge = wx.StaticText(self, -1, "充值人数", pos = (leftvolue, 160))
		tx_number_online = wx.StaticText(self, -1, "在线人数", pos = (leftvolue, 190))

		self.tc_up_amount_recharge = wx.TextCtrl(self, pos = (85, 8), size = (210, 20))
		self.tc_up_amount_drawing  = wx.TextCtrl(self, pos = (85, 38), size = (210, 20))
		self.tc_up_flow_volume  = wx.TextCtrl(self, pos = (85, 68), size = (210, 20))
		self.tc_up_number_cnter = wx.TextCtrl(self, pos = (85, 98), size = (210, 20))
		self.tc_up_number_register = wx.TextCtrl(self, pos = (85, 128), size = (210, 20))
		self.tc_up_number_recharge = wx.TextCtrl(self, pos = (85, 158), size = (210, 20))
		self.tc_up_number_online = wx.TextCtrl(self, pos = (85, 188), size = (210, 20))

		btn_sublime = wx.Button(self, -1, "提交", pos = (84, 215), size = (105, 25))
		btn_empty   = wx.Button(self, -1, "清空", pos = (191, 215), size = (105, 25))

		self.Bind(wx.EVT_BUTTON, self.OnSublime, btn_sublime)
		self.Bind(wx.EVT_BUTTON, self.OnEmpty, btn_empty)


	def OnSublime(self, event):
		down_amount_recharge = self.tc_up_amount_recharge.GetValue()
		down_amount_drawing  = self.tc_up_amount_drawing.GetValue()
		down_flow_volume  = self.tc_up_flow_volume.GetValue()
		down_number_cnter = self.tc_up_number_cnter.GetValue()
		down_number_register = self.tc_up_number_register.GetValue()
		down_number_recharge = self.tc_up_number_recharge.GetValue()
		down_number_online = self.tc_up_number_online.GetValue()


	def OnEmpty(self, event):
		self.tc_up_amount_recharge.SetValue("")
		self.tc_up_amount_drawing.SetValue("")
		self.tc_up_flow_volume.SetValue("")
		self.tc_up_number_cnter.SetValue("")
		self.tc_up_number_register.SetValue("")
		self.tc_up_number_recharge.SetValue("")
		self.tc_up_number_online.SetValue("")


"""
下班报表布局
"""
class PageDownWork(wx.Panel):
	def __init__(self, parent):
		super(PageDownWork, self).__init__(parent, size = (0, 0))
		panel = wx.Panel(self)

		leftvolue = 22
		tx_number_cnter = wx.StaticText(self, -1, "引流人数", pos = (leftvolue, 10))
		tx_number_register = wx.StaticText(self, -1, "注册人数", pos = (leftvolue, 40))
		tx_number_recharge = wx.StaticText(self, -1, "充值人数", pos = (leftvolue, 70))

		self.tc_down_number_cnter = wx.TextCtrl(self, pos = (85, 8), size = (210, 20))
		self.tc_down_number_register = wx.TextCtrl(self, pos = (85, 38), size = (210, 20))
		self.tc_down_number_recharge = wx.TextCtrl(self, pos = (85, 68), size = (210, 20))

		btn_sublime = wx.Button(self, -1, "提交", pos = (84, 95), size = (105, 25))
		btn_empty   = wx.Button(self, -1, "清空", pos = (191, 95), size = (105, 25))

		self.Bind(wx.EVT_BUTTON, self.OnSublime, btn_sublime)
		self.Bind(wx.EVT_BUTTON, self.OnEmpty, btn_empty)


	def OnSublime(self, event):
		down_amount_recharge = self.tc_down_number_cnter.GetValue()
		down_number_register = self.tc_down_number_register.GetValue()
		down_number_recharge = self.tc_down_number_recharge.GetValue()


	def OnEmpty(self, event):
		self.tc_down_number_cnter.SetValue("")
		self.tc_down_number_register.SetValue("")
		self.tc_down_number_recharge.SetValue("")


class Home():
	def __init__(self):
		app = wx.App()
		Layout(None, title="报表系统")
		app.MainLoop()
