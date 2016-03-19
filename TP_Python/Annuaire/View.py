#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# View.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from threading import RLock
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
	##		PARTIE INITIALISATION
	def __init__(self,control):
		QMainWindow.__init__(self)
		self.control = control
		self.control.setView(self)
		self.__baseVide = False
		self.__idActif = None
		self.__barreActive = "AtoZ"
		self.idContacts = []
		self.idContactsGroupe = []
		self.verrou = RLock()
		self.setWindowTitle("Annuaire")
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.setGeometry(0,0,TAILLE_FENETRE_DEMARRAGE_X,TAILLE_FENETRE_DEMARRAGE_Y)
		self.creerWidget()
		self.connecterWidget()
	def creerWidget(self):
		""" Cette fonction va définir tous les boutons ainsi que les espaces conteneur de la fenetre """
		##########################
		#
		#	Déclaration de tous les object (view)
		#
		##########################
		self.conteneur = QWidget(self)
		self.setCentralWidget(self.conteneur)
		
		# Définition des deux gros widget de la fenetre
		self.barHaut = QWidget(self.conteneur)
		self.dessousFenetre =QWidget(self.conteneur)
		
		self.nouveauContactWidget = QPushButton(self.barHaut)
		self.rechercheWidget = QLineEdit(self.barHaut)
		self.rechercheLabel = QLabel(self.barHaut)
		
		# Définition de la partie de gauche du dessous de la fenetre
		self.tab = QTabWidget(self.dessousFenetre)
		self.AtoZ = QListWidget()
		self.Groupe = QListWidget()
		self.tab.addTab(self.AtoZ,"&A-Z")
		self.tab.addTab(self.Groupe,"&Groupes")
		
		self.zoneAddMod = QWidget(self.dessousFenetre)
		self.layoutZoneAddMod = QGridLayout()
		self.conteneurBoutonEditSuppr = QWidget(self.zoneAddMod)
		self.formulaire = WidgetContact(self.zoneAddMod)
		self.boutonEdit = QPushButton("Ajouter", self.conteneurBoutonEditSuppr)
		self.boutonSupprimer = QPushButton("Supprimer", self.conteneurBoutonEditSuppr)
		self.layoutZoneAddMod.addWidget(self.formulaire,0,0,1,2)
		self.layoutZoneAddMod.addWidget(self.conteneurBoutonEditSuppr,0,3,1,1)
		self.zoneAddMod.setLayout(self.layoutZoneAddMod)
		
		##########################
		#
		#	Propriété
		#
		##########################
		self.conteneur.setObjectName("FenetrePrincipale")
		self.conteneur.setStyleSheet("QWidget#FenetrePrincipale{background-image:url(IMAGES/fond.jpg)}") #background-color:rgba(200,200,200,125)
		self.conteneur.setGeometry(0,0,self.size().width(),self.size().height())
		self.conteneur.setMinimumWidth(4*TAILLE_BOUTON_CARRE+TAILLE_BARRE_RECHERCHE)
		self.barHaut.setGeometry(0,0,self.conteneur.size().width(),75)
		self.barHaut.setFixedHeight(75)
		self.dessousFenetre.setGeometry(0,75,TAILLE_FENETRE_DEMARRAGE_X,TAILLE_FENETRE_DEMARRAGE_Y-75)
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
		self.layoutZoneAddMod.setMargin(0)
		self.layoutZoneAddMod.setSpacing(0)
		self.AtoZ.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.conteneurBoutonEditSuppr.setFixedWidth(TAILLE_BOUTON_RECTANGLE_X*8/5)
		self.boutonEdit.setGeometry(QRect(self.conteneurBoutonEditSuppr.size().width()-(TAILLE_BOUTON_RECTANGLE_X/4*5), TAILLE_BOUTON_RECTANGLE_Y/2,TAILLE_BOUTON_RECTANGLE_X,TAILLE_BOUTON_RECTANGLE_Y))
		self.boutonSupprimer.setGeometry(QRect(self.conteneurBoutonEditSuppr.size().width()-(TAILLE_BOUTON_RECTANGLE_X/4*5), 3*TAILLE_BOUTON_RECTANGLE_Y/2,TAILLE_BOUTON_RECTANGLE_X,TAILLE_BOUTON_RECTANGLE_Y))
		self.boutonSupprimer.hide()
		self.tab.setGeometry(QRect(15, 15, (self.size().width())*35/100-30,self.dessousFenetre.size().height()-30))
		self.zoneAddMod.setGeometry(QRect(37+ (self.size().width())*35/100-30, 15, (self.size().width())*60/100,self.dessousFenetre.size().height()-30))
		self.zoneAddMod.setObjectName("zoneAddMod")
		self.zoneAddMod.setStyleSheet("QWidget#zoneAddMod{background-image:url(IMAGES/fondFormulaire.jpg);border:5px groove #666462;}")
		self.tab.setStyleSheet("background-image:url(IMAGES/fondFormulaire.jpg)")
		self.formulaire.setStyleSheet("background:transparent;")
		self.AtoZ.setStyleSheet("QListWidget::item{background:transparent;}")
		self.Groupe.setStyleSheet("QListWidget::item{background:transparent;}")
		self.control.updateAffichageContacts(self.rechercheWidget.text())
		
	def idActif(self,index):
		if index == None:
			self.__idActif == None
		else:
			with self.verrou:
				if self.getBarreActive() == "AtoZ":
					if len(self.idContacts) != 0 and len(self.idContacts) > index:
						self.__idActif = self.idContacts[index]
					else:
						self.__idActif = None
				elif self.getBarreActive() == "Groupe":
					if len(self.idContactsGroupe) != 0 and len(self.idContactsGroupe) > index:
						self.__idActif = self.idContactsGroupe[index]
					else:
						self.__idActif = None
	def getIdActif(self):
		return self.__idActif
	def barreActive(self,barre):
		if barre == "AtoZ" or barre == "Groupe":
			self.__barreActive = barre
		else:
			raise ValueError("Statut doit etre egale à Editer,Ajouter ou Visualiser")
	def getBarreActive(self):
		return self.__barreActive 
	def getDictionnaire(self):
			contact = self.control.getContactById(self.getIdActif())
			return contact
		
	def updateAffichageContactBar(self,contacts,contactsGroupe):
		with self.verrou:
			#Partie pour l'onglet AtoZ
			try:
				self.idContacts=[]
				liste=[]
				self.AtoZ.selectionModel().currentChanged.disconnect()
				self.AtoZ.clear()
				for contact in contacts:
					self.idContacts.append(contact[0])
					self.AtoZ.addItem(contact[1] + " " + contact[2])
					item = self.AtoZ.item(self.AtoZ.count()-1)
					item.setTextAlignment(Qt.AlignCenter)
				self.AtoZ.selectionModel().currentChanged.connect(self.SLOT_SelectionContact)
			except IndexError:
				print("bug")
			#Partie pour l'onglet Groupe
			try:
				self.idContactsGroupe=[]
				liste=[]
				self.Groupe.selectionModel().currentChanged.disconnect()
				self.Groupe.clear()
				groupe=""
				for contact in contactsGroupe:
					if groupe != contact[3]:
						groupe=contact[3]
						self.idContactsGroupe.append(None)
						self.Groupe.addItem("--"+groupe+"--")
						item = self.Groupe.item(self.Groupe.count()-1)
						item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
						item.setTextAlignment(Qt.AlignCenter)
					self.idContactsGroupe.append(contact[0])
					self.Groupe.addItem(contact[1] + " " + contact[2])
					item = self.Groupe.item(self.Groupe.count()-1)
					item.setTextAlignment(Qt.AlignCenter)
				self.Groupe.selectionModel().currentChanged.connect(self.SLOT_SelectionContactGroupe)
			except IndexError:
				print("bug")
	def editerContact(self):
		contact=self.formulaire.getValeurs()
		contact["id_contact"]=self.getIdActif()
		self.control.controlerModifier(contact)
	def testBaseVide(self):
		if self.control.testBaseVide() != 1:
			return 0
		QMessageBox.critical(self, "Aucun contact", "Aucun contact dans la base à afficher")
		self.formulaire.statut("Ajouter",{})
		self.boutonEdit.setText("Ajouter")
		self.boutonSupprimer.hide()
		return 1
	##		PARTIE EVENT
	def connecterWidget(self):
		""" Ici nous connectons chaque bouton à sa fonction associé """
		self.AtoZ.selectionModel().currentChanged.connect(self.SLOT_SelectionContact)
		self.Groupe.selectionModel().currentChanged.connect(self.SLOT_SelectionContactGroupe)	
		#self.connect(self.rechercheWidget, SIGNAL("textChanged(QString&)"),SLOT("self.SLOT_BarreRecherche(QString)"))
		self.rechercheWidget.textChanged.connect(self.SLOT_BarreRecherche)
		self.connect(self.nouveauContactWidget, SIGNAL("clicked()"),self.SLOT_nouveau)
		self.connect(self.boutonEdit, SIGNAL("clicked()"),self.SLOT_Edition)
		self.connect(self.boutonSupprimer, SIGNAL("clicked()"),self.SLOT_Supprimer)
	def SLOT_nouveau(self):
		self.idActif(None)
		self.formulaire.statut("Ajouter",{})
		self.boutonEdit.setText("Ajouter")
		self.boutonSupprimer.hide()
	def SLOT_BarreRecherche(self):
		self.control.updateAffichageContacts(self.rechercheWidget.text())
	def SLOT_Edition(self):	
		if self.formulaire.getStatut() == "Visualiser":
			if self.getIdActif() != None:
				self.formulaire.statut("Editer",self.getDictionnaire())
				self.boutonEdit.setText("Fin édition")
				self.boutonSupprimer.show()
				self.boutonSupprimer.setText("Annuler")
			else:
				self.formulaire.statut("Ajouter",{})
				self.boutonEdit.setText("Ajouter")
				self.boutonSupprimer.hide()
		elif self.formulaire.getStatut() == "Editer":
			self.editerContact()
			self.control.updateAffichageContacts(self.rechercheWidget.text())
			if self.getBarreActive() == "AtoZ":
				self.idActif(0)
			else:
				self.idActif(1)
			self.formulaire.statut("Visualiser",self.getDictionnaire())
			self.boutonSupprimer.show()
			self.boutonEdit.setText("Editer")
			self.boutonSupprimer.setText("Supprimer")
		elif self.formulaire.getStatut() == "Ajouter":
			ajout=self.control.controlerAjouter(self.formulaire.getValeurs())
			if ajout == 1:
				QMessageBox.critical(self, "Pas assez d'informations", "Vérifiez d'avoir bien rentré au moins le nom et le prenom du contact")
			else:
				self.control.updateAffichageContacts(self.rechercheWidget.text())
				if self.getBarreActive() == "AtoZ":
					self.idActif(0)
				else:
					self.idActif(1)
				self.formulaire.statut("Visualiser",self.getDictionnaire())
				self.boutonSupprimer.show()
				self.boutonEdit.setText("Editer")
				self.boutonSupprimer.setText("Supprimer")					
				
	def SLOT_Supprimer(self):
		if self.formulaire.getStatut() == "Visualiser":
			if self.getIdActif() != None:
				reponse = QMessageBox.question(self, "Confirmer suppression", "Etes vous sûr de vouloir supprimer définitivement ce contact ?", QMessageBox.Yes | QMessageBox.No)
				if reponse == QMessageBox.Yes:
					self.control.supprimerContact(self.getIdActif())
					self.control.updateAffichageContacts(self.rechercheWidget.text())
					self.formulaire.viderFormulaire()
					if self.testBaseVide() == 0:
						self.idActif(0)
						self.formulaire.statut("Visualiser",self.getDictionnaire())
				else:
					self.idActif(None)
					self.formulaire.viderFormulaire()
		else:
			self.idActif(None)
			self.formulaire.statut("Visualiser",self.getDictionnaire())
			self.boutonEdit.setText("Editer")
			self.boutonSupprimer.setText("Supprimer")
			self.boutonSupprimer.show()
	def SLOT_SelectionContact(self,nouvelIndex):
		self.barreActive("AtoZ")
		self.idActif(nouvelIndex.row())
		self.formulaire.statut("Visualiser",self.getDictionnaire())
		self.boutonEdit.setText("Editer")
		self.boutonSupprimer.setText("Supprimer")
		self.boutonSupprimer.show()
	def SLOT_SelectionContactGroupe(self,nouvelIndex):
		self.barreActive("Groupe")
		self.idActif(nouvelIndex.row())
		self.formulaire.statut("Visualiser",self.getDictionnaire())
		self.boutonEdit.setText("Editer")
		self.boutonSupprimer.show()
	#	REDIMENSIONNEMENT
	def resizeEvent(self, evt=None):
		self.barHaut.resize(self.conteneur.size().width(),self.barHaut.size().height())
		self.rechercheWidget.move(self.size().width()- self.rechercheWidget.size().width() - TAILLE_BOUTON_CARRE - TAILLE_BOUTON_CARRE,(self.barHaut.size().height()-TAILLE_BOUTON_CARRE) / 2)
		self.rechercheLabel.move(self.size().width() - TAILLE_BOUTON_CARRE - TAILLE_BOUTON_CARRE/2,(self.barHaut.size().height()-TAILLE_BOUTON_CARRE) / 2)
		self.dessousFenetre.setGeometry(0,75,self.size().width(), self.size().height()-self.barHaut.size().height())
		if self.size().width()*35/100-30 < 200:
			self.tab.setGeometry(QRect(15, 15, (self.size().width())*35/100-30,self.dessousFenetre.size().height()-30))
			self.zoneAddMod.setGeometry(QRect(37+ (self.size().width())*35/100-30, 15, (self.size().width())*60/100,self.dessousFenetre.size().height()-30))
		else:
			self.tab.setGeometry(QRect(15, 15, 200,self.dessousFenetre.size().height()-30))
			self.zoneAddMod.setGeometry(QRect(37+ 200, 15, self.size().width()- 274,self.dessousFenetre.size().height()-30))
		
		
		self.boutonEdit.setGeometry(QRect(self.conteneurBoutonEditSuppr.size().width()-(TAILLE_BOUTON_RECTANGLE_X/4*5), TAILLE_BOUTON_RECTANGLE_Y/2,TAILLE_BOUTON_RECTANGLE_X,TAILLE_BOUTON_RECTANGLE_Y))
		self.boutonSupprimer.setGeometry(QRect(self.conteneurBoutonEditSuppr.size().width()-(TAILLE_BOUTON_RECTANGLE_X/4*5), 3*TAILLE_BOUTON_RECTANGLE_Y/2,TAILLE_BOUTON_RECTANGLE_X,TAILLE_BOUTON_RECTANGLE_Y))
		

