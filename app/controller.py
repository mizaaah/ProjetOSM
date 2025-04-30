from app.models import Utilisateur, db

def ajouter_utilisateur(nom, email, mot_de_passe):
    """Ajoute un nouvel utilisateur à la base de données."""
    nouvel_utilisateur = Utilisateur(nom_utilisateur=nom, email=email, mot_de_passe=mot_de_passe)
    db.session.add(nouvel_utilisateur)
    db.session.commit()

def obtenir_tous_les_utilisateurs():
    """Récupère tous les utilisateurs de la base de données."""
    return Utilisateur.query.all()