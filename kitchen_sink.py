# -*- coding: utf-8 -*-
import kivy
import kivymd

kivy.require('1.9.0')

from kivy.app import App
from kivy.metrics import dp
from kivymd.bottom_sheet import BottomSheet, SingleLineItem
from kivymd.layouts import MaterialRelativeLayout
from kivymd.toolbar import Toolbar
from kivymd.navigationdrawer import NavigationDrawer, NavigationDrawerButton, \
	NavigationDrawerCategory


class MainWidget(MaterialRelativeLayout):

	def __init__(self, **kwargs):
		self.toolbar = Toolbar(title="KivyMD")
		self.nav = NavigationDrawer(
			side="left",
			header_img=kivymd.images_path + "PLACEHOLDER_BG.jpg",
			width=dp(400))
		super(MainWidget, self).__init__(**kwargs)

		self.background_color = (1,1,1,1)

		self.toolbar.nav_button = ["md-menu", lambda: self.nav.toggle()]
		self.toolbar.add_action_button("md-insert-photo")
		self.toolbar.add_action_button(
			"md-security",
			action=lambda x: self.open_bottom_sheet())

		self.cat1 = NavigationDrawerCategory(subheader=False)
		self.cat_vendedores = NavigationDrawerCategory(text="Category 1")
		self.cat1.add_widget(NavigationDrawerButton(text="Button 1"))
		self.cat1.add_widget(NavigationDrawerButton(text="Button 2"))
		self.cat1.add_widget(NavigationDrawerButton(text="Button 3"))
		self.cat1.add_widget(NavigationDrawerButton(text="Button 4"))
		self.cat_vendedores.add_widget(NavigationDrawerButton(text="Button A"))
		self.cat_vendedores.add_widget(NavigationDrawerButton(text="Button B"))
		self.cat_vendedores.add_widget(NavigationDrawerButton(text="Button C"))
		self.nav.add_widget(self.cat1)
		self.nav.add_widget(self.cat_vendedores)


		self.add_widget(self.toolbar)
		self.add_widget(self.nav)

	def open_bottom_sheet(self):
		self.bottom_sheet = BottomSheet()
		for i in range(0, 40):
			self.bottom_sheet.add_item(SingleLineItem(
				text="Test",
				divider=False,
				on_touch_down=lambda x, y: self.close_bottom_sheet()))
		self.bottom_sheet.open()

	def close_bottom_sheet(self):
		self.bottom_sheet.dismiss()

	def on_width(self, instance, value):
		self.toolbar.width = value

	def on_height(self, instance, value):
		self.toolbar.y = self.height - self.toolbar.height


class KitchenSink(App):

	def __init__(self, **kwargs):
		super(KitchenSink, self).__init__(**kwargs)

	def build(self):
		return MainWidget()

	def on_pause(self):
		return True

	def on_stop(self):
		pass

if __name__ == '__main__':
	KitchenSink().run()