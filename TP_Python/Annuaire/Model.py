#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Model.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3


class Model:
	def __init__(self,control):
		self.control=control
		self.control.setModel(self)
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()

		""" Creation de la table des noms et prenoms"""
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS nom_prenom(
		     id_contact INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
		     nom TEXT,
			 prenom TEXT,
			 groupe TEXT,
			 favori TEXT
		)
		""")
		conn.commit()

		""" Creation de la table des numeros"""
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS numero(
		     id_numero INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
			 numero TEXT,
			 libelle TEXT,
			  id_contact INTEGER,
			 FOREIGN KEY(id_contact) REFERENCES nom_prenom(id_contact)
		)
		""")
		conn.commit()

		""" Creation de la table mail"""
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS mail(
		     id_mail INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
			 mail TEXT,
			 libelle TEXT,
			  id_contact INTEGER,
			 FOREIGN KEY(id_contact) REFERENCES nom_prenom(id_contact)
		)
		""")
		conn.commit()

		""" Creation de la table adresse"""
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS adresse(
		     id_numero INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
			 adresse TEXT,
			 libelle TEXT,
			 id_contact INTEGER,
			 FOREIGN KEY(id_contact) REFERENCES nom_prenom(id_contact)
		)
		""")
		conn.commit()
		conn.close()
	def ajouter_contact(self,contact):
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		""" Fonction pour ajouter un nouveau contact"""
	
		# Insertion du nom et prenom
		cursor.execute("""
		INSERT INTO nom_prenom(nom,prenom,groupe,favori) VALUES(
			:nom,
			:prenom,
			:groupe,
			:favori
		)
		""",contact)
		conn.commit()
	
		# Recuperation de l'id
		cursor.execute("""SELECT MAX(id_contact) from nom_prenom""")
		id_contact = cursor.fetchone()[0]
		contact["id_contact"] = id_contact
	
		#Insertion du numero
		cursor.execute("""
		INSERT INTO numero(numero,libelle,id_contact) VALUES(
			:numero,
			:libelle_numero,
			:id_contact
		)
		""",contact)
	
		#Insertion du mail
		cursor.execute("""
		INSERT INTO mail(mail,libelle,id_contact) VALUES(
			:mail,
			:libelle_mail,
			:id_contact
		)
		""",contact)
	
		#Insertion de l'adresse
		cursor.execute("""
		INSERT INTO adresse(adresse,libelle,id_contact) VALUES(
			:adresse,
			:libelle_adresse,
			:id_contact
		)
		""",contact)
	
		conn.commit()
		conn.close()
		self.getContacts()
	#-----------------------------------------------
	def editer_contact(self,contact):
		""" Fonction pour editer un contact """
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		cursor.execute("""
		UPDATE nom_prenom
			SET nom=:nom,prenom=:prenom,groupe=:groupe,favori=:favori
			WHERE id_contact=:id_contact
		""",contact)
	
		cursor.execute("""
		UPDATE numero
			SET numero=:numero,libelle=:libelle_numero
			WHERE id_contact=:id_contact
		""",contact)
	
		cursor.execute("""
		UPDATE mail
			SET mail=:mail,libelle=:libelle_mail
			WHERE id_contact=:id_contact
		""",contact)
	
		cursor.execute("""
		UPDATE adresse
			SET adresse=:adresse,libelle=:libelle_adresse
			WHERE id_contact=:id_contact
		""",contact)
	
		conn.commit()
		conn.close()
	def getContacts(self):
		""" Fonction qui retourne le nom et le prénom de la personne afin de les afficher dans la QListView"""
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		cursor.execute("""
		SELECT id_contact,nom,prenom FROM nom_prenom
		ORDER BY nom,prenom
		""")
		a = cursor.fetchall()
		return a
	def afficherConsoleContacts(self):
		# Code pour afficher
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		cursor.execute("""
		SELECT * FROM nom_prenom
		""")
		a = cursor.fetchall()
		print(a)

		cursor.execute("""
		SELECT * FROM numero
		""")
		a = cursor.fetchall()
		print(a)

		cursor.execute("""
		SELECT * FROM mail
		""")
		a = cursor.fetchall()
		print(a)

		cursor.execute("""
		SELECT * FROM adresse
		""")
		a = cursor.fetchall()
		print(a)
		#---------
	def __del__(self):
		pass
	#-----------------------------------------------------------------------
	#contact = {"nom":"Didelot","prenom":"Keke","groupe":"Ami","favori":"non",
	#"numero":"12345678","libelle_numero":"portable","mail":"kevin.didelot@esme.com","libelle_mail":"profesionnel",
	#"adresse":"devant l''ecole","libelle_adresse":"bureau","id_contact" : 7}
	#
	#editer_contact(contact)	
	#----------------------------------------
	# Code pour supprimer toutes les donnees
	#cursor.execute("""
	#DELETE FROM nom_prenom
	#""")
	#conn.commit()

	#cursor.execute("""
	#DELETE FROM numero 
	#""")
	#conn.commit()

	#cursor.execute("""
	#DELETE FROM mail 
	#""")
	#conn.commit()

	#cursor.execute("""
	#DELETE FROM adresse
	#""")
	#conn.commit()

#----------------------------------------

