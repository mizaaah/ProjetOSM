from app import create_app, db
from app.models import Etablissement, Categorie

app = create_app()

etablissements_data = [
    # --- RESTAURANTS ---
    ("Le Meurice", "228 Rue de Rivoli", "Paris", 48.8656, 2.3285, "Restaurant"),
    ("La Table d'Eugène", "18 Rue Eugène Sue", "Paris", 48.8925, 2.3446, "Restaurant"),
    ("La Petite Maison", "11 Rue Saint-François de Paule", "Nice", 43.6954, 7.2743, "Restaurant"),
    ("L'Auberge du Pont de Collonges", "40 Quai de la Plage", "Collonges-au-Mont-d'Or", 45.8193, 4.8309, "Restaurant"),
    ("L'Assiette Champenoise", "40 Avenue Paul Vaillant", "Reims", 49.2481, 4.0012, "Restaurant"),
    ("Le Bistrot Paul Bert", "18 Rue Paul Bert", "Paris", 48.8510, 2.3850, "Restaurant"),
    ("Septime", "80 Rue de Charonne", "Paris", 48.8530, 2.3869, "Restaurant"),
    ("Les Apothicaires", "23 Rue de Sèze", "Lyon", 45.7640, 4.8441, "Restaurant"),
    ("Le Jardin des Plumes", "1 Rue du Milieu", "Giverny", 49.0757, 1.5337, "Restaurant"),
    ("Le Vieux Logis", "24510 Trémolat", "Trémolat", 44.8669, 0.8365, "Restaurant"),
    ("L’Arpège", "84 Rue de Varenne", "Paris", 48.8536, 2.3165, "Restaurant"),
    ("Maison Troisgros", "Route de Villerest", "Ouches", 46.0423, 4.0205, "Restaurant"),
    ("La Mare aux Oiseaux", "223 rue du Chef de l'Ile", "Saint-Joachim", 47.3981, -2.1865, "Restaurant"),
    ("La Grenouillère", "19 Rue de la Grenouillère", "Montreuil", 50.4645, 1.7713, "Restaurant"),
    ("Le Gindreau", "Le Bourg", "Saint-Médard", 44.5791, 1.4043, "Restaurant"),
    ("Le Pré Catelan", "Bois de Boulogne", "Paris", 48.8665, 2.2524, "Restaurant"),
    ("Le Grand Véfour", "17 Rue de Beaujolais", "Paris", 48.8669, 2.3361, "Restaurant"),
    ("Michel Sarran", "21 Boulevard Armand Duportal", "Toulouse", 43.6080, 1.4386, "Restaurant"),
    ("La Co(o)rniche", "46 Avenue Louis Gaume", "Pyla-sur-Mer", 44.6262, -1.2083, "Restaurant"),
    ("Chez Fonfon", "140 Rue du Vallon des Auffes", "Marseille", 43.2832, 5.3502, "Restaurant"),
    ("Chez Janou", "2 Rue Roger Verlomme", "Paris", 48.8575, 2.3652, "Restaurant"),
    ("Le Petit Nice", "Anse de Maldormé", "Marseille", 43.2780, 5.3493, "Restaurant"),
    ("Pierre Gagnaire", "6 Rue Balzac", "Paris", 48.8735, 2.3017, "Restaurant"),
    ("Le Chateaubriand", "129 Avenue Parmentier", "Paris", 48.8677, 2.3747, "Restaurant"),
    ("Le Panier", "24 Rue du Panier", "Marseille", 43.3001, 5.3705, "Restaurant"),

    # --- HOTELS ---
    ("Hôtel Negresco", "37 Promenade des Anglais", "Nice", 43.6950, 7.2653, "Hôtel"),
    ("Hôtel de Crillon", "10 Place de la Concorde", "Paris", 48.8688, 2.3210, "Hôtel"),
    ("Le Chabichou", "Rue des Chenus", "Courchevel", 45.4141, 6.6325, "Hôtel"),
    ("InterContinental Marseille", "1 Place Daviel", "Marseille", 43.2964, 5.3695, "Hôtel"),
    ("Hôtel Barrière Le Normandy", "38 Rue Jean Mermoz", "Deauville", 49.3593, 0.0747, "Hôtel"),
    ("Hôtel Lutetia", "45 Boulevard Raspail", "Paris", 48.8519, 2.3243, "Hôtel"),
    ("Hôtel Royal", "13 Avenue des Mateirons", "Évian-les-Bains", 46.4068, 6.5798, "Hôtel"),
    ("Hôtel Martinez", "73 Boulevard de la Croisette", "Cannes", 43.5514, 7.0267, "Hôtel"),
    ("Le Bristol", "112 Rue du Faubourg Saint-Honoré", "Paris", 48.8725, 2.3143, "Hôtel"),
    ("Grand Hôtel du Palais Royal", "4 Rue de Valois", "Paris", 48.8642, 2.3366, "Hôtel"),
    ("Hôtel du Cap-Eden-Roc", "Boulevard JF Kennedy", "Antibes", 43.5522, 7.1301, "Hôtel"),
    ("Le Roch Hotel & Spa", "28 Rue Saint-Roch", "Paris", 48.8663, 2.3321, "Hôtel"),
    ("Hôtel La Mirande", "4 Place de l'Amirande", "Avignon", 43.9497, 4.8055, "Hôtel"),
    ("Hôtel des Grands Boulevards", "17 Boulevard Poissonnière", "Paris", 48.8722, 2.3440, "Hôtel"),
    ("Hôtel Maison Mère", "7 Rue Mayran", "Paris", 48.8792, 2.3479, "Hôtel"),
    ("Le Pigalle", "9 Rue Frochot", "Paris", 48.8821, 2.3377, "Hôtel"),
    ("Hôtel d’Aubusson", "33 Rue Dauphine", "Paris", 48.8541, 2.3396, "Hôtel"),
    ("Hôtel Plaza Athénée", "25 Avenue Montaigne", "Paris", 48.8666, 2.3058, "Hôtel"),
    ("Hôtel Bachaumont", "18 Rue Bachaumont", "Paris", 48.8660, 2.3451, "Hôtel"),
    ("Hôtel Providence", "90 Rue René Boulanger", "Paris", 48.8700, 2.3613, "Hôtel"),
    ("Hôtel Fabric", "31 Rue de la Folie Méricourt", "Paris", 48.8645, 2.3741, "Hôtel"),
    ("Hôtel Henriette", "9 Rue des Gobelins", "Paris", 48.8411, 2.3515, "Hôtel"),
    ("Hôtel Le Belleval", "16 Rue de la Pépinière", "Paris", 48.8757, 2.3241, "Hôtel"),
    ("Hôtel Le Six", "14 Rue Stanislas", "Paris", 48.8447, 2.3298, "Hôtel"),
    ("Hôtel Monge", "55 Rue Monge", "Paris", 48.8428, 2.3520, "Hôtel")
]

def insert_etablissements():
    with app.app_context():
        categories = {c.nom: c for c in Categorie.query.all()}
        if not categories:
            print("Aucune catégorie trouvée. Exécute init_db.py d'abord.")
            return

        for nom, adresse, ville, lat, lon, cat_nom in etablissements_data:
            categorie = categories.get(cat_nom)
            if not categorie:
                print(f"Catégorie '{cat_nom}' introuvable en base.")
                continue

            exist = Etablissement.query.filter_by(nom=nom, ville=ville).first()
            if exist:
                print(f"⏭️ {nom} à {ville} existe déjà, ignoré.")
                continue

            e = Etablissement(
                nom=nom,
                adresse=adresse,
                ville=ville,
                latitude=lat,
                longitude=lon,
                categorie_id=categorie.id
            )
            db.session.add(e)

        db.session.commit()
        print("50 établissements insérés avec succès.")

if __name__ == "__main__":
    insert_etablissements()