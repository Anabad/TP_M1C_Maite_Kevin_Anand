#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Control.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Model import Model
from View import View
import sys

class Control:
	def __init__(self):
		self.view
		self.model
	def controlerEnvoyer(self,dictionnaire):
		ajouter_contact(dictionnaire)
	def setView(self,view):
		self.view=view
	def setModel(self,model):
		self.model=model
	
