import tkinter as tk
from tkinter import scrolledtext

class fenetre_notifs(tk.Toplevel):
    def __init__(self, controleur):
        super().__init__()
        self.controleur = controleur
        self.controleur.lier_vue_notifs(self)
        self.creation_widget()
        self.remplir_notifs()
        
    def creation_widget(self):
        self.title("Notifications")
        self.geometry("800x800")
        
        # Zone de notifs
        self.zone_notifs = scrolledtext.ScrolledText(self, width=10, height=10)
        self.zone_notifs.pack(fill=tk.BOTH, expand=True)
        
        # bouton retour
        self.bouton_validation = tk.Button(self, text = "Quitter")
        self.bouton_validation.pack(fill=tk.X)
        self.bouton_validation.bind('<Button-1>', self.quitter_notifs)
        
        
    def remplir_notifs(self):
        for widget in self.zone_notifs.winfo_children():
            widget.destroy()
        
        notifications = self.controleur.donnees[self.controleur.userid_courant]["Notifications"]

        for i, liste in enumerate(notifications):
            # Définition du type de notif et de l'utilsateur concerné
            [type_notif, user] = liste
            
            # Création d'un cadre pour chaque notif 
            cadre = tk.Frame(self.zone_notifs)
            cadre.pack(fill=tk.X)
            
            # Création du texte et du bouton qui seront changés après
            label = tk.Label(cadre, text="")
            label.pack(side=tk.LEFT, fill=tk.X)
            
            bouton = tk.Button(cadre, text = "")
            bouton.pack(side=tk.RIGHT)
            bouton.user = user
            bouton.label = label
            bouton.parent = cadre
            bouton.type_notif = type_notif
            
            if type_notif == 0: # Reception de demande pour un profil privé
            
                label.config(text= f"{user} a demandé à vous suivre")
                bouton.config(text="Accepter")
                bouton.bind('<Button-1>', self.accepter_demande_maj_visu)

            elif type_notif == 1: # Notif de suivi
                label.config(text = f"{user} a commencé à vous suivre")
                if user in self.controleur.donnees[self.controleur.userid_courant].get("Amis suivis",[]):
                    bouton.config(text = "Lu")
                    bouton.bind('<Button-1>', self.notif_vue_maj_visu)
                    
                else:
                    bouton.config(text="Ajouter en retour")
                    bouton.bind('<Button-1>', self.ajout_retour_maj_visu)
           
            elif type_notif == 2: # Notif pour dire qu'un profil privé a accepté notre deamnde
                label.config(text = f"{user} a accepté votre demande")
                bouton.config(text = "Lu")
                bouton.bind('<Button-1>', self.notif_vue_maj_visu)
                
            
            
    def accepter_demande_maj_visu(self,event):
        bouton = event.widget
        user = bouton.user
        self.controleur.accepter_demande(user)
        if user in self.controleur.donnees[self.controleur.userid_courant].get("Amis suivis", []):
            bouton.label.configure(text = f"Vous suivez déjà {user}")
            bouton.configure(text = "Lu")
            bouton.unbind('<Button-1>')
            bouton.bind('<Button-1>', self.notif_vue_maj_visu)
            
        else:
            bouton.label.configure(text = f"Ajouter {user} en retour")
            bouton.configure(text = "Ajouter")
            bouton.unbind('<Button-1>')
            bouton.bind('<Button-1>', self.ajout_retour_maj_visu)
            
            
    def ajout_retour_maj_visu(self, event):
        bouton = event.widget
        user = bouton.user
        self.controleur.ajout_retour(user)
        if self.controleur.donnees[user]["Prive"]:
            bouton.label.config(text = f"Vous avez envoyé une demande à {bouton.user}")
        else:
            bouton.label.config(text = f"Vous avez ajouté {bouton.user} en retour")
            
        bouton.config(text = "Lu")
        bouton.unbind('<Button-1>')
        bouton.bind('<Button-1>', self.notif_vue_maj_visu)
      
        
    def notif_vue_maj_visu(self, event):
        bouton = event.widget
        user = bouton.user
        type_notif = bouton.type_notif
        self.controleur.notif_vue(type_notif, user)
        bouton.label.destroy()
        bouton.parent.destroy()
        bouton.destroy()
        
    def quitter_notifs(self, event):
        self.controleur.page_principale.deiconify()
        self.destroy()
        

