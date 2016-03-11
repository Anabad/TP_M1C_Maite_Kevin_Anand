#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# View.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from WidgetContact import WidgetContact
import sys

class View(QMainWindow):
""" Cette class est la fenetre principale de l'annuaire"""
	def __init__(self):
		QMainWindow.__init__(self)
		self.setWindowTitle("Annuaire")
		self.creerWidget()
		self.connecterWidget()

	def creerWidget(self):
		""" Cette fonction va définir tous les boutons ainsi que les espaces conteneur de la fenetre """
		# Définition des conteneurs principaux de la fenetre
		self.conteneur = QWidget(self)
		self.layoutConteneur = QGridLayout()
		self.layoutConteneur.setSpacing(0)
		self.layoutConteneur.setMargin(0)
		self.setCentralWidget(self.conteneur)
		
		# Définition des deux gros widget de la fenetre
		self.barHaut = QWidget(self)
		self.barHaut.setStyleSheet("background:url(IMAGES/texture.jpg);border-bottom:3px groove black")
		
		self.dessousBar =QWidget(self)
		
		self.layoutConteneur.addWidget(self.barHaut,0,0,1,1)
		self.layoutConteneur.addWidget(self.dessousBar,1,0,6,1)
		self.conteneur.setLayout(self.layoutConteneur)
		
		# Définition des widgets dans la bar du haut
		self.layoutBar = QHBoxLayout()
		
		self.quoiWidget = QLineEdit(self.barHaut)
		self.quoiWidget.setStyleSheet("background-color:rgb(255,255,255)")
		
		self.ouWidget = QLineEdit(self.barHaut)
		self.ouWidget.setStyleSheet("background-color:rgb(255,255,255)")
		
		self.bouttonValideRecherche = QPushButton(self.barHaut)
		self.bouttonValideRecherche.setIcon(QIcon(QPixmap("IMAGES/loupe.png")));
		self.bouttonValideRecherche.setStyleSheet("background:rgb(255,255,0);border-bottom:none")
		
		self.layoutBar.addWidget(self.quoiWidget)
		self.layoutBar.addWidget(self.ouWidget)
		self.layoutBar.addWidget(self.bouttonValideRecherche)
		self.barHaut.setLayout(self.layoutBar)
		
		# Définition des widgets dans la partie inférieur de l'écran
		self.layoutDessousBar = QGridLayout()
		
		self.barGauche = QWidget(self.dessousBar)
		self.zoneAddMod = WidgetContact(self.dessousBar)
		
		self.layoutDessousBar.addWidget(self.barGauche,0,0,1,1)
		self.layoutDessousBar.addWidget(self.zoneAddMod,0,1,1,5)
		#self.zoneAddMod.hide()
		
		self.dessousBar.setLayout(self.layoutDessousBar)
		
		# Définition des widgets dans la barre de gauche
		self.layoutBarGauche = QVBoxLayout()
		
		self.boutonAjouter = QPushButton("Ajouter",self.barGauche)
		self.zoneAffichage = QScrollArea()
		self.layoutBarGauche.addWidget(self.boutonAjouter)
		self.layoutBarGauche.addWidget(self.zoneAffichage)
		self.barGauche.setLayout(self.layoutBarGauche)
		
	def connecterWidget(self):
		self.connect(self.boutonAjouter, SIGNAL("clicked()"),self.SLOT_Ajouter)
			
	def SLOT_Ajouter(self):
		pass
		#self.zoneAddMod.show()

