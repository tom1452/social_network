import tkinter as tk
from fenetre_bio import fenetre_bio

class fenetre_parametre(tk.Toplevel):
    def __init__(self, controleur):
        super().__init__()
        self.controleur = controleur 
        self.controleur.lier_vue_parametre(self)
        self.creation_widget()
        
    
    def creation_widget(self):
        # Bouton suppression profil
        self.bouton_supr_profil = tk.Button(self, text = "Supprimer mon profil")
        self.bouton_supr_profil.pack()
        self.bouton_supr_profil.bind('<Button-1>', self.controleur.suppression_profil)
        
        # bouton ajout ou modif de la biographie
        if self.controleur.donnees[self.controleur.userid_courant].get("Biographie", "") == "":
            self.bouton_ajout_bio = tk.Button(self, text = "Ajouter une biographie")
            self.bouton_ajout_bio.pack()
            self.bouton_ajout_bio.bind('<Button-1>', self.modif_bio)
        else:
            self.bouton_modif_bio = tk.Button(self, text = "Modifier la biographie")
            self.bouton_modif_bio.pack()
            self.bouton_modif_bio.bind('<Button-1>', self.modif_bio)
            
        # Bouton quitter les paramètres
        self.bouton_retour = tk.Button(self, text = "Retour")
        self.bouton_retour.pack()
        self.bouton_retour.bind('<Button-1>', self.quitter_parametre)
        
        
    def quitter_parametre(self, event):
        """ Quitte la page des paramètres et met à jour la page profil"""
        self.controleur.nettoyage_page(self.controleur.page_principale)
        self.controleur.page_principale.creation_widget()
        self.controleur.page_principale.deiconify()
        self.destroy()
        
    def modif_bio(self, event):
        """ Ouvre la page pour modifier la biographie """
        self.withdraw()
        Fenetre_bio = fenetre_bio(self.controleur)
        self.wait_window(Fenetre_bio)
        
        
