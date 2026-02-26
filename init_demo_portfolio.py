from app import app
from models import db, PortfolioProject

def init_portfolio():
    with app.app_context():
        # Clear existing projects
        db.session.query(PortfolioProject).delete()

        projects = [
            {
                "title": "Shabaka Alu+ (PWA Devis)",
                "category": "PropTech & BTP",
                "description": "Dans un contexte de forte demande résidentielle et commerciale, cet outil standardise le chiffrage en menuiserie aluminium. En générant des devis techniques précis en moins de 30 secondes, il élimine l'erreur humaine et décuple la productivité commerciale.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Shabaka Syndic",
                "category": "PropTech & BTP",
                "description": "Une plateforme collaborative qui professionnalise la gestion des copropriétés. En digitalisant les appels de fonds et les quittances, elle instaure une transparence totale, apaisant les relations entre résidents et gestionnaires.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Gestion Chantiers (Partenariat Bellari)",
                "category": "PropTech & BTP",
                "description": "Un outil de contrôle financier en temps réel. Grâce au pointage automatisé et à la traçabilité des achats par preuve visuelle, il éradique le gaspillage sur site et sécurise les marges opérationnelles.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Shabaka IMMO",
                "category": "PropTech & BTP",
                "description": "Cette solution synchronise reconnaissance d'image et traitement vocal pour générer instantanément des rapports de visite enrichis, accélérant de manière critique la prise de décision client.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "SGI-GP (GoPass)",
                "category": "GovTech & LegalTech",
                "description": "Déployé pour la maximisation des recettes aéroportuaires, ce système repose sur une architecture Zero Trust et le principe \"Flight-Bound\" (1 billet = 1 vol spécifique = 1 date unique). Il permet une réconciliation infaillible entre les manifestes de vol et les flux financiers réels.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "LexIA (Jurisprudence IA)",
                "category": "GovTech & LegalTech",
                "description": "Bien plus qu'un moteur de recherche, LexIA sécurise les arguments juridiques par une analyse sémantique des précédents judiciaires, offrant aux avocats une certitude légale et un gain de temps stratégique.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "AfrikaID (MOA Digital)",
                "category": "GovTech & LegalTech",
                "description": "Un rempart de KYC avancé conçu pour protéger les écosystèmes numériques contre les usurpations d'identité et les attaques Sybil grâce à l'analyse des hash MRZ et la vérification biométrique.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "GEC (Gestion Électronique des Courriels)",
                "category": "GovTech & LegalTech",
                "description": "Assure la pérennité de la mémoire administrative en fluidifiant les circuits de décision via une traçabilité immuable des échanges officiels.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "MyCharika",
                "category": "GovTech & LegalTech",
                "description": "Une plateforme de dématérialisation qui simplifie radicalement la création d'entreprise et l'extraction automatisée de données fiscales.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Intel ATM-RDC",
                "category": "Sécurité & Mobilité",
                "description": "Un système de Situational Awareness dédié à la sanctuarisation de l'espace aérien. Il utilise l'IA comportementale pour détecter les menaces non déclarées et les manœuvres suspectes en temps réel.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Shabaka Safety",
                "category": "Sécurité & Mobilité",
                "description": "Une solution intégrée (hardware/software) qui réduit drastiquement les accidents de travail. Son IA analyse les flux vidéo pour détecter automatiquement le non-port des Équipements de Protection Individuelle (EPI).",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Busconnect",
                "category": "Sécurité & Mobilité",
                "description": "Optimise la mobilité urbaine par une analyse granulaire des flux, permettant une gestion prédictive des transports publics.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Algorithme AAPCMLU (Dr. KALONJI)",
                "category": "HealthTech",
                "description": "Ce moteur d'inférence propriétaire utilise une analyse probabiliste pour classifier les lithiases urinaires. En corrélant imagerie et biologie, il fournit un diagnostic de précision et des conseils de prévention personnalisés, réduisant ainsi les taux de récidive.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Urgence Gabon",
                "category": "HealthTech",
                "description": "Système d'optimisation logistique pour les interventions médicales critiques, visant la réduction du temps de réponse vital.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "AI Journalist Manager",
                "category": "Média, Retail et Quotidien",
                "description": "Une plateforme de veille stratégique multilingue intégrant les technologies ElevenLabs pour le clonage vocal ultra-réaliste et Perplexity pour la validation factuelle en temps réel.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Hannout AI",
                "category": "Média, Retail et Quotidien",
                "description": "Modernise le commerce de proximité grâce à la reconnaissance visuelle automatique des produits en caisse, fluidifiant le parcours client sans saisie manuelle.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Disparus.org",
                "category": "Média, Retail et Quotidien",
                "description": "Une solution à fort impact social utilisant l'IA pour la génération automatique de visuels optimisés pour les réseaux sociaux et d'affiches munies de QR Codes dynamiques pour les avis de recherche.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Talento",
                "category": "Média, Retail et Quotidien",
                "description": "Matching intelligent de talents par analyse sémantique de CV.",
                "project_url": "https://www.shabakainnovlab.com/"
            },
            {
                "title": "Quick Receipt",
                "category": "Média, Retail et Quotidien",
                "description": "Simplification transactionnelle via quittances thermiques et WhatsApp.",
                "project_url": "https://www.shabakainnovlab.com/"
            }
        ]

        for p_data in projects:
            project = PortfolioProject(
                title=p_data['title'],
                category=p_data['category'],
                description=p_data['description'],
                project_url=p_data['project_url'],
                is_active=True
            )
            db.session.add(project)

        try:
            db.session.commit()
            print("Portfolio initialized successfully with demo projects.")
        except Exception as e:
            db.session.rollback()
            print(f"Error initializing portfolio: {e}")

if __name__ == "__main__":
    init_portfolio()
