from random import*

#Système de personnage

def creation_personnage(nom,classe,type):
    if type == "Joueur" :
        if classe == "Guerrier" :
            return {
            "nom" : nom,
            "classe" : "Guerrier",
            "pv" : 25,
            "pv_max" : 25,
            "force" : 16,
            "dexterite" : 12,
            "intelligence" : 8,
            "resistance" : 0,
            "niveau" : 1,
            "experience" : 0,
            "inventaire" : {}
            }
        elif classe == "Mage" :
            return {
            "nom" : nom,
            "classe" : "Mage",
            "pv" : 12,
            "pv_max" : 12,
            "force" : 8,
            "dexterite" : 10,
            "intelligence" : 18,
            "resistance" : 0,
            "niveau" : 1,
            "experience" : 0,
            "inventaire" : {}
            }
        elif classe == "Voleur" :
            return {
            "nom" : nom,
            "classe" : "Voleur",
            "pv" : 16,
            "pv_max" : 16,
            "force" : 10,
            "dexterite" : 18,
            "intelligence" : 12,
            "resistance" : 0,
            "niveau" : 1,
            "experience" : 0,
            "inventaire" : {}
            }
    elif type == "Monstre" :
        if classe == "Guerrier" :
            return {
            "nom" : nom,
            "classe" : "Guerrier",
            "pv" : 18,
            "pv_max" : 18,
            "force" : 12,
            "dexterite" : 9,
            "intelligence" : 6,
            "resistance" : 0,
            "niveau" : 1,
            "experience" : 0
            }
        elif classe == "Mage" :
            return {
            "nom" : nom,
            "classe" : "Mage",
            "pv" : 9,
            "pv_max" : 9,
            "force" : 6,
            "dexterite" : 7,
            "intelligence" : 13,
            "resistance" : 0,
            "niveau" : 1,
            "experience" : 0
            }
        elif classe == "Voleur" :
            return {
            "nom" : nom,
            "classe" : "Voleur",
            "pv" : 12,
            "pv_max" : 12,
            "force" : 7,
            "dexterite" : 13,
            "intelligence" : 9,
            "resistance" : 0,
            "niveau" : 1,
            "experience" : 0
            }

    

    
# Création de personnages

joueur1 = creation_personnage("Thorfinn","Guerrier","Joueur")
monstre = [creation_personnage("Gobelin","Voleur","Monstre"),creation_personnage("Troll","Guerrier","Monstre"),creation_personnage("Nécromancien","Mage","Monstre")]



# Fonction affichage personnage

def affichage_personnage(personnage) :

    print("=== FICHE PERSONNAGE ===")
    print("Nom : ", personnage["nom"])
    print("Classe : ", personnage["classe"])
    print("Niveau : ", personnage["niveau"])
    print("PV : ", personnage["pv"])
    print("Force : ", personnage["force"])
    print("Dextérité : ", personnage["dexterite"])
    print("Intelligence : ", personnage["intelligence"])


# Affichage des personnages

affichage_personnage(joueur1)
print("") # créer une ligne vide
for mobs in monstre :
    affichage_personnage(mobs)
    print("")

# Fonctions barre de vie

def barre_de_vie(joueur) :
    cases_pleines = int((joueur["pv"]/joueur["pv_max"])*10)
    barre = "🟩" * cases_pleines + "🟥" *(10 - cases_pleines)
    pourcentage = int((joueur["pv"]/joueur["pv_max"])*100)

    if pourcentage > 60 :
        coeur = "❤️"
    elif pourcentage > 30 :
        coeur = "🧡"
    else :
        coeur = "💔"

    print(coeur, f"{joueur["nom"]}", barre, pourcentage,"%")

# Fonction lancer de dés

def lancer_des(faces):
    resultat = randint(1,faces)
    print(f"Lancé de d{faces}... résultat : {resultat}")
    return resultat

# Fonctions calcul de dégats en fonction de la force

def calculer_modificateur(stats) :
    return (stats - 10)//2

# Fonctions combat

def attaque(attaquant,defenseur) :
    print(f"\n{attaquant['nom']} attaque {defenseur['nom']} !")
    # \n permet ici de faire un saut de ligne
    jet_attaque = lancer_des(20)

    if jet_attaque >= 10 :
        degats = lancer_des(6) + calculer_modificateur(attaquant['force'])
        if degats > defenseur["resistance"] : 
            defenseur["pv"] -= degats
            print(f"Touché ! {defenseur["nom"]} perd {degats} PV")
        elif degats <= defenseur["resistance"] :
            print(f"Dommage, {defenseur['nom']} bloque l'attaque de {attaquant['nom']}")
    else :
        print("Raté, l'attaque ne touche pas")

