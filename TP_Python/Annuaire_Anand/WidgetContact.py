#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# View.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Control import Control
import sys

class WidgetContact(QGroupBox):
	""" Cette class sera la class qui fera l'affichage d'un contact"""
	def __init__(self,parent,control):
		self.control = control
		QGroupBox.__init__(self,parent)
		self.Edit = False
		self.creerWidgets()
		self.connecterWidgets()
	def creerWidgets(self):
		# Définition du layout qui va contenir et organiser tous les widgets
		self.layout= QGridLayout()
		self.layout.setMargin(30)
		# Définition de tous les widgets
		self.boutonEdit = QPushButton("Editer", self)
		self.boutonSupprimer = QPushButton("Supprimer", self)
		self.nomLabel = QLabel("NOM ", self)
		self.prenomLabel = QLabel("PRENOM ", self)
		self.numeroLabel = QLabel("NUMERO ", self)
		self.adresseLabel = QLabel("ADRESSE ", self)
		self.typeLabel = QLabel("TYPE ", self)
		self.nomLineEdit = QLineEdit(self)
		self.prenomLineEdit = QLineEdit("prenom",self)
		self.numeroLineEdit = QLineEdit(self)
		self.adresseLineEdit = QLineEdit(self)
		self.typeLineEdit = QLineEdit(self)
		
		# Positionnement de tous les Widgets dans le layout
		self.layout.addWidget(self.nomLabel,0,0,1,1)
		self.layout.addWidget(self.nomLineEdit,0,0,1,1)
		self.layout.addWidget(self.boutonEdit,0,2,1,1)
		self.layout.addWidget(self.prenomLabel,0,1,1,1)
		self.layout.addWidget(self.prenomLineEdit,0,1,1,1)
		self.layout.addWidget(self.numeroLabel,1,0,1,1)
		self.layout.addWidget(self.boutonSupprimer,1,2,1,1)
		self.layout.addWidget(self.numeroLineEdit,1,0,1,1)
		self.layout.addWidget(self.adresseLabel,2,0,1,1)
		self.layout.addWidget(self.adresseLineEdit,2,0,1,1)
		self.layout.addWidget(self.typeLabel,3,0,1,1)
		self.layout.addWidget(self.typeLineEdit,3,0,1,1)
		self.setLayout(self.layout)
		# Au démarrage on désactive l'édition
		self.desactiverEdition()
		# Définition des propriétés du widget (contenant)
		self.setStyleSheet("border:2px black solid;border-radius:2px")
		# Définition de toutes les propriétés de tous les widgets (contenu)
		self.nomLineEdit.setStyleSheet("background-color:rgb(255,255,255)")
		self.prenomLineEdit.setStyleSheet("background-color:rgb(255,255,255)")
		self.numeroLineEdit.setStyleSheet("background-color:rgb(255,255,255)")
		self.adresseLineEdit.setStyleSheet("background-color:rgb(255,255,255)")
		self.typeLineEdit.setStyleSheet("background-color:rgb(255,255,255)")
	def connecterWidgets(self):
		self.connect(self.boutonEdit, SIGNAL("clicked()"),self.SLOT_Edition)
	def SLOT_Edition(self):
		if self.Edit == False:
			self.activerEdition()
		else:
			self.desactiverEdition()
	def activerEdition(self):
		self.Edit = True
		self.boutonEdit.setText("Fin édition")
		self.nomLabel.hide()
		self.prenomLabel.hide()
		self.numeroLabel.hide()
		self.adresseLabel.hide()
		self.typeLabel.hide()
		self.nomLineEdit.show()
		self.prenomLineEdit.show()
		self.numeroLineEdit.show()
		self.adresseLineEdit.show()
		self.typeLineEdit.show()
		
		self.modifierValeurLineEdit()
	def desactiverEdition(self):
		self.Edit = False
		self.boutonEdit.setText("Editer")
		self.nomLabel.show()
		self.prenomLabel.show()
		self.numeroLabel.show()
		self.adresseLabel.show()
		self.typeLabel.show()
		self.nomLineEdit.hide()
		self.prenomLineEdit.hide()
		self.numeroLineEdit.hide()
		self.adresseLineEdit.hide()
		self.typeLineEdit.hide()
		
		self.sauvegarderModification()
	def sauvegarderModification(self):
		dictionnaire = {}
		dictionnaire["nom"] = self.nomLineEdit.Text()
		dictionnaire["prenom"] = self.nomLineEdit.Text()
		self.control.controlerEnvoyer(dictionnaire)
		modifierValeurLabel()
	def modifierValeurLabel(self):
		pass
	def modifierValeurLineEdit(self):
		pass
	def resizeEvent(self, evt=None):
		print("PATRON")

