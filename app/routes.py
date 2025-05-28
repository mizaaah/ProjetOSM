from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import generate_password_hash
from app.models import db, Utilisateur, Etablissement, Categorie, Avis

routes = Blueprint('routes', __name__)

# Pages classiques
@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/accueil')
def accueil():
    return render_template('accueil.html')

@routes.route('/admin')
def admin():
    utilisateurs = Utilisateur.query.all()
    return render_template('admin.html', utilisateurs=utilisateurs)

@routes.route('/map')
def map():
    categories = Categorie.query.all()
    return render_template('map.html', categories=categories)

# === API dynamique ===
@routes.route('/api/etablissements')
def api_etablissements():
    categorie_id = request.args.get('categorie_id')
    query = Etablissement.query
    if categorie_id:
        query = query.filter_by(categorie_id=categorie_id)
    etablissements = query.all()
    data = [{
        "id": e.id,
        "nom": e.nom,
        "adresse": e.adresse,
        "ville": e.ville,
        "latitude": e.latitude,
        "longitude": e.longitude
    } for e in etablissements]
    return jsonify(data)

# === Établissements ===
@routes.route('/etablissements/ajouter', methods=['GET', 'POST'])
def ajouter_etablissement():
    categories = Categorie.query.filter(Categorie.nom.in_(['Restaurant', 'Hôtel'])).all()
    if request.method == 'POST':
        etab = Etablissement(
            nom=request.form['nom'],
            adresse=request.form['adresse'],
            ville=request.form['ville'],
            latitude=request.form['latitude'],
            longitude=request.form['longitude'],
            categorie_id=request.form['categorie_id']
        )
        db.session.add(etab)
        db.session.commit()
        flash("Établissement ajouté avec succès.")
        return redirect(url_for('routes.map'))
    return render_template('ajouter_etablissement.html', categories=categories)

@routes.route('/etablissements/<int:id>/modifier', methods=['GET', 'POST'])
def modifier_etablissement(id):
    etab = Etablissement.query.get_or_404(id)
    categories = Categorie.query.filter(Categorie.nom.in_(['Restaurant', 'Hôtel'])).all()
    if request.method == 'POST':
        etab.nom = request.form['nom']
        etab.adresse = request.form['adresse']
        etab.ville = request.form['ville']
        etab.latitude = request.form['latitude']
        etab.longitude = request.form['longitude']
        etab.categorie_id = request.form['categorie_id']
        db.session.commit()
        flash("Établissement modifié.")
        return redirect(url_for('routes.map'))
    return render_template('modifier_etablissement.html', etablissement=etab, categories=categories)

@routes.route('/etablissements/<int:id>/supprimer', methods=['POST'])
def supprimer_etablissement(id):
    etab = Etablissement.query.get_or_404(id)
    db.session.delete(etab)
    db.session.commit()
    flash("Établissement supprimé.")
    return redirect(url_for('routes.map'))

# === Utilisateurs ===
@routes.route('/utilisateurs/ajouter', methods=['GET', 'POST'])
def ajouter_utilisateur():
    if request.method == 'POST':
        mdp = generate_password_hash(request.form['mdp'])
        user = Utilisateur(
            code_util=request.form['code_util'],
            nom=request.form['nom'],
            prenom=request.form['prenom'],
            nom_utilisateur=request.form['nom_utilisateur'],
            mail_util=request.form['mail_util'],
            mdp=mdp,
            statut=request.form.get('statut') == 'on'
        )
        db.session.add(user)
        db.session.commit()
        flash("Utilisateur ajouté.")
        return redirect(url_for('routes.admin'))
    return render_template('ajouter_utilisateur.html')

@routes.route('/utilisateurs/<code_util>/modifier', methods=['GET', 'POST'])
def modifier_utilisateur(code_util):
    user = Utilisateur.query.get_or_404(code_util)
    if request.method == 'POST':
        user.nom = request.form['nom']
        user.prenom = request.form['prenom']
        user.nom_utilisateur = request.form['nom_utilisateur']
        user.mail_util = request.form['mail_util']
        user.statut = request.form.get('statut') == 'on'
        if request.form['mdp']:
            user.mdp = generate_password_hash(request.form['mdp'])
        db.session.commit()
        flash("Utilisateur modifié.")
        return redirect(url_for('routes.admin'))
    return render_template('modifier_utilisateur.html', utilisateur=user)

@routes.route('/utilisateurs/<code_util>/supprimer', methods=['POST'])
def supprimer_utilisateur(code_util):
    user = Utilisateur.query.get_or_404(code_util)
    db.session.delete(user)
    db.session.commit()
    flash("Utilisateur supprimé.")
    return redirect(url_for('routes.admin'))

# === Avis ===
@routes.route('/avis/ajouter', methods=['GET', 'POST'])
def ajouter_avis():
    utilisateurs = Utilisateur.query.all()
    etablissements = Etablissement.query.all()
    if request.method == 'POST':
        avis = Avis(
            utilisateur_id=request.form['utilisateur_id'],
            etablissement_id=request.form['etablissement_id'],
            evaluation=request.form['evaluation'],
            commentaire=request.form['commentaire']
        )
        db.session.add(avis)
        db.session.commit()
        flash("Avis ajouté.")
        return redirect(url_for('routes.map'))
    return render_template('ajouter_avis.html', utilisateurs=utilisateurs, etablissements=etablissements)

@routes.route('/avis/<int:id>/modifier', methods=['GET', 'POST'])
def modifier_avis(id):
    avis = Avis.query.get_or_404(id)
    if request.method == 'POST':
        avis.evaluation = request.form['evaluation']
        avis.commentaire = request.form['commentaire']
        db.session.commit()
        flash("Avis modifié.")
        return redirect(url_for('routes.map'))
    return render_template('modifier_avis.html', avis=avis)

@routes.route('/avis/<int:id>/supprimer', methods=['POST'])
def supprimer_avis(id):
    avis = Avis.query.get_or_404(id)
    db.session.delete(avis)
    db.session.commit()
    flash("Avis supprimé.")
    return redirect(url_for('routes.map'))