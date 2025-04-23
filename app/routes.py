from flask import Blueprint, render_template, request
from app.models import db, Utilisateur, Etablissement, Avis, Ville, Categorie

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/accueil')
def accueil():
    villes = Ville.query.all()
    return render_template('accueil.html', villes=villes)

@routes.route('/admin')
def admin():
    utilisateurs = Utilisateur.query.all()
    etablissements = Etablissement.query.all()
    return render_template('admin.html', utilisateurs=utilisateurs, etablissements=etablissements)