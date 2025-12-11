import tkinter as tk
from tkinter import scrolledtext

class fenetre_bio(tk.Toplevel):
    def __init__(self, controleur):
        super().__init__()
        self.controleur = controleur
        self.controleur.lier_vue_bio(self)
        self.creation_widget()
        
    def creation_widget(self):
        # Format de fenêtre
        self.title("Biographie")
        self.geometry("300x300")
        
        # Zone pour la bio
        self.zone_bio = scrolledtext.ScrolledText(self, width=10, height=10)
        self.zone_bio.pack(fill=tk.BOTH, expand=True)
        self.zone_bio.insert("1.0", self.controleur.donnees[self.controleur.userid_courant].get("Biographie",""))
                             
                             
        # bouton validation
        self.bouton_validation = tk.Button(self, text = "Valider")
        self.bouton_validation.pack(fill=tk.X)
        self.bouton_validation.bind('<Button-1>', self.controleur.maj_bio)
        
