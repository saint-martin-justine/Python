def foctionIndefini(**args):
#args permet de passer de multiples arguments et des arguments nommés à une fonction
  for i, j in args.items():
      print(i, j)
# items() dont le rôle est de récupérer les différentes paires de clefs : valeurs d’un dictionnaire
foctionIndefini(prenom= "Justine", nom= "Saint-Marrtin" , age=28 , ville="Marseille")

