from fenetre_principale import fenetre_principale
from controleur import controleur

Controleur = controleur()
Fenetre = fenetre_principale(Controleur)
Controleur.page_principale.mainloop()