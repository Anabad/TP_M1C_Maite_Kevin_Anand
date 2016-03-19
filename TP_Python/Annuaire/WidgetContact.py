#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# View.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

TAILLE_ESPACE=20
TAILLE_ICONE_MOYENNE=69
TAILLE_LIGNE = TAILLE_ESPACE

TAILLE_ICONE_PETITE=35
TAILLE_LINE_EDIT_X=250
TAILLE_LINE_EDIT_Y=TAILLE_ICONE_MOYENNE-2*TAILLE_ESPACE
TAILLE_COMBO_BOX_X=90
TAILLE_COMBO_BOX_Y=35
TAILLE_NUMERO_X=200
TAILLE_NUMERO_Y=35
#Plus très utile
TAILLE_CONTENEUR_X=2*TAILLE_ESPACE+TAILLE_ICONE_MOYENNE+TAILLE_LINE_EDIT_X*3/2
TAILLE_CONTENEUR_Y=1200

class WidgetContact(QGroupBox):
	""" Cette class sera la class qui fera l'affichage d'un contact"""
	##		PARTIE INITIALISATION
	def __init__(self,parent):
		QGroupBox.__init__(self,parent)
		self.__statut = None
		self.dictionnaire = {"nom":"","prenom":"","groupe":"","favori":"non","libelle_numero":[""],"libelle_mail":[""],"libelle_adresse":[""],"numero":"","mail":"","adresse":"","id_numero":[""],"id_mail":[""],"id_adresse":[""]}
		self.creerWidgets()
		self.statut("Ajouter",{})
	def creerWidgets(self):
		##########################
		#
		#	Déclaration de tous les object (view)
		#
		##########################
		self.scroll = QScrollArea(self)
		self.conteneurScroll = QWidget(self)
		self.scroll.setWidget(self.conteneurScroll)
		# Définition de tous les widgets
		self.labelNomPrenom = QLabel(self.conteneurScroll)
		self.nomLineEdit = QLineEdit(self.conteneurScroll)
		self.prenomLineEdit = QLineEdit(self.conteneurScroll)
		self.favori = QPushButton(self.conteneurScroll)
		
		self.labelNumero = QLabel(self.conteneurScroll)
		self.numerolibelleComboBox = []
		self.numeroLineEdit = []
		self.supprimernumeroPushButton = []
		self.numeroAjouterPushButton = QPushButton(self.conteneurScroll)
		
		self.labelmail = QLabel(self.conteneurScroll)
		self.mailLibelleComboBox = []
		self.mailLineEdit = []
		self.supprimerMailPushButton = []
		self.mailAjouterPushButton = QPushButton(self.conteneurScroll)
		
		self.labelAdresse = QLabel(self.conteneurScroll)
		self.adresseLibelleComboBox = []
		self.adresseLineEdit = []
		self.supprimerAdressePushButton = []
		self.adresseAjouterPushButton = QPushButton(self.conteneurScroll)
		
		self.groupeComboBox = QComboBox(self.conteneurScroll)
		self.groupeComboBox.addItem("Aucun groupe","Aucun groupe")
		self.groupeComboBox.addItem("Plan cul","Plan cul")
		self.groupeComboBox.addItem("Ami","Ami")
		self.groupeComboBox.addItem("Travail","Travail")
		
		self.ligne = QFrame(self.conteneurScroll)
		self.ligne.setFrameShape(QFrame.HLine)
		self.ligne.setFrameShadow(QFrame.Sunken)
		self.ligne2 = QFrame(self.conteneurScroll)
		self.ligne2.setFrameShape(QFrame.HLine)
		self.ligne2.setFrameShadow(QFrame.Sunken)
		self.ligne3 = QFrame(self.conteneurScroll)
		self.ligne3.setFrameShape(QFrame.HLine)
		self.ligne3.setFrameShadow(QFrame.Sunken)
		self.ligne4 = QFrame(self.conteneurScroll)
		self.ligne4.setFrameShape(QFrame.HLine)
		self.ligne4.setFrameShadow(QFrame.Sunken)
		##########################
		#
		#	Propriété
		#
		##########################
		self.scroll.setFrameShape(QFrame.NoFrame);
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
		self.__desactiverEdition()
		self.nomLineEdit.setStyleSheet("background-color:rgba(255,255,255,0);color: #F24C04;font-weight: bold") 
		self.prenomLineEdit.setStyleSheet("background-color:rgba(255,255,255,0);color: #F24C04;font-weight: bold") 
		self.groupeComboBox.setStyleSheet("background-color:rgb(255,255,255,0);color: #F24C04;font-weight: bold")
		
		self.connecterWidget()
		
	##		FONCTIONS UTILES
	def __activerEdition(self):
		self.nomLineEdit.setEnabled(True) 
		self.prenomLineEdit.setEnabled(True)
		self.favori.setEnabled(True)
		self.groupeComboBox.setEnabled(True)
		for numeroLibelle in self.numerolibelleComboBox:
			numeroLibelle.setEnabled(True)
		for numero in self.numeroLineEdit:
			numero.setEnabled(True) 
		for mailLibelle in self.mailLibelleComboBox:
			mailLibelle.setEnabled(True)
		for mail in self.mailLineEdit:
			mail.setEnabled(True)
		for adresseLibelle in self.adresseLibelleComboBox:
			adresseLibelle.setEnabled(True)
		for adresse in self.adresseLineEdit:
			adresse.setEnabled(True)
		self.numeroAjouterPushButton.show()
		self.mailAjouterPushButton.show()
		self.adresseAjouterPushButton.show()
	def __desactiverEdition(self):
		self.nomLineEdit.setEnabled(False)
		self.prenomLineEdit.setEnabled(False)
		self.favori.setEnabled(False)
		for numeroLibelle in self.numerolibelleComboBox:
			numeroLibelle.setEnabled(False)
		for numero in self.numeroLineEdit:
			numero.setEnabled(False) 
		for mailLibelle in self.mailLibelleComboBox:
			mailLibelle.setEnabled(False)
		for mail in self.mailLineEdit:
			mail.setEnabled(False)
		for adresseLibelle in self.adresseLibelleComboBox:
			adresseLibelle.setEnabled(False)
		for adresse in self.adresseLineEdit:
			adresse.setEnabled(False)
		self.groupeComboBox.setEnabled(False)
		self.numeroAjouterPushButton.hide()
		self.mailAjouterPushButton.hide()
		self.adresseAjouterPushButton.hide()
		
	def positionnerWidget(self):
		self.curseur_y=0
		
		self.labelNomPrenom.setGeometry(TAILLE_ESPACE,TAILLE_ESPACE,TAILLE_ICONE_MOYENNE,TAILLE_ICONE_MOYENNE)
		self.nomLineEdit.setGeometry(2*TAILLE_ESPACE+TAILLE_ICONE_MOYENNE,TAILLE_ESPACE,TAILLE_LINE_EDIT_X,TAILLE_LINE_EDIT_Y)
		self.favori.setGeometry(2*TAILLE_ESPACE+TAILLE_ICONE_MOYENNE+TAILLE_LINE_EDIT_X+TAILLE_ESPACE/2,TAILLE_ESPACE,TAILLE_ICONE_PETITE,TAILLE_ICONE_PETITE)
		self.curseur_y=TAILLE_ESPACE+TAILLE_LINE_EDIT_Y
		if self.dictionnaire["favori"] == "non":
			self.favori.setObjectName("oui")
			self.favori.setStyleSheet("QPushButton {border-image: url(IMAGES/nonfavoris.png); }")
		else:
			self.favori.setObjectName("non")
			self.favori.setStyleSheet("QPushButton {border-image: url(IMAGES/favoris.png); }")
		self.prenomLineEdit.setGeometry(2*TAILLE_ESPACE+TAILLE_ICONE_MOYENNE,TAILLE_ESPACE+self.curseur_y,TAILLE_LINE_EDIT_X,TAILLE_LINE_EDIT_Y);self.curseur_y = self.curseur_y + TAILLE_ESPACE + TAILLE_LINE_EDIT_Y
		self.__ajouterComboLinePushbutton(self.ligne,self.labelNumero,self.numerolibelleComboBox,self.numeroLineEdit,self.supprimernumeroPushButton,self.numeroAjouterPushButton,"numero",["Mobile","Domicile","Bureau"])	
		self.__ajouterComboLinePushbutton(self.ligne2,self.labelmail,self.mailLibelleComboBox,self.mailLineEdit,self.supprimerMailPushButton,self.mailAjouterPushButton,"mail",["Domicile","Bureau"])
		self.__ajouterComboLinePushbutton(self.ligne3,self.labelAdresse,self.adresseLibelleComboBox,self.adresseLineEdit,self.supprimerAdressePushButton,self.adresseAjouterPushButton,"adresse",["Domicile","Bureau"])
		self.ligne4.setGeometry(TAILLE_ESPACE,self.curseur_y,TAILLE_CONTENEUR_X-2*TAILLE_ESPACE,TAILLE_LIGNE)
		self.groupeComboBox.setGeometry(2*TAILLE_ESPACE+TAILLE_ICONE_MOYENNE,self.curseur_y+TAILLE_ESPACE,TAILLE_LINE_EDIT_X,TAILLE_LINE_EDIT_Y);self.curseur_y=self.curseur_y+TAILLE_LINE_EDIT_Y+2*TAILLE_ESPACE
		self.conteneurScroll.setGeometry(0,0,self.size().width(),self.curseur_y)
		
	def __ajouterComboLinePushbutton(self,ligne,label,libelle,line,supprimer,ajouter,donnee,items):
		ligne.setGeometry(TAILLE_ESPACE,self.curseur_y,TAILLE_CONTENEUR_X-2*TAILLE_ESPACE,TAILLE_LIGNE)
		label.setGeometry(TAILLE_ESPACE+(TAILLE_ICONE_MOYENNE-TAILLE_ICONE_PETITE)/2,self.curseur_y+TAILLE_ESPACE,TAILLE_ICONE_PETITE,TAILLE_ICONE_PETITE)
		if len(libelle)!=0:
			for l in libelle:
				l.setParent(None)
				del l
			del libelle[:]
		if len(line)!=0:
			for l in line:
				l.setParent(None)
				del l
			del line[:]
		if len(supprimer)!=0:
			for s in supprimer:
				s.setParent(None)
				del s
			del supprimer[:]
		for i in range(0,len(self.dictionnaire["libelle_"+donnee])):
			libelle.append(QComboBox(self.conteneurScroll))
			line.append(QLineEdit(self.conteneurScroll))
			for item in items:
				libelle[-1].addItem(item,item)
			libelle[-1].setGeometry(2*TAILLE_ESPACE+TAILLE_ICONE_MOYENNE,self.curseur_y+TAILLE_ESPACE,TAILLE_COMBO_BOX_X,TAILLE_COMBO_BOX_Y)
			libelle[-1].setStyleSheet("background-color:rgb(255,255,255,0);color: #F24C04;font-weight: bold")
			line[-1].setGeometry(2*TAILLE_ESPACE+TAILLE_ICONE_MOYENNE+TAILLE_COMBO_BOX_X+TAILLE_ESPACE/2,self.curseur_y+TAILLE_ESPACE,TAILLE_NUMERO_X,TAILLE_NUMERO_Y)
			if len(self.dictionnaire["libelle_"+donnee]) > 1:
				if self.__statut != "Visualiser":
					supprimer.append(QPushButton(self.conteneurScroll))
					supprimer[-1].setGeometry(2*TAILLE_ESPACE+TAILLE_ICONE_MOYENNE+TAILLE_COMBO_BOX_X+TAILLE_ESPACE/2+TAILLE_NUMERO_X+TAILLE_ESPACE/2,self.curseur_y+TAILLE_ESPACE,TAILLE_ICONE_PETITE,TAILLE_ICONE_PETITE)
					supprimer[-1].show()
					supprimer[-1].setIcon(QIcon(QPixmap("IMAGES/supprimerNumeroIcone.png")))
					supprimer[-1].setIconSize(QSize(TAILLE_ICONE_PETITE-2,TAILLE_ICONE_PETITE-2))
					supprimer[-1].setObjectName("supprimer"+donnee.capitalize()+str(i))
					self.connect(supprimer[-1], SIGNAL("clicked()"),self.SLOT_supprimerDonnee)
			self.curseur_y=self.curseur_y+TAILLE_ESPACE+TAILLE_NUMERO_Y
			line[-1].setStyleSheet("background-color:rgba(255,255,255,0);color: #F24C04;font-weight: bold")
			line[-1].setPlaceholderText(donnee.capitalize())
			line[-1].show()
			libelle[-1].show()
		if self.__statut != "Visualiser":
			ajouter.setGeometry(2*TAILLE_ESPACE+TAILLE_ICONE_MOYENNE+(TAILLE_LINE_EDIT_X-TAILLE_ICONE_PETITE)/2,self.curseur_y+TAILLE_ESPACE/2,TAILLE_ICONE_PETITE,TAILLE_ICONE_PETITE);self.curseur_y=self.curseur_y + TAILLE_ESPACE/2 + TAILLE_ICONE_PETITE
			ajouter.show()
		else:
			ajouter.hide()
		
		
	# GESTION DES DONNEES INTERNES
	def setValeurs(self):
		self.positionnerWidget()
		self.nomLineEdit.setText(self.dictionnaire["nom"])
		self.prenomLineEdit.setText(self.dictionnaire["prenom"])
		if self.dictionnaire["favori"] == "non":
			self.favori.setObjectName("non")
			self.favori.setStyleSheet("QPushButton {border-image: url(IMAGES/nonfavoris.png); }")
		else:
			self.favori.setObjectName("oui")
			self.favori.setStyleSheet("QPushButton {border-image: url(IMAGES/favoris.png); }")
		self.groupeComboBox.setCurrentIndex(self.groupeComboBox.findData(self.dictionnaire["groupe"]))
		#dictionnaire["favori"] = "non"
		i=0
		for value in self.dictionnaire["numero"]:
			self.numeroLineEdit[i].setText(value)
			i=i+1
		i=0
		for value in self.dictionnaire["libelle_numero"]:
			self.numerolibelleComboBox[i].setCurrentIndex(self.numerolibelleComboBox[i].findData(value))
			i=i+1
		i=0
		for value in self.dictionnaire["mail"]:
			self.mailLineEdit[i].setText(value)
			i=i+1
		i=0
		for value in self.dictionnaire["libelle_mail"]:
			self.mailLibelleComboBox[i].setCurrentIndex(self.mailLibelleComboBox[i].findData(value))
			i=i+1
		i=0
		for value in self.dictionnaire["adresse"]:
			self.adresseLineEdit[i].setText(value)
			i=i+1
		i=0
		for value in self.dictionnaire["libelle_adresse"]:
			self.adresseLibelleComboBox[i].setCurrentIndex(self.adresseLibelleComboBox[i].findData(value))
			i=i+1
		#On redesactive l'édition car en récuperant les valeurs dans les widgets ils se sont réactivés
		if self.__statut == "Visualiser":
			self.__desactiverEdition()
	def getValeurs(self):
		""" Cette fonction retourne toutes les informations contenues dans le formulaire """
		dictionnaire = {}
		dictionnaire["nom"] = self.nomLineEdit.text()
		dictionnaire["prenom"] = self.prenomLineEdit.text()
		dictionnaire["favori"] = self.favori.objectName()
		dictionnaire["groupe"] = self.groupeComboBox.currentText()
		i=0
		if "id_adresse" in self.dictionnaire.keys():
			dictionnaire["id_adresse"]=self.dictionnaire["id_adresse"]
		if "id_numero" in self.dictionnaire.keys():
			dictionnaire["id_numero"]=self.dictionnaire["id_numero"]
		if "id_mail" in self.dictionnaire.keys():
			dictionnaire["id_mail"]=self.dictionnaire["id_mail"]
		if "id_contact" in self.dictionnaire.keys():
			dictionnaire["id_contact"]=self.dictionnaire["id_contact"]
		dictionnaire["numero"]=[]
		for value in self.dictionnaire["libelle_numero"]:
			dictionnaire["numero"].append(self.numeroLineEdit[i].text())
			i=i+1
		i=0
		dictionnaire["libelle_numero"]=[]
		for value in self.dictionnaire["libelle_numero"]:
			dictionnaire["libelle_numero"].append(self.numerolibelleComboBox[i].currentText())
			i=i+1
		i=0
		dictionnaire["mail"]=[]
		for value in self.dictionnaire["libelle_mail"]:
			dictionnaire["mail"].append(self.mailLineEdit[i].text())
			i=i+1
		i=0
		dictionnaire["libelle_mail"]=[]
		for value in self.dictionnaire["libelle_mail"]:
			dictionnaire["libelle_mail"].append(self.mailLibelleComboBox[i].currentText())
			i=i+1
		i=0
		dictionnaire["adresse"]=[]
		for value in self.dictionnaire["libelle_adresse"]:
			dictionnaire["adresse"].append(self.adresseLineEdit[i].text())
			i=i+1
		i=0
		dictionnaire["libelle_adresse"]=[]
		for value in self.dictionnaire["libelle_adresse"]:
			dictionnaire["libelle_adresse"].append(self.adresseLibelleComboBox[i].currentText())
			i=i+1
		if self.__statut == "Visualiser":
			self.__desactiverEdition()
		self.dictionnaire=dictionnaire
		return dictionnaire
	def viderFormulaire(self):
		self.nomLineEdit.setText("")
		self.prenomLineEdit.setText("")
		self.dictionnaire={"nom":"","prenom":"","groupe":"","favori":"non","libelle_numero":[""],"libelle_mail":[""],"libelle_adresse":[""],"numero":"","mail":"","adresse":"","id_numero":[""],"id_mail":[""],"id_adresse":[""]}
		self.positionnerWidget()
		
	def statut(self,futurStatut,dictionnaire):
		self.__statut = futurStatut 
		if futurStatut == "Editer":
			self.dictionnaire=dictionnaire
			self.__activerEdition()
			self.setValeurs()
		elif futurStatut == "Ajouter":
			self.__activerEdition()
			self.viderFormulaire()
		elif futurStatut == "Visualiser":
			self.dictionnaire=dictionnaire
			self.setValeurs()
			self.__desactiverEdition()
		else:
			raise ValueError("Statut doit etre egale à Editer,Ajouter ou Visualiser")
	def getStatut(self):
		return self.__statut
		
	def delValueDictionnaire(self,index,key):
		print(self.dictionnaire["libelle_"+key])
		if ("id_"+key) in self.dictionnaire.keys():
			if index < len(self.dictionnaire[("id_"+key)]):
				del self.dictionnaire["id_"+key][index]
				if len(self.dictionnaire["id_"+key]) == 0:
					del self.dictionnaire["id_"+key]
		del self.dictionnaire["libelle_"+key][index]
		del self.dictionnaire[key][index]
	##		PARTIE EVENT
	def connecterWidget(self):
		self.connect(self.numeroAjouterPushButton, SIGNAL("clicked()"),self.SLOT_ajouterDonnee)
		self.connect(self.mailAjouterPushButton, SIGNAL("clicked()"),self.SLOT_ajouterDonnee)
		self.connect(self.adresseAjouterPushButton, SIGNAL("clicked()"),self.SLOT_ajouterDonnee)
		self.connect(self.favori, SIGNAL("clicked()"),self.SLOT_Favoris)
		
	#	SLOTS
	def SLOT_ajouterDonnee(self):
				# Ici on utilise getValeurs car celle ci met aussi à jour notre dictionnaire qui sera utilisé dans le setValeur
		self.getValeurs()
		if self.sender() == self.numeroAjouterPushButton:
			self.dictionnaire["libelle_numero"].append("Mobile")
		elif self.sender() == self.mailAjouterPushButton:
			self.dictionnaire["libelle_mail"].append("Domicile")
		elif self.sender() == self.adresseAjouterPushButton:
			self.dictionnaire["libelle_adresse"].append("Domicile")
		self.positionnerWidget()
		self.setValeurs()
	def SLOT_supprimerDonnee(self):
		# Ici on utilise getValeurs car celle ci met aussi à jour notre dictionnaire qui sera utilisé dans le setValeur
		self.getValeurs()
		if self.sender().objectName()[:-1] == "supprimerNumero":
			self.delValueDictionnaire(int(self.sender().objectName()[-1]),"numero")
		elif self.sender().objectName()[:-1] == "supprimerMail":
			self.delValueDictionnaire(int(self.sender().objectName()[-1]),"mail")
		elif self.sender().objectName()[:-1] == "supprimerAdresse":
			self.delValueDictionnaire(int(self.sender().objectName()[-1]),"adresse")
		self.positionnerWidget()
		self.setValeurs()
		
	def SLOT_Favoris(self):
		if self.favori.objectName() == "non":
			self.favori.setObjectName("oui")
			self.favori.setStyleSheet("QPushButton {border-image: url(IMAGES/favoris.png); }")
		else:
			self.favori.setObjectName("non")
			self.favori.setStyleSheet("QPushButton {border-image: url(IMAGES/nonfavoris.png); }")
			print(self.favori.objectName())
	#	REDIMENSIONNEMENT
	def resizeEvent(self, evt=None):
		self.scroll.setGeometry(0,5,self.size().width(),self.size().height()-10)
		self.conteneurScroll.setGeometry(0,0,self.scroll.size().width()-15,self.curseur_y)

