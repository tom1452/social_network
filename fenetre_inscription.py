import tkinter as tk 
from tkinter import ttk

class fenetre_inscription(tk.Toplevel):
    
    def __init__(self, controleur):
        super().__init__()
        self.controleur = controleur
        self.controleur.lier_vue_inscription(self)
        self.creation_widget()
        
    def creation_widget(self):
        # Ajustement fenêtre
        self.title("Inscription")
        self.geometry("350x300")
        
        # Création des labels
        label_user_id = tk.Label(self, text = "Choisissez un identifiant")
        label_user_id.grid(row=0, column=0)
        
        label_pseudo = tk.Label(self, text = "Choisissez un pseudonyme")
        label_pseudo.grid(row=1, column=0)
        
        label_age = tk.Label(self, text = "Indiquez votre âge")
        label_age.grid(row=2, column=0)
        
        label_type_profil = tk.Label(self, text = "Choisissez le type de profil")
        label_type_profil.grid(row=3, column=0)
        
        label_mdp = tk.Label(self, text = "Définissez un mot de passe")
        label_mdp.grid(row = 4, column = 0, columnspan=2)
        
        label_conf_mdp = tk.Label(self, text = "Confirmez votre mot de passe")
        label_conf_mdp.grid(row = 6, column=0, columnspan=2)
        
        
        # Création des entrées
        self.entre_user_id = tk.Entry(self)
        self.entre_user_id.grid(row=0, column=1)
        
        self.entre_pseudo = tk.Entry(self)
        self.entre_pseudo.grid(row=1, column=1)
        
        self.entre_age = tk.Entry(self)
        self.entre_age.grid(row=2, column=1)
        
        self.entre_type_profil = ttk.Combobox(self, values=["Privé", "Public"], state = "readonly")
        self.entre_type_profil.grid(row=3, column=1)
        
        self.entre_mdp = tk.Entry(self)
        self.entre_mdp.grid(row=5, column=0, columnspan=2)
        
        self.entre_conf_mdp = tk.Entry(self)
        self.entre_conf_mdp.grid(row=7, column=0, columnspan=2)
        
        # Boutons
        self.bouton_conf = tk.Button(self, text = "S'inscrire")
        self.bouton_conf.grid(row=8, column=0)
        self.bouton_conf.bind('<Button-1>', self.controleur.inscription)
        
        self.bouton_retour = tk.Button(self, text = "Retour")
        self.bouton_retour.grid(row=8, column=1)
        self.bouton_retour.bind('<Button-1>', self.retour)

    def retour(self, event):
        self.controleur.page_connexion.deiconify()
        self.destroy()     
        
