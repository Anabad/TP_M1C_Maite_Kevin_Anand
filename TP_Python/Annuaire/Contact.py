
import os
import re

class Contact:
	"""Classe qui nous sert à stoquer les informations de chaque contact"""
	def __init__(self):
		"""Dans le constructeur on défini les variables pour caractériser une personne tels que:
				- le nom
				- le prenom
				- son numéro de téléphone"""
		self.nom=""
		self.prenom=""
		self.num=""
	def __str__(self):
		"""Affichage personnalisé de notre objet"""
		return "-Nom:{0}\n-Prenom:{1}\n-Numéro de téléphone:{2}\n".format(self.nom, self.prenom, self.num)
	def __repr__(self):
		"""Affichage personnalisé de notre objet"""
		return "-Nom:{0}\n-Prenom:{1}\n-Numéro de téléphone:{2}\n".format(self.nom, self.prenom, self.num)
	def __gt__(self,other):
		if self.nom < other.nom:
			return False
		if self.prenom < other.prenom:
			return False
		return True
	def __eq__(self,other):
		if self.nom != other.nom:
			return False
		if self.prenom != other.prenom:
			return False
		if self.num != other.num:
			return False
		return True


