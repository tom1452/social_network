import tkinter as tk
from fenetre_connexion import fenetre_connexion
from fenetre_parametre import fenetre_parametre
from fenetre_notifs import fenetre_notifs


class fenetre_principale(tk.Tk):
    
    def __init__(self, controleur):
        super().__init__()
        self.controleur = controleur
        self.controleur.lier_vue_principale(self)
        self.ouverture_connexion()
        

    def creation_widget(self):
        """ Creéation de la page du profil"""
        # Format de la page
        self.title(f"Bienvenue {self.controleur.donnees[self.controleur.userid_courant]['Pseudonyme']}")
        self.geometry("700x700")
        
        # Affichage ou non de la biographie
        if self.controleur.donnees[self.controleur.userid_courant].get("Biographie", "") != "":
            label_bio = tk.Label(self, text = self.controleur.donnees[self.controleur.userid_courant]["Biographie"])
            label_bio.grid(row = 0, column=0)
            
        # Bouton paramètre
        self.bouton_parametres = tk.Button(self, text = "Paramètres")
        self.bouton_parametres.grid(row=1, column=0)
        self.bouton_parametres.bind('<Button-1>', self.ouverture_parametre)
        
        # Bouton déconnexion
        self.bouton_deco = tk.Button(self, text = "Déconnexion")
        self.bouton_deco.grid(row=1, column=1)
        self.bouton_deco.bind('<Button-1>', self.deconnexion)
        
        # Ajout d'ami
        label_ajout_ami = tk.Label(self, text = "Rechercher un ami par son identifiant")
        label_ajout_ami.grid(row=2, column=0)
        self.entre_userid = tk.Entry(self)
        self.entre_userid.grid(row=2, column=1)
        self.bouton_valider_recherche = tk.Button(self, text = "Ajouter")
        self.bouton_valider_recherche.grid(row=2, column=2)
        self.bouton_valider_recherche.bind('<Button-1>', self.controleur.demande_ajout_ami)
        
        # Bouton notifs 
        self.bouton_notifs = tk.Button(self, text = "Notifications")
        self.bouton_notifs.grid(row=3, column=0)
        self.bouton_notifs.bind('<Button-1>', self.ouverture_notifs)
        
    def ouverture_connexion(self):
        """ Cache la fenêtre principale et ouvre la page de connexion"""
        self.withdraw()
        Fenetre_connexion = fenetre_connexion(self.controleur)
        self.wait_window(Fenetre_connexion)
        
    def ouverture_parametre(self, event):
        """ Ouvre la page des paramètre"""
        self.withdraw()
        Fenetre_parametre = fenetre_parametre(self.controleur)
        self.wait_window(Fenetre_parametre)
        
    def ouverture_notifs(self, event):
        """ Cache la fenêtre principale et ouvre la page de notifs"""
        self.withdraw()
        Fenetre_notifs = fenetre_notifs(self.controleur)
        self.wait_window(Fenetre_notifs)
        
    def deconnexion(self, event):
        """ Permet de changer de profil courant """
        self.ouverture_connexion()
        
    
        
