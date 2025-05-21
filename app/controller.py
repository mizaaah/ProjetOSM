from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app.models import db, Utilisateur
from flask import current_app

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/utilisateurs')
def liste_utilisateurs():
    utilisateurs = Utilisateur.query.all()
    return render_template('admin.html', utilisateurs=utilisateurs)

@user_routes.route('/utilisateurs/<int:utilisateur_id>')
def afficher_utilisateur(utilisateur_id):
    utilisateur = Utilisateur.query.get_or_404(utilisateur_id)
    return render_template('details.html', utilisateur=utilisateur)

@user_routes.route('/utilisateurs/ajouter', methods=['GET', 'POST'])
def ajouter_utilisateur():
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form['mot_de_passe'])

        nouvel_utilisateur = Utilisateur(
            nom_utilisateur=request.form['nom_utilisateur'],
            email=request.form['email'],
            mot_de_passe=hashed_password
        )
        db.session.add(nouvel_utilisateur)
        db.session.commit()
        flash('Utilisateur ajouté avec succès')
        return redirect(url_for('user_routes.liste_utilisateurs'))

    return render_template('ajouter_utilisateur.html')

@user_routes.route('/utilisateurs/<int:utilisateur_id>/modifier', methods=['GET', 'POST'])
def modifier_utilisateur(utilisateur_id):
    utilisateur = Utilisateur.query.get_or_404(utilisateur_id)
    
    if request.method == 'POST':
        utilisateur.nom_utilisateur = request.form['nom_utilisateur']
        utilisateur.email = request.form['email']
        if request.form['mot_de_passe']:
            utilisateur.mot_de_passe = generate_password_hash(request.form['mot_de_passe'])

        db.session.commit()
        flash('Utilisateur modifié avec succès')
        return redirect(url_for('user_routes.liste_utilisateurs'))

    return render_template('modifier_utilisateur.html', utilisateur=utilisateur)

@user_routes.route('/utilisateurs/<int:utilisateur_id>/supprimer', methods=['POST'])
def supprimer_utilisateur(utilisateur_id):
    utilisateur = Utilisateur.query.get_or_404(utilisateur_id)
    db.session.delete(utilisateur)
    db.session.commit()
    flash('Utilisateur supprimé avec succès')
    return redirect(url_for('user_routes.liste_utilisateurs'))