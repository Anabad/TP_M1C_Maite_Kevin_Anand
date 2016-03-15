#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# View.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from threading import Lock
from WidgetContact import WidgetContact
import sys


TAILLE_FENETRE_DEMARRAGE_X=850
TAILLE_FENETRE_DEMARRAGE_Y=500
TAILLE_BOUTON_CARRE=35
TAILLE_BOUTON_RECTANGLE_X=80
TAILLE_BOUTON_RECTANGLE_Y=35
TAILLE_BARRE_RECHERCHE=300

class View(QMainWindow):
	""" Cette class est la fenetre principale de l'annuaire"""
	def __init__(self,control):
		QMainWindow.__init__(self)
		self.control = control
		self.idActif = None
		self.mutex = Lock()
		self.control.setView(self)
		self.idContacts = []
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
		self.conteneur.setMinimumWidth(4*TAILLE_BOUTON_CARRE+TAILLE_BARRE_RECHERCHE)
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
		self.rechercheLabel = QLabel(self.barHaut)
		
		self.nouveauContactWidget.setFlat(True)
		self.nouveauContactWidget.setFixedSize(TAILLE_BOUTON_CARRE,TAILLE_BOUTON_CARRE)
		self.rechercheWidget.setFixedSize(TAILLE_BARRE_RECHERCHE,TAILLE_BOUTON_CARRE-1)
		self.rechercheLabel.setFixedSize(TAILLE_BOUTON_CARRE,TAILLE_BOUTON_CARRE)
		self.nouveauContactWidget.move((self.barHaut.size().height()-TAILLE_BOUTON_CARRE) / 2,(self.barHaut.size().height()-TAILLE_BOUTON_CARRE) / 2)
		self.rechercheWidget.move(self.size().width() - self.rechercheWidget.size().width() - TAILLE_BOUTON_CARRE - TAILLE_BOUTON_CARRE,15)
		self.rechercheLabel.move(self.size().width() - TAILLE_BOUTON_CARRE - TAILLE_BOUTON_CARRE/2,(self.barHaut.size().height()-TAILLE_BOUTON_CARRE) / 2)
		self.rechercheWidget.setPlaceholderText("Rechercher")
		self.nouveauContactWidget.setIcon(QIcon(QPixmap("IMAGES/ajouterIcone.png")))
		self.nouveauContactWidget.setIconSize(QSize(TAILLE_BOUTON_CARRE-2,TAILLE_BOUTON_CARRE-2))
		self.nouveauContactWidget.setStyleSheet("background:rgb(255,255,255);border-bottom:none;outline: none;")
		self.rechercheWidget.setStyleSheet("background-color:rgb(255,255,255)")
		self.rechercheLabel.setPixmap(QPixmap("IMAGES/loupe.png").scaled(TAILLE_BOUTON_CARRE-2,TAILLE_BOUTON_CARRE-2))
		self.rechercheLabel.setStyleSheet("border-bottom:none;outline: none;")
	def creerDessousFenetre(self):
		# Définition de la partie de gauche du dessous de la fenetre
		self.tab = QTabWidget(self.dessousFenetre)
		self.AtoZ = QListWidget()
		self.Groupe = QWidget()
		self.tab.addTab(self.AtoZ,"&A-Z")
		self.tab.addTab(self.Groupe,"&Groupe")
		self.zoneAddMod = QWidget(self.dessousFenetre)
		self.layoutZoneAddMod = QGridLayout()
		self.conteneurBoutonEditSuppr = QWidget(self.zoneAddMod)
		self.formulaire = WidgetContact(self.zoneAddMod)
		self.boutonEdit = QPushButton("Ajouter", self.conteneurBoutonEditSuppr)
		self.boutonSupprimer = QPushButton("Supprimer", self.conteneurBoutonEditSuppr)
		self.layoutZoneAddMod.addWidget(self.formulaire,0,0,1,2)
		self.layoutZoneAddMod.addWidget(self.conteneurBoutonEditSuppr,0,3,1,1)
		self.zoneAddMod.setLayout(self.layoutZoneAddMod)
		
		self.layoutZoneAddMod.setMargin(0)
		self.layoutZoneAddMod.setSpacing(0)
		self.AtoZ.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.conteneurBoutonEditSuppr.setMinimumWidth(2*TAILLE_BOUTON_RECTANGLE_X)
		self.boutonEdit.setGeometry(QRect(self.conteneurBoutonEditSuppr.size().width()-(TAILLE_BOUTON_RECTANGLE_X/4*5), TAILLE_BOUTON_RECTANGLE_Y/2,TAILLE_BOUTON_RECTANGLE_X,TAILLE_BOUTON_RECTANGLE_Y))
		self.boutonSupprimer.setGeometry(QRect(self.conteneurBoutonEditSuppr.size().width()-(TAILLE_BOUTON_RECTANGLE_X/4*5), 3*TAILLE_BOUTON_RECTANGLE_Y/2,TAILLE_BOUTON_RECTANGLE_X,TAILLE_BOUTON_RECTANGLE_Y))
		self.boutonSupprimer.hide()
		self.tab.setGeometry(QRect(15, 15, (self.size().width())*35/100-30,self.dessousFenetre.size().height()-30))
		self.zoneAddMod.setGeometry(QRect(37+ (self.size().width())*35/100-30, 15, (self.size().width())*60/100,self.dessousFenetre.size().height()-30))
		self.zoneAddMod.setObjectName("zoneAddMod")
		self.zoneAddMod.setStyleSheet("QWidget#zoneAddMod{border:1px solid white;background-color:rgba(200,200,200,220)}")
		self.control.updateAffichageContacts(self.rechercheWidget.text())
	def connecterWidget(self):
		""" Ici nous connectons chaque bouton à sa fonction associé """
		self.AtoZ.selectionModel().currentChanged.connect(self.SLOT_SelectionContact)		
		#self.connect(self.rechercheWidget, SIGNAL("textChanged(QString&)"),SLOT("self.SLOT_BarreRecherche(QString)"))
		self.rechercheWidget.textChanged.connect(self.SLOT_BarreRecherche)
		self.connect(self.nouveauContactWidget, SIGNAL("clicked()"),self.SLOT_nouveau)
		self.connect(self.boutonEdit, SIGNAL("clicked()"),self.SLOT_Edition)
		self.connect(self.boutonSupprimer, SIGNAL("clicked()"),self.SLOT_Supprimer)
	# Les 3 fonctions suivantes sont les slots de tout nos boutons
	def SLOT_nouveau(self):
		self.boutonEdit.setText("Ajouter")
		self.boutonSupprimer.hide()
		self.formulaire.activerEdition("Ajouter")
		self.formulaire.viderFormulaire()
	def SLOT_Edition(self): 	
		if self.formulaire.Statut == "Visualiser":
			self.boutonSupprimer.show()
			self.boutonEdit.setText("Fin édition")
			self.boutonSupprimer.setText("Annuler")
			self.formulaire.activerEdition("Editer")
		elif self.formulaire.Statut == "Editer":
			self.boutonSupprimer.show()
			self.boutonEdit.setText("Editer")
			self.boutonSupprimer.setText("Supprimer")
			contact = self.formulaire.getModification()
			self.modifierContact()
			self.formulaire.desactiverEdition()
			self.control.updateAffichageContacts(self.rechercheWidget.text())
		elif self.formulaire.Statut == "Ajouter":
			self.boutonSupprimer.show()
			self.boutonEdit.setText("Editer")
			self.boutonSupprimer.setText("Supprimer")
			self.ajouterContact()
			self.formulaire.desactiverEdition()
			self.control.updateAffichageContacts(self.rechercheWidget.text())
		else:
			self.boutonEdit.setText("Ajouter")
			self.boutonSupprimer.hide()
			contact = self.formulaire.getModification()
			self.ajouterContact()
			self.formulaire.desactiverEdition()
			self.control.updateAffichageContacts(self.rechercheWidget.text())
			
	def SLOT_Supprimer(self):
		if self.formulaire.Statut == "Visualiser":
			if self.idActif != None:
				reponse = QMessageBox.question(self, "Confirmer suppression", "Etes vous sûr de vouloir supprimer définitivement ce contact ?", QMessageBox.Yes | QMessageBox.No)
				if reponse == QMessageBox.Yes:
					self.control.supprimerContact(self.idActif)
					self.control.updateAffichageContacts(self.rechercheWidget.text())
					if len(self.idContacts):
						self.idActif=self.idContacts[0]				 
						self.AtoZ.setCurrentIndex(self.AtoZ.rootIndex())
					else:
						self.idActif=None		
		else:
			self.formulaire.Statut = "Visualiser"
			self.boutonEdit.setText("Editer")
			self.boutonSupprimer.setText("Supprimer")
			self.boutonSupprimer.show()
			self.updateFormulaire()
			self.formulaire.desactiverEdition()
	def SLOT_SelectionContact(self,nouvelIndex):
		self.formulaire.Statut = "Visualiser"
		self.boutonEdit.setText("Editer")
		self.boutonSupprimer.show()
		self.formulaire.desactiverEdition()
		try:
			self.idActif = self.idContacts[nouvelIndex.row()]
			self.updateFormulaire()
		except IndexError:
			return
	def updateFormulaire(self):
		contact = self.control.getContactById(self.idActif)
		if len(contact) != 0:
			dictionnaire= {}
			dictionnaire["nom"] = contact[1]
			dictionnaire["prenom"] = contact[2]
			dictionnaire["groupe"] = contact[3]
			dictionnaire["favori"] = contact[4]
			dictionnaire["numero"] = contact[5]
			dictionnaire["libelle_numero"] = contact[6]
			dictionnaire["mail"] = contact[7]
			dictionnaire["libelle_mail"] = contact[8]
			dictionnaire["adresse"] = contact[9]
			dictionnaire["libelle_adresse"] = contact[10]
			self.formulaire.setValeurs(dictionnaire)
	def SLOT_BarreRecherche(self):
		self.control.updateAffichageContacts(self.rechercheWidget.text())
		
	def ajouterContact(self):
		self.control.controlerAjouter(self.formulaire.getModification())
	def modifierContact(self):
		contact = self.formulaire.getModification()
		contact["id_contact"] = self.idActif
		self.control.controlerModifier(contact)
	def updateAffichageContactBar(self,contacts):
		try:
			self.idContacts=[]
			liste=[]
			self.AtoZ.clear()
			for contact in contacts:
				self.idContacts.append(contact[0])
				self.AtoZ.addItem(contact[1] + " " + contact[2])
		except IndexError:
			return
	def resizeEvent(self, evt=None):
		self.barHaut.resize(self.conteneur.size().width(),self.barHaut.size().height())
		self.rechercheWidget.move(self.size().width()- self.rechercheWidget.size().width() - TAILLE_BOUTON_CARRE - TAILLE_BOUTON_CARRE,(self.barHaut.size().height()-TAILLE_BOUTON_CARRE) / 2)
		self.rechercheLabel.move(self.size().width() - TAILLE_BOUTON_CARRE - TAILLE_BOUTON_CARRE/2,(self.barHaut.size().height()-TAILLE_BOUTON_CARRE) / 2)
		self.dessousFenetre.setGeometry(0,75,self.size().width(), self.size().height()-self.barHaut.size().height())
		self.tab.setGeometry(QRect(15, 15, (self.size().width())*35/100-30,self.dessousFenetre.size().height()-30))
		self.zoneAddMod.setGeometry(QRect(37+ (self.size().width())*35/100-30, 15, (self.size().width())*60/100,self.dessousFenetre.size().height()-30))
		self.boutonEdit.setGeometry(QRect(self.conteneurBoutonEditSuppr.size().width()-(TAILLE_BOUTON_RECTANGLE_X/4*5), TAILLE_BOUTON_RECTANGLE_Y/2,TAILLE_BOUTON_RECTANGLE_X,TAILLE_BOUTON_RECTANGLE_Y))
		self.boutonSupprimer.setGeometry(QRect(self.conteneurBoutonEditSuppr.size().width()-(TAILLE_BOUTON_RECTANGLE_X/4*5), 3*TAILLE_BOUTON_RECTANGLE_Y/2,TAILLE_BOUTON_RECTANGLE_X,TAILLE_BOUTON_RECTANGLE_Y))
		

