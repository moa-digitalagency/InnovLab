from app import app
from models import db, PortfolioProject

def init_portfolio():
    with app.app_context():
        # Clear existing projects
        db.session.query(PortfolioProject).delete()

        projects = [   {   'title': {   'fr': 'Shabaka Alu+ (PWA Devis)',
                     'en': 'Shabaka Alu+ (PWA Devis)',
                     'es': 'Shabaka Alu+ (PWA Devis)',
                     'pt': 'Shabaka Alu+ (PWA Devis)',
                     'it': 'Shabaka Alu+ (PWA Devis)',
                     'de': 'Shabaka Alu+ (PWA Devis)',
                     'ar': 'Shabaka Alu+ (PWA Devis)',
                     'zh': 'Shabaka Alu+ (PWA Devis)',
                     'ja': 'Shabaka Alu+ (PWA Devis)',
                     'ko': 'Shabaka Alu+ (PWA Devis)'},
        'category': {   'fr': 'PropTech & BTP',
                        'en': 'PropTech & BTP',
                        'es': 'PropTech & BTP',
                        'pt': 'PropTech & BTP',
                        'it': 'PropTech & BTP',
                        'de': 'PropTech & BTP',
                        'ar': 'PropTech & BTP',
                        'zh': 'PropTech & BTP',
                        'ja': 'PropTech & BTP',
                        'ko': 'PropTech & BTP'},
        'short_desc': {   'fr': 'Dans un contexte de forte demande '
                                'résidentielle et commerciale, cet outil '
                                'standardise le chiffrage en menuiserie '
                                'aluminium. En générant des devis techniques '
                                'précis en moins de 30 secondes, il élimine '
                                "l'erreur humaine et décuple la productivité "
                                'commerciale.',
                          'en': 'Dans un contexte de forte demande '
                                'résidentielle et commerciale, cet outil '
                                'standardise le chiffrage en menuiserie '
                                'aluminium. En générant des devis techniques '
                                'précis en moins de 30 secondes, il élimine '
                                "l'erreur humaine et décuple la productivité "
                                'commerciale.',
                          'es': 'Dans un contexte de forte demande '
                                'résidentielle et commerciale, cet outil '
                                'standardise le chiffrage en menuiserie '
                                'aluminium. En générant des devis techniques '
                                'précis en moins de 30 secondes, il élimine '
                                "l'erreur humaine et décuple la productivité "
                                'commerciale.',
                          'pt': 'Dans un contexte de forte demande '
                                'résidentielle et commerciale, cet outil '
                                'standardise le chiffrage en menuiserie '
                                'aluminium. En générant des devis techniques '
                                'précis en moins de 30 secondes, il élimine '
                                "l'erreur humaine et décuple la productivité "
                                'commerciale.',
                          'it': 'Dans un contexte de forte demande '
                                'résidentielle et commerciale, cet outil '
                                'standardise le chiffrage en menuiserie '
                                'aluminium. En générant des devis techniques '
                                'précis en moins de 30 secondes, il élimine '
                                "l'erreur humaine et décuple la productivité "
                                'commerciale.',
                          'de': 'Dans un contexte de forte demande '
                                'résidentielle et commerciale, cet outil '
                                'standardise le chiffrage en menuiserie '
                                'aluminium. En générant des devis techniques '
                                'précis en moins de 30 secondes, il élimine '
                                "l'erreur humaine et décuple la productivité "
                                'commerciale.',
                          'ar': 'Dans un contexte de forte demande '
                                'résidentielle et commerciale, cet outil '
                                'standardise le chiffrage en menuiserie '
                                'aluminium. En générant des devis techniques '
                                'précis en moins de 30 secondes, il élimine '
                                "l'erreur humaine et décuple la productivité "
                                'commerciale.',
                          'zh': 'Dans un contexte de forte demande '
                                'résidentielle et commerciale, cet outil '
                                'standardise le chiffrage en menuiserie '
                                'aluminium. En générant des devis techniques '
                                'précis en moins de 30 secondes, il élimine '
                                "l'erreur humaine et décuple la productivité "
                                'commerciale.',
                          'ja': 'Dans un contexte de forte demande '
                                'résidentielle et commerciale, cet outil '
                                'standardise le chiffrage en menuiserie '
                                'aluminium. En générant des devis techniques '
                                'précis en moins de 30 secondes, il élimine '
                                "l'erreur humaine et décuple la productivité "
                                'commerciale.',
                          'ko': 'Dans un contexte de forte demande '
                                'résidentielle et commerciale, cet outil '
                                'standardise le chiffrage en menuiserie '
                                'aluminium. En générant des devis techniques '
                                'précis en moins de 30 secondes, il élimine '
                                "l'erreur humaine et décuple la productivité "
                                'commerciale.'},
        'full_desc': {   'fr': 'Dans un contexte de forte demande '
                               'résidentielle et commerciale, cet outil '
                               'standardise le chiffrage en menuiserie '
                               'aluminium. En générant des devis techniques '
                               'précis en moins de 30 secondes, il élimine '
                               "l'erreur humaine et décuple la productivité "
                               'commerciale.',
                         'en': 'Dans un contexte de forte demande '
                               'résidentielle et commerciale, cet outil '
                               'standardise le chiffrage en menuiserie '
                               'aluminium. En générant des devis techniques '
                               'précis en moins de 30 secondes, il élimine '
                               "l'erreur humaine et décuple la productivité "
                               'commerciale.',
                         'es': 'Dans un contexte de forte demande '
                               'résidentielle et commerciale, cet outil '
                               'standardise le chiffrage en menuiserie '
                               'aluminium. En générant des devis techniques '
                               'précis en moins de 30 secondes, il élimine '
                               "l'erreur humaine et décuple la productivité "
                               'commerciale.',
                         'pt': 'Dans un contexte de forte demande '
                               'résidentielle et commerciale, cet outil '
                               'standardise le chiffrage en menuiserie '
                               'aluminium. En générant des devis techniques '
                               'précis en moins de 30 secondes, il élimine '
                               "l'erreur humaine et décuple la productivité "
                               'commerciale.',
                         'it': 'Dans un contexte de forte demande '
                               'résidentielle et commerciale, cet outil '
                               'standardise le chiffrage en menuiserie '
                               'aluminium. En générant des devis techniques '
                               'précis en moins de 30 secondes, il élimine '
                               "l'erreur humaine et décuple la productivité "
                               'commerciale.',
                         'de': 'Dans un contexte de forte demande '
                               'résidentielle et commerciale, cet outil '
                               'standardise le chiffrage en menuiserie '
                               'aluminium. En générant des devis techniques '
                               'précis en moins de 30 secondes, il élimine '
                               "l'erreur humaine et décuple la productivité "
                               'commerciale.',
                         'ar': 'Dans un contexte de forte demande '
                               'résidentielle et commerciale, cet outil '
                               'standardise le chiffrage en menuiserie '
                               'aluminium. En générant des devis techniques '
                               'précis en moins de 30 secondes, il élimine '
                               "l'erreur humaine et décuple la productivité "
                               'commerciale.',
                         'zh': 'Dans un contexte de forte demande '
                               'résidentielle et commerciale, cet outil '
                               'standardise le chiffrage en menuiserie '
                               'aluminium. En générant des devis techniques '
                               'précis en moins de 30 secondes, il élimine '
                               "l'erreur humaine et décuple la productivité "
                               'commerciale.',
                         'ja': 'Dans un contexte de forte demande '
                               'résidentielle et commerciale, cet outil '
                               'standardise le chiffrage en menuiserie '
                               'aluminium. En générant des devis techniques '
                               'précis en moins de 30 secondes, il élimine '
                               "l'erreur humaine et décuple la productivité "
                               'commerciale.',
                         'ko': 'Dans un contexte de forte demande '
                               'résidentielle et commerciale, cet outil '
                               'standardise le chiffrage en menuiserie '
                               'aluminium. En générant des devis techniques '
                               'précis en moins de 30 secondes, il élimine '
                               "l'erreur humaine et décuple la productivité "
                               'commerciale.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Shabaka Syndic',
                     'en': 'Shabaka Syndic',
                     'es': 'Shabaka Syndic',
                     'pt': 'Shabaka Syndic',
                     'it': 'Shabaka Syndic',
                     'de': 'Shabaka Syndic',
                     'ar': 'Shabaka Syndic',
                     'zh': 'Shabaka Syndic',
                     'ja': 'Shabaka Syndic',
                     'ko': 'Shabaka Syndic'},
        'category': {   'fr': 'PropTech & BTP',
                        'en': 'PropTech & BTP',
                        'es': 'PropTech & BTP',
                        'pt': 'PropTech & BTP',
                        'it': 'PropTech & BTP',
                        'de': 'PropTech & BTP',
                        'ar': 'PropTech & BTP',
                        'zh': 'PropTech & BTP',
                        'ja': 'PropTech & BTP',
                        'ko': 'PropTech & BTP'},
        'short_desc': {   'fr': 'Une plateforme collaborative qui '
                                'professionnalise la gestion des copropriétés. '
                                'En digitalisant les appels de fonds et les '
                                'quittances, elle instaure une transparence '
                                'totale, apaisant les relations entre '
                                'résidents et gestionnaires.',
                          'en': 'Une plateforme collaborative qui '
                                'professionnalise la gestion des copropriétés. '
                                'En digitalisant les appels de fonds et les '
                                'quittances, elle instaure une transparence '
                                'totale, apaisant les relations entre '
                                'résidents et gestionnaires.',
                          'es': 'Une plateforme collaborative qui '
                                'professionnalise la gestion des copropriétés. '
                                'En digitalisant les appels de fonds et les '
                                'quittances, elle instaure une transparence '
                                'totale, apaisant les relations entre '
                                'résidents et gestionnaires.',
                          'pt': 'Une plateforme collaborative qui '
                                'professionnalise la gestion des copropriétés. '
                                'En digitalisant les appels de fonds et les '
                                'quittances, elle instaure une transparence '
                                'totale, apaisant les relations entre '
                                'résidents et gestionnaires.',
                          'it': 'Une plateforme collaborative qui '
                                'professionnalise la gestion des copropriétés. '
                                'En digitalisant les appels de fonds et les '
                                'quittances, elle instaure une transparence '
                                'totale, apaisant les relations entre '
                                'résidents et gestionnaires.',
                          'de': 'Une plateforme collaborative qui '
                                'professionnalise la gestion des copropriétés. '
                                'En digitalisant les appels de fonds et les '
                                'quittances, elle instaure une transparence '
                                'totale, apaisant les relations entre '
                                'résidents et gestionnaires.',
                          'ar': 'Une plateforme collaborative qui '
                                'professionnalise la gestion des copropriétés. '
                                'En digitalisant les appels de fonds et les '
                                'quittances, elle instaure une transparence '
                                'totale, apaisant les relations entre '
                                'résidents et gestionnaires.',
                          'zh': 'Une plateforme collaborative qui '
                                'professionnalise la gestion des copropriétés. '
                                'En digitalisant les appels de fonds et les '
                                'quittances, elle instaure une transparence '
                                'totale, apaisant les relations entre '
                                'résidents et gestionnaires.',
                          'ja': 'Une plateforme collaborative qui '
                                'professionnalise la gestion des copropriétés. '
                                'En digitalisant les appels de fonds et les '
                                'quittances, elle instaure une transparence '
                                'totale, apaisant les relations entre '
                                'résidents et gestionnaires.',
                          'ko': 'Une plateforme collaborative qui '
                                'professionnalise la gestion des copropriétés. '
                                'En digitalisant les appels de fonds et les '
                                'quittances, elle instaure une transparence '
                                'totale, apaisant les relations entre '
                                'résidents et gestionnaires.'},
        'full_desc': {   'fr': 'Une plateforme collaborative qui '
                               'professionnalise la gestion des copropriétés. '
                               'En digitalisant les appels de fonds et les '
                               'quittances, elle instaure une transparence '
                               'totale, apaisant les relations entre résidents '
                               'et gestionnaires.',
                         'en': 'Une plateforme collaborative qui '
                               'professionnalise la gestion des copropriétés. '
                               'En digitalisant les appels de fonds et les '
                               'quittances, elle instaure une transparence '
                               'totale, apaisant les relations entre résidents '
                               'et gestionnaires.',
                         'es': 'Une plateforme collaborative qui '
                               'professionnalise la gestion des copropriétés. '
                               'En digitalisant les appels de fonds et les '
                               'quittances, elle instaure une transparence '
                               'totale, apaisant les relations entre résidents '
                               'et gestionnaires.',
                         'pt': 'Une plateforme collaborative qui '
                               'professionnalise la gestion des copropriétés. '
                               'En digitalisant les appels de fonds et les '
                               'quittances, elle instaure une transparence '
                               'totale, apaisant les relations entre résidents '
                               'et gestionnaires.',
                         'it': 'Une plateforme collaborative qui '
                               'professionnalise la gestion des copropriétés. '
                               'En digitalisant les appels de fonds et les '
                               'quittances, elle instaure une transparence '
                               'totale, apaisant les relations entre résidents '
                               'et gestionnaires.',
                         'de': 'Une plateforme collaborative qui '
                               'professionnalise la gestion des copropriétés. '
                               'En digitalisant les appels de fonds et les '
                               'quittances, elle instaure une transparence '
                               'totale, apaisant les relations entre résidents '
                               'et gestionnaires.',
                         'ar': 'Une plateforme collaborative qui '
                               'professionnalise la gestion des copropriétés. '
                               'En digitalisant les appels de fonds et les '
                               'quittances, elle instaure une transparence '
                               'totale, apaisant les relations entre résidents '
                               'et gestionnaires.',
                         'zh': 'Une plateforme collaborative qui '
                               'professionnalise la gestion des copropriétés. '
                               'En digitalisant les appels de fonds et les '
                               'quittances, elle instaure une transparence '
                               'totale, apaisant les relations entre résidents '
                               'et gestionnaires.',
                         'ja': 'Une plateforme collaborative qui '
                               'professionnalise la gestion des copropriétés. '
                               'En digitalisant les appels de fonds et les '
                               'quittances, elle instaure une transparence '
                               'totale, apaisant les relations entre résidents '
                               'et gestionnaires.',
                         'ko': 'Une plateforme collaborative qui '
                               'professionnalise la gestion des copropriétés. '
                               'En digitalisant les appels de fonds et les '
                               'quittances, elle instaure une transparence '
                               'totale, apaisant les relations entre résidents '
                               'et gestionnaires.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Gestion Chantiers (Partenariat Bellari)',
                     'en': 'Gestion Chantiers (Partenariat Bellari)',
                     'es': 'Gestion Chantiers (Partenariat Bellari)',
                     'pt': 'Gestion Chantiers (Partenariat Bellari)',
                     'it': 'Gestion Chantiers (Partenariat Bellari)',
                     'de': 'Gestion Chantiers (Partenariat Bellari)',
                     'ar': 'Gestion Chantiers (Partenariat Bellari)',
                     'zh': 'Gestion Chantiers (Partenariat Bellari)',
                     'ja': 'Gestion Chantiers (Partenariat Bellari)',
                     'ko': 'Gestion Chantiers (Partenariat Bellari)'},
        'category': {   'fr': 'PropTech & BTP',
                        'en': 'PropTech & BTP',
                        'es': 'PropTech & BTP',
                        'pt': 'PropTech & BTP',
                        'it': 'PropTech & BTP',
                        'de': 'PropTech & BTP',
                        'ar': 'PropTech & BTP',
                        'zh': 'PropTech & BTP',
                        'ja': 'PropTech & BTP',
                        'ko': 'PropTech & BTP'},
        'short_desc': {   'fr': 'Un outil de contrôle financier en temps réel. '
                                'Grâce au pointage automatisé et à la '
                                'traçabilité des achats par preuve visuelle, '
                                'il éradique le gaspillage sur site et '
                                'sécurise les marges opérationnelles.',
                          'en': 'Un outil de contrôle financier en temps réel. '
                                'Grâce au pointage automatisé et à la '
                                'traçabilité des achats par preuve visuelle, '
                                'il éradique le gaspillage sur site et '
                                'sécurise les marges opérationnelles.',
                          'es': 'Un outil de contrôle financier en temps réel. '
                                'Grâce au pointage automatisé et à la '
                                'traçabilité des achats par preuve visuelle, '
                                'il éradique le gaspillage sur site et '
                                'sécurise les marges opérationnelles.',
                          'pt': 'Un outil de contrôle financier en temps réel. '
                                'Grâce au pointage automatisé et à la '
                                'traçabilité des achats par preuve visuelle, '
                                'il éradique le gaspillage sur site et '
                                'sécurise les marges opérationnelles.',
                          'it': 'Un outil de contrôle financier en temps réel. '
                                'Grâce au pointage automatisé et à la '
                                'traçabilité des achats par preuve visuelle, '
                                'il éradique le gaspillage sur site et '
                                'sécurise les marges opérationnelles.',
                          'de': 'Un outil de contrôle financier en temps réel. '
                                'Grâce au pointage automatisé et à la '
                                'traçabilité des achats par preuve visuelle, '
                                'il éradique le gaspillage sur site et '
                                'sécurise les marges opérationnelles.',
                          'ar': 'Un outil de contrôle financier en temps réel. '
                                'Grâce au pointage automatisé et à la '
                                'traçabilité des achats par preuve visuelle, '
                                'il éradique le gaspillage sur site et '
                                'sécurise les marges opérationnelles.',
                          'zh': 'Un outil de contrôle financier en temps réel. '
                                'Grâce au pointage automatisé et à la '
                                'traçabilité des achats par preuve visuelle, '
                                'il éradique le gaspillage sur site et '
                                'sécurise les marges opérationnelles.',
                          'ja': 'Un outil de contrôle financier en temps réel. '
                                'Grâce au pointage automatisé et à la '
                                'traçabilité des achats par preuve visuelle, '
                                'il éradique le gaspillage sur site et '
                                'sécurise les marges opérationnelles.',
                          'ko': 'Un outil de contrôle financier en temps réel. '
                                'Grâce au pointage automatisé et à la '
                                'traçabilité des achats par preuve visuelle, '
                                'il éradique le gaspillage sur site et '
                                'sécurise les marges opérationnelles.'},
        'full_desc': {   'fr': 'Un outil de contrôle financier en temps réel. '
                               'Grâce au pointage automatisé et à la '
                               'traçabilité des achats par preuve visuelle, il '
                               'éradique le gaspillage sur site et sécurise '
                               'les marges opérationnelles.',
                         'en': 'Un outil de contrôle financier en temps réel. '
                               'Grâce au pointage automatisé et à la '
                               'traçabilité des achats par preuve visuelle, il '
                               'éradique le gaspillage sur site et sécurise '
                               'les marges opérationnelles.',
                         'es': 'Un outil de contrôle financier en temps réel. '
                               'Grâce au pointage automatisé et à la '
                               'traçabilité des achats par preuve visuelle, il '
                               'éradique le gaspillage sur site et sécurise '
                               'les marges opérationnelles.',
                         'pt': 'Un outil de contrôle financier en temps réel. '
                               'Grâce au pointage automatisé et à la '
                               'traçabilité des achats par preuve visuelle, il '
                               'éradique le gaspillage sur site et sécurise '
                               'les marges opérationnelles.',
                         'it': 'Un outil de contrôle financier en temps réel. '
                               'Grâce au pointage automatisé et à la '
                               'traçabilité des achats par preuve visuelle, il '
                               'éradique le gaspillage sur site et sécurise '
                               'les marges opérationnelles.',
                         'de': 'Un outil de contrôle financier en temps réel. '
                               'Grâce au pointage automatisé et à la '
                               'traçabilité des achats par preuve visuelle, il '
                               'éradique le gaspillage sur site et sécurise '
                               'les marges opérationnelles.',
                         'ar': 'Un outil de contrôle financier en temps réel. '
                               'Grâce au pointage automatisé et à la '
                               'traçabilité des achats par preuve visuelle, il '
                               'éradique le gaspillage sur site et sécurise '
                               'les marges opérationnelles.',
                         'zh': 'Un outil de contrôle financier en temps réel. '
                               'Grâce au pointage automatisé et à la '
                               'traçabilité des achats par preuve visuelle, il '
                               'éradique le gaspillage sur site et sécurise '
                               'les marges opérationnelles.',
                         'ja': 'Un outil de contrôle financier en temps réel. '
                               'Grâce au pointage automatisé et à la '
                               'traçabilité des achats par preuve visuelle, il '
                               'éradique le gaspillage sur site et sécurise '
                               'les marges opérationnelles.',
                         'ko': 'Un outil de contrôle financier en temps réel. '
                               'Grâce au pointage automatisé et à la '
                               'traçabilité des achats par preuve visuelle, il '
                               'éradique le gaspillage sur site et sécurise '
                               'les marges opérationnelles.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Shabaka IMMO',
                     'en': 'Shabaka IMMO',
                     'es': 'Shabaka IMMO',
                     'pt': 'Shabaka IMMO',
                     'it': 'Shabaka IMMO',
                     'de': 'Shabaka IMMO',
                     'ar': 'Shabaka IMMO',
                     'zh': 'Shabaka IMMO',
                     'ja': 'Shabaka IMMO',
                     'ko': 'Shabaka IMMO'},
        'category': {   'fr': 'PropTech & BTP',
                        'en': 'PropTech & BTP',
                        'es': 'PropTech & BTP',
                        'pt': 'PropTech & BTP',
                        'it': 'PropTech & BTP',
                        'de': 'PropTech & BTP',
                        'ar': 'PropTech & BTP',
                        'zh': 'PropTech & BTP',
                        'ja': 'PropTech & BTP',
                        'ko': 'PropTech & BTP'},
        'short_desc': {   'fr': 'Cette solution synchronise reconnaissance '
                                "d'image et traitement vocal pour générer "
                                'instantanément des rapports de visite '
                                'enrichis, accélérant de manière critique la '
                                'prise de décision client.',
                          'en': 'Cette solution synchronise reconnaissance '
                                "d'image et traitement vocal pour générer "
                                'instantanément des rapports de visite '
                                'enrichis, accélérant de manière critique la '
                                'prise de décision client.',
                          'es': 'Cette solution synchronise reconnaissance '
                                "d'image et traitement vocal pour générer "
                                'instantanément des rapports de visite '
                                'enrichis, accélérant de manière critique la '
                                'prise de décision client.',
                          'pt': 'Cette solution synchronise reconnaissance '
                                "d'image et traitement vocal pour générer "
                                'instantanément des rapports de visite '
                                'enrichis, accélérant de manière critique la '
                                'prise de décision client.',
                          'it': 'Cette solution synchronise reconnaissance '
                                "d'image et traitement vocal pour générer "
                                'instantanément des rapports de visite '
                                'enrichis, accélérant de manière critique la '
                                'prise de décision client.',
                          'de': 'Cette solution synchronise reconnaissance '
                                "d'image et traitement vocal pour générer "
                                'instantanément des rapports de visite '
                                'enrichis, accélérant de manière critique la '
                                'prise de décision client.',
                          'ar': 'Cette solution synchronise reconnaissance '
                                "d'image et traitement vocal pour générer "
                                'instantanément des rapports de visite '
                                'enrichis, accélérant de manière critique la '
                                'prise de décision client.',
                          'zh': 'Cette solution synchronise reconnaissance '
                                "d'image et traitement vocal pour générer "
                                'instantanément des rapports de visite '
                                'enrichis, accélérant de manière critique la '
                                'prise de décision client.',
                          'ja': 'Cette solution synchronise reconnaissance '
                                "d'image et traitement vocal pour générer "
                                'instantanément des rapports de visite '
                                'enrichis, accélérant de manière critique la '
                                'prise de décision client.',
                          'ko': 'Cette solution synchronise reconnaissance '
                                "d'image et traitement vocal pour générer "
                                'instantanément des rapports de visite '
                                'enrichis, accélérant de manière critique la '
                                'prise de décision client.'},
        'full_desc': {   'fr': 'Cette solution synchronise reconnaissance '
                               "d'image et traitement vocal pour générer "
                               'instantanément des rapports de visite '
                               'enrichis, accélérant de manière critique la '
                               'prise de décision client.',
                         'en': 'Cette solution synchronise reconnaissance '
                               "d'image et traitement vocal pour générer "
                               'instantanément des rapports de visite '
                               'enrichis, accélérant de manière critique la '
                               'prise de décision client.',
                         'es': 'Cette solution synchronise reconnaissance '
                               "d'image et traitement vocal pour générer "
                               'instantanément des rapports de visite '
                               'enrichis, accélérant de manière critique la '
                               'prise de décision client.',
                         'pt': 'Cette solution synchronise reconnaissance '
                               "d'image et traitement vocal pour générer "
                               'instantanément des rapports de visite '
                               'enrichis, accélérant de manière critique la '
                               'prise de décision client.',
                         'it': 'Cette solution synchronise reconnaissance '
                               "d'image et traitement vocal pour générer "
                               'instantanément des rapports de visite '
                               'enrichis, accélérant de manière critique la '
                               'prise de décision client.',
                         'de': 'Cette solution synchronise reconnaissance '
                               "d'image et traitement vocal pour générer "
                               'instantanément des rapports de visite '
                               'enrichis, accélérant de manière critique la '
                               'prise de décision client.',
                         'ar': 'Cette solution synchronise reconnaissance '
                               "d'image et traitement vocal pour générer "
                               'instantanément des rapports de visite '
                               'enrichis, accélérant de manière critique la '
                               'prise de décision client.',
                         'zh': 'Cette solution synchronise reconnaissance '
                               "d'image et traitement vocal pour générer "
                               'instantanément des rapports de visite '
                               'enrichis, accélérant de manière critique la '
                               'prise de décision client.',
                         'ja': 'Cette solution synchronise reconnaissance '
                               "d'image et traitement vocal pour générer "
                               'instantanément des rapports de visite '
                               'enrichis, accélérant de manière critique la '
                               'prise de décision client.',
                         'ko': 'Cette solution synchronise reconnaissance '
                               "d'image et traitement vocal pour générer "
                               'instantanément des rapports de visite '
                               'enrichis, accélérant de manière critique la '
                               'prise de décision client.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'SGI-GP (GoPass)',
                     'en': 'SGI-GP (GoPass)',
                     'es': 'SGI-GP (GoPass)',
                     'pt': 'SGI-GP (GoPass)',
                     'it': 'SGI-GP (GoPass)',
                     'de': 'SGI-GP (GoPass)',
                     'ar': 'SGI-GP (GoPass)',
                     'zh': 'SGI-GP (GoPass)',
                     'ja': 'SGI-GP (GoPass)',
                     'ko': 'SGI-GP (GoPass)'},
        'category': {   'fr': 'GovTech & LegalTech',
                        'en': 'GovTech & LegalTech',
                        'es': 'GovTech & LegalTech',
                        'pt': 'GovTech & LegalTech',
                        'it': 'GovTech & LegalTech',
                        'de': 'GovTech & LegalTech',
                        'ar': 'GovTech & LegalTech',
                        'zh': 'GovTech & LegalTech',
                        'ja': 'GovTech & LegalTech',
                        'ko': 'GovTech & LegalTech'},
        'short_desc': {   'fr': 'Déployé pour la maximisation des recettes '
                                'aéroportuaires, ce système repose sur une '
                                'architecture Zero Trust et le principe '
                                '"Flight-Bound" (1 billet = 1 vol spécifique = '
                                '1 date unique). Il permet une réconciliation '
                                'infaillible entre les manifestes de vol et '
                                'les flux financiers réels.',
                          'en': 'Déployé pour la maximisation des recettes '
                                'aéroportuaires, ce système repose sur une '
                                'architecture Zero Trust et le principe '
                                '"Flight-Bound" (1 billet = 1 vol spécifique = '
                                '1 date unique). Il permet une réconciliation '
                                'infaillible entre les manifestes de vol et '
                                'les flux financiers réels.',
                          'es': 'Déployé pour la maximisation des recettes '
                                'aéroportuaires, ce système repose sur une '
                                'architecture Zero Trust et le principe '
                                '"Flight-Bound" (1 billet = 1 vol spécifique = '
                                '1 date unique). Il permet une réconciliation '
                                'infaillible entre les manifestes de vol et '
                                'les flux financiers réels.',
                          'pt': 'Déployé pour la maximisation des recettes '
                                'aéroportuaires, ce système repose sur une '
                                'architecture Zero Trust et le principe '
                                '"Flight-Bound" (1 billet = 1 vol spécifique = '
                                '1 date unique). Il permet une réconciliation '
                                'infaillible entre les manifestes de vol et '
                                'les flux financiers réels.',
                          'it': 'Déployé pour la maximisation des recettes '
                                'aéroportuaires, ce système repose sur une '
                                'architecture Zero Trust et le principe '
                                '"Flight-Bound" (1 billet = 1 vol spécifique = '
                                '1 date unique). Il permet une réconciliation '
                                'infaillible entre les manifestes de vol et '
                                'les flux financiers réels.',
                          'de': 'Déployé pour la maximisation des recettes '
                                'aéroportuaires, ce système repose sur une '
                                'architecture Zero Trust et le principe '
                                '"Flight-Bound" (1 billet = 1 vol spécifique = '
                                '1 date unique). Il permet une réconciliation '
                                'infaillible entre les manifestes de vol et '
                                'les flux financiers réels.',
                          'ar': 'Déployé pour la maximisation des recettes '
                                'aéroportuaires, ce système repose sur une '
                                'architecture Zero Trust et le principe '
                                '"Flight-Bound" (1 billet = 1 vol spécifique = '
                                '1 date unique). Il permet une réconciliation '
                                'infaillible entre les manifestes de vol et '
                                'les flux financiers réels.',
                          'zh': 'Déployé pour la maximisation des recettes '
                                'aéroportuaires, ce système repose sur une '
                                'architecture Zero Trust et le principe '
                                '"Flight-Bound" (1 billet = 1 vol spécifique = '
                                '1 date unique). Il permet une réconciliation '
                                'infaillible entre les manifestes de vol et '
                                'les flux financiers réels.',
                          'ja': 'Déployé pour la maximisation des recettes '
                                'aéroportuaires, ce système repose sur une '
                                'architecture Zero Trust et le principe '
                                '"Flight-Bound" (1 billet = 1 vol spécifique = '
                                '1 date unique). Il permet une réconciliation '
                                'infaillible entre les manifestes de vol et '
                                'les flux financiers réels.',
                          'ko': 'Déployé pour la maximisation des recettes '
                                'aéroportuaires, ce système repose sur une '
                                'architecture Zero Trust et le principe '
                                '"Flight-Bound" (1 billet = 1 vol spécifique = '
                                '1 date unique). Il permet une réconciliation '
                                'infaillible entre les manifestes de vol et '
                                'les flux financiers réels.'},
        'full_desc': {   'fr': 'Déployé pour la maximisation des recettes '
                               'aéroportuaires, ce système repose sur une '
                               'architecture Zero Trust et le principe '
                               '"Flight-Bound" (1 billet = 1 vol spécifique = '
                               '1 date unique). Il permet une réconciliation '
                               'infaillible entre les manifestes de vol et les '
                               'flux financiers réels.',
                         'en': 'Déployé pour la maximisation des recettes '
                               'aéroportuaires, ce système repose sur une '
                               'architecture Zero Trust et le principe '
                               '"Flight-Bound" (1 billet = 1 vol spécifique = '
                               '1 date unique). Il permet une réconciliation '
                               'infaillible entre les manifestes de vol et les '
                               'flux financiers réels.',
                         'es': 'Déployé pour la maximisation des recettes '
                               'aéroportuaires, ce système repose sur une '
                               'architecture Zero Trust et le principe '
                               '"Flight-Bound" (1 billet = 1 vol spécifique = '
                               '1 date unique). Il permet une réconciliation '
                               'infaillible entre les manifestes de vol et les '
                               'flux financiers réels.',
                         'pt': 'Déployé pour la maximisation des recettes '
                               'aéroportuaires, ce système repose sur une '
                               'architecture Zero Trust et le principe '
                               '"Flight-Bound" (1 billet = 1 vol spécifique = '
                               '1 date unique). Il permet une réconciliation '
                               'infaillible entre les manifestes de vol et les '
                               'flux financiers réels.',
                         'it': 'Déployé pour la maximisation des recettes '
                               'aéroportuaires, ce système repose sur une '
                               'architecture Zero Trust et le principe '
                               '"Flight-Bound" (1 billet = 1 vol spécifique = '
                               '1 date unique). Il permet une réconciliation '
                               'infaillible entre les manifestes de vol et les '
                               'flux financiers réels.',
                         'de': 'Déployé pour la maximisation des recettes '
                               'aéroportuaires, ce système repose sur une '
                               'architecture Zero Trust et le principe '
                               '"Flight-Bound" (1 billet = 1 vol spécifique = '
                               '1 date unique). Il permet une réconciliation '
                               'infaillible entre les manifestes de vol et les '
                               'flux financiers réels.',
                         'ar': 'Déployé pour la maximisation des recettes '
                               'aéroportuaires, ce système repose sur une '
                               'architecture Zero Trust et le principe '
                               '"Flight-Bound" (1 billet = 1 vol spécifique = '
                               '1 date unique). Il permet une réconciliation '
                               'infaillible entre les manifestes de vol et les '
                               'flux financiers réels.',
                         'zh': 'Déployé pour la maximisation des recettes '
                               'aéroportuaires, ce système repose sur une '
                               'architecture Zero Trust et le principe '
                               '"Flight-Bound" (1 billet = 1 vol spécifique = '
                               '1 date unique). Il permet une réconciliation '
                               'infaillible entre les manifestes de vol et les '
                               'flux financiers réels.',
                         'ja': 'Déployé pour la maximisation des recettes '
                               'aéroportuaires, ce système repose sur une '
                               'architecture Zero Trust et le principe '
                               '"Flight-Bound" (1 billet = 1 vol spécifique = '
                               '1 date unique). Il permet une réconciliation '
                               'infaillible entre les manifestes de vol et les '
                               'flux financiers réels.',
                         'ko': 'Déployé pour la maximisation des recettes '
                               'aéroportuaires, ce système repose sur une '
                               'architecture Zero Trust et le principe '
                               '"Flight-Bound" (1 billet = 1 vol spécifique = '
                               '1 date unique). Il permet une réconciliation '
                               'infaillible entre les manifestes de vol et les '
                               'flux financiers réels.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'LexIA (Jurisprudence IA)',
                     'en': 'LexIA (Jurisprudence IA)',
                     'es': 'LexIA (Jurisprudence IA)',
                     'pt': 'LexIA (Jurisprudence IA)',
                     'it': 'LexIA (Jurisprudence IA)',
                     'de': 'LexIA (Jurisprudence IA)',
                     'ar': 'LexIA (Jurisprudence IA)',
                     'zh': 'LexIA (Jurisprudence IA)',
                     'ja': 'LexIA (Jurisprudence IA)',
                     'ko': 'LexIA (Jurisprudence IA)'},
        'category': {   'fr': 'GovTech & LegalTech',
                        'en': 'GovTech & LegalTech',
                        'es': 'GovTech & LegalTech',
                        'pt': 'GovTech & LegalTech',
                        'it': 'GovTech & LegalTech',
                        'de': 'GovTech & LegalTech',
                        'ar': 'GovTech & LegalTech',
                        'zh': 'GovTech & LegalTech',
                        'ja': 'GovTech & LegalTech',
                        'ko': 'GovTech & LegalTech'},
        'short_desc': {   'fr': "Bien plus qu'un moteur de recherche, LexIA "
                                'sécurise les arguments juridiques par une '
                                'analyse sémantique des précédents '
                                'judiciaires, offrant aux avocats une '
                                'certitude légale et un gain de temps '
                                'stratégique.',
                          'en': "Bien plus qu'un moteur de recherche, LexIA "
                                'sécurise les arguments juridiques par une '
                                'analyse sémantique des précédents '
                                'judiciaires, offrant aux avocats une '
                                'certitude légale et un gain de temps '
                                'stratégique.',
                          'es': "Bien plus qu'un moteur de recherche, LexIA "
                                'sécurise les arguments juridiques par une '
                                'analyse sémantique des précédents '
                                'judiciaires, offrant aux avocats une '
                                'certitude légale et un gain de temps '
                                'stratégique.',
                          'pt': "Bien plus qu'un moteur de recherche, LexIA "
                                'sécurise les arguments juridiques par une '
                                'analyse sémantique des précédents '
                                'judiciaires, offrant aux avocats une '
                                'certitude légale et un gain de temps '
                                'stratégique.',
                          'it': "Bien plus qu'un moteur de recherche, LexIA "
                                'sécurise les arguments juridiques par une '
                                'analyse sémantique des précédents '
                                'judiciaires, offrant aux avocats une '
                                'certitude légale et un gain de temps '
                                'stratégique.',
                          'de': "Bien plus qu'un moteur de recherche, LexIA "
                                'sécurise les arguments juridiques par une '
                                'analyse sémantique des précédents '
                                'judiciaires, offrant aux avocats une '
                                'certitude légale et un gain de temps '
                                'stratégique.',
                          'ar': "Bien plus qu'un moteur de recherche, LexIA "
                                'sécurise les arguments juridiques par une '
                                'analyse sémantique des précédents '
                                'judiciaires, offrant aux avocats une '
                                'certitude légale et un gain de temps '
                                'stratégique.',
                          'zh': "Bien plus qu'un moteur de recherche, LexIA "
                                'sécurise les arguments juridiques par une '
                                'analyse sémantique des précédents '
                                'judiciaires, offrant aux avocats une '
                                'certitude légale et un gain de temps '
                                'stratégique.',
                          'ja': "Bien plus qu'un moteur de recherche, LexIA "
                                'sécurise les arguments juridiques par une '
                                'analyse sémantique des précédents '
                                'judiciaires, offrant aux avocats une '
                                'certitude légale et un gain de temps '
                                'stratégique.',
                          'ko': "Bien plus qu'un moteur de recherche, LexIA "
                                'sécurise les arguments juridiques par une '
                                'analyse sémantique des précédents '
                                'judiciaires, offrant aux avocats une '
                                'certitude légale et un gain de temps '
                                'stratégique.'},
        'full_desc': {   'fr': "Bien plus qu'un moteur de recherche, LexIA "
                               'sécurise les arguments juridiques par une '
                               'analyse sémantique des précédents judiciaires, '
                               'offrant aux avocats une certitude légale et un '
                               'gain de temps stratégique.',
                         'en': "Bien plus qu'un moteur de recherche, LexIA "
                               'sécurise les arguments juridiques par une '
                               'analyse sémantique des précédents judiciaires, '
                               'offrant aux avocats une certitude légale et un '
                               'gain de temps stratégique.',
                         'es': "Bien plus qu'un moteur de recherche, LexIA "
                               'sécurise les arguments juridiques par une '
                               'analyse sémantique des précédents judiciaires, '
                               'offrant aux avocats une certitude légale et un '
                               'gain de temps stratégique.',
                         'pt': "Bien plus qu'un moteur de recherche, LexIA "
                               'sécurise les arguments juridiques par une '
                               'analyse sémantique des précédents judiciaires, '
                               'offrant aux avocats une certitude légale et un '
                               'gain de temps stratégique.',
                         'it': "Bien plus qu'un moteur de recherche, LexIA "
                               'sécurise les arguments juridiques par une '
                               'analyse sémantique des précédents judiciaires, '
                               'offrant aux avocats une certitude légale et un '
                               'gain de temps stratégique.',
                         'de': "Bien plus qu'un moteur de recherche, LexIA "
                               'sécurise les arguments juridiques par une '
                               'analyse sémantique des précédents judiciaires, '
                               'offrant aux avocats une certitude légale et un '
                               'gain de temps stratégique.',
                         'ar': "Bien plus qu'un moteur de recherche, LexIA "
                               'sécurise les arguments juridiques par une '
                               'analyse sémantique des précédents judiciaires, '
                               'offrant aux avocats une certitude légale et un '
                               'gain de temps stratégique.',
                         'zh': "Bien plus qu'un moteur de recherche, LexIA "
                               'sécurise les arguments juridiques par une '
                               'analyse sémantique des précédents judiciaires, '
                               'offrant aux avocats une certitude légale et un '
                               'gain de temps stratégique.',
                         'ja': "Bien plus qu'un moteur de recherche, LexIA "
                               'sécurise les arguments juridiques par une '
                               'analyse sémantique des précédents judiciaires, '
                               'offrant aux avocats une certitude légale et un '
                               'gain de temps stratégique.',
                         'ko': "Bien plus qu'un moteur de recherche, LexIA "
                               'sécurise les arguments juridiques par une '
                               'analyse sémantique des précédents judiciaires, '
                               'offrant aux avocats une certitude légale et un '
                               'gain de temps stratégique.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'AfrikaID (MOA Digital)',
                     'en': 'AfrikaID (MOA Digital)',
                     'es': 'AfrikaID (MOA Digital)',
                     'pt': 'AfrikaID (MOA Digital)',
                     'it': 'AfrikaID (MOA Digital)',
                     'de': 'AfrikaID (MOA Digital)',
                     'ar': 'AfrikaID (MOA Digital)',
                     'zh': 'AfrikaID (MOA Digital)',
                     'ja': 'AfrikaID (MOA Digital)',
                     'ko': 'AfrikaID (MOA Digital)'},
        'category': {   'fr': 'GovTech & LegalTech',
                        'en': 'GovTech & LegalTech',
                        'es': 'GovTech & LegalTech',
                        'pt': 'GovTech & LegalTech',
                        'it': 'GovTech & LegalTech',
                        'de': 'GovTech & LegalTech',
                        'ar': 'GovTech & LegalTech',
                        'zh': 'GovTech & LegalTech',
                        'ja': 'GovTech & LegalTech',
                        'ko': 'GovTech & LegalTech'},
        'short_desc': {   'fr': 'Un rempart de KYC avancé conçu pour protéger '
                                'les écosystèmes numériques contre les '
                                "usurpations d'identité et les attaques Sybil "
                                "grâce à l'analyse des hash MRZ et la "
                                'vérification biométrique.',
                          'en': 'Un rempart de KYC avancé conçu pour protéger '
                                'les écosystèmes numériques contre les '
                                "usurpations d'identité et les attaques Sybil "
                                "grâce à l'analyse des hash MRZ et la "
                                'vérification biométrique.',
                          'es': 'Un rempart de KYC avancé conçu pour protéger '
                                'les écosystèmes numériques contre les '
                                "usurpations d'identité et les attaques Sybil "
                                "grâce à l'analyse des hash MRZ et la "
                                'vérification biométrique.',
                          'pt': 'Un rempart de KYC avancé conçu pour protéger '
                                'les écosystèmes numériques contre les '
                                "usurpations d'identité et les attaques Sybil "
                                "grâce à l'analyse des hash MRZ et la "
                                'vérification biométrique.',
                          'it': 'Un rempart de KYC avancé conçu pour protéger '
                                'les écosystèmes numériques contre les '
                                "usurpations d'identité et les attaques Sybil "
                                "grâce à l'analyse des hash MRZ et la "
                                'vérification biométrique.',
                          'de': 'Un rempart de KYC avancé conçu pour protéger '
                                'les écosystèmes numériques contre les '
                                "usurpations d'identité et les attaques Sybil "
                                "grâce à l'analyse des hash MRZ et la "
                                'vérification biométrique.',
                          'ar': 'Un rempart de KYC avancé conçu pour protéger '
                                'les écosystèmes numériques contre les '
                                "usurpations d'identité et les attaques Sybil "
                                "grâce à l'analyse des hash MRZ et la "
                                'vérification biométrique.',
                          'zh': 'Un rempart de KYC avancé conçu pour protéger '
                                'les écosystèmes numériques contre les '
                                "usurpations d'identité et les attaques Sybil "
                                "grâce à l'analyse des hash MRZ et la "
                                'vérification biométrique.',
                          'ja': 'Un rempart de KYC avancé conçu pour protéger '
                                'les écosystèmes numériques contre les '
                                "usurpations d'identité et les attaques Sybil "
                                "grâce à l'analyse des hash MRZ et la "
                                'vérification biométrique.',
                          'ko': 'Un rempart de KYC avancé conçu pour protéger '
                                'les écosystèmes numériques contre les '
                                "usurpations d'identité et les attaques Sybil "
                                "grâce à l'analyse des hash MRZ et la "
                                'vérification biométrique.'},
        'full_desc': {   'fr': 'Un rempart de KYC avancé conçu pour protéger '
                               'les écosystèmes numériques contre les '
                               "usurpations d'identité et les attaques Sybil "
                               "grâce à l'analyse des hash MRZ et la "
                               'vérification biométrique.',
                         'en': 'Un rempart de KYC avancé conçu pour protéger '
                               'les écosystèmes numériques contre les '
                               "usurpations d'identité et les attaques Sybil "
                               "grâce à l'analyse des hash MRZ et la "
                               'vérification biométrique.',
                         'es': 'Un rempart de KYC avancé conçu pour protéger '
                               'les écosystèmes numériques contre les '
                               "usurpations d'identité et les attaques Sybil "
                               "grâce à l'analyse des hash MRZ et la "
                               'vérification biométrique.',
                         'pt': 'Un rempart de KYC avancé conçu pour protéger '
                               'les écosystèmes numériques contre les '
                               "usurpations d'identité et les attaques Sybil "
                               "grâce à l'analyse des hash MRZ et la "
                               'vérification biométrique.',
                         'it': 'Un rempart de KYC avancé conçu pour protéger '
                               'les écosystèmes numériques contre les '
                               "usurpations d'identité et les attaques Sybil "
                               "grâce à l'analyse des hash MRZ et la "
                               'vérification biométrique.',
                         'de': 'Un rempart de KYC avancé conçu pour protéger '
                               'les écosystèmes numériques contre les '
                               "usurpations d'identité et les attaques Sybil "
                               "grâce à l'analyse des hash MRZ et la "
                               'vérification biométrique.',
                         'ar': 'Un rempart de KYC avancé conçu pour protéger '
                               'les écosystèmes numériques contre les '
                               "usurpations d'identité et les attaques Sybil "
                               "grâce à l'analyse des hash MRZ et la "
                               'vérification biométrique.',
                         'zh': 'Un rempart de KYC avancé conçu pour protéger '
                               'les écosystèmes numériques contre les '
                               "usurpations d'identité et les attaques Sybil "
                               "grâce à l'analyse des hash MRZ et la "
                               'vérification biométrique.',
                         'ja': 'Un rempart de KYC avancé conçu pour protéger '
                               'les écosystèmes numériques contre les '
                               "usurpations d'identité et les attaques Sybil "
                               "grâce à l'analyse des hash MRZ et la "
                               'vérification biométrique.',
                         'ko': 'Un rempart de KYC avancé conçu pour protéger '
                               'les écosystèmes numériques contre les '
                               "usurpations d'identité et les attaques Sybil "
                               "grâce à l'analyse des hash MRZ et la "
                               'vérification biométrique.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'GEC (Gestion Électronique des Courriels)',
                     'en': 'GEC (Gestion Électronique des Courriels)',
                     'es': 'GEC (Gestion Électronique des Courriels)',
                     'pt': 'GEC (Gestion Électronique des Courriels)',
                     'it': 'GEC (Gestion Électronique des Courriels)',
                     'de': 'GEC (Gestion Électronique des Courriels)',
                     'ar': 'GEC (Gestion Électronique des Courriels)',
                     'zh': 'GEC (Gestion Électronique des Courriels)',
                     'ja': 'GEC (Gestion Électronique des Courriels)',
                     'ko': 'GEC (Gestion Électronique des Courriels)'},
        'category': {   'fr': 'GovTech & LegalTech',
                        'en': 'GovTech & LegalTech',
                        'es': 'GovTech & LegalTech',
                        'pt': 'GovTech & LegalTech',
                        'it': 'GovTech & LegalTech',
                        'de': 'GovTech & LegalTech',
                        'ar': 'GovTech & LegalTech',
                        'zh': 'GovTech & LegalTech',
                        'ja': 'GovTech & LegalTech',
                        'ko': 'GovTech & LegalTech'},
        'short_desc': {   'fr': 'Assure la pérennité de la mémoire '
                                'administrative en fluidifiant les circuits de '
                                'décision via une traçabilité immuable des '
                                'échanges officiels.',
                          'en': 'Assure la pérennité de la mémoire '
                                'administrative en fluidifiant les circuits de '
                                'décision via une traçabilité immuable des '
                                'échanges officiels.',
                          'es': 'Assure la pérennité de la mémoire '
                                'administrative en fluidifiant les circuits de '
                                'décision via une traçabilité immuable des '
                                'échanges officiels.',
                          'pt': 'Assure la pérennité de la mémoire '
                                'administrative en fluidifiant les circuits de '
                                'décision via une traçabilité immuable des '
                                'échanges officiels.',
                          'it': 'Assure la pérennité de la mémoire '
                                'administrative en fluidifiant les circuits de '
                                'décision via une traçabilité immuable des '
                                'échanges officiels.',
                          'de': 'Assure la pérennité de la mémoire '
                                'administrative en fluidifiant les circuits de '
                                'décision via une traçabilité immuable des '
                                'échanges officiels.',
                          'ar': 'Assure la pérennité de la mémoire '
                                'administrative en fluidifiant les circuits de '
                                'décision via une traçabilité immuable des '
                                'échanges officiels.',
                          'zh': 'Assure la pérennité de la mémoire '
                                'administrative en fluidifiant les circuits de '
                                'décision via une traçabilité immuable des '
                                'échanges officiels.',
                          'ja': 'Assure la pérennité de la mémoire '
                                'administrative en fluidifiant les circuits de '
                                'décision via une traçabilité immuable des '
                                'échanges officiels.',
                          'ko': 'Assure la pérennité de la mémoire '
                                'administrative en fluidifiant les circuits de '
                                'décision via une traçabilité immuable des '
                                'échanges officiels.'},
        'full_desc': {   'fr': 'Assure la pérennité de la mémoire '
                               'administrative en fluidifiant les circuits de '
                               'décision via une traçabilité immuable des '
                               'échanges officiels.',
                         'en': 'Assure la pérennité de la mémoire '
                               'administrative en fluidifiant les circuits de '
                               'décision via une traçabilité immuable des '
                               'échanges officiels.',
                         'es': 'Assure la pérennité de la mémoire '
                               'administrative en fluidifiant les circuits de '
                               'décision via une traçabilité immuable des '
                               'échanges officiels.',
                         'pt': 'Assure la pérennité de la mémoire '
                               'administrative en fluidifiant les circuits de '
                               'décision via une traçabilité immuable des '
                               'échanges officiels.',
                         'it': 'Assure la pérennité de la mémoire '
                               'administrative en fluidifiant les circuits de '
                               'décision via une traçabilité immuable des '
                               'échanges officiels.',
                         'de': 'Assure la pérennité de la mémoire '
                               'administrative en fluidifiant les circuits de '
                               'décision via une traçabilité immuable des '
                               'échanges officiels.',
                         'ar': 'Assure la pérennité de la mémoire '
                               'administrative en fluidifiant les circuits de '
                               'décision via une traçabilité immuable des '
                               'échanges officiels.',
                         'zh': 'Assure la pérennité de la mémoire '
                               'administrative en fluidifiant les circuits de '
                               'décision via une traçabilité immuable des '
                               'échanges officiels.',
                         'ja': 'Assure la pérennité de la mémoire '
                               'administrative en fluidifiant les circuits de '
                               'décision via une traçabilité immuable des '
                               'échanges officiels.',
                         'ko': 'Assure la pérennité de la mémoire '
                               'administrative en fluidifiant les circuits de '
                               'décision via une traçabilité immuable des '
                               'échanges officiels.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'MyCharika',
                     'en': 'MyCharika',
                     'es': 'MyCharika',
                     'pt': 'MyCharika',
                     'it': 'MyCharika',
                     'de': 'MyCharika',
                     'ar': 'MyCharika',
                     'zh': 'MyCharika',
                     'ja': 'MyCharika',
                     'ko': 'MyCharika'},
        'category': {   'fr': 'GovTech & LegalTech',
                        'en': 'GovTech & LegalTech',
                        'es': 'GovTech & LegalTech',
                        'pt': 'GovTech & LegalTech',
                        'it': 'GovTech & LegalTech',
                        'de': 'GovTech & LegalTech',
                        'ar': 'GovTech & LegalTech',
                        'zh': 'GovTech & LegalTech',
                        'ja': 'GovTech & LegalTech',
                        'ko': 'GovTech & LegalTech'},
        'short_desc': {   'fr': 'Une plateforme de dématérialisation qui '
                                'simplifie radicalement la création '
                                "d'entreprise et l'extraction automatisée de "
                                'données fiscales.',
                          'en': 'Une plateforme de dématérialisation qui '
                                'simplifie radicalement la création '
                                "d'entreprise et l'extraction automatisée de "
                                'données fiscales.',
                          'es': 'Une plateforme de dématérialisation qui '
                                'simplifie radicalement la création '
                                "d'entreprise et l'extraction automatisée de "
                                'données fiscales.',
                          'pt': 'Une plateforme de dématérialisation qui '
                                'simplifie radicalement la création '
                                "d'entreprise et l'extraction automatisée de "
                                'données fiscales.',
                          'it': 'Une plateforme de dématérialisation qui '
                                'simplifie radicalement la création '
                                "d'entreprise et l'extraction automatisée de "
                                'données fiscales.',
                          'de': 'Une plateforme de dématérialisation qui '
                                'simplifie radicalement la création '
                                "d'entreprise et l'extraction automatisée de "
                                'données fiscales.',
                          'ar': 'Une plateforme de dématérialisation qui '
                                'simplifie radicalement la création '
                                "d'entreprise et l'extraction automatisée de "
                                'données fiscales.',
                          'zh': 'Une plateforme de dématérialisation qui '
                                'simplifie radicalement la création '
                                "d'entreprise et l'extraction automatisée de "
                                'données fiscales.',
                          'ja': 'Une plateforme de dématérialisation qui '
                                'simplifie radicalement la création '
                                "d'entreprise et l'extraction automatisée de "
                                'données fiscales.',
                          'ko': 'Une plateforme de dématérialisation qui '
                                'simplifie radicalement la création '
                                "d'entreprise et l'extraction automatisée de "
                                'données fiscales.'},
        'full_desc': {   'fr': 'Une plateforme de dématérialisation qui '
                               'simplifie radicalement la création '
                               "d'entreprise et l'extraction automatisée de "
                               'données fiscales.',
                         'en': 'Une plateforme de dématérialisation qui '
                               'simplifie radicalement la création '
                               "d'entreprise et l'extraction automatisée de "
                               'données fiscales.',
                         'es': 'Une plateforme de dématérialisation qui '
                               'simplifie radicalement la création '
                               "d'entreprise et l'extraction automatisée de "
                               'données fiscales.',
                         'pt': 'Une plateforme de dématérialisation qui '
                               'simplifie radicalement la création '
                               "d'entreprise et l'extraction automatisée de "
                               'données fiscales.',
                         'it': 'Une plateforme de dématérialisation qui '
                               'simplifie radicalement la création '
                               "d'entreprise et l'extraction automatisée de "
                               'données fiscales.',
                         'de': 'Une plateforme de dématérialisation qui '
                               'simplifie radicalement la création '
                               "d'entreprise et l'extraction automatisée de "
                               'données fiscales.',
                         'ar': 'Une plateforme de dématérialisation qui '
                               'simplifie radicalement la création '
                               "d'entreprise et l'extraction automatisée de "
                               'données fiscales.',
                         'zh': 'Une plateforme de dématérialisation qui '
                               'simplifie radicalement la création '
                               "d'entreprise et l'extraction automatisée de "
                               'données fiscales.',
                         'ja': 'Une plateforme de dématérialisation qui '
                               'simplifie radicalement la création '
                               "d'entreprise et l'extraction automatisée de "
                               'données fiscales.',
                         'ko': 'Une plateforme de dématérialisation qui '
                               'simplifie radicalement la création '
                               "d'entreprise et l'extraction automatisée de "
                               'données fiscales.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Intel ATM-RDC',
                     'en': 'Intel ATM-RDC',
                     'es': 'Intel ATM-RDC',
                     'pt': 'Intel ATM-RDC',
                     'it': 'Intel ATM-RDC',
                     'de': 'Intel ATM-RDC',
                     'ar': 'Intel ATM-RDC',
                     'zh': 'Intel ATM-RDC',
                     'ja': 'Intel ATM-RDC',
                     'ko': 'Intel ATM-RDC'},
        'category': {   'fr': 'Sécurité & Mobilité',
                        'en': 'Sécurité & Mobilité',
                        'es': 'Sécurité & Mobilité',
                        'pt': 'Sécurité & Mobilité',
                        'it': 'Sécurité & Mobilité',
                        'de': 'Sécurité & Mobilité',
                        'ar': 'Sécurité & Mobilité',
                        'zh': 'Sécurité & Mobilité',
                        'ja': 'Sécurité & Mobilité',
                        'ko': 'Sécurité & Mobilité'},
        'short_desc': {   'fr': 'Un système de Situational Awareness dédié à '
                                "la sanctuarisation de l'espace aérien. Il "
                                "utilise l'IA comportementale pour détecter "
                                'les menaces non déclarées et les manœuvres '
                                'suspectes en temps réel.',
                          'en': 'Un système de Situational Awareness dédié à '
                                "la sanctuarisation de l'espace aérien. Il "
                                "utilise l'IA comportementale pour détecter "
                                'les menaces non déclarées et les manœuvres '
                                'suspectes en temps réel.',
                          'es': 'Un système de Situational Awareness dédié à '
                                "la sanctuarisation de l'espace aérien. Il "
                                "utilise l'IA comportementale pour détecter "
                                'les menaces non déclarées et les manœuvres '
                                'suspectes en temps réel.',
                          'pt': 'Un système de Situational Awareness dédié à '
                                "la sanctuarisation de l'espace aérien. Il "
                                "utilise l'IA comportementale pour détecter "
                                'les menaces non déclarées et les manœuvres '
                                'suspectes en temps réel.',
                          'it': 'Un système de Situational Awareness dédié à '
                                "la sanctuarisation de l'espace aérien. Il "
                                "utilise l'IA comportementale pour détecter "
                                'les menaces non déclarées et les manœuvres '
                                'suspectes en temps réel.',
                          'de': 'Un système de Situational Awareness dédié à '
                                "la sanctuarisation de l'espace aérien. Il "
                                "utilise l'IA comportementale pour détecter "
                                'les menaces non déclarées et les manœuvres '
                                'suspectes en temps réel.',
                          'ar': 'Un système de Situational Awareness dédié à '
                                "la sanctuarisation de l'espace aérien. Il "
                                "utilise l'IA comportementale pour détecter "
                                'les menaces non déclarées et les manœuvres '
                                'suspectes en temps réel.',
                          'zh': 'Un système de Situational Awareness dédié à '
                                "la sanctuarisation de l'espace aérien. Il "
                                "utilise l'IA comportementale pour détecter "
                                'les menaces non déclarées et les manœuvres '
                                'suspectes en temps réel.',
                          'ja': 'Un système de Situational Awareness dédié à '
                                "la sanctuarisation de l'espace aérien. Il "
                                "utilise l'IA comportementale pour détecter "
                                'les menaces non déclarées et les manœuvres '
                                'suspectes en temps réel.',
                          'ko': 'Un système de Situational Awareness dédié à '
                                "la sanctuarisation de l'espace aérien. Il "
                                "utilise l'IA comportementale pour détecter "
                                'les menaces non déclarées et les manœuvres '
                                'suspectes en temps réel.'},
        'full_desc': {   'fr': 'Un système de Situational Awareness dédié à la '
                               "sanctuarisation de l'espace aérien. Il utilise "
                               "l'IA comportementale pour détecter les menaces "
                               'non déclarées et les manœuvres suspectes en '
                               'temps réel.',
                         'en': 'Un système de Situational Awareness dédié à la '
                               "sanctuarisation de l'espace aérien. Il utilise "
                               "l'IA comportementale pour détecter les menaces "
                               'non déclarées et les manœuvres suspectes en '
                               'temps réel.',
                         'es': 'Un système de Situational Awareness dédié à la '
                               "sanctuarisation de l'espace aérien. Il utilise "
                               "l'IA comportementale pour détecter les menaces "
                               'non déclarées et les manœuvres suspectes en '
                               'temps réel.',
                         'pt': 'Un système de Situational Awareness dédié à la '
                               "sanctuarisation de l'espace aérien. Il utilise "
                               "l'IA comportementale pour détecter les menaces "
                               'non déclarées et les manœuvres suspectes en '
                               'temps réel.',
                         'it': 'Un système de Situational Awareness dédié à la '
                               "sanctuarisation de l'espace aérien. Il utilise "
                               "l'IA comportementale pour détecter les menaces "
                               'non déclarées et les manœuvres suspectes en '
                               'temps réel.',
                         'de': 'Un système de Situational Awareness dédié à la '
                               "sanctuarisation de l'espace aérien. Il utilise "
                               "l'IA comportementale pour détecter les menaces "
                               'non déclarées et les manœuvres suspectes en '
                               'temps réel.',
                         'ar': 'Un système de Situational Awareness dédié à la '
                               "sanctuarisation de l'espace aérien. Il utilise "
                               "l'IA comportementale pour détecter les menaces "
                               'non déclarées et les manœuvres suspectes en '
                               'temps réel.',
                         'zh': 'Un système de Situational Awareness dédié à la '
                               "sanctuarisation de l'espace aérien. Il utilise "
                               "l'IA comportementale pour détecter les menaces "
                               'non déclarées et les manœuvres suspectes en '
                               'temps réel.',
                         'ja': 'Un système de Situational Awareness dédié à la '
                               "sanctuarisation de l'espace aérien. Il utilise "
                               "l'IA comportementale pour détecter les menaces "
                               'non déclarées et les manœuvres suspectes en '
                               'temps réel.',
                         'ko': 'Un système de Situational Awareness dédié à la '
                               "sanctuarisation de l'espace aérien. Il utilise "
                               "l'IA comportementale pour détecter les menaces "
                               'non déclarées et les manœuvres suspectes en '
                               'temps réel.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Shabaka Safety',
                     'en': 'Shabaka Safety',
                     'es': 'Shabaka Safety',
                     'pt': 'Shabaka Safety',
                     'it': 'Shabaka Safety',
                     'de': 'Shabaka Safety',
                     'ar': 'Shabaka Safety',
                     'zh': 'Shabaka Safety',
                     'ja': 'Shabaka Safety',
                     'ko': 'Shabaka Safety'},
        'category': {   'fr': 'Sécurité & Mobilité',
                        'en': 'Sécurité & Mobilité',
                        'es': 'Sécurité & Mobilité',
                        'pt': 'Sécurité & Mobilité',
                        'it': 'Sécurité & Mobilité',
                        'de': 'Sécurité & Mobilité',
                        'ar': 'Sécurité & Mobilité',
                        'zh': 'Sécurité & Mobilité',
                        'ja': 'Sécurité & Mobilité',
                        'ko': 'Sécurité & Mobilité'},
        'short_desc': {   'fr': 'Une solution intégrée (hardware/software) qui '
                                'réduit drastiquement les accidents de '
                                'travail. Son IA analyse les flux vidéo pour '
                                'détecter automatiquement le non-port des '
                                'Équipements de Protection Individuelle (EPI).',
                          'en': 'Une solution intégrée (hardware/software) qui '
                                'réduit drastiquement les accidents de '
                                'travail. Son IA analyse les flux vidéo pour '
                                'détecter automatiquement le non-port des '
                                'Équipements de Protection Individuelle (EPI).',
                          'es': 'Une solution intégrée (hardware/software) qui '
                                'réduit drastiquement les accidents de '
                                'travail. Son IA analyse les flux vidéo pour '
                                'détecter automatiquement le non-port des '
                                'Équipements de Protection Individuelle (EPI).',
                          'pt': 'Une solution intégrée (hardware/software) qui '
                                'réduit drastiquement les accidents de '
                                'travail. Son IA analyse les flux vidéo pour '
                                'détecter automatiquement le non-port des '
                                'Équipements de Protection Individuelle (EPI).',
                          'it': 'Une solution intégrée (hardware/software) qui '
                                'réduit drastiquement les accidents de '
                                'travail. Son IA analyse les flux vidéo pour '
                                'détecter automatiquement le non-port des '
                                'Équipements de Protection Individuelle (EPI).',
                          'de': 'Une solution intégrée (hardware/software) qui '
                                'réduit drastiquement les accidents de '
                                'travail. Son IA analyse les flux vidéo pour '
                                'détecter automatiquement le non-port des '
                                'Équipements de Protection Individuelle (EPI).',
                          'ar': 'Une solution intégrée (hardware/software) qui '
                                'réduit drastiquement les accidents de '
                                'travail. Son IA analyse les flux vidéo pour '
                                'détecter automatiquement le non-port des '
                                'Équipements de Protection Individuelle (EPI).',
                          'zh': 'Une solution intégrée (hardware/software) qui '
                                'réduit drastiquement les accidents de '
                                'travail. Son IA analyse les flux vidéo pour '
                                'détecter automatiquement le non-port des '
                                'Équipements de Protection Individuelle (EPI).',
                          'ja': 'Une solution intégrée (hardware/software) qui '
                                'réduit drastiquement les accidents de '
                                'travail. Son IA analyse les flux vidéo pour '
                                'détecter automatiquement le non-port des '
                                'Équipements de Protection Individuelle (EPI).',
                          'ko': 'Une solution intégrée (hardware/software) qui '
                                'réduit drastiquement les accidents de '
                                'travail. Son IA analyse les flux vidéo pour '
                                'détecter automatiquement le non-port des '
                                'Équipements de Protection Individuelle '
                                '(EPI).'},
        'full_desc': {   'fr': 'Une solution intégrée (hardware/software) qui '
                               'réduit drastiquement les accidents de travail. '
                               'Son IA analyse les flux vidéo pour détecter '
                               'automatiquement le non-port des Équipements de '
                               'Protection Individuelle (EPI).',
                         'en': 'Une solution intégrée (hardware/software) qui '
                               'réduit drastiquement les accidents de travail. '
                               'Son IA analyse les flux vidéo pour détecter '
                               'automatiquement le non-port des Équipements de '
                               'Protection Individuelle (EPI).',
                         'es': 'Une solution intégrée (hardware/software) qui '
                               'réduit drastiquement les accidents de travail. '
                               'Son IA analyse les flux vidéo pour détecter '
                               'automatiquement le non-port des Équipements de '
                               'Protection Individuelle (EPI).',
                         'pt': 'Une solution intégrée (hardware/software) qui '
                               'réduit drastiquement les accidents de travail. '
                               'Son IA analyse les flux vidéo pour détecter '
                               'automatiquement le non-port des Équipements de '
                               'Protection Individuelle (EPI).',
                         'it': 'Une solution intégrée (hardware/software) qui '
                               'réduit drastiquement les accidents de travail. '
                               'Son IA analyse les flux vidéo pour détecter '
                               'automatiquement le non-port des Équipements de '
                               'Protection Individuelle (EPI).',
                         'de': 'Une solution intégrée (hardware/software) qui '
                               'réduit drastiquement les accidents de travail. '
                               'Son IA analyse les flux vidéo pour détecter '
                               'automatiquement le non-port des Équipements de '
                               'Protection Individuelle (EPI).',
                         'ar': 'Une solution intégrée (hardware/software) qui '
                               'réduit drastiquement les accidents de travail. '
                               'Son IA analyse les flux vidéo pour détecter '
                               'automatiquement le non-port des Équipements de '
                               'Protection Individuelle (EPI).',
                         'zh': 'Une solution intégrée (hardware/software) qui '
                               'réduit drastiquement les accidents de travail. '
                               'Son IA analyse les flux vidéo pour détecter '
                               'automatiquement le non-port des Équipements de '
                               'Protection Individuelle (EPI).',
                         'ja': 'Une solution intégrée (hardware/software) qui '
                               'réduit drastiquement les accidents de travail. '
                               'Son IA analyse les flux vidéo pour détecter '
                               'automatiquement le non-port des Équipements de '
                               'Protection Individuelle (EPI).',
                         'ko': 'Une solution intégrée (hardware/software) qui '
                               'réduit drastiquement les accidents de travail. '
                               'Son IA analyse les flux vidéo pour détecter '
                               'automatiquement le non-port des Équipements de '
                               'Protection Individuelle (EPI).'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Busconnect',
                     'en': 'Busconnect',
                     'es': 'Busconnect',
                     'pt': 'Busconnect',
                     'it': 'Busconnect',
                     'de': 'Busconnect',
                     'ar': 'Busconnect',
                     'zh': 'Busconnect',
                     'ja': 'Busconnect',
                     'ko': 'Busconnect'},
        'category': {   'fr': 'Sécurité & Mobilité',
                        'en': 'Sécurité & Mobilité',
                        'es': 'Sécurité & Mobilité',
                        'pt': 'Sécurité & Mobilité',
                        'it': 'Sécurité & Mobilité',
                        'de': 'Sécurité & Mobilité',
                        'ar': 'Sécurité & Mobilité',
                        'zh': 'Sécurité & Mobilité',
                        'ja': 'Sécurité & Mobilité',
                        'ko': 'Sécurité & Mobilité'},
        'short_desc': {   'fr': 'Optimise la mobilité urbaine par une analyse '
                                'granulaire des flux, permettant une gestion '
                                'prédictive des transports publics.',
                          'en': 'Optimise la mobilité urbaine par une analyse '
                                'granulaire des flux, permettant une gestion '
                                'prédictive des transports publics.',
                          'es': 'Optimise la mobilité urbaine par une analyse '
                                'granulaire des flux, permettant une gestion '
                                'prédictive des transports publics.',
                          'pt': 'Optimise la mobilité urbaine par une analyse '
                                'granulaire des flux, permettant une gestion '
                                'prédictive des transports publics.',
                          'it': 'Optimise la mobilité urbaine par une analyse '
                                'granulaire des flux, permettant une gestion '
                                'prédictive des transports publics.',
                          'de': 'Optimise la mobilité urbaine par une analyse '
                                'granulaire des flux, permettant une gestion '
                                'prédictive des transports publics.',
                          'ar': 'Optimise la mobilité urbaine par une analyse '
                                'granulaire des flux, permettant une gestion '
                                'prédictive des transports publics.',
                          'zh': 'Optimise la mobilité urbaine par une analyse '
                                'granulaire des flux, permettant une gestion '
                                'prédictive des transports publics.',
                          'ja': 'Optimise la mobilité urbaine par une analyse '
                                'granulaire des flux, permettant une gestion '
                                'prédictive des transports publics.',
                          'ko': 'Optimise la mobilité urbaine par une analyse '
                                'granulaire des flux, permettant une gestion '
                                'prédictive des transports publics.'},
        'full_desc': {   'fr': 'Optimise la mobilité urbaine par une analyse '
                               'granulaire des flux, permettant une gestion '
                               'prédictive des transports publics.',
                         'en': 'Optimise la mobilité urbaine par une analyse '
                               'granulaire des flux, permettant une gestion '
                               'prédictive des transports publics.',
                         'es': 'Optimise la mobilité urbaine par une analyse '
                               'granulaire des flux, permettant une gestion '
                               'prédictive des transports publics.',
                         'pt': 'Optimise la mobilité urbaine par une analyse '
                               'granulaire des flux, permettant une gestion '
                               'prédictive des transports publics.',
                         'it': 'Optimise la mobilité urbaine par une analyse '
                               'granulaire des flux, permettant une gestion '
                               'prédictive des transports publics.',
                         'de': 'Optimise la mobilité urbaine par une analyse '
                               'granulaire des flux, permettant une gestion '
                               'prédictive des transports publics.',
                         'ar': 'Optimise la mobilité urbaine par une analyse '
                               'granulaire des flux, permettant une gestion '
                               'prédictive des transports publics.',
                         'zh': 'Optimise la mobilité urbaine par une analyse '
                               'granulaire des flux, permettant une gestion '
                               'prédictive des transports publics.',
                         'ja': 'Optimise la mobilité urbaine par une analyse '
                               'granulaire des flux, permettant une gestion '
                               'prédictive des transports publics.',
                         'ko': 'Optimise la mobilité urbaine par une analyse '
                               'granulaire des flux, permettant une gestion '
                               'prédictive des transports publics.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Algorithme AAPCMLU (Dr. KALONJI)',
                     'en': 'Algorithme AAPCMLU (Dr. KALONJI)',
                     'es': 'Algorithme AAPCMLU (Dr. KALONJI)',
                     'pt': 'Algorithme AAPCMLU (Dr. KALONJI)',
                     'it': 'Algorithme AAPCMLU (Dr. KALONJI)',
                     'de': 'Algorithme AAPCMLU (Dr. KALONJI)',
                     'ar': 'Algorithme AAPCMLU (Dr. KALONJI)',
                     'zh': 'Algorithme AAPCMLU (Dr. KALONJI)',
                     'ja': 'Algorithme AAPCMLU (Dr. KALONJI)',
                     'ko': 'Algorithme AAPCMLU (Dr. KALONJI)'},
        'category': {   'fr': 'HealthTech',
                        'en': 'HealthTech',
                        'es': 'HealthTech',
                        'pt': 'HealthTech',
                        'it': 'HealthTech',
                        'de': 'HealthTech',
                        'ar': 'HealthTech',
                        'zh': 'HealthTech',
                        'ja': 'HealthTech',
                        'ko': 'HealthTech'},
        'short_desc': {   'fr': "Ce moteur d'inférence propriétaire utilise "
                                'une analyse probabiliste pour classifier les '
                                'lithiases urinaires. En corrélant imagerie et '
                                'biologie, il fournit un diagnostic de '
                                'précision et des conseils de prévention '
                                'personnalisés, réduisant ainsi les taux de '
                                'récidive.',
                          'en': "Ce moteur d'inférence propriétaire utilise "
                                'une analyse probabiliste pour classifier les '
                                'lithiases urinaires. En corrélant imagerie et '
                                'biologie, il fournit un diagnostic de '
                                'précision et des conseils de prévention '
                                'personnalisés, réduisant ainsi les taux de '
                                'récidive.',
                          'es': "Ce moteur d'inférence propriétaire utilise "
                                'une analyse probabiliste pour classifier les '
                                'lithiases urinaires. En corrélant imagerie et '
                                'biologie, il fournit un diagnostic de '
                                'précision et des conseils de prévention '
                                'personnalisés, réduisant ainsi les taux de '
                                'récidive.',
                          'pt': "Ce moteur d'inférence propriétaire utilise "
                                'une analyse probabiliste pour classifier les '
                                'lithiases urinaires. En corrélant imagerie et '
                                'biologie, il fournit un diagnostic de '
                                'précision et des conseils de prévention '
                                'personnalisés, réduisant ainsi les taux de '
                                'récidive.',
                          'it': "Ce moteur d'inférence propriétaire utilise "
                                'une analyse probabiliste pour classifier les '
                                'lithiases urinaires. En corrélant imagerie et '
                                'biologie, il fournit un diagnostic de '
                                'précision et des conseils de prévention '
                                'personnalisés, réduisant ainsi les taux de '
                                'récidive.',
                          'de': "Ce moteur d'inférence propriétaire utilise "
                                'une analyse probabiliste pour classifier les '
                                'lithiases urinaires. En corrélant imagerie et '
                                'biologie, il fournit un diagnostic de '
                                'précision et des conseils de prévention '
                                'personnalisés, réduisant ainsi les taux de '
                                'récidive.',
                          'ar': "Ce moteur d'inférence propriétaire utilise "
                                'une analyse probabiliste pour classifier les '
                                'lithiases urinaires. En corrélant imagerie et '
                                'biologie, il fournit un diagnostic de '
                                'précision et des conseils de prévention '
                                'personnalisés, réduisant ainsi les taux de '
                                'récidive.',
                          'zh': "Ce moteur d'inférence propriétaire utilise "
                                'une analyse probabiliste pour classifier les '
                                'lithiases urinaires. En corrélant imagerie et '
                                'biologie, il fournit un diagnostic de '
                                'précision et des conseils de prévention '
                                'personnalisés, réduisant ainsi les taux de '
                                'récidive.',
                          'ja': "Ce moteur d'inférence propriétaire utilise "
                                'une analyse probabiliste pour classifier les '
                                'lithiases urinaires. En corrélant imagerie et '
                                'biologie, il fournit un diagnostic de '
                                'précision et des conseils de prévention '
                                'personnalisés, réduisant ainsi les taux de '
                                'récidive.',
                          'ko': "Ce moteur d'inférence propriétaire utilise "
                                'une analyse probabiliste pour classifier les '
                                'lithiases urinaires. En corrélant imagerie et '
                                'biologie, il fournit un diagnostic de '
                                'précision et des conseils de prévention '
                                'personnalisés, réduisant ainsi les taux de '
                                'récidive.'},
        'full_desc': {   'fr': "Ce moteur d'inférence propriétaire utilise une "
                               'analyse probabiliste pour classifier les '
                               'lithiases urinaires. En corrélant imagerie et '
                               'biologie, il fournit un diagnostic de '
                               'précision et des conseils de prévention '
                               'personnalisés, réduisant ainsi les taux de '
                               'récidive.',
                         'en': "Ce moteur d'inférence propriétaire utilise une "
                               'analyse probabiliste pour classifier les '
                               'lithiases urinaires. En corrélant imagerie et '
                               'biologie, il fournit un diagnostic de '
                               'précision et des conseils de prévention '
                               'personnalisés, réduisant ainsi les taux de '
                               'récidive.',
                         'es': "Ce moteur d'inférence propriétaire utilise une "
                               'analyse probabiliste pour classifier les '
                               'lithiases urinaires. En corrélant imagerie et '
                               'biologie, il fournit un diagnostic de '
                               'précision et des conseils de prévention '
                               'personnalisés, réduisant ainsi les taux de '
                               'récidive.',
                         'pt': "Ce moteur d'inférence propriétaire utilise une "
                               'analyse probabiliste pour classifier les '
                               'lithiases urinaires. En corrélant imagerie et '
                               'biologie, il fournit un diagnostic de '
                               'précision et des conseils de prévention '
                               'personnalisés, réduisant ainsi les taux de '
                               'récidive.',
                         'it': "Ce moteur d'inférence propriétaire utilise une "
                               'analyse probabiliste pour classifier les '
                               'lithiases urinaires. En corrélant imagerie et '
                               'biologie, il fournit un diagnostic de '
                               'précision et des conseils de prévention '
                               'personnalisés, réduisant ainsi les taux de '
                               'récidive.',
                         'de': "Ce moteur d'inférence propriétaire utilise une "
                               'analyse probabiliste pour classifier les '
                               'lithiases urinaires. En corrélant imagerie et '
                               'biologie, il fournit un diagnostic de '
                               'précision et des conseils de prévention '
                               'personnalisés, réduisant ainsi les taux de '
                               'récidive.',
                         'ar': "Ce moteur d'inférence propriétaire utilise une "
                               'analyse probabiliste pour classifier les '
                               'lithiases urinaires. En corrélant imagerie et '
                               'biologie, il fournit un diagnostic de '
                               'précision et des conseils de prévention '
                               'personnalisés, réduisant ainsi les taux de '
                               'récidive.',
                         'zh': "Ce moteur d'inférence propriétaire utilise une "
                               'analyse probabiliste pour classifier les '
                               'lithiases urinaires. En corrélant imagerie et '
                               'biologie, il fournit un diagnostic de '
                               'précision et des conseils de prévention '
                               'personnalisés, réduisant ainsi les taux de '
                               'récidive.',
                         'ja': "Ce moteur d'inférence propriétaire utilise une "
                               'analyse probabiliste pour classifier les '
                               'lithiases urinaires. En corrélant imagerie et '
                               'biologie, il fournit un diagnostic de '
                               'précision et des conseils de prévention '
                               'personnalisés, réduisant ainsi les taux de '
                               'récidive.',
                         'ko': "Ce moteur d'inférence propriétaire utilise une "
                               'analyse probabiliste pour classifier les '
                               'lithiases urinaires. En corrélant imagerie et '
                               'biologie, il fournit un diagnostic de '
                               'précision et des conseils de prévention '
                               'personnalisés, réduisant ainsi les taux de '
                               'récidive.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Urgence Gabon',
                     'en': 'Urgence Gabon',
                     'es': 'Urgence Gabon',
                     'pt': 'Urgence Gabon',
                     'it': 'Urgence Gabon',
                     'de': 'Urgence Gabon',
                     'ar': 'Urgence Gabon',
                     'zh': 'Urgence Gabon',
                     'ja': 'Urgence Gabon',
                     'ko': 'Urgence Gabon'},
        'category': {   'fr': 'HealthTech',
                        'en': 'HealthTech',
                        'es': 'HealthTech',
                        'pt': 'HealthTech',
                        'it': 'HealthTech',
                        'de': 'HealthTech',
                        'ar': 'HealthTech',
                        'zh': 'HealthTech',
                        'ja': 'HealthTech',
                        'ko': 'HealthTech'},
        'short_desc': {   'fr': "Système d'optimisation logistique pour les "
                                'interventions médicales critiques, visant la '
                                'réduction du temps de réponse vital.',
                          'en': "Système d'optimisation logistique pour les "
                                'interventions médicales critiques, visant la '
                                'réduction du temps de réponse vital.',
                          'es': "Système d'optimisation logistique pour les "
                                'interventions médicales critiques, visant la '
                                'réduction du temps de réponse vital.',
                          'pt': "Système d'optimisation logistique pour les "
                                'interventions médicales critiques, visant la '
                                'réduction du temps de réponse vital.',
                          'it': "Système d'optimisation logistique pour les "
                                'interventions médicales critiques, visant la '
                                'réduction du temps de réponse vital.',
                          'de': "Système d'optimisation logistique pour les "
                                'interventions médicales critiques, visant la '
                                'réduction du temps de réponse vital.',
                          'ar': "Système d'optimisation logistique pour les "
                                'interventions médicales critiques, visant la '
                                'réduction du temps de réponse vital.',
                          'zh': "Système d'optimisation logistique pour les "
                                'interventions médicales critiques, visant la '
                                'réduction du temps de réponse vital.',
                          'ja': "Système d'optimisation logistique pour les "
                                'interventions médicales critiques, visant la '
                                'réduction du temps de réponse vital.',
                          'ko': "Système d'optimisation logistique pour les "
                                'interventions médicales critiques, visant la '
                                'réduction du temps de réponse vital.'},
        'full_desc': {   'fr': "Système d'optimisation logistique pour les "
                               'interventions médicales critiques, visant la '
                               'réduction du temps de réponse vital.',
                         'en': "Système d'optimisation logistique pour les "
                               'interventions médicales critiques, visant la '
                               'réduction du temps de réponse vital.',
                         'es': "Système d'optimisation logistique pour les "
                               'interventions médicales critiques, visant la '
                               'réduction du temps de réponse vital.',
                         'pt': "Système d'optimisation logistique pour les "
                               'interventions médicales critiques, visant la '
                               'réduction du temps de réponse vital.',
                         'it': "Système d'optimisation logistique pour les "
                               'interventions médicales critiques, visant la '
                               'réduction du temps de réponse vital.',
                         'de': "Système d'optimisation logistique pour les "
                               'interventions médicales critiques, visant la '
                               'réduction du temps de réponse vital.',
                         'ar': "Système d'optimisation logistique pour les "
                               'interventions médicales critiques, visant la '
                               'réduction du temps de réponse vital.',
                         'zh': "Système d'optimisation logistique pour les "
                               'interventions médicales critiques, visant la '
                               'réduction du temps de réponse vital.',
                         'ja': "Système d'optimisation logistique pour les "
                               'interventions médicales critiques, visant la '
                               'réduction du temps de réponse vital.',
                         'ko': "Système d'optimisation logistique pour les "
                               'interventions médicales critiques, visant la '
                               'réduction du temps de réponse vital.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'AI Journalist Manager',
                     'en': 'AI Journalist Manager',
                     'es': 'AI Journalist Manager',
                     'pt': 'AI Journalist Manager',
                     'it': 'AI Journalist Manager',
                     'de': 'AI Journalist Manager',
                     'ar': 'AI Journalist Manager',
                     'zh': 'AI Journalist Manager',
                     'ja': 'AI Journalist Manager',
                     'ko': 'AI Journalist Manager'},
        'category': {   'fr': 'Média, Retail et Quotidien',
                        'en': 'Média, Retail et Quotidien',
                        'es': 'Média, Retail et Quotidien',
                        'pt': 'Média, Retail et Quotidien',
                        'it': 'Média, Retail et Quotidien',
                        'de': 'Média, Retail et Quotidien',
                        'ar': 'Média, Retail et Quotidien',
                        'zh': 'Média, Retail et Quotidien',
                        'ja': 'Média, Retail et Quotidien',
                        'ko': 'Média, Retail et Quotidien'},
        'short_desc': {   'fr': 'Une plateforme de veille stratégique '
                                'multilingue intégrant les technologies '
                                'ElevenLabs pour le clonage vocal '
                                'ultra-réaliste et Perplexity pour la '
                                'validation factuelle en temps réel.',
                          'en': 'Une plateforme de veille stratégique '
                                'multilingue intégrant les technologies '
                                'ElevenLabs pour le clonage vocal '
                                'ultra-réaliste et Perplexity pour la '
                                'validation factuelle en temps réel.',
                          'es': 'Une plateforme de veille stratégique '
                                'multilingue intégrant les technologies '
                                'ElevenLabs pour le clonage vocal '
                                'ultra-réaliste et Perplexity pour la '
                                'validation factuelle en temps réel.',
                          'pt': 'Une plateforme de veille stratégique '
                                'multilingue intégrant les technologies '
                                'ElevenLabs pour le clonage vocal '
                                'ultra-réaliste et Perplexity pour la '
                                'validation factuelle en temps réel.',
                          'it': 'Une plateforme de veille stratégique '
                                'multilingue intégrant les technologies '
                                'ElevenLabs pour le clonage vocal '
                                'ultra-réaliste et Perplexity pour la '
                                'validation factuelle en temps réel.',
                          'de': 'Une plateforme de veille stratégique '
                                'multilingue intégrant les technologies '
                                'ElevenLabs pour le clonage vocal '
                                'ultra-réaliste et Perplexity pour la '
                                'validation factuelle en temps réel.',
                          'ar': 'Une plateforme de veille stratégique '
                                'multilingue intégrant les technologies '
                                'ElevenLabs pour le clonage vocal '
                                'ultra-réaliste et Perplexity pour la '
                                'validation factuelle en temps réel.',
                          'zh': 'Une plateforme de veille stratégique '
                                'multilingue intégrant les technologies '
                                'ElevenLabs pour le clonage vocal '
                                'ultra-réaliste et Perplexity pour la '
                                'validation factuelle en temps réel.',
                          'ja': 'Une plateforme de veille stratégique '
                                'multilingue intégrant les technologies '
                                'ElevenLabs pour le clonage vocal '
                                'ultra-réaliste et Perplexity pour la '
                                'validation factuelle en temps réel.',
                          'ko': 'Une plateforme de veille stratégique '
                                'multilingue intégrant les technologies '
                                'ElevenLabs pour le clonage vocal '
                                'ultra-réaliste et Perplexity pour la '
                                'validation factuelle en temps réel.'},
        'full_desc': {   'fr': 'Une plateforme de veille stratégique '
                               'multilingue intégrant les technologies '
                               'ElevenLabs pour le clonage vocal '
                               'ultra-réaliste et Perplexity pour la '
                               'validation factuelle en temps réel.',
                         'en': 'Une plateforme de veille stratégique '
                               'multilingue intégrant les technologies '
                               'ElevenLabs pour le clonage vocal '
                               'ultra-réaliste et Perplexity pour la '
                               'validation factuelle en temps réel.',
                         'es': 'Une plateforme de veille stratégique '
                               'multilingue intégrant les technologies '
                               'ElevenLabs pour le clonage vocal '
                               'ultra-réaliste et Perplexity pour la '
                               'validation factuelle en temps réel.',
                         'pt': 'Une plateforme de veille stratégique '
                               'multilingue intégrant les technologies '
                               'ElevenLabs pour le clonage vocal '
                               'ultra-réaliste et Perplexity pour la '
                               'validation factuelle en temps réel.',
                         'it': 'Une plateforme de veille stratégique '
                               'multilingue intégrant les technologies '
                               'ElevenLabs pour le clonage vocal '
                               'ultra-réaliste et Perplexity pour la '
                               'validation factuelle en temps réel.',
                         'de': 'Une plateforme de veille stratégique '
                               'multilingue intégrant les technologies '
                               'ElevenLabs pour le clonage vocal '
                               'ultra-réaliste et Perplexity pour la '
                               'validation factuelle en temps réel.',
                         'ar': 'Une plateforme de veille stratégique '
                               'multilingue intégrant les technologies '
                               'ElevenLabs pour le clonage vocal '
                               'ultra-réaliste et Perplexity pour la '
                               'validation factuelle en temps réel.',
                         'zh': 'Une plateforme de veille stratégique '
                               'multilingue intégrant les technologies '
                               'ElevenLabs pour le clonage vocal '
                               'ultra-réaliste et Perplexity pour la '
                               'validation factuelle en temps réel.',
                         'ja': 'Une plateforme de veille stratégique '
                               'multilingue intégrant les technologies '
                               'ElevenLabs pour le clonage vocal '
                               'ultra-réaliste et Perplexity pour la '
                               'validation factuelle en temps réel.',
                         'ko': 'Une plateforme de veille stratégique '
                               'multilingue intégrant les technologies '
                               'ElevenLabs pour le clonage vocal '
                               'ultra-réaliste et Perplexity pour la '
                               'validation factuelle en temps réel.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Hannout AI',
                     'en': 'Hannout AI',
                     'es': 'Hannout AI',
                     'pt': 'Hannout AI',
                     'it': 'Hannout AI',
                     'de': 'Hannout AI',
                     'ar': 'Hannout AI',
                     'zh': 'Hannout AI',
                     'ja': 'Hannout AI',
                     'ko': 'Hannout AI'},
        'category': {   'fr': 'Média, Retail et Quotidien',
                        'en': 'Média, Retail et Quotidien',
                        'es': 'Média, Retail et Quotidien',
                        'pt': 'Média, Retail et Quotidien',
                        'it': 'Média, Retail et Quotidien',
                        'de': 'Média, Retail et Quotidien',
                        'ar': 'Média, Retail et Quotidien',
                        'zh': 'Média, Retail et Quotidien',
                        'ja': 'Média, Retail et Quotidien',
                        'ko': 'Média, Retail et Quotidien'},
        'short_desc': {   'fr': 'Modernise le commerce de proximité grâce à la '
                                'reconnaissance visuelle automatique des '
                                'produits en caisse, fluidifiant le parcours '
                                'client sans saisie manuelle.',
                          'en': 'Modernise le commerce de proximité grâce à la '
                                'reconnaissance visuelle automatique des '
                                'produits en caisse, fluidifiant le parcours '
                                'client sans saisie manuelle.',
                          'es': 'Modernise le commerce de proximité grâce à la '
                                'reconnaissance visuelle automatique des '
                                'produits en caisse, fluidifiant le parcours '
                                'client sans saisie manuelle.',
                          'pt': 'Modernise le commerce de proximité grâce à la '
                                'reconnaissance visuelle automatique des '
                                'produits en caisse, fluidifiant le parcours '
                                'client sans saisie manuelle.',
                          'it': 'Modernise le commerce de proximité grâce à la '
                                'reconnaissance visuelle automatique des '
                                'produits en caisse, fluidifiant le parcours '
                                'client sans saisie manuelle.',
                          'de': 'Modernise le commerce de proximité grâce à la '
                                'reconnaissance visuelle automatique des '
                                'produits en caisse, fluidifiant le parcours '
                                'client sans saisie manuelle.',
                          'ar': 'Modernise le commerce de proximité grâce à la '
                                'reconnaissance visuelle automatique des '
                                'produits en caisse, fluidifiant le parcours '
                                'client sans saisie manuelle.',
                          'zh': 'Modernise le commerce de proximité grâce à la '
                                'reconnaissance visuelle automatique des '
                                'produits en caisse, fluidifiant le parcours '
                                'client sans saisie manuelle.',
                          'ja': 'Modernise le commerce de proximité grâce à la '
                                'reconnaissance visuelle automatique des '
                                'produits en caisse, fluidifiant le parcours '
                                'client sans saisie manuelle.',
                          'ko': 'Modernise le commerce de proximité grâce à la '
                                'reconnaissance visuelle automatique des '
                                'produits en caisse, fluidifiant le parcours '
                                'client sans saisie manuelle.'},
        'full_desc': {   'fr': 'Modernise le commerce de proximité grâce à la '
                               'reconnaissance visuelle automatique des '
                               'produits en caisse, fluidifiant le parcours '
                               'client sans saisie manuelle.',
                         'en': 'Modernise le commerce de proximité grâce à la '
                               'reconnaissance visuelle automatique des '
                               'produits en caisse, fluidifiant le parcours '
                               'client sans saisie manuelle.',
                         'es': 'Modernise le commerce de proximité grâce à la '
                               'reconnaissance visuelle automatique des '
                               'produits en caisse, fluidifiant le parcours '
                               'client sans saisie manuelle.',
                         'pt': 'Modernise le commerce de proximité grâce à la '
                               'reconnaissance visuelle automatique des '
                               'produits en caisse, fluidifiant le parcours '
                               'client sans saisie manuelle.',
                         'it': 'Modernise le commerce de proximité grâce à la '
                               'reconnaissance visuelle automatique des '
                               'produits en caisse, fluidifiant le parcours '
                               'client sans saisie manuelle.',
                         'de': 'Modernise le commerce de proximité grâce à la '
                               'reconnaissance visuelle automatique des '
                               'produits en caisse, fluidifiant le parcours '
                               'client sans saisie manuelle.',
                         'ar': 'Modernise le commerce de proximité grâce à la '
                               'reconnaissance visuelle automatique des '
                               'produits en caisse, fluidifiant le parcours '
                               'client sans saisie manuelle.',
                         'zh': 'Modernise le commerce de proximité grâce à la '
                               'reconnaissance visuelle automatique des '
                               'produits en caisse, fluidifiant le parcours '
                               'client sans saisie manuelle.',
                         'ja': 'Modernise le commerce de proximité grâce à la '
                               'reconnaissance visuelle automatique des '
                               'produits en caisse, fluidifiant le parcours '
                               'client sans saisie manuelle.',
                         'ko': 'Modernise le commerce de proximité grâce à la '
                               'reconnaissance visuelle automatique des '
                               'produits en caisse, fluidifiant le parcours '
                               'client sans saisie manuelle.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Disparus.org',
                     'en': 'Disparus.org',
                     'es': 'Disparus.org',
                     'pt': 'Disparus.org',
                     'it': 'Disparus.org',
                     'de': 'Disparus.org',
                     'ar': 'Disparus.org',
                     'zh': 'Disparus.org',
                     'ja': 'Disparus.org',
                     'ko': 'Disparus.org'},
        'category': {   'fr': 'Média, Retail et Quotidien',
                        'en': 'Média, Retail et Quotidien',
                        'es': 'Média, Retail et Quotidien',
                        'pt': 'Média, Retail et Quotidien',
                        'it': 'Média, Retail et Quotidien',
                        'de': 'Média, Retail et Quotidien',
                        'ar': 'Média, Retail et Quotidien',
                        'zh': 'Média, Retail et Quotidien',
                        'ja': 'Média, Retail et Quotidien',
                        'ko': 'Média, Retail et Quotidien'},
        'short_desc': {   'fr': 'Une solution à fort impact social utilisant '
                                "l'IA pour la génération automatique de "
                                'visuels optimisés pour les réseaux sociaux et '
                                "d'affiches munies de QR Codes dynamiques pour "
                                'les avis de recherche.',
                          'en': 'Une solution à fort impact social utilisant '
                                "l'IA pour la génération automatique de "
                                'visuels optimisés pour les réseaux sociaux et '
                                "d'affiches munies de QR Codes dynamiques pour "
                                'les avis de recherche.',
                          'es': 'Une solution à fort impact social utilisant '
                                "l'IA pour la génération automatique de "
                                'visuels optimisés pour les réseaux sociaux et '
                                "d'affiches munies de QR Codes dynamiques pour "
                                'les avis de recherche.',
                          'pt': 'Une solution à fort impact social utilisant '
                                "l'IA pour la génération automatique de "
                                'visuels optimisés pour les réseaux sociaux et '
                                "d'affiches munies de QR Codes dynamiques pour "
                                'les avis de recherche.',
                          'it': 'Une solution à fort impact social utilisant '
                                "l'IA pour la génération automatique de "
                                'visuels optimisés pour les réseaux sociaux et '
                                "d'affiches munies de QR Codes dynamiques pour "
                                'les avis de recherche.',
                          'de': 'Une solution à fort impact social utilisant '
                                "l'IA pour la génération automatique de "
                                'visuels optimisés pour les réseaux sociaux et '
                                "d'affiches munies de QR Codes dynamiques pour "
                                'les avis de recherche.',
                          'ar': 'Une solution à fort impact social utilisant '
                                "l'IA pour la génération automatique de "
                                'visuels optimisés pour les réseaux sociaux et '
                                "d'affiches munies de QR Codes dynamiques pour "
                                'les avis de recherche.',
                          'zh': 'Une solution à fort impact social utilisant '
                                "l'IA pour la génération automatique de "
                                'visuels optimisés pour les réseaux sociaux et '
                                "d'affiches munies de QR Codes dynamiques pour "
                                'les avis de recherche.',
                          'ja': 'Une solution à fort impact social utilisant '
                                "l'IA pour la génération automatique de "
                                'visuels optimisés pour les réseaux sociaux et '
                                "d'affiches munies de QR Codes dynamiques pour "
                                'les avis de recherche.',
                          'ko': 'Une solution à fort impact social utilisant '
                                "l'IA pour la génération automatique de "
                                'visuels optimisés pour les réseaux sociaux et '
                                "d'affiches munies de QR Codes dynamiques pour "
                                'les avis de recherche.'},
        'full_desc': {   'fr': 'Une solution à fort impact social utilisant '
                               "l'IA pour la génération automatique de visuels "
                               'optimisés pour les réseaux sociaux et '
                               "d'affiches munies de QR Codes dynamiques pour "
                               'les avis de recherche.',
                         'en': 'Une solution à fort impact social utilisant '
                               "l'IA pour la génération automatique de visuels "
                               'optimisés pour les réseaux sociaux et '
                               "d'affiches munies de QR Codes dynamiques pour "
                               'les avis de recherche.',
                         'es': 'Une solution à fort impact social utilisant '
                               "l'IA pour la génération automatique de visuels "
                               'optimisés pour les réseaux sociaux et '
                               "d'affiches munies de QR Codes dynamiques pour "
                               'les avis de recherche.',
                         'pt': 'Une solution à fort impact social utilisant '
                               "l'IA pour la génération automatique de visuels "
                               'optimisés pour les réseaux sociaux et '
                               "d'affiches munies de QR Codes dynamiques pour "
                               'les avis de recherche.',
                         'it': 'Une solution à fort impact social utilisant '
                               "l'IA pour la génération automatique de visuels "
                               'optimisés pour les réseaux sociaux et '
                               "d'affiches munies de QR Codes dynamiques pour "
                               'les avis de recherche.',
                         'de': 'Une solution à fort impact social utilisant '
                               "l'IA pour la génération automatique de visuels "
                               'optimisés pour les réseaux sociaux et '
                               "d'affiches munies de QR Codes dynamiques pour "
                               'les avis de recherche.',
                         'ar': 'Une solution à fort impact social utilisant '
                               "l'IA pour la génération automatique de visuels "
                               'optimisés pour les réseaux sociaux et '
                               "d'affiches munies de QR Codes dynamiques pour "
                               'les avis de recherche.',
                         'zh': 'Une solution à fort impact social utilisant '
                               "l'IA pour la génération automatique de visuels "
                               'optimisés pour les réseaux sociaux et '
                               "d'affiches munies de QR Codes dynamiques pour "
                               'les avis de recherche.',
                         'ja': 'Une solution à fort impact social utilisant '
                               "l'IA pour la génération automatique de visuels "
                               'optimisés pour les réseaux sociaux et '
                               "d'affiches munies de QR Codes dynamiques pour "
                               'les avis de recherche.',
                         'ko': 'Une solution à fort impact social utilisant '
                               "l'IA pour la génération automatique de visuels "
                               'optimisés pour les réseaux sociaux et '
                               "d'affiches munies de QR Codes dynamiques pour "
                               'les avis de recherche.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Talento',
                     'en': 'Talento',
                     'es': 'Talento',
                     'pt': 'Talento',
                     'it': 'Talento',
                     'de': 'Talento',
                     'ar': 'Talento',
                     'zh': 'Talento',
                     'ja': 'Talento',
                     'ko': 'Talento'},
        'category': {   'fr': 'Média, Retail et Quotidien',
                        'en': 'Média, Retail et Quotidien',
                        'es': 'Média, Retail et Quotidien',
                        'pt': 'Média, Retail et Quotidien',
                        'it': 'Média, Retail et Quotidien',
                        'de': 'Média, Retail et Quotidien',
                        'ar': 'Média, Retail et Quotidien',
                        'zh': 'Média, Retail et Quotidien',
                        'ja': 'Média, Retail et Quotidien',
                        'ko': 'Média, Retail et Quotidien'},
        'short_desc': {   'fr': 'Matching intelligent de talents par analyse '
                                'sémantique de CV.',
                          'en': 'Matching intelligent de talents par analyse '
                                'sémantique de CV.',
                          'es': 'Matching intelligent de talents par analyse '
                                'sémantique de CV.',
                          'pt': 'Matching intelligent de talents par analyse '
                                'sémantique de CV.',
                          'it': 'Matching intelligent de talents par analyse '
                                'sémantique de CV.',
                          'de': 'Matching intelligent de talents par analyse '
                                'sémantique de CV.',
                          'ar': 'Matching intelligent de talents par analyse '
                                'sémantique de CV.',
                          'zh': 'Matching intelligent de talents par analyse '
                                'sémantique de CV.',
                          'ja': 'Matching intelligent de talents par analyse '
                                'sémantique de CV.',
                          'ko': 'Matching intelligent de talents par analyse '
                                'sémantique de CV.'},
        'full_desc': {   'fr': 'Matching intelligent de talents par analyse '
                               'sémantique de CV.',
                         'en': 'Matching intelligent de talents par analyse '
                               'sémantique de CV.',
                         'es': 'Matching intelligent de talents par analyse '
                               'sémantique de CV.',
                         'pt': 'Matching intelligent de talents par analyse '
                               'sémantique de CV.',
                         'it': 'Matching intelligent de talents par analyse '
                               'sémantique de CV.',
                         'de': 'Matching intelligent de talents par analyse '
                               'sémantique de CV.',
                         'ar': 'Matching intelligent de talents par analyse '
                               'sémantique de CV.',
                         'zh': 'Matching intelligent de talents par analyse '
                               'sémantique de CV.',
                         'ja': 'Matching intelligent de talents par analyse '
                               'sémantique de CV.',
                         'ko': 'Matching intelligent de talents par analyse '
                               'sémantique de CV.'},
        'project_url': 'https://www.shabakainnovlab.com/'},
    {   'title': {   'fr': 'Quick Receipt',
                     'en': 'Quick Receipt',
                     'es': 'Quick Receipt',
                     'pt': 'Quick Receipt',
                     'it': 'Quick Receipt',
                     'de': 'Quick Receipt',
                     'ar': 'Quick Receipt',
                     'zh': 'Quick Receipt',
                     'ja': 'Quick Receipt',
                     'ko': 'Quick Receipt'},
        'category': {   'fr': 'Média, Retail et Quotidien',
                        'en': 'Média, Retail et Quotidien',
                        'es': 'Média, Retail et Quotidien',
                        'pt': 'Média, Retail et Quotidien',
                        'it': 'Média, Retail et Quotidien',
                        'de': 'Média, Retail et Quotidien',
                        'ar': 'Média, Retail et Quotidien',
                        'zh': 'Média, Retail et Quotidien',
                        'ja': 'Média, Retail et Quotidien',
                        'ko': 'Média, Retail et Quotidien'},
        'short_desc': {   'fr': 'Simplification transactionnelle via '
                                'quittances thermiques et WhatsApp.',
                          'en': 'Simplification transactionnelle via '
                                'quittances thermiques et WhatsApp.',
                          'es': 'Simplification transactionnelle via '
                                'quittances thermiques et WhatsApp.',
                          'pt': 'Simplification transactionnelle via '
                                'quittances thermiques et WhatsApp.',
                          'it': 'Simplification transactionnelle via '
                                'quittances thermiques et WhatsApp.',
                          'de': 'Simplification transactionnelle via '
                                'quittances thermiques et WhatsApp.',
                          'ar': 'Simplification transactionnelle via '
                                'quittances thermiques et WhatsApp.',
                          'zh': 'Simplification transactionnelle via '
                                'quittances thermiques et WhatsApp.',
                          'ja': 'Simplification transactionnelle via '
                                'quittances thermiques et WhatsApp.',
                          'ko': 'Simplification transactionnelle via '
                                'quittances thermiques et WhatsApp.'},
        'full_desc': {   'fr': 'Simplification transactionnelle via quittances '
                               'thermiques et WhatsApp.',
                         'en': 'Simplification transactionnelle via quittances '
                               'thermiques et WhatsApp.',
                         'es': 'Simplification transactionnelle via quittances '
                               'thermiques et WhatsApp.',
                         'pt': 'Simplification transactionnelle via quittances '
                               'thermiques et WhatsApp.',
                         'it': 'Simplification transactionnelle via quittances '
                               'thermiques et WhatsApp.',
                         'de': 'Simplification transactionnelle via quittances '
                               'thermiques et WhatsApp.',
                         'ar': 'Simplification transactionnelle via quittances '
                               'thermiques et WhatsApp.',
                         'zh': 'Simplification transactionnelle via quittances '
                               'thermiques et WhatsApp.',
                         'ja': 'Simplification transactionnelle via quittances '
                               'thermiques et WhatsApp.',
                         'ko': 'Simplification transactionnelle via quittances '
                               'thermiques et WhatsApp.'},
        'project_url': 'https://www.shabakainnovlab.com/'}]



        for p_data in projects:
            project = PortfolioProject(
                title=p_data['title'],
                category=p_data['category'],
                short_desc=p_data['short_desc'],
                full_desc=p_data['full_desc'],
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
