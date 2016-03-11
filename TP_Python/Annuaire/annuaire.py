import pickle
import re

class Contact:
	def __init__(self,Nom,Prenom,Tel):
		self.Nom = Nom
		self.Prenom = Prenom
		self.Tel = Tel

class Annuaire : 
	def __init__(self):
		self.Liste = pickle.load(open("annuaire.p","rb"))
	def ajouterContact(self,Nom,Prenom,Tel):
		self.Liste.append(Contact(Nom,Prenom,Tel))
		pickle.dump(self.Liste,open("annuaire.p","wb"))
		print("Contact ajoute:")
		print("Nom: " + Nom)
		print("Prenom: " + Prenom)
		print("Tel: " + Tel)
		print()
	def supprimerContact(self,Nom,Prenom):
		for c in self.Liste:
			if(c.Nom == Nom and c.Prenom == Prenom):
				self.Liste.remove(c)
				pickle.dump(self.Liste,open("annuaire.p","wb"))
				print("Contact supprime")
				print()
				return
		print("Pas de contact a ce nom")
			
	def consulterContact(self,search):
		for c in self.Liste:
			if(re.search("(?i)"+search,c.Nom) or re.search("(?i)"+search,c.Prenom) or re.search("(?i)"+search,c.Tel)):
				print("Nom: " + c.Nom)
				print("Prenom: " + c.Prenom)
				print("Tel: " + c.Tel)
				print()
				return
		print("Pas de contact a ce nom")
		print()

		
Annu = Annuaire()
print("Bienvenue dans votre annuaire")
choix = input("Voulez vous ajouter, supprimer, consulter ou quitter? : ")
print()
while(choix != "quitter"):
	if (choix == "ajouter"):
		Nom  = input("Nom:")
		Prenom = input("Prenom:")
		Tel = input("Tel:")
		print()
		Annu.ajouterContact(Nom,Prenom,Tel)
	elif(choix == "supprimer"):
		Nom = input("Nom:")
		Prenom = input("Prenom:")
		print()
		Annu.supprimerContact(Nom,Prenom)
	elif(choix == "consulter"):
		search = input("Recherche: ")
		print()
		Annu.consulterContact(search)
	elif(choix == "quitter"):
			break
	else:
		print("Choix non valide")
		print()
	choix = input("Voulez vous ajouter, supprimer, consulter ou quitter? :") 
	print()