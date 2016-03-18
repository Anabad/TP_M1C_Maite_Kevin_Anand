#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Control.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Control:
	def __init__(self):
		self.view = None
		self.model = None
	def controlerAjouter(self,dictionnaire):
		if dictionnaire["nom"] != "" and dictionnaire["prenom"] != "":
			self.model.ajouter_contact(dictionnaire)
			return 0
		else:
			return 1
	def controlerModifier(self,dictionnaire):
		self.model.editer_contact(dictionnaire)
	def supprimerContact(self,index):
		self.model.supprimerContact(index)
	def setView(self,view):
		self.view=view
	def setModel(self,model):
		self.model=model
	def updateAffichageContacts(self,recherche):
		contacts = self.model.rechercher_contact(recherche,[""])
		contactsGroupe = self.model.rechercher_contact(recherche,["Plan cul","Ami","Travail"])
		self.view.updateAffichageContactBar(contacts,contactsGroupe)
	def getContactById(self,index):
		return self.model.getContactById(index)
		
		
	
