import customtkinter as ctk
import sys
from gui.book import BookManagementScreen

class LibrarySystem(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Système de Gestion de Bibliothèque")
        self.geometry("600x400")
        
        # Configuration de l'apparence
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")
        
        # Création du cadre principal
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=20, padx=30, fill="both", expand=True)
        
        # Titre
        title_label = ctk.CTkLabel(self.main_frame, text="Système de Gestion de Bibliothèque", font=("Arial", 24, "bold"))
        title_label.pack(pady=15)
        
        # Boutons du menu principal
        button_frame = ctk.CTkFrame(self.main_frame)
        button_frame.pack(fill="both", expand=True)
        
        self.book_button = ctk.CTkButton(button_frame, text="Gérer les livres", command=self.open_book_management)
        self.book_button.grid(row=0, column=0, padx=20, pady=10)
        
        self.user_button = ctk.CTkButton(button_frame, text="Gérer les utilisateurs", command=self.open_user_management)
        self.user_button.grid(row=1, column=0, padx=20, pady=10)
        
        self.borrow_button = ctk.CTkButton(button_frame, text="Effectuer des emprunts", command=self.open_borrow_management)
        self.borrow_button.grid(row=2, column=0, padx=20, pady=10)
        
        self.stats_button = ctk.CTkButton(button_frame, text="Afficher les statistiques", command=self.open_statistics)
        self.stats_button.grid(row=3, column=0, padx=20, pady=10)
        
        self.quit_button = ctk.CTkButton(button_frame, text="Quitter", fg_color=("red", "#ff4d4d"), command=self.quit_app)
        self.quit_button.grid(row=4, column=0, padx=20, pady=10)
        
        # Initialisation des variables d'état
        self.current_screen = None
        
    def open_book_management(self):
        self.main_frame.pack_forget()

        self.book_screen = BookManagementScreen(self)
        self.book_screen.pack(fill="both", expand=True)
        
    def open_user_management(self):
        # Placeholder pour ouvrir la gestion des utilisateurs
        pass
        
    def open_borrow_management(self):
        # Placeholder pour ouvrir la gestion des emprunts
        pass
        
    def open_statistics(self):
        # Placeholder pour ouvrir les statistiques
        pass
        
    def quit_app(self):
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    app = LibrarySystem()
    app.mainloop()