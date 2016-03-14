#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# View.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class WidgetContact(QGroupBox):
	""" Cette class sera la class qui fera l'affichage d'un contact"""
	def __init__(self,parent):
		QGroupBox.__init__(self,parent)
		self.Statut = "Ajouter"
		self.creerWidgets()
	def creerWidgets(self):
		# Définition du layout qui va contenir et organiser tous les widgets
		self.layout= QGridLayout()
		self.layout.setMargin(30)
		# Définition de tous les widgets
		self.nomLineEdit = QLineEdit(self)
		self.prenomLineEdit = QLineEdit(self)
		self.numeroLineEdit = QLineEdit(self)
		self.adresseLineEdit = QLineEdit(self)
		self.typeLineEdit = QLineEdit(self)
		
		# Positionnement de tous les Widgets dans le layout
		self.layout.addWidget(self.nomLineEdit,0,0,1,1)
		self.layout.addWidget(self.prenomLineEdit,0,1,1,1)
		self.layout.addWidget(self.numeroLineEdit,1,0,1,1)
		self.layout.addWidget(self.adresseLineEdit,2,0,1,1)
		self.layout.addWidget(self.typeLineEdit,3,0,1,1)
		self.setLayout(self.layout)
		# Au démarrage on désactive l'édition
		self.desactiverEdition()
		# Définition des propriétés du widget (contenant)
		self.setStyleSheet("border:2px black solid;border-radius:2px")
	def activerEdition(self,statut):
		self.Statut = statu
		self.nomLineEdit.setEnabled(True) 
		self.prenomLineEdit.setEnabled(True) 
		self.numeroLineEdit.setEnabled(True) 
		self.adresseLineEdit.setEnabled(True) 
		self.typeLineEdit.setEnabled(True)
		self.nomLineEdit.setStyleSheet("background-color:rgb(255,255,255)") 
		self.prenomLineEdit.setStyleSheet("background-color:rgb(255,255,255)") 
		self.numeroLineEdit.setStyleSheet("background-color:rgb(255,255,255)")
		self.adresseLineEdit.setStyleSheet("background-color:rgb(255,255,255)") 
		self.typeLineEdit.setStyleSheet("background-color:rgb(255,255,255)")
	def desactiverEdition(self):
		self.Statut = "Visualiser"
		self.nomLineEdit.setEnabled(False) 
		self.prenomLineEdit.setEnabled(False) 
		self.numeroLineEdit.setEnabled(False) 
		self.adresseLineEdit.setEnabled(False) 
		self.typeLineEdit.setEnabled(False)
		self.nomLineEdit.setStyleSheet("background-color:rgba(255,255,255,0)") 
		self.prenomLineEdit.setStyleSheet("background-color:rgba(255,255,255,0)") 
		self.numeroLineEdit.setStyleSheet("background-color:rgba(255,255,255,0)")
		self.adresseLineEdit.setStyleSheet("background-color:rgba(255,255,255,0)") 
		self.typeLineEdit.setStyleSheet("background-color:rgba(255,255,255,0)")
	def setValeurs(self,dictionnaire):
		self.nomLineEdit.setText(dictionnaire["nom"])
		self.prenomLineEdit.setText(dictionnaire["prenom"])
	def getModification(self):
		""" Cette fonction retourne toutes les informations contenues dans le formulaire """
		dictionnaire = {}
		dictionnaire["nom"] = self.nomLineEdit.text()
		dictionnaire["prenom"] = self.prenomLineEdit.text()
		dictionnaire["groupe"] = " "
		dictionnaire["favori"] = " "
		dictionnaire["numero"] = " "
		dictionnaire["libelle_numero"] = " "
		dictionnaire["mail"] = " "
		dictionnaire["libelle_mail"] = " "
		dictionnaire["adresse"] = " "
		dictionnaire["libelle_adresse"] = " "
		return dictionnaire