# Fonctions defense

def defense(defenseur,attaquant) :
    print(f"\n{defenseur['nom']} se défend de la prochaine attaque de {attaquant['nom']} !")
    # \n permet ici de faire un saut de ligne
    jet_defense = lancer_des(20)

    if jet_defense >= 10 :
        resistance = lancer_des(6) + calculer_modificateur(defenseur['dexterite'])
        defenseur["resistance"] = resistance
        print(f"Réussi ! {defenseur["nom"]} gagne {resistance} de résistence pour la prochaine attaque")
    else :
        print("Raté, la défense ne marchera pas.")

# # Fonctions soins

def soin(defenseur) :
    print(f"\n{defenseur["nom"]} essaie de se soigner")
    jet_soin = lancer_des(20)

    if jet_soin >= 10 :
        soin = lancer_des(6) + calculer_modificateur(defenseur['intelligence'])
        defenseur["pv"] = min(defenseur["pv"] + soin, defenseur["pv_max"])
        print(f"Réussi ! {defenseur["nom"]} gagne {soin} PV")
    else :
        print("Raté, le soin ne marchera pas.")

# Fonctions sort

def sort(attaquant, defenseur) :
    if attaquant["classe"] != "Mage" :
        print("Attention, seul les mages peuvent lancer des sorts !")
        return
    print(f"\n {attaquant["nom"]} lance un sort sur {defenseur["nom"]}")
    jet_sort = lancer_des(20)

    if jet_sort >= 8 :
        sort = lancer_des(6) + calculer_modificateur(attaquant["intelligence"])
        defenseur["pv"] -= sort
        print(f"Touché ! {defenseur["nom"]} perd {sort} PV")
    else :
        print("Raté l'attaque ne touche pas ! ")

# Fonction potion

def potion(defenseur) :
    # Vérifie si le joueur a des potions
    if defenseur["inventaire"].get("Potion de soin", 0) > 0:
        soin = lancer_des(6) + 2
        defenseur["pv"] = min(defenseur["pv"] + soin, defenseur["pv_max"])
        defenseur["inventaire"]["Potion de soin"] -= 1

        # Supprime l'objet si quantité = 0
        if defenseur["inventaire"]["Potion de soin"] == 0:
            del defenseur["inventaire"]["Potion de soin"]
        print("Tu bois une potion de soin et récupères", soin,"PV" )
    else :
        print("Tu n'as pas de potion de soin")

# Fonctions ramassage d'objets

def rammasage_objet(joueur, objet) :
    if objet not in joueur["inventaire"] :
        joueur["inventaire"][objet] = 1
    else :
        joueur["inventaire"][objet] += 1
    print("Tu as rammassé", objet, " !")


# Fonctions expérience

def gain_experience(joueur, xp) :
    joueur["experience"] += xp
    print(f"Tu gagnes", xp, f"XP ! (Total : {joueur["experience"]} XP)")

    if joueur["experience"] >= joueur["niveau"]*100 :
        joueur["niveau"] += 1
        joueur["pv_max"] += 5
        joueur["force"] += 1 
        joueur["pv"] = joueur["pv_max"]
        print("Félicitations, tu as un gagné un niveau ! Tes stats augmentent.")
        print("Tu as récupéré tous tes PV !")


# Fonctions de combat

