# coding: utf-8

# Importações do Kivy
import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.lang import Builder # Builder necessário para utilizar o Builder.load_string
from kivy.uix.screenmanager import Screen, ScreenManager

# Nesse caso, as classes devem estender Screen

class Menu(Screen):
	# Fecha a tela (menu lateral) voltando para a tela principal
	def fechar_menu(self):
		self.manager.current = 'tela_principal'

class TelaPrincipal(Screen):
	# Chama outra tela que contém o menu e uma imagem do logotipo
	def clique_iniciar(self):
		self.manager.current = 'menu'
	
class MyScreenManager(ScreenManager):
    pass
class DisjuntoreseCia(App):
	def build(self):
		# Retornar com função Builder.load_string evita erros em acentuação.
		return Builder.load_string(open('nomealeatorio.kv', encoding='UTF-8').read())
		
DC=DisjuntoreseCia()
DC.run()