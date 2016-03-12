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
	def controlerEnvoyer(self,dictionnaire):
		print(dictionnaire)
		self.model.ajouter_contact(dictionnaire)
	def setView(self,view):
		self.view=view
	def setModel(self,model):
		self.model=model
	def updateAffichageContacts(self):
		contacts = self.model.getContacts()
		self.view.updateAffichageContactBar(contacts)
	
