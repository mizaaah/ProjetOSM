from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'
    code_util = db.Column(db.String(64), primary_key=True)
    nom = db.Column(db.String(64), nullable=False)
    prenom = db.Column(db.String(64), nullable=False)
    nom_utilisateur = db.Column(db.String(64), unique=True, nullable=False)
    mail_util = db.Column(db.String(120), unique=True, nullable=False)
    mdp = db.Column(db.String(256), nullable=False)
    statut = db.Column(db.Boolean, default=True)

    avis = db.relationship('Avis', back_populates='utilisateur', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Utilisateur {self.nom_utilisateur}>"

class Categorie(db.Model):
    __tablename__ = 'categorie'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), unique=True, nullable=False)

    etablissements = db.relationship('Etablissement', back_populates='categorie', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Categorie {self.nom}>"

class Etablissement(db.Model):
    __tablename__ = 'etablissement'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), nullable=False)

    categorie = db.relationship('Categorie', back_populates='etablissements')
    avis = db.relationship('Avis', back_populates='etablissement', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Etablissement {self.nom}>"

class Avis(db.Model):
    __tablename__ = 'avis'
    id = db.Column(db.Integer, primary_key=True)
    utilisateur_id = db.Column(db.String(64), db.ForeignKey('utilisateur.code_util'), nullable=False)
    etablissement_id = db.Column(db.Integer, db.ForeignKey('etablissement.id'), nullable=False)
    evaluation = db.Column(db.Integer, nullable=False)
    commentaire = db.Column(db.Text, nullable=True)
    date_creation = db.Column(db.DateTime, default=db.func.current_timestamp())

    utilisateur = db.relationship('Utilisateur', back_populates='avis')
    etablissement = db.relationship('Etablissement', back_populates='avis')

    def __repr__(self):
        return f"<Avis {self.evaluation}/5 - {self.commentaire}>"

class Ville(db.Model):
    __tablename__ = 'ville'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), unique=True, nullable=False)
    pays = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Ville {self.nom}, {self.pays}>"