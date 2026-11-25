import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class BookManagementScreen(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        
        # Création des champs de saisie
        self.title_label = ctk.CTkLabel(self, text="Gestion des Livres", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)
        
        # Champ pour le titre du livre
        self.title_entry_label = ctk.CTkLabel(self, text="Titre:")
        self.title_entry_label.pack(pady=5)
        self.title_entry = ctk.CTkEntry(self)
        self.title_entry.pack(pady=5)
        
        # Champ pour l'auteur du livre
        self.author_entry_label = ctk.CTkLabel(self, text="Auteur:")
        self.author_entry_label.pack(pady=5)
        self.author_entry = ctk.CTkEntry(self)
        self.author_entry.pack(pady=5)
        
        # Champ pour l'ISBN du livre
        self.isbn_entry_label = ctk.CTkLabel(self, text="ISBN:")
        self.isbn_entry_label.pack(pady=5)
        self.isbn_entry = ctk.CTkEntry(self)
        self.isbn_entry.pack(pady=5)
        
        # Bouton Ajouter
        self.add_button = ctk.CTkButton(self, text="Ajouter", command=self.add_book)
        self.add_button.pack(pady=10)
        
        # Bouton Retour
        self.back_button = ctk.CTkButton(self, text="Retour", command=self.back_to_main)
        self.back_button.pack(pady=5)
    
    def add_book(self):
        # Placeholder pour l'ajout d'un livre
        pass
        
    def back_to_main(self):
        self.destroy()
        self.parent.main_frame.pack(
            pady=20,
            padx=30,
            fill="both",
            expand=True
        )