from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_utilisateur = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"<Utilisateur {self.nom_utilisateur}>"

class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<Categorie {self.nom}>"

class Etablissement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), nullable=False)
    categorie = db.relationship('Categorie', backref=db.backref('etablissements', lazy=True))

    def __repr__(self):
        return f"<Etablissement {self.nom}>"

class Avis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)
    etablissement_id = db.Column(db.Integer, db.ForeignKey('etablissement.id'), nullable=False)
    evaluation = db.Column(db.Integer, nullable=False)
    commentaire = db.Column(db.Text, nullable=True)
    date_creation = db.Column(db.DateTime, default=db.func.current_timestamp())

    utilisateur = db.relationship('Utilisateur', backref=db.backref('avis', lazy=True))
    etablissement = db.relationship('Etablissement', backref=db.backref('avis', lazy=True))

    def __repr__(self):
        return f"<Avis {self.evaluation} - {self.commentaire}>"

class Ville(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), unique=True, nullable=False)
    pays = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Ville {self.nom}, {self.pays}>"