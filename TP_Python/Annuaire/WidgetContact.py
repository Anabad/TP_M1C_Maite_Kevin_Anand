#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# View.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

TAILLE_ICONE_MOYENNE=50
TAILLE_ICONE_PETITE=30

class WidgetContact(QGroupBox):
	""" Cette class sera la class qui fera l'affichage d'un contact"""
	def __init__(self,parent):
		QGroupBox.__init__(self,parent)
		self.Statut = "Ajouter"
		self.creerWidgets()
	def creerWidgets(self):
		
		self.scroll = QScrollArea()
		self.conteneurScroll = QWidget(self)
		# Définition du layout qui va contenir et organiser tous les widgets
		self.layout= QGridLayout()
		self.layout.setMargin(30)
		# Définition de tous les widgets
		self.labelNomPrenom = QLabel(self)
		self.nomLineEdit = QLineEdit(self)
		self.prenomLineEdit = QLineEdit(self)
		
		self.labelNumero = QLabel(self)
		self.numerolibelleComboBox = QComboBox(self)
		self.numerolibelleComboBox.addItem("Mobile")
		self.numerolibelleComboBox.addItem("Domicile")
		self.numerolibelleComboBox.addItem("Bureau")
		self.numeroLineEdit = QLineEdit(self)
		self.numeroAjouterPushButton = QPushButton(self)
		
		self.labelmail = QLabel(self)
		self.mailLibelleComboBox = QComboBox(self)
		self.mailLibelleComboBox.addItem("Domicile")
		self.mailLibelleComboBox.addItem("Bureau")
		self.mailLineEdit = QLineEdit(self)
		self.mailAjouterPushButton = QPushButton(self)
		
		self.labelAdresse = QLabel(self)
		self.adresseLibelleComboBox = QComboBox(self)
		self.adresseLibelleComboBox.addItem("Domicile")
		self.adresseLibelleComboBox.addItem("Bureau")
		self.adresseLineEdit = QLineEdit(self)
		self.adresseAjouterPushButton = QPushButton(self)
		
		self.groupeComboBox = QComboBox(self)
		self.groupeComboBox.addItem("Aucun groupe")
		self.groupeComboBox.addItem("Plan cul")
		self.groupeComboBox.addItem("Ami")
		self.groupeComboBox.addItem("Travail")
		
		self.ligne = QFrame(self)
		self.ligne.setFrameShape(QFrame.HLine)
		self.ligne.setFrameShadow(QFrame.Sunken)
		self.ligne2 = QFrame(self)
		self.ligne2.setFrameShape(QFrame.HLine)
		self.ligne2.setFrameShadow(QFrame.Sunken)
		self.ligne3 = QFrame(self)
		self.ligne3.setFrameShape(QFrame.HLine)
		self.ligne3.setFrameShadow(QFrame.Sunken)
		self.ligne4 = QFrame(self)
		self.ligne4.setFrameShape(QFrame.HLine)
		self.ligne4.setFrameShadow(QFrame.Sunken)
		# Positionnement de tous les Widgets dans le layout
		self.positionnerWidget()
		#self.setStyleSheet("")
		##########################
		#
		#	Propriété
		#
		##########################
		self.labelNomPrenom.setPixmap(QPixmap("IMAGES/IdentiteIcone.png").scaled(TAILLE_ICONE_MOYENNE,TAILLE_ICONE_MOYENNE))
		self.labelNumero.setPixmap(QPixmap("IMAGES/TelephoneIcone.png").scaled(TAILLE_ICONE_PETITE,TAILLE_ICONE_PETITE))
		self.labelmail.setPixmap(QPixmap("IMAGES/MailIcone.png").scaled(TAILLE_ICONE_PETITE,TAILLE_ICONE_PETITE))
		self.labelAdresse.setPixmap(QPixmap("IMAGES/AdresseIcone.png").scaled(TAILLE_ICONE_PETITE,TAILLE_ICONE_PETITE))
		self.numeroAjouterPushButton.setIcon(QIcon(QPixmap("IMAGES/ajouterIcone.png")))
		self.numeroAjouterPushButton.setIconSize(QSize(TAILLE_ICONE_PETITE-2,TAILLE_ICONE_PETITE-2))
		self.numeroAjouterPushButton.setFlat(True)
		self.mailAjouterPushButton.setIcon(QIcon(QPixmap("IMAGES/ajouterIcone.png")))
		self.mailAjouterPushButton.setIconSize(QSize(TAILLE_ICONE_PETITE-2,TAILLE_ICONE_PETITE-2))
		self.mailAjouterPushButton.setFlat(True)
		self.adresseAjouterPushButton.setIcon(QIcon(QPixmap("IMAGES/ajouterIcone.png")))
		self.adresseAjouterPushButton.setIconSize(QSize(TAILLE_ICONE_PETITE-2,TAILLE_ICONE_PETITE-2))
		self.adresseAjouterPushButton.setFlat(True)
		self.nomLineEdit.setPlaceholderText("Nom")
		self.prenomLineEdit.setPlaceholderText("Prenom")
		self.numeroLineEdit.setPlaceholderText("Numéro")
		self.mailLineEdit.setPlaceholderText("Mail")
		self.adresseLineEdit.setPlaceholderText("Adresse")
		self.desactiverEdition()
	def activerEdition(self,statut):
		self.Statut = statut
		self.nomLineEdit.setEnabled(True) 
		self.prenomLineEdit.setEnabled(True) 
		self.numeroLineEdit.setEnabled(True) 
		self.mailLineEdit.setEnabled(True)
		self.adresseLineEdit.setEnabled(True)
		self.numerolibelleComboBox.setEnabled(True)
		self.mailLibelleComboBox.setEnabled(True)
		self.adresseLibelleComboBox.setEnabled(True)
		self.groupeComboBox.setEnabled(True)
		
		self.numeroAjouterPushButton.show()
		self.mailAjouterPushButton.show()
		self.adresseAjouterPushButton.show()
		self.nomLineEdit.setStyleSheet("background-color:rgb(255,255,255)") 
		self.prenomLineEdit.setStyleSheet("background-color:rgb(255,255,255)") 
		self.numeroLineEdit.setStyleSheet("background-color:rgb(255,255,255)")
		self.mailLineEdit.setStyleSheet("background-color:rgb(255,255,255)") 
		self.adresseLineEdit.setStyleSheet("background-color:rgb(255,255,255)")
		self.numerolibelleComboBox.setStyleSheet("background-color:rgb(255,255,255)")
		self.mailLibelleComboBox.setStyleSheet("background-color:rgb(255,255,255)")
		self.adresseLibelleComboBox.setStyleSheet("background-color:rgb(255,255,255)")
		self.groupeComboBox.setStyleSheet("background-color:rgb(255,255,255)")
		self.positionnerWidget()
	def desactiverEdition(self):
		self.Statut = "Visualiser"
		self.nomLineEdit.setEnabled(False) 
		self.prenomLineEdit.setEnabled(False) 
		self.numeroLineEdit.setEnabled(False) 
		self.mailLineEdit.setEnabled(False) 
		self.adresseLineEdit.setEnabled(False)
		self.numerolibelleComboBox.setEnabled(False)
		self.mailLibelleComboBox.setEnabled(False)
		self.adresseLibelleComboBox.setEnabled(False)
		self.groupeComboBox.setEnabled(False)
		self.numeroAjouterPushButton.hide()
		self.mailAjouterPushButton.hide()
		self.adresseAjouterPushButton.hide()
		self.nomLineEdit.setStyleSheet("background-color:rgba(255,255,255,0)") 
		self.prenomLineEdit.setStyleSheet("background-color:rgba(255,255,255,0)") 
		self.numeroLineEdit.setStyleSheet("background-color:rgba(255,255,255,0)")
		self.mailLineEdit.setStyleSheet("background-color:rgba(255,255,255,0)")
		self.adresseLineEdit.setStyleSheet("background-color:rgb(255,255,255,0)")
		self.numerolibelleComboBox.setStyleSheet("background-color:rgb(255,255,255,0)")
		self.mailLibelleComboBox.setStyleSheet("background-color:rgb(255,255,255,0)")
		self.adresseLibelleComboBox.setStyleSheet("background-color:rgb(255,255,250,0)")
		self.groupeComboBox.setStyleSheet("background-color:rgb(255,255,255,0)")
		self.positionnerWidget()
	def positionnerWidget(self):
		self.layout.addWidget(self.labelNomPrenom,0,0,2,3)
		self.layout.addWidget(self.nomLineEdit,0,3,1,3)
		self.layout.addWidget(self.prenomLineEdit,1,3,1,3)
		self.layout.addWidget(self.ligne,2,0,1,6)
		self.layout.addWidget(self.labelNumero,3,0,1,3)
		self.layout.addWidget(self.numerolibelleComboBox,3,3,1,1)
		self.layout.addWidget(self.numeroLineEdit,3,4,1,2)
		self.layout.addWidget(self.numeroAjouterPushButton,4,3,1,3)
		self.layout.addWidget(self.ligne2,5,0,1,6)
		self.layout.addWidget(self.labelmail,6,0,1,3)
		self.layout.addWidget(self.mailLibelleComboBox,6,3,1,1)
		self.layout.addWidget(self.mailLineEdit,6,4,1,2)
		self.layout.addWidget(self.mailAjouterPushButton,7,3,1,3)
		self.layout.addWidget(self.ligne3,8,0,1,6)
		self.layout.addWidget(self.labelAdresse,9,0,1,3)
		self.layout.addWidget(self.adresseLibelleComboBox,9,3,1,1)
		self.layout.addWidget(self.adresseLineEdit,9,4,1,2)
		self.layout.addWidget(self.adresseAjouterPushButton,10,3,1,3)
		self.layout.addWidget(self.ligne4,11,0,1,6)
		self.layout.addWidget(self.groupeComboBox,12,3,1,3)
		self.conteneurScroll.setLayout(self.layout)
	def setValeurs(self,dictionnaire):
		self.nomLineEdit.setText(dictionnaire["nom"])
		self.prenomLineEdit.setText(dictionnaire["prenom"])
		self.groupeComboBox.setCurrentIndex(self.groupeComboBox.findData(dictionnaire["groupe"]))
		#dictionnaire["favori"] = "non"
		self.numeroLineEdit.setText(dictionnaire["numero"])
		self.numerolibelleComboBox.setCurrentIndex(self.numerolibelleComboBox.findData(dictionnaire["libelle_numero"]))
		self.mailLineEdit.setText(dictionnaire["mail"])
		self.mailLibelleComboBox.setCurrentIndex(self.mailLibelleComboBox.findData(dictionnaire["libelle_mail"]))
		self.adresseLineEdit.setText(dictionnaire["adresse"])
		self.adresseLibelleComboBox.setCurrentIndex(self.adresseLibelleComboBox.findData(dictionnaire["libelle_adresse"]))
	def viderFormulaire(self):
		self.nomLineEdit.setText("")
		self.prenomLineEdit.setText("")
		self.numeroLineEdit.setText("")
		self.mailLineEdit.setText("")
	def getModification(self):
		""" Cette fonction retourne toutes les informations contenues dans le formulaire """
		dictionnaire = {}
		dictionnaire["nom"] = self.nomLineEdit.text()
		dictionnaire["prenom"] = self.prenomLineEdit.text()
		dictionnaire["groupe"] = self.groupeComboBox.itemData(self.numerolibelleComboBox.currentIndex())
		dictionnaire["favori"] = "non"
		dictionnaire["numero"] = self.numeroLineEdit.text()
		dictionnaire["libelle_numero"] = self.numerolibelleComboBox.itemData(self.numerolibelleComboBox.currentIndex())
		dictionnaire["mail"] = self.mailLineEdit.text()
		dictionnaire["libelle_mail"] = self.mailLibelleComboBox.itemData(self.mailLibelleComboBox.currentIndex())
		dictionnaire["adresse"] = self.adresseLineEdit.text()
		dictionnaire["libelle_adresse"] = self.adresseLibelleComboBox.itemData(self.adresseLibelleComboBox.currentIndex())
		return dictionnaire

