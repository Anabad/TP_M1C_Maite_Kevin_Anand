#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# View.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class View(QMainWindow):
	""" Cette class sera la class qui fera l'affichage de tout l'annuaire"""
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
		
		self.zoneAddMod = QWidget(self.dessousBar)
		self.zoneAffichage = QScrollArea()
		
		self.layoutDessousBar.addWidget(self.barGauche,0,0,1,1)
		self.layoutDessousBar.addWidget(self.zoneAddMod,0,1,1,5)
		self.layoutDessousBar.addWidget(self.zoneAffichage,0,1,1,5)
		self.zoneAddMod.hide()
		
		self.dessousBar.setLayout(self.layoutDessousBar)
		
		# Définition des widgets dans la barre de gauche
		self.layoutBarGauche = QVBoxLayout()
		
		self.boutonAjouter = QPushButton("Ajouter",self.barGauche)
		self.boutonEditer = QPushButton("Editer",self.barGauche)
		self.boutonSupprimer = QPushButton("Supprimer",self.barGauche)
		
		self.layoutBarGauche.addWidget(self.boutonAjouter)
		self.layoutBarGauche.addWidget(self.boutonEditer)
		self.layoutBarGauche.addWidget(self.boutonSupprimer)
		self.barGauche.setLayout(self.layoutBarGauche)
		
		# Définition du widget conteneur du ScrollArea
		self.conteneurScrollArea = QWidget(self.zoneAffichage)
		
		# Définition du widgets qui va contenir le formulaire pour ajouter et modifier un contact
		
		self.layoutConteneurAddMod = QGridLayout()
		
		self.titreLabel = QLabel("*******", self)
		self.nomAddModLabel = QLabel("NOM", self)
		self.prenomAddModLabel = QLabel("PRENOM", self)
		self.numeroAddModLabel = QLabel("NUMERO", self)
		self.adresseAddModLabel = QLabel("ADRESSE", self)
		self.typeAddModLabel = QLabel("TYPE", self)
		self.nomAddModWidget = QLineEdit(self.conteneurScrollArea)
		self.prenomAddModWidget = QLineEdit("prenom",self.conteneurScrollArea)
		self.numeroAddModWidget = QLineEdit(self.conteneurScrollArea)
		self.adresseAddModWidget = QLineEdit(self.conteneurScrollArea)
		self.typeAddModWidget = QLineEdit(self.conteneurScrollArea)
		self.boutonValiderAddMod = QPushButton("Valider",self.conteneurScrollArea)
		
		
		
		self.nomAddModWidget.setStyleSheet("background-color:rgb(255,255,255)")
		self.prenomAddModWidget.setStyleSheet("background-color:rgb(255,255,255)")
		self.numeroAddModWidget.setStyleSheet("background-color:rgb(255,255,255)")
		self.adresseAddModWidget.setStyleSheet("background-color:rgb(255,255,255)")
		self.typeAddModWidget.setStyleSheet("background-color:rgb(255,255,255)")
		
		self.layoutConteneurAddMod.addWidget(self.titreLabel,0,3,1,1)
		self.layoutConteneurAddMod.addWidget(self.nomAddModLabel,1,0,1,7)
		self.layoutConteneurAddMod.addWidget(self.nomAddModWidget,2,0,1,7)
		self.layoutConteneurAddMod.addWidget(self.prenomAddModLabel,3,0,1,7)
		self.layoutConteneurAddMod.addWidget(self.prenomAddModWidget,4,0,1,7)
		self.layoutConteneurAddMod.addWidget(self.numeroAddModLabel,5,0,1,7)
		self.layoutConteneurAddMod.addWidget(self.numeroAddModWidget,6,0,1,7)
		self.layoutConteneurAddMod.addWidget(self.adresseAddModLabel,7,0,1,7)
		self.layoutConteneurAddMod.addWidget(self.adresseAddModWidget,8,0,1,7)
		self.layoutConteneurAddMod.addWidget(self.typeAddModLabel,9,0,1,7)
		self.layoutConteneurAddMod.addWidget(self.typeAddModWidget,10,0,1,7)
		self.layoutConteneurAddMod.addWidget(self.boutonValiderAddMod,11,3,1,1)
		self.zoneAddMod.setLayout(self.layoutConteneurAddMod)
		

	def connecterWidget(self):
		self.connect(self.boutonAjouter, SIGNAL("clicked()"),self.SLOT_Ajouter)
			
	def SLOT_Ajouter(self):
		self.zoneAffichage.hide()
		self.titreLabel.setText("Ajouter")
		self.nomAddModWidget.setText("")
		self.prenomAddModWidget.setText("")
		self.numeroAddModWidget.setText("")
		self.adresseAddModWidget.setText("")
		self.typeAddModWidget.setText("")
		self.zoneAddMod.show()
		
		
		
		

