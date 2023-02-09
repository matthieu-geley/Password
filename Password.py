import hashlib
import json

#mot de passe:
#doit contenir 8 caractères
#1 Majuscule
#1 minuscule
#1 chiffre
#1 caractère spécial (!, @, #, $, %, ^, &, *)



def longueur(mdp):
	if len(mdp) >= 8:
		return True


def chiffres(mdp):
	chiffre = "0123456789"
	for i in mdp:
		if i in chiffre:
			return True


def majuscule(mdp):
	majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in mdp:
		if i in majuscule:
			return True


def minuscule(mdp):
	minuscule = "abcdefghijklmnopqrstuvwxyz"
	for i in mdp:
		if i in minuscule:
			return True


def speciale(mdp):
	ponctuation = "!@#$%^&*"
	for i in mdp:
		if i in ponctuation:
			return True


def verification(mdp):
	i = 0
	for i in mdp:
		if longueur(mdp) == True and minuscule(mdp) == True and majuscule(mdp) == True and speciale(mdp) == True:
			print("le mot de passe est valide")


def motdepasse():
	verification = False
	while verification != True:
		motdepass = input("Insérez votre mot de passe :\n Il doit posséder 8 caractère,\n Il doit avoir une lettre majuscule & minuscule\n Il doit avoir un signe spéciale (!, @, #, $, %, ^, &, *).\n")
		mdp = str(motdepass)

		if longueur(mdp) == True and minuscule(mdp) == True and majuscule(mdp) == True and speciale(mdp) == True and chiffres(mdp) == True:
			verification = True
		else:
			print("le mot de passe ne respecte pas les exigences de sécuritées")
		if verification == True:
			Sha = hashlib.sha256(mdp.encode("UTF-8")).hexdigest()
			Jason = 'password.json'
			fichier = open("password.json", 'r')
			listeObj = {}
			listeObj.update({"Hash": Sha,})
			Jason_objet = json.dumps(listeObj, indent=4)
			with open("password.json", "a") as sortie:
				sortie.write(Jason_objet)


motdepasse()