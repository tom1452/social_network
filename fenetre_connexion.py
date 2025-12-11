import tkinter as tk
from fenetre_inscription import fenetre_inscription

class fenetre_connexion(tk.Toplevel):
    def __init__(self, controleur):
        super().__init__()
        self.controleur = controleur
        self.controleur.lier_vue_connexion(self)
        self.creation_widget()
        
    def creation_widget(self):
        # Taille
        self.title("Connexion")
        self.geometry("300x300")

        # Création des Labels
        label_connexion = tk.Label(self, text = "Connexion")
        label_connexion.grid(row = 0, column=0, columnspan=2)
        label_user = tk.Label(self, text = "Identifiant :")
        label_user.grid(row = 1, column = 0)
        label_mdp = tk.Label(self, text = "Mot de passe :")
        label_mdp.grid(row = 2, column = 0)
        label_pas_de_compte = tk.Label(self, text = "Je n'ai pas de compte : ")
        label_pas_de_compte.grid(row = 4, column=0, columnspan=2)

        # Entrées pour le nom d'utilisateur et le mdp
        self.entre_user = tk.Entry(self)
        self.entre_user.grid(row = 1, column=1)
        self.entre_mdp = tk.Entry(self)
        self.entre_mdp.grid(row = 2, column=1)

        # Boutons d'action pour connexion et inscription
        self.bouton_connexion = tk.Button(self, text = "Connexion")
        self.bouton_connexion.grid(row = 3, column=0, columnspan=2)
        self.bouton_connexion.bind('<Button-1>', self.controleur.verif_connexion)
        
        self.bouton_inscription = tk.Button(self, text = "Inscription")
        self.bouton_inscription.grid(row = 5, column=0, columnspan=2 )
        self.bouton_inscription.bind('<Button-1>', self.ouverture_inscription)
        
        self.bouton_quitter = tk.Button(self, text = "Quitter l'application")
        self.bouton_quitter.grid(row=6, column=0, columnspan=2)
        self.bouton_quitter.bind('<Button-1>', self.quitter)
        
    def ouverture_inscription(self, event):
        self.withdraw()
        Fenetre_inscription = fenetre_inscription(self.controleur)
        self.wait_window(Fenetre_inscription)
        
    def quitter(self, event):
        self.destroy()
        self.controleur.page_principale.destroy()
        

