#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# View.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from WidgetContact import WidgetContact
import sys


TAILLE_FENETRE_DEMARRAGE_X=800
TAILLE_FENETRE_DEMARRAGE_Y=400
TAILLE_BOUTON=35
TAILLE_BARRE_RECHERCHE=300

class View(QMainWindow):
	""" Cette class est la fenetre principale de l'annuaire"""
	def __init__(self,control):
		QMainWindow.__init__(self)
		self.control = control
		self.control.setView(self)
		self.setWindowTitle("Annuaire")
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.setStyleSheet("background:transparent;background-color:rgba(200,200,200,125)")
		self.setGeometry(0,0,TAILLE_FENETRE_DEMARRAGE_X,TAILLE_FENETRE_DEMARRAGE_Y)
		self.creerWidget()
		self.connecterWidget()

	def creerWidget(self):
		""" Cette fonction va définir tous les boutons ainsi que les espaces conteneur de la fenetre """
		# Définition des conteneurs principaux de la fenetre
		self.conteneur = QWidget(self)
		self.conteneur.setGeometry(0,0,self.size().width(),self.size().height())
		self.conteneur.setMinimumWidth(4*TAILLE_BOUTON+TAILLE_BARRE_RECHERCHE)
		self.setCentralWidget(self.conteneur)
		
		# Définition des deux gros widget de la fenetre
		self.barHaut = QWidget(self.conteneur)
		self.dessousFenetre =QWidget(self.conteneur)
		self.barHaut.setGeometry(0,0,self.conteneur.size().width(),75)
		self.barHaut.setFixedHeight(75)
		self.dessousFenetre.setGeometry(0,75,TAILLE_FENETRE_DEMARRAGE_X,TAILLE_FENETRE_DEMARRAGE_Y-75)
		
		
		# Définition des widgets dans la bar du haut
		self.creerBarHautWidget()
		# Définition des widgets dans la partie inférieur de l'écran
		self.creerDessousFenetre()
	def creerBarHautWidget(self):
		""" Cette fonction défini la bar du haut """
		self.nouveauContactWidget = QPushButton(self.barHaut)
		self.rechercheWidget = QLineEdit(self.barHaut)
		self.bouttonValideRecherche = QPushButton(self.barHaut)
		
		self.nouveauContactWidget.setFlat(True)
		self.nouveauContactWidget.setFixedSize(TAILLE_BOUTON,TAILLE_BOUTON)
		self.rechercheWidget.setFixedSize(TAILLE_BARRE_RECHERCHE,TAILLE_BOUTON-1)
		self.bouttonValideRecherche.setFixedSize(TAILLE_BOUTON,TAILLE_BOUTON)
		self.bouttonValideRecherche.setFlat(True)
		self.nouveauContactWidget.move((self.barHaut.size().height()-TAILLE_BOUTON) / 2,(self.barHaut.size().height()-TAILLE_BOUTON) / 2)
		self.rechercheWidget.move(self.size().width() - self.rechercheWidget.size().width() - TAILLE_BOUTON - TAILLE_BOUTON,15)
		self.bouttonValideRecherche.move(self.size().width() - TAILLE_BOUTON - TAILLE_BOUTON/2,(self.barHaut.size().height()-TAILLE_BOUTON) / 2)
		
		self.nouveauContactWidget.setIcon(QIcon(QPixmap("IMAGES/ajouterIcone.jpg")));
		self.nouveauContactWidget.setIconSize(QSize(TAILLE_BOUTON-2,TAILLE_BOUTON-2))
		self.nouveauContactWidget.setStyleSheet("background:rgb(255,255,255);border-bottom:none;outline: none;")
		self.rechercheWidget.setStyleSheet("background-color:rgb(255,255,255)")
		self.bouttonValideRecherche.setIcon(QIcon(QPixmap("IMAGES/loupe.png")));
		self.bouttonValideRecherche.setIconSize(QSize(TAILLE_BOUTON-2,TAILLE_BOUTON-2))
		self.bouttonValideRecherche.setStyleSheet("border-bottom:none;outline: none;")
	def creerDessousFenetre(self):
		# Définition de la partie de gauche du dessous de la fenetre
		self.tab = QTabWidget(self.dessousFenetre)
		self.AtoZ = QListView()
		self.Groupe = QWidget()
		self.tab.addTab(self.AtoZ,"&A-Z")
		self.tab.addTab(self.Groupe,"&Groupe")
		self.zoneAddMod = WidgetContact(self.dessousFenetre,self.control)
		self.AtoZ.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tab.setGeometry(QRect(15, 15, (self.size().width())*35/100-30,self.dessousFenetre.size().height()-30))
		self.zoneAddMod.setGeometry(QRect(37+ (self.size().width())*35/100-30, 15, (self.size().width())*60/100,self.dessousFenetre.size().height()-30))
		
		self.zoneAddMod.setStyleSheet("WidgetContact{border:1px solid white;background-color:rgba(200,200,200,220)}")
	def connecterWidget(self):
		#self.connect(self.AtoZ, SIGNAL("clicked(QModelIndex)"),self.SLOT_Editer)
		self.AtoZ.selectionModel().currentChanged.connect(self.SLOT_Editer)
	def updateAffichageContactBar(self,contacts):
		self.listeContactAtoZ = []
		self.idContacts = []
		for contact in contacts:
			self.idContacts.append(contact[0])
			self.listeContactAtoZ.append(contact[1]+" "+contact[2])
		model = QStringListModel(self.listeContactAtoZ)
		self.AtoZ.setModel(model)			
	def SLOT_Editer(self,nouvelIndex,ancienIndex):
		print("PAAATRON"+str(nouvelIndex.row()))
	def resizeEvent(self, evt=None):
		self.barHaut.resize(self.conteneur.size().width(),self.barHaut.size().height())
		self.rechercheWidget.move(self.size().width()- self.rechercheWidget.size().width() - TAILLE_BOUTON - TAILLE_BOUTON,(self.barHaut.size().height()-TAILLE_BOUTON) / 2)
		self.bouttonValideRecherche.move(self.size().width() - TAILLE_BOUTON - TAILLE_BOUTON/2,(self.barHaut.size().height()-TAILLE_BOUTON) / 2)
		self.dessousFenetre.setGeometry(0,75,self.size().width(), self.size().height()-self.barHaut.size().height())
		self.tab.setGeometry(QRect(15, 15, (self.size().width())*35/100-30,self.dessousFenetre.size().height()-30))
		self.zoneAddMod.setGeometry(QRect(37+ (self.size().width())*35/100-30, 15, (self.size().width())*60/100,self.dessousFenetre.size().height()-30))
		

