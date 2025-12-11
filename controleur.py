import json
import tkinter as tk
from tkinter import messagebox


class controleur():
    
    def __init__(self):
        self.donnees = self.lecture_donnees()
        
    def lecture_donnees(self):
        """ Lis et charge les données du json contenant les données du json"""
        with open("donnees.json", 'r') as f:
            data = json.load(f)
        return data
    
    def maj_json(self):
        """ Met à jour le json lorsque les données sur les profils sont modifiées"""
        with open("donnees.json", 'w') as f:
            json.dump(self.donnees, f, indent=4)
              
            
    # Fonctions pour lier chaque type de vue au controleur
    def lier_vue_principale(self, page_principale):
        self.page_principale = page_principale
    
    def lier_vue_connexion(self, page_connexion):
        self.page_connexion = page_connexion
        
    def lier_vue_inscription(self, page_inscription):
        self.page_inscription = page_inscription
        
    def lier_vue_parametre(self, page_parametre):
        self.page_parametre = page_parametre
        
    def lier_vue_bio(self, page_bio):
        self.page_bio = page_bio
        
    def lier_vue_notifs(self, page_notifs):
        self.page_notifs = page_notifs
        
    # Fonction pour nettoyer les widgets d'une page
    def nettoyage_page(self, page):
        for widget in page.winfo_children():
            widget.destroy()
        
    def verif_connexion(self, event):
        """ Permet de vérifier si les coordonnées rentrées sont bien renseignées
        dans le fichier de données.
        Si c'est le cas, la page du profil correspondant s'ouvre"""
        id_rentree = self.page_connexion.entre_user.get()
        mdp_rentre = self.page_connexion.entre_mdp.get()
        
        if id_rentree not in self.donnees.keys():
            messagebox.showerror("Erreur", "Cet identifiant n'existe pas")
        elif id_rentree in self.donnees.keys() and self.donnees[id_rentree]["Mdp"] != mdp_rentre:
            messagebox.showerror("Erreur", "Le mot de passe est incorect")
        elif id_rentree in self.donnees.keys() and self.donnees[id_rentree]["Mdp"] == mdp_rentre:
            self.page_connexion.destroy()
            self.userid_courant = id_rentree
            self.nettoyage_page(self.page_principale)
            self.page_principale.creation_widget()
            self.page_principale.deiconify()
        else:
            messagebox.showerror("Attention", "Veuillez vérifiez vos informations")
        
        
        
    def inscription(self, event):
        """ Si le nom d'utilisateur n'est pas utilisé, crée le profil avec
        les coordonnées renseignées et l'ajoute dans le fichier de données"""
        identifiant = self.page_inscription.entre_user_id.get()
        if identifiant in self.donnees:
            messagebox.showerror("Erreur", "Identifiant déjà utilisé")
        else:
            Mdp1 = self.page_inscription.entre_mdp.get()
            Mdp2 = self.page_inscription.entre_conf_mdp.get()
            if Mdp1 == Mdp2:
                pseudo = self.page_inscription.entre_pseudo.get()
                age = int(self.page_inscription.entre_age.get())
                confidentialite = self.page_inscription.entre_type_profil.get() == "Privé"
                self.donnees[identifiant] = {"Userid":identifiant, "Pseudonyme":pseudo, "Mdp":Mdp1, "Age":age, "Prive":confidentialite, "Notifications":[]}
                self.maj_json()
                messagebox.showinfo("Confirmation", "Votre compte a été créé avec succès")
                self.page_connexion.deiconify()
                self.page_inscription.destroy()
        
            elif Mdp1 != Mdp2:
                messagebox.showerror("Erreur", "Les deux mots de passe ne coïncident pas")
            
        
        
    def suppression_profil(self, event):
        """ Permet de supprimer le profil courant du fichier de données et
        renvoie à la page de connexion"""
        del self.donnees[self.userid_courant]
        del self.userid_courant
        self.maj_json()
        self.page_parametre.destroy()
        messagebox.showinfo("Information", "Votre compte a été supprimé avec succès")
        self.page_principale.ouverture_connexion()
        
        
    def maj_bio(self, event):
        """ Met à jour la biographie du profil courant dans le fichier de données
        et actualise la page du profil avec la nouvelle bio"""
        messagebox.showinfo("Information", "Biographie mise à jour")
        bio = self.page_bio.zone_bio.get("1.0", tk.END).rstrip("\n")
        self.donnees[self.userid_courant]["Biographie"] = bio
        self.maj_json()
        self.page_bio.destroy()
        self.nettoyage_page(self.page_parametre)
        self.page_parametre.creation_widget()
        self.page_parametre.deiconify()
     
        
    def demande_ajout_ami(self, event):
        """ Gère une demande d'ami dans la fenêtre principale en fonction du statut privé ou public du compte recherché"""
        ami_recherche = self.page_principale.entre_userid.get()
        
        if ami_recherche not in self.donnees:
            messagebox.showerror("Erreur", "Cet utilisateur n'existe pas")     
            
        elif self.donnees[ami_recherche]["Prive"]:
            if ami_recherche not in self.donnees[self.userid_courant].get("Demande envoye", []) and ami_recherche not in self.donnees[self.userid_courant].get("Amis suivis", []):
                self.donnees[self.userid_courant]["Demande envoye"] = self.donnees[self.userid_courant].get("Demande envoye", []) + [ami_recherche]
                self.donnees[ami_recherche]["Demande recu"] = self.donnees[ami_recherche].get("Demande recu", []) + [self.userid_courant]
                self.donnees[ami_recherche]["Notifications"].insert(0, [0, self.userid_courant])
                self.maj_json()
                messagebox.showinfo("Information", "Demande d'ami envoyée")
                    
            elif ami_recherche not in self.donnees[self.userid_courant].get("Demande envoye", []) and ami_recherche in self.donnees[self.userid_courant].get("Amis suivis", []):
                    messagebox.showerror("Erreur", "Vous suivez déjà cette personne")
                    
            elif ami_recherche in self.donnees[self.userid_courant].get("Demande envoye", []):
                    messagebox.showerror("Erreur", "Demande d'ami déjà envoyée")
                    
        else:
            if ami_recherche not in self.donnees[self.userid_courant].get("Amis suivis", []):
                self.donnees[self.userid_courant]["Amis suivis"] = self.donnees[self.userid_courant].get("Amis suivis", []) + [ami_recherche]
                self.donnees[ami_recherche]["Notifications"].insert(0, [1, self.userid_courant])
                self.maj_json()
                messagebox.showinfo("Information", "Ami(e) ajouté(e)")
            else:
                messagebox.showerror("Erreur", "Vous suivez déjà cette personne")
                    

    def accepter_demande(self, demandeur):
        if demandeur in self.donnees[self.userid_courant].get("Demande recu", []):
            self.donnees[self.userid_courant]["Demande recu"].remove(demandeur)
            self.donnees[demandeur]["Amis suivis"] = self.donnees[demandeur].get("Amis suivis",[]) + [self.userid_courant]
            self.donnees[demandeur]["Demande envoye"].remove(self.userid_courant)
            self.donnees[demandeur]["Notifications"] = self.donnees[demandeur].get("Notifications", []) + [[2, self.userid_courant]]
            self.maj_json()
            
            
 
    def ajout_retour(self, utilisateur):
        if utilisateur not in self.donnees[self.userid_courant].get("Amis suivis", []):
            if self.donnees[utilisateur]["Prive"]:
                self.donnees[self.userid_courant]["Demande envoye"] = self.donnees[self.userid_courant].get("Demande envoye", []) + [utilisateur]
                self.donnees[utilisateur]["Demande recu"] = self.donnees[utilisateur].get("Demande recu", []) + [self.userid_courant]
                self.donnees[utilisateur]["Notifications"].insert(0, [0, self.userid_courant])   
            else:
                self.donnees[self.userid_courant]["Amis suivis"] = self.donnees[self.userid_courant].get("Amis suivis", []) + [utilisateur]
                self.donnees[utilisateur]["Notifications"].insert(0, [1, self.userid_courant])       
        self.maj_json()
            
            
    def notif_vue(self, type_notif, utilisateur):
        self.donnees[self.userid_courant]["Notifications"].remove([type_notif, utilisateur])
        self.maj_json()
        
        
        
