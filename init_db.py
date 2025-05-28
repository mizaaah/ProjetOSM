from app import create_app, db
from app.models import Categorie

app = create_app()

def init_database():
    with app.app_context():
        print("Création des tables...")
        #db.drop_all()
        db.create_all()

        print("Ajout des catégories par défaut...")
        db.session.add_all([
            Categorie(nom="Restaurant"),
            Categorie(nom="Hôtel")
        ])
        db.session.commit()
        print("Base de données initialisée.")

if __name__ == "__main__":
    init_database()
