annee = input ("Saisissez une année: )

try:
    annee = int(annee)
    assert annee>0
except ValueError:
    print ("Vous n'avez pas saisie de nombre.")
except AssertionError:
    print ("L'année saisie est inférieure ou égale à 0")

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 !=0):
    print ("L'année saisie est bissextile.")
else:
    print ("L'année saisie n'est pas bissextile.")

