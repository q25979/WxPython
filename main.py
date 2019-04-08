#!/usr/bin/python
# -*- coding: UTF-8 -*-
import wx


"""
公司报表统计软件
主页布局
"""

class Home(wx.Frame):
	def __init__(self, parent, title):
		super(Home, self).__init__(parent, title = title, size = (350,450))
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


	# 登录按钮
	def OnLogin(self, event):
		wx.MessageBox("You selected the simple menu item")


	# 退出按钮
	def OnExit(self, event):
		self.Close()


	# 指南按钮
	def OnHelp(self, event):
		pass


	# 关于按钮
	def OnAbout(self, event):
		pass


# 上班报表
class PageUpWork(wx.Panel):
	def __init__(self, parent):
		super(PageUpWork, self).__init__(parent)
		text = wx.TextCtrl(self, style = wx.TE_MULTILINE, size = (350,150))


# 下班报表
class PageDownWork(wx.Panel):
	def __init__(self, parent):
		super(PageDownWork, self).__init__(parent)
		text = wx.TextCtrl(self, style = wx.TE_MULTILINE, size = (250,150))


# 主函数
if __name__ == '__main__':
	app = wx.App()
	Home(None, title="报表系统")
	app.MainLoop()