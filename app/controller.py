from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app.models import db
from flask import current_app

routes = Blueprint('routes', __name__)

# === MODELE UTILISATEUR ===
class Utilisateur(db.Model):
    __tablename__ = 'utilisateurs'

    code_util = db.Column(db.String(64), primary_key=True)
    nom = db.Column(db.String(64), nullable=False)
    prenom = db.Column(db.String(64), nullable=False)
    nom_utilisateur = db.Column(db.String(64), unique=True, nullable=False)
    statut = db.Column(db.Boolean, nullable=False)
    mail_util = db.Column(db.String(64), unique=True, nullable=False)
    mdp = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"<Utilisateur '{self.nom_utilisateur}'>"

# === ROUTES FLASK CLASSIQUES ===

@routes.route('/utilisateurs')
def liste_utilisateurs():
    utilisateurs = Utilisateur.query.all()
    return render_template('utilisateurs/liste.html', utilisateurs=utilisateurs)

@routes.route('/utilisateurs/<code_util>')
def afficher_utilisateur(code_util):
    utilisateur = Utilisateur.query.get_or_404(code_util)
    return render_template('utilisateurs/detail.html', utilisateur=utilisateur)

@routes.route('/utilisateurs/ajouter', methods=['GET', 'POST'])
def ajouter_utilisateur():
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form['mdp'])

        nouvel_utilisateur = Utilisateur(
            code_util=request.form['code_util'],
            nom=request.form['nom'],
            prenom=request.form['prenom'],
            nom_utilisateur=request.form['nom_utilisateur'],
            statut=request.form.get('statut') == 'on',
            mail_util=request.form['mail_util'],
            mdp=hashed_password
        )
        db.session.add(nouvel_utilisateur)
        db.session.commit()
        flash('Utilisateur ajouté avec succès')
        return redirect(url_for('routes.liste_utilisateurs'))
    
    return render_template('utilisateurs/ajouter.html')

@routes.route('/utilisateurs/<code_util>/modifier', methods=['GET', 'POST'])
def modifier_utilisateur(code_util):
    utilisateur = Utilisateur.query.get_or_404(code_util)
    
    if request.method == 'POST':
        utilisateur.nom = request.form['nom']
        utilisateur.prenom = request.form['prenom']
        utilisateur.nom_utilisateur = request.form['nom_utilisateur']
        utilisateur.mail_util = request.form['mail_util']
        utilisateur.statut = request.form.get('statut') == 'on'
        if request.form['mdp']:
            utilisateur.mdp = generate_password_hash(request.form['mdp'])

        db.session.commit()
        flash('Utilisateur modifié avec succès')
        return redirect(url_for('routes.liste_utilisateurs'))

    return render_template('utilisateurs/modifier.html', utilisateur=utilisateur)

@routes.route('/utilisateurs/<code_util>/supprimer', methods=['POST'])
def supprimer_utilisateur(code_util):
    utilisateur = Utilisateur.query.get_or_404(code_util)
    db.session.delete(utilisateur)
    db.session.commit()
    flash('Utilisateur supprimé avec succès')
    return redirect(url_for('routes.liste_utilisateurs'))