def combat(combattant1,combattant2) :
    print(f"\n{'='*40}")
    # cette ligne permet de créer une séparation avec le symbole =
    print("Début du combat")
    print(f"{combattant1["nom"]} VS {combattant2["nom"]}")
    print(f"{'='*40}")

    tour = 1

    while combattant1["pv"] > 0 and combattant2["pv"] > 0 :
        print(f"\n--- Tour {tour} ---")
        barre_de_vie(combattant1)
        barre_de_vie(combattant2)

        # Menu selon la classe du joueur

        print("Quelle action souhaites-tu faire ?")

        if joueur["classe"] == "Mage" :
            print("1 Attaquer")
            print("2 Se soigner")
            print("3 Lancer un sort")
            print("4 Utiliser une potion")
            print("5 Fuir")
            options_valides = (1, 2, 3, 4, 5)
        else :
            print("1 Attaquer")
            print("2 Bloquer")
            print("3 Utiliser une potion")
            print("4 Fuir")
            options_valides = (1, 2, 3, 4)


        if combattant1["pv"] <= 0 :
            return False
        
        while True :
            try :
                choix_action = int(input("Fais ton choix : "))
                if choix_action in options_valides :
                    break
                print("Choix invalide ! ")
            except ValueError :
                print("Tapes un chiffre !")

        if joueur["classe"] == "Guerrier" :
            if choix_action == 1 :
                attaque(combattant1,combattant2)
            elif choix_action == 2 :
                defense(combattant1,combattant2)
            elif choix_action == 3 :
                potion(combattant1)
            elif choix_action == 4 :
                print(f"{combattant1["nom"]} déserte !")
                return False
        elif joueur["classe"] == "Mage" :
            if choix_action == 1 :
                attaque(combattant1,combattant2)
            elif choix_action == 2 :
                soin(combattant1)
            elif choix_action == 3 :
                sort(combattant1, combattant2)
            elif choix_action == 4 : 
                potion(combattant1)
            elif choix_action == 5 :
                print(f"{combattant1["nom"]} déserte !")
                return False
        elif joueur["classe"] == "Voleur" :
            if choix_action == 1 :
                attaque(combattant1,combattant2)
            elif choix_action == 2 :
                defense(combattant1,combattant2)
            elif choix_action == 3 :
                potion(combattant1)
            elif choix_action == 4 :
                print(f"{combattant1["nom"]} déserte !")
                return False
        

        combattant2["resistance"] = 0
        if combattant2["pv"] <= 0 :
            return True
        print(f"\n{combattant2["nom"]} a le choix entre Attaquer, Se Défendre et Fuir. Que fera-t-il ?")
        if combattant2["pv"] < 0.3 * combattant2["pv_max"] :
            choix_action = choice([1,2,2,2])
        elif combattant2["pv"] < 0.6 * combattant2["pv_max"] :
            choix_action = choice([1,1,1,2])
        else :
            choix_action = 1

        if choix_action == 1 :
            if combattant2["classe"] == "Mage" :
                sort(combattant2,combattant1)
            else :
                attaque(combattant2, combattant1)
        elif choix_action == 2 :
            defense(combattant2,combattant1)
        elif choix_action == 3 :
            print(f"{combattant2["nom"]} déserte !")
            break
        combattant1["resistance"] = 0
        tour += 1

    print(f"\n{"="*40}")
    if combattant1["pv"] <= 0 :
        print(f"{combattant2['nom']} remporte le combat !")
    elif combattant2["pv"] <= 0 :
        print(f"{combattant1["nom"]} remporte le combat !")
    print(f"{"="*40}")

# Fonctions aventure

def aventure(joueur) :
    monstre = [creation_personnage("Gobelin","Voleur","Monstre"),creation_personnage("Troll","Guerrier","Monstre"),creation_personnage("Nécromancien","Mage","Monstre")]
    gain_xp = [50,75,150]
    inventaire = {}
    butin = ["Potion de soin", "Talisman de force", "Potion de soin"]

    for i, mobs in enumerate(monstre) :
        print(f"{"🌑"*20}")
        print(f"Un {mobs["nom"]} apparaît ! ")
        print(f"{"🌑"*20}")

        victoire = combat(joueur,mobs)

        if not victoire :
            print("Fin de l'aventure")
            return

        gain_experience(joueur, gain_xp[i])
        rammasage_objet(joueur, butin[i])

    print(f"\n{"="*40}")
    print("Félicitation !")
    print(f"Tu as traversé The Hollow Realm et vaincu tous les ennemis !!!")
    print(f"\n{"="*40}")

# Début de l'aventure

print("=" * 40)
print("Bienvenue dans The Hollow Realm ! ")
print("=" * 40)

caractere_autorise = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_éèçà"

while True:
    nom = input("\n Entre le nom de ton personnage : ")
    if nom == "" :
        print("Ton personnage doit obligatoirement avoir un nom ! ")
    elif any(c not in caractere_autorise for c in nom) :
        print("Pas de chiffres ni de caractères spéciaux !")
    else :
        break

classe = ["Guerrier", "Mage","Voleur"]

while True :
    classe_personnage = str(input("Choisis une classe parmis Guerrier, Mage ou Voleur : "))
    if classe_personnage not in classe :
        print("Attentier l'orthographe compte !")
    else :
        break


joueur = creation_personnage(nom, classe_personnage,"Joueur")
affichage_personnage(joueur)
input("\n Appuie sur Entrée pour commencer l'aventure ...")
aventure(joueur)