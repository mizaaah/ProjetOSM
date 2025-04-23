CREATE TABLE Utilisateur (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_utilisateur TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    mot_de_passe TEXT NOT NULL
);

CREATE TABLE Categorie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL UNIQUE
);

CREATE TABLE Etablissement (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    adresse TEXT NOT NULL,
    ville TEXT NOT NULL,
    categorie_id INTEGER NOT NULL,
    FOREIGN KEY (categorie_id) REFERENCES Categorie(id)
);

CREATE TABLE Avis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utilisateur_id INTEGER NOT NULL,
    etablissement_id INTEGER NOT NULL,
    evaluation INTEGER NOT NULL,
    commentaire TEXT,
    date_creation DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (utilisateur_id) REFERENCES Utilisateur(id),
    FOREIGN KEY (etablissement_id) REFERENCES Etablissement(id)
);

CREATE TABLE Ville (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL UNIQUE,
    pays TEXT NOT NULL
);