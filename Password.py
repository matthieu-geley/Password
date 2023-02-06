#mot de passe:
#doit contenir 8 caractères
#1 Majuscule
#1 minuscule
#1 chiffre
#1 caractère spécial (!, @, #, $, %, ^, &, *)

def longueur(mdp):
	if len(mdp) >= 8:
		return True
	else:
		return "Le mot de passe est trop court"

def chiffres(mdp):
	chiffre = "0123456789"
	for i in mdp:
		if i in chiffre:
			return True
		else:
			return "Il manque un chiffre"

def majuscule(mdp):
	majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in mdp:
		if i in majuscule:
			return True
		else:
			return "Il manque une majuscule"

def minuscule(mdp):
	minuscule = "abcdefghijklmnopqrstuvwxyz"
	for i in mdp:
		if i in minuscule:
			return True
		else:
			return "Il manque une minuscule"

def speciale(mdp):
	ponctuation = "!@#$%^&*"
	for i in mdp:
		if i in ponctuation:
			return True
		else:
			return "Il manque un caractère spéciale"

def motdepasse():
	motdepass = input("Insérez votre mot de passe :\n Il doit posséder 8 caractère,\n Il doit avoir une lettre majuscule & minuscule\n Il doit avoir un signe spéciale (!, @, #, $, %, ^, &, *).\n")
	mdp = str(motdepass)
	while True:
		if longueur(mdp) == 1:
			print("il y a asser de caractères")
		else:
			print(longueur(mdp))
		if minuscule(mdp) == 1:
			print("il y a une minuscule")
			break
		else:
			print(minuscule(mdp))
		if majuscule(mdp) == 1:
			print("il y a une majuscule")
		else:
			print(majuscule(mdp))
			break
		if speciale(mdp) == 1:
			print("le mot de passe est bon")
		else:
			print(speciale(mdp))
			break
		if chiffres(mdp) == 1:
			print("il y a un chiffre")
		else:
			print(chiffres(mdp))
			break

motdepasse()