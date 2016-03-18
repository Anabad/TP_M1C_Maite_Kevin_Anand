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
		     id_adresse INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
			 adresse TEXT,
			 libelle TEXT,
			 id_contact INTEGER,
			 FOREIGN KEY(id_contact) REFERENCES nom_prenom(id_contact)
		)
		""")
		conn.commit()
		conn.close()
	def ajouter_contact(self,contact):
		""" Fonction pour ajouter un nouveau contact"""
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
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
	
		self.editer_contact(contact)
	
		conn.commit()
		conn.close()
	
	#-----------------------------------------------
	def editer_contact(self,contact):
		""" Fonction pour editer un contact """
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
	
		# Modification du nom, prenom, groupe, et favori s'il a lieu
		cursor.execute("""
		UPDATE nom_prenom
			SET nom=:nom,prenom=:prenom,groupe=:groupe,favori=:favori
			WHERE id_contact=:id_contact
		""",contact)
	
		#-----------------------------------------------------------------------
		# Ajout, suppression et modification des numeros de telephone

		# On cherche combien de numeros sont stockes dans la base
		
		cursor.execute("""
		SELECT id_numero
		FROM numero
		WHERE id_contact =:id_contact
		""",contact)
		id = cursor.fetchall()
		remID = list(id)
	

		#Suppression	
		if (len(id) > len(contact["numero"])):
			for i in contact["id_numero"]:
				remID.remove((i,))
		
			for rem in remID:
				cursor.execute("""
				DELETE FROM numero
				WHERE id_numero =?
				""",rem)
	
		# Ajout
		elif (len(id) < len(contact["numero"])):
			for i in range(len(id),len(contact["numero"])):
				cursor.execute("""
				INSERT INTO numero(numero,libelle,id_contact) VALUES(
				?,
				?,
				?
				)
				""",(contact["numero"][i],contact["libelle_numero"][i],contact["id_contact"]))
	
		#Modification a toujours lieu sauf a la creation du premier numero
		if ("id_numero" in contact.keys()):
			for i in range(0,len(id)): 
				cursor.execute("""
				UPDATE numero
					SET numero=?,libelle=?
					WHERE id_numero=?
				""",(contact["numero"][i],contact["libelle_numero"][i],contact["id_numero"][i]))
	
		#---------------------------------------------------------------------------------------
		# Ajout, suppression et modification des mails
	
		# On cherche combien de mails sont stockes dans la base
		cursor.execute("""
		SELECT id_mail
		FROM mail
		WHERE id_contact =:id_contact
		""",contact)
		id = cursor.fetchall()
		remID = list(id)
	

		#Suppression	
		if (len(id) > len(contact["mail"])):
			for i in contact["id_mail"]:
				remID.remove((i,))
		
			for rem in remID:
				cursor.execute("""
				DELETE FROM mail
				WHERE id_mail =?
				""",rem)
	
		# Ajout
		elif (len(id) < len(contact["mail"])):
			for i in range(len(id),len(contact["mail"])):
				cursor.execute("""
				INSERT INTO mail(mail,libelle,id_contact) VALUES(
				?,
				?,
				?
				)
				""",(contact["mail"][i],contact["libelle_mail"][i],contact["id_contact"]))
	
		#Modification a toujours lieu sauf a la creation du premier mail
		if ("id_mail" in contact.keys()):
			for i in range(0,len(id)): 
				cursor.execute("""
				UPDATE mail
					SET mail=?,libelle=?
					WHERE id_mail=?
				""",(contact["mail"][i],contact["libelle_mail"][i],contact["id_mail"][i]))
	
		#---------------------------------------------------------------------------------------
		# Ajout, suppression et modification des adresses
	
		# On cherche combien de adresses sont stockes dans la base
		cursor.execute("""
		SELECT id_adresse
		FROM adresse
		WHERE id_contact =:id_contact
		""",contact)
		id = cursor.fetchall()
		remID = list(id)

		#Suppression	
		if (len(id) > len(contact["adresse"])):
			for i in contact["id_adresse"]:
				remID.remove((i,))
		
			for rem in remID:
				cursor.execute("""
				DELETE FROM adresse
				WHERE id_adresse =?
				""",rem)
	
		# Ajout
		elif (len(id) < len(contact["adresse"])):
			for i in range(len(id),len(contact["adresse"])):
				cursor.execute("""
				INSERT INTO adresse(adresse,libelle,id_contact) VALUES(
				?,
				?,
				?
				)
				""",(contact["adresse"][i],contact["libelle_adresse"][i],contact["id_contact"]))
	
		#Modification a toujours lieu sauf a la creation de la premiere adresse
		if ("id_adresse" in contact.keys()):
			for i in range(0,len(id)): 
				cursor.execute("""
				UPDATE adresse
					SET adresse=?,libelle=?
					WHERE id_adresse=?
				""",(contact["adresse"][i],contact["libelle_adresse"][i],contact["id_adresse"][i]))

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
	def rechercher_contact(self,recherche,groupes):
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		resultatFinal = []
		for groupe in groupes:
			resultat = []
			if len(recherche) != 0:
				if recherche[-1] == ' ':
					recherche = recherche[:-1]
			mots = recherche.split(' ')
			iterator=0
			tous=0
			if groupe == "":
				tous = 1
			for mot in mots:
				if iterator == 0 and len(mots) > 1:
					mot = '%' + mot
				else:
					mot = '%' + mot+ '%'
			
				# Recherche par nom
				cursor.execute("""
				SELECT np.id_contact,np.nom,np.prenom,np.groupe FROM nom_prenom np
				INNER JOIN numero nu
					on np.id_contact = nu.id_contact
				INNER JOIN mail ma
					on np.id_contact = ma.id_contact
				INNER JOIN adresse ad
					on np.id_contact = ad.id_contact
				WHERE (np.nom LIKE ? or np.prenom LIKE ? or nu.numero LIKE ?) and (np.groupe LIKE ? or ? = 1)
				ORDER BY np.nom,np.prenom
				""",(mot,mot,mot,groupe,tous))
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
			if len(resultat) > 0:
				resultatFinal= resultatFinal + resultat
		conn.close()
		return set(resultatFinal)
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
		if index == None:
			print("Pas d'index")
			return
		""" Fonction qui retourne toutes les informations d'une personne identifié par son id """
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		
		# Recuperation de nom_prenom
		cursor.execute("""
			SELECT id_contact
				, nom
				, prenom
				, groupe
				, favori
			FROM nom_prenom
			WHERE id_contact = ?
			""",(index,))
		data = cursor.fetchone()
		contact = {"id_contact":data[0],"nom":data[1],"prenom":data[2],"groupe":data[3],"favori":data[4]}
		
		# Recuperation des numeros
		cursor.execute("""
			SELECT id_contact
				, numero
				, libelle
				, id_numero
			FROM numero
			WHERE id_contact = ?
			""",(index,))
		data = cursor.fetchall()
		num =[]
		lib_num =[]
		id_num = []
		for d in data:
			num.append(d[1])
			lib_num.append(d[2])
			id_num.append(d[3])
			
		
		contact["numero"] = num
		contact["libelle_numero"] =lib_num
		contact["id_numero"] =id_num
		
		# Recuperation des mails
		cursor.execute("""
			SELECT id_contact
				, mail
				, libelle
				, id_mail
			FROM mail
			WHERE id_contact = ?
			""",(index,))
		data = cursor.fetchall()
		mai =[]
		lib_mai =[]
		id_mai =[]
		for d in data:
			mai.append(d[1])
			lib_mai.append(d[2])
			id_mai.append(d[3])
		
		contact["mail"] = mai
		contact["libelle_mail"] =lib_mai
		contact["id_mail"] = id_mai
		
		# Recuperation des adresses
		cursor.execute("""
			SELECT id_contact
				, adresse
				, libelle
				, id_adresse
			FROM adresse
			WHERE id_contact = ?
			""",(index,))
		data = cursor.fetchall()
		adr =[]
		lib_adr =[]
		id_adr = []
		for d in data:
			adr.append(d[1])
			lib_adr.append(d[2])
			id_adr.append(d[3])
		
		contact["adresse"] = adr
		contact["libelle_adresse"] = lib_adr
		contact["id_adresse"] = id_adr
		
		conn.close()
		return contact
		
	def ajouter_donnee(self,contact,typedonnee):
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		
		#Insertion du numero
		cursor.execute("""
		INSERT INTO ?(?,libelle,id_contact) VALUES(
			:donnee,
			:libelle_donnee,
			:id_contact
		)
		""",(typedonnee,typedonnee),contact)
		
		conn.commit()
		conn.close()
	def supprimer_donnee(self,contact,typedonnee):
		conn = sqlite3.connect('annuaire.db')
		cursor = conn.cursor()
		
		cursor.execute("""
		DELETE FROM ?
		WHERE id_contact =:id_contact 
		AND donnee =:donnee 
		AND libelle=:libelle_donnee
		""",(typedonnee,),contact)
		
		conn.commit()
		conn.close()
		
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
	a = rechercher_contact("did")
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
