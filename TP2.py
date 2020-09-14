#---------------------------------------------------------------------------------------
#------------------------------------ Exercice 1 ---------------------------------------
#---------------------------------------------------------------------------------------

tableau1 = [("Achille", 36),("Laura", 25),("Sylvain", 52),("Hugues", 25)]
#assert total_depense(tableau1) == 138, "True"

def total_depense(tab):
    """
    Prend en entrée un tableau de tuples (nom, dépense)
    Retourne la somme des dépenses
    """
    total = 0
    for _,valeur in tab:
        total += valeur
    return(total)

#print(total_depense(tableau1))

#---------------------------------------------------------------------------------------
#------------------------------------ Exercice 2 ---------------------------------------
#---------------------------------------------------------------------------------------

tableau2 = [("Achille", 36),("Laura", 25),("Laura", 12),("Sylvain", 52),("Hugues", 25),("Achille", 72),("Hugues", 13)]
#assert somme_personne(tableau2, "Hugues") == 38, "True"

def somme_personne(tab,prenom):
    """
    Prend en entrée un tableau de tuples (nom, dépense)
    Retourne la somme des dépenses associées à la valeur prénom
    """
    total = 0
    for nom,valeur in tab:
        if nom == prenom:
            total += valeur
    return(total)

#print(somme_personne(tableau2, "Laura"))

#---------------------------------------------------------------------------------------
#------------------------------------ Exercice 3 ---------------------------------------
#---------------------------------------------------------------------------------------

tableau3 = [("Achille", 36),("Laura", 25),("Laura", 12),("Sylvain", 52),("Hugues", 25),("Achille", 72),("Hugues", 13)]
#assert somme_par_personne(tableau3) == [("Achille", 108), ("Laura",37),("Sylvain",52),("Hugues",38)]

def somme_par_personne(tab):
    """
    Prend en entrée un tableau de tuples (nom, dépense)
    Retourne la somme des dépenses associées à chaque personne
    """
    res_liste = []
    liste_dict = dict(tab)
    for nom in liste_dict.keys():
        res_liste.append((nom,somme_personne(tab,nom)))
    return(res_liste)

#print(somme_par_personne(tableau3))

#---------------------------------------------------------------------------------------
#------------------------------------ Exercice 4 ---------------------------------------
#---------------------------------------------------------------------------------------

tableau4 = [("Achille", 36),("Laura", 25),("Laura", 12),("Sylvain", 52),("Hugues", 25),("Achille", 72),("Hugues", 13)]

def avoir_par_personne(tab):
    """
    Prend en entrée un tableau de tuples (nom, dépense)
    Retourne un tableau dans le lequel se trouve chaque personne et l'avoir qu'elle doit recevoir
    """
    avoir = somme_par_personne(tab)
    moyenne_depense = total_depense(avoir) / len(avoir)
    res_liste = []
    for personne in avoir:
        res_liste.append((personne[0], moyenne_depense - personne[1]))
    return(res_liste)

#print(avoir_par_personne(tableau4))