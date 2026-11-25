import customtkinter as ctk
from typing import Any

class UserManagementScreen(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.parent = parent  # Référence à la fenêtre principale pour pouvoir revenir en arrière
        
        # Création des champs de saisie
        self.title_label = ctk.CTkLabel(self, text="Gestion des Utilisateurs", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)
        
        # Champ pour le nom de l'utilisateur
        self.name_entry_label = ctk.CTkLabel(self, text="Nom:")
        self.name_entry_label.pack(pady=5)
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.pack(pady=5)
        
        # Champ pour l'identifiant de l'utilisateur
        self.id_entry_label = ctk.CTkLabel(self, text="Identifiant:")
        self.id_entry_label.pack(pady=5)
        self.id_entry = ctk.CTkEntry(self)
        self.id_entry.pack(pady=5)
        
        # Bouton Ajouter
        self.add_button = ctk.CTkButton(self, text="Ajouter", command=self.add_user)
        self.add_button.pack(pady=10)
        
        # Bouton Retour
        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_to_main)
        self.back_button.pack(pady=5)
    
    def add_user(self):
        # Placeholder pour l'ajout d'un utilisateur
        pass
        
    def back_to_main(self):
        self.destroy()

        self.parent.main_frame.pack(
            pady=20,
            padx=30,
            fill="both",
            expand=True
        )