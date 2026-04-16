from random import randint

#Système de personnage

def creation_personnage(nom,classe):
    if classe == "Guerrier" :
        return {
        "nom" : nom,
        "classe" : "Guerrier",
        "pv" : 25,
        "pv_max" : 25,
        "force" : 16,
        "dexterite" : 12,
        "intelligence" : 8,
        "resistance" : 0
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
        "resistance" : 0
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
        "resistance" : 0
        }
    
# Création de personnages

joueur1 = creation_personnage("Thorfinn","Guerrier")
joueur2 = creation_personnage("Lux", "Mage")



# Fonction affichage personnage

def affichage_personnage(personnage) :

    print("=== FICHE PERSONNAGE ===")
    print("Nom : ", personnage["nom"])
    print("Classe : ", personnage["classe"])
    print("PV : ", personnage["pv"])
    print("Force : ", personnage["force"])
    print("Dextérité : ", personnage["dexterite"])
    print("Intelligence : ", personnage["intelligence"])

# Affichage des personnages

affichage_personnage(joueur1)
print("") # créer une ligne vide
affichage_personnage(joueur2)



# Fonction lancer de dés

def lancer_des(faces):
    resultat = randint(1,faces)
    print(f"Tu lances un d{faces}... résultat : {resultat}")
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

# Boucle de combat

def combat(combattant1,combattant2) :
    print(f"\n{'='*40}")
    # cette ligne permet de créer une séparation avec le symbole =
    print("Début du combat")
    print(f"{combattant1["nom"]} VS {combattant2["nom"]}")
    print(f"{'='*40}")
    tour = 1
    while combattant1["pv"] > 0 and combattant2["pv"] > 0 :
        print(f"\n--- Tour {tour} ---")
        print("Tu as le choix entre Attaquer, Se Défendre et Fuir. Que fais-tu ?")
        
        while True :
            choix_action = int(input("Tapes 1, 2 ou 3 : "))
            if choix_action  in (1, 2, 3) :
                break
            print("Choix invalide, tapes 1,2 ou 3 : ")
        if choix_action == 1 :
            attaque(combattant1,combattant2)
        elif choix_action == 2 :
            defense(combattant1,combattant2)
        elif choix_action == 3 :
            print(f"{combattant1["nom"]} déserte !")
            break
        

        combattant2["resistance"] = 0
        if combattant2["pv"] <= 0 :
            break
        print("Lux a le choix entre Attaquer, Se Défendre et Fuir. Que fait-elle ?")
        choix_action = int(input("Tapes 1, 2 ou 3 : "))
        if choix_action not in (1, 2, 3) :
            raise ValueError("Tu dois taper 1, 2 ou 3")
        elif choix_action == 1 :
            attaque(combattant2,combattant1)
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

thorfinn = creation_personnage("Thorfinn", "Guerrier")
lux = creation_personnage("Lux", "Mage")

nom_personnage = str(input("Choisis un nom de personnage : "))

caractere_autorise = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_éèçà"

if nom_personnage == "" :
    raise ValueError("Le nom est obligatoire ! ")
for car in nom_personnage :
    if car not in caractere_autorise :
        raise ValueError("Le nom ne doit pas contenir de caractères spéciaux ou de chiffres !")
classe = ["Guerrier", "Mage","Voleur"]

classe_personnage = str(input("Choisis une classe parmis Guerrier, Mage ou Voleur : "))

if classe_personnage not in classe :
    raise ValueError("Tu dois choisir parmis les classes disponibles, l'orthographe compte !")



combat(joueur1, joueur2)