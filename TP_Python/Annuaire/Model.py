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
	def supprimerContact(self,contact):
		""" Fonction pour supprimer un contact """
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		cursor.execute("""
		DELETE FROM nom_prenom
			WHERE id_contact= ?
		""",(contact,))
	
		cursor.execute("""
		DELETE FROM numero
			WHERE id_contact= ?
		""",(contact,))
	
		cursor.execute("""
		DELETE FROM mail
			WHERE id_contact= ?
		""",(contact,))
	
		cursor.execute("""
		DELETE FROM adresse
			WHERE id_contact= ?
		""",(contact,))
	
		conn.commit()
		conn.close()
	def rechercher_contact(self,recherche):
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		if len(recherche) != 0:
			if recherche[-1] == ' ':
				recherche = recherche[:-1]
		mots = recherche.split(' ')
		resultat = []
		iterator=0
		for mot in mots:
			if iterator == 0 and len(mots) > 1:
				mot = '%' + mot
			else:
				mot = '%' + mot+ '%'
			
			# Recherche par nom
			cursor.execute("""
			SELECT * FROM nom_prenom np
			INNER JOIN numero nu
				on np.id_contact = nu.id_contact
			INNER JOIN mail ma
				on np.id_contact = ma.id_contact
			INNER JOIN adresse ad
				on np.id_contact = ad.id_contact
			WHERE np.nom LIKE ? or np.prenom LIKE ? or nu.numero LIKE ?
			ORDER BY np.nom,np.prenom
			""",(mot,mot,mot))
			resultatRequete=cursor.fetchall()
			if iterator > 0:
				for contact in resultatRequete:
					if resultatRequete in resultat:
						resultat = resultat + resultatRequete
			else:
				resultat = resultatRequete
			if len(mots) > 1 and len(resultat) == 0:
				break
			iterator= iterator + 1 
		if len(mots) > 1:
			while 1:
				sansDoublon = list(set(resultat))
				if len(sansDoublon) == len(resultat):
					break
				for contact in sansDoublon:
					resultat.remove(contact)
		conn.close()
		print(resultat)
		return resultat
	def getContacts(self):
		""" Fonction qui retourne le nom et le prénom de tous les contacts afin de les afficher dans la QListView"""
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		cursor.execute("""
		SELECT id_contact,nom,prenom FROM nom_prenom
		ORDER BY nom,prenom
		""")
		a = cursor.fetchall()
		conn.close()
		return a
	def getContactById(self,index):
		""" Fonction qui retourne toutes les informations d'une personne identifié par son id """
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		cursor.execute("""
			SELECT np.id_contact
				, np.nom
				, np.prenom
				, np.groupe
				, np.favori
				, nu.numero
				, nu.libelle
				, ma.mail
				, ma.libelle
				, ad.adresse
				, ad.libelle
			FROM nom_prenom np
			INNER JOIN numero nu
				on np.id_contact = nu.id_contact
			INNER JOIN mail ma
				on np.id_contact = ma.id_contact
			INNER JOIN adresse ad
				on np.id_contact = ad.id_contact
			WHERE np.id_contact = ?
			ORDER BY np.nom, np.prenom
			""",(index,))
		a = cursor.fetchall()
		conn.close()
		if len(a) != 0:
			return a[0]
		else:
			return []
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
		conn.close()
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
def rechercher_contact(recherche):
	pass		
		
def ajouter_contact(contact):
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
if __name__ == "__main__":
	conn = sqlite3.connect('annuaire.db')
	cursor = conn.cursor()
	#contact = {"nom":"Dilot","prenom":"Kevin","groupe":"Ami","favori":"non",
	#"numero":"12345678","libelle_numero":"portable","mail":"kevin.didelot@esme.com","libelle_mail":"profesionnel",
	#"adresse":"devant l''ecole","libelle_adresse":"bureau"}
	

	
	cursor.execute("""
		SELECT * FROM nom_prenom
		""")
	a = cursor.fetchall()
	print(a)
	print("--------------------")
	a = rechercher_contact("")
	print(a)
	print("--------------------")
	b = rechercher_contact("kev")
	print(b)
	print("--------------------")
	c = rechercher_contact("ke did")
	print(c)
	print("--------------------")
	d = rechercher_contact("123")
	print(d)
	print("--------------------")
	conn.close()
