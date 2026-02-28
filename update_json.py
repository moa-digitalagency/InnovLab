import json
import os
import re
from glob import glob

# Collect hardcoded french text and map to translation keys
translations = {
    # base.html
    "footer": {
        "description": "Le hub d'innovation de Shabaka Invest Group. Nous transformons les idées audacieuses en leaders technologiques continentaux.",
        "quick_links": "Liens Rapides",
        "legal": "Légal",
        "contact": "Contact",
        "privacy_policy": "Politique de Confidentialité",
        "terms_conditions": "Conditions Générales",
        "admin": "Admin",
        "powered_by": "Propulsé par",
        "all_rights_reserved": "Tous droits réservés."
    },

    # index.html
    "hero": {
        "badge": "Innovation par la collaboration",
        "title": "Construire <br/> le <span class=\"text-transparent bg-clip-text bg-gradient-to-r from-[#1d5865] via-[#30a192] to-[#1d5865] bg-[length:200%_auto] animate-[gradient_4s_linear_infinite]\">Futur Technologique</span> <br/> de l'Afrique.",
        "description": "Déployez des solutions d'avant-garde à travers un partenariat intégré. Nous fusionnons notre expertise R&D avec vos ambitions pour transformer durablement votre avantage compétitif.",
        "founder_title": "Je suis Fondateur",
        "founder_desc": "Accélérez votre vision",
        "startup_title": "Je suis Startup",
        "startup_desc": "Changez l'échelle",
        "investor_title": "Je suis Investisseur",
        "investor_desc": "Financez l'impact"
    },

    "about_section": {
        "badge": "Qui sommes-nous ?",
        "title": "Le hub entrepreneurial qui transforme les idées en <span class=\"text-[#30a192]\">leaders de demain.</span>",
        "description": "Shabaka InnovLab est la filiale dédiée à l'innovation technologique de <strong class=\"text-[#15344b]\">Shabaka Invest Group</strong>. Conçue pour positionner Marrakech comme un pôle régional d'excellence, notre structure agit comme un catalyseur de croissance inédit.",
        "btn_submit": "Soumettre un projet",
        "btn_more": "En savoir plus",
        "card_title": "Un Écosystème Global",
        "card_desc": "Nous créons un pont solide entre les startups, les investisseurs institutionnels et le secteur privé pour générer une création de valeur partagée (Win-Win).",
        "card_badge_title": "Acteur Clé",
        "card_badge_desc": "Innovation Africaine"
    },

    "journey": {
        "badge": "La route vers le sommet",
        "title": "Votre Journey Entrepreneuriale",
        "description": "Un parcours clair, séquencé et soutenu pour passer de l'idée à l'impact mondial.",
        "step1_title": "L'Étincelle",
        "step1_desc": "Notre Studio Dev transforme votre concept en un MVP robuste et évolutif.",
        "step1_label": "ÉTAPE 01",
        "step2_title": "L'Armure",
        "step2_desc": "Intégration native de l'IA et cybersécurité pour une confiance totale du marché.",
        "step2_label": "ÉTAPE 02",
        "step3_title": "Le Décollage",
        "step3_desc": "Programme intensif de 3-6 mois pour dominer votre Go-to-Market.",
        "step3_label": "ÉTAPE 03",
        "step4_title": "La Sérénité",
        "step4_desc": "Ingénierie légale et fiscale proactive pour protéger votre croissance.",
        "step4_label": "ÉTAPE 04",
        "step5_title": "L'Expansion",
        "step5_desc": "Accès direct au capital de Shabaka Invest et au réseau mondial.",
        "step5_label": "ÉTAPE 05",
        "btn_start": "Démarrer votre étape 01"
    },

    "startups": {
        "badge": "Pour les Startups",
        "title": "Accélérez votre Croissance",
        "description": "Transformez votre potentiel en leadership. Nous connectons votre agilité à notre puissance réseau pour multiplier vos opportunités de marché.",
        "market_access": "Accès Marché",
        "market_access_desc": "Connexions stratégiques avec les grands comptes et partenaires clés.",
        "tech_support": "Support Technique",
        "tech_support_desc": "Accès à nos infrastructures et experts pour sécuriser votre scale-up.",
        "btn_apply": "Postuler au programme d'incubation",
        "dashboard_title": "Scale-up Ready",
        "dashboard_subtitle": "Indice de potentiel de croissance",
        "product_maturity": "Maturité Produit",
        "market_traction": "Traction Marché",
        "quote": "\"Nous transformons les startups prometteuses en champions continentaux.\"",
        "operational_systems": "Systèmes Opérationnels"
    },

    "why_us": {
        "approach_title": "L'Approche<br/>\"Zéro Friction\"",
        "approach_quote": "\"Le succès d'une idée dépend de l'absence de résistance à son mouvement.\"",
        "approach_desc": "Notre mission est simple : nous gérons la complexité (technique, juridique, financière) pour que vous puissiez vous concentrer exclusivement sur votre vision.",
        "powered_by": "Propulsé par<br/>Shabaka Invest Group",
        "badge": "Pourquoi nous ?",
        "title": "Une Communauté<br/>de Bâtisseurs",
        "expertise": "Expertise Partagée",
        "expertise_desc": "Bénéficiez des leçons apprises par nos fondateurs seniors.",
        "speed": "Vitesse d'Exécution",
        "speed_desc": "Passez du prototype au marché en un temps record.",
        "network": "Réseau Panafricain",
        "network_desc": "Un tremplin vers les marchés stratégiques du continent."
    },

    "infrastructure": {
        "badge": "Infrastructure & Ressources",
        "title": "L'Espace InnovLab",
        "description": "L'accès à nos infrastructures est conçu non pas comme une location, mais comme une ressource stratégique mise à la disposition exclusive des projets incubés pour maximiser leur productivité.",
        "coworking": "Espaces de Coworking<br/>Collaboratif",
        "coworking_desc": "Des zones de travail ouvertes et modulables, conçues pour encourager les échanges, le partage de compétences et la collaboration spontanée entre les porteurs de projets.",
        "open_space": "Bureaux<br/>(Open-Space)",
        "open_space_desc": "Des plateaux de travail dédiés aux équipes projet en phase de développement favorisant une immersion totale dans la dynamique collective, sans barrières.",
        "meeting_rooms": "Salles de Réunion &<br/>Brainstorming",
        "meeting_rooms_desc": "Des espaces équipés de technologies de présentation mis à disposition des incubés pour leurs sessions de travail stratégiques et rencontres investisseurs.",
        "btn_visit": "Planifier une visite de l'espace"
    },

    "sis": {
        "badge": "Filiale Technologique",
        "title": "Shabaka Intelligence Systems (SIS)",
        "description": "Shabaka InnovLab détient et pilote sa propre structure technologique de pointe. Détenue majoritairement par l'incubateur, SIS est une Société par Actions Simplifiée (SAS) qui agit comme le moteur R&D du groupe.",
        "sovereignty": "Souveraineté<br/>Numérique",
        "sovereignty_desc": "Création de solutions IA adaptées aux spécificités du marché marocain et africain.",
        "hardware": "Hardware &<br/>Software",
        "hardware_desc": "Recherche et développement de matériel propriétaire et de logiciels avancés.",
        "integration": "Intégration<br/>Métier",
        "integration_desc": "Déploiement de l'IA dans les secteurs clés (immobilier, énergie, santé, juridique)."
    },

    "solutions": {
        "badge": "Solutions Avancées",
        "title": "Nos Pôles d'Excellence<br/>Corporate",
        "description": "Des infrastructures logicielles robustes et modulables, prêtes à être déployées au sein de vos architectures existantes.",
        "ai": "Intelligence<br/>Synthétique",
        "ai_desc": "Moteurs d'IA générative et prédictive adaptés aux spécificités de votre secteur métier.",
        "cyber": "Forteresse<br/>Cyber",
        "cyber_desc": "Architectures Zero-Trust et protection proactive des données stratégiques africaines.",
        "networks": "Réseaux<br/>Connectés",
        "networks_desc": "Écosystèmes IoT et API unifiées pour une interopérabilité totale de vos services.",
        "tailored": "Tailored<br/>Tech",
        "tailored_desc": "Développement sur mesure de briques logicielles critiques pour vos métiers.",
        "expertise_label": "Expertise",
        "btn_consultation": "Demander une consultation technique"
    },

    "external_services": {
        "badge": "Ouvert aux entreprises externes",
        "title": "Votre Partenaire de<br/>Transformation Digitale",
        "description": "Au-delà de l'incubation, la force de frappe de Shabaka InnovLab est à votre disposition. Que vous soyez une PME ou un grand compte, nous mettons notre écosystème d'experts au service de vos projets technologiques.",
        "btn_launch": "Lancer un projet",
        "btn_catalog": "Voir le catalogue complet",
        "dev_studio": "Studio Dev Web & Mobile",
        "dev_studio_desc": "Développement sur mesure de plateformes (Web, Mobile, E-commerce) et ingénierie logicielle pour des architectures robustes et évolutives.",
        "ai_cyber": "Expertise IA & Cybersécurité",
        "ai_cyber_desc": "Automatisation des processus, intégration de solutions IA et protection absolue de vos données stratégiques.",
        "academy": "Conseil & Shabaka Academy",
        "academy_desc": "Appui stratégique (marketing, gestion), et formations certifiantes en nouvelles technologies pour vos équipes."
    },

    "portfolio_section": {
        "badge": "Portfolio Stratégique",
        "title": "Nos Forteresses Sectorielles",
        "description": "Des solutions verticales propriétaires conçues pour dominer des marchés spécifiques.",
        "proptech": "PropTech",
        "proptech_desc": "Révolutionner la gestion immobilière et le BTP.",
        "legaltech": "LegalTech",
        "legaltech_desc": "Sécuriser les arguments juridiques par l'IA.",
        "healthtech": "HealthTech",
        "healthtech_desc": "Optimisation logistique et aide au diagnostic.",
        "media": "Média & Retail",
        "media_desc": "Agilité digitale et veille stratégique IA.",
        "flagship": "Flagship Product",
        "btn_start": "Démarrer un Projet",
        "btn_explore": "Explorer les Forteresses"
    },

    "testimonials": {
        "title": "Échos de l'Écosystème",
        "description": "Ils bâtissent l'Afrique de demain avec Shabaka InnovLab.",
        "label_testimonial": "Témoignage",
        "label_featured": "À la une"
    },

    "contact_page": {
        "title": "Contact",
        "subtitle": "Contactez notre équipe",
        "description": "Prêt à transformer votre vision en réalité ? Notre équipe est à votre disposition pour discuter de vos projets et ambitions.",
        "contact_info": "Informations de Contact",
        "email_us": "Écrivez-nous",
        "call_us": "Appelez-nous",
        "visit_us": "Rendez-nous visite",
        "form_title": "Envoyez-nous un message",
        "form_desc": "Remplissez le formulaire ci-dessous et nous vous répondrons dans les plus brefs délais.",
        "label_name": "Nom complet",
        "label_email": "Adresse email",
        "label_phone": "Téléphone",
        "label_subject": "Sujet de votre message",
        "label_message": "Votre message",
        "placeholder_name": "John Doe",
        "placeholder_email": "john@example.com",
        "placeholder_phone": "+212 600 000 000",
        "placeholder_subject": "Comment pouvons-nous vous aider ?",
        "placeholder_message": "Détaillez votre projet ou votre demande ici...",
        "btn_submit": "Envoyer le Message"
    }
}

en_translations = {
    # base.html
    "footer": {
        "description": "Shabaka Invest Group's innovation hub. We transform bold ideas into continental technology leaders.",
        "quick_links": "Quick Links",
        "legal": "Legal",
        "contact": "Contact",
        "privacy_policy": "Privacy Policy",
        "terms_conditions": "Terms & Conditions",
        "admin": "Admin",
        "powered_by": "Powered by",
        "all_rights_reserved": "All rights reserved."
    },

    # index.html
    "hero": {
        "badge": "Innovation through collaboration",
        "title": "Building <br/> Africa's <br/> <span class=\"text-transparent bg-clip-text bg-gradient-to-r from-[#1d5865] via-[#30a192] to-[#1d5865] bg-[length:200%_auto] animate-[gradient_4s_linear_infinite]\">Technological Future</span>.",
        "description": "Deploy cutting-edge solutions through an integrated partnership. We merge our R&D expertise with your ambitions to sustainably transform your competitive advantage.",
        "founder_title": "I am a Founder",
        "founder_desc": "Accelerate your vision",
        "startup_title": "I am a Startup",
        "startup_desc": "Scale up",
        "investor_title": "I am an Investor",
        "investor_desc": "Fund impact"
    },

    "about_section": {
        "badge": "Who are we?",
        "title": "The entrepreneurial hub that transforms ideas into <span class=\"text-[#30a192]\">tomorrow's leaders.</span>",
        "description": "Shabaka InnovLab is the dedicated technological innovation subsidiary of <strong class=\"text-[#15344b]\">Shabaka Invest Group</strong>. Designed to position Marrakech as a regional center of excellence, our structure acts as an unprecedented growth catalyst.",
        "btn_submit": "Submit a project",
        "btn_more": "Learn more",
        "card_title": "A Global Ecosystem",
        "card_desc": "We create a solid bridge between startups, institutional investors, and the private sector to generate shared value creation (Win-Win).",
        "card_badge_title": "Key Player",
        "card_badge_desc": "African Innovation"
    },

    "journey": {
        "badge": "The road to the top",
        "title": "Your Entrepreneurial Journey",
        "description": "A clear, sequenced, and supported path to go from idea to global impact.",
        "step1_title": "The Spark",
        "step1_desc": "Our Dev Studio transforms your concept into a robust and scalable MVP.",
        "step1_label": "STEP 01",
        "step2_title": "The Armor",
        "step2_desc": "Native integration of AI and cybersecurity for total market trust.",
        "step2_label": "STEP 02",
        "step3_title": "Liftoff",
        "step3_desc": "Intensive 3-6 month program to dominate your Go-to-Market.",
        "step3_label": "STEP 03",
        "step4_title": "Serenity",
        "step4_desc": "Proactive legal and fiscal engineering to protect your growth.",
        "step4_label": "STEP 04",
        "step5_title": "Expansion",
        "step5_desc": "Direct access to Shabaka Invest capital and the global network.",
        "step5_label": "STEP 05",
        "btn_start": "Start your step 01"
    },

    "startups": {
        "badge": "For Startups",
        "title": "Accelerate your Growth",
        "description": "Transform your potential into leadership. We connect your agility to our network power to multiply your market opportunities.",
        "market_access": "Market Access",
        "market_access_desc": "Strategic connections with key accounts and key partners.",
        "tech_support": "Technical Support",
        "tech_support_desc": "Access to our infrastructure and experts to secure your scale-up.",
        "btn_apply": "Apply to the incubation program",
        "dashboard_title": "Scale-up Ready",
        "dashboard_subtitle": "Growth potential index",
        "product_maturity": "Product Maturity",
        "market_traction": "Market Traction",
        "quote": "\"We transform promising startups into continental champions.\"",
        "operational_systems": "Operational Systems"
    },

    "why_us": {
        "approach_title": "The<br/>\"Zero Friction\" Approach",
        "approach_quote": "\"The success of an idea depends on the absence of resistance to its movement.\"",
        "approach_desc": "Our mission is simple: we manage the complexity (technical, legal, financial) so you can focus exclusively on your vision.",
        "powered_by": "Powered by<br/>Shabaka Invest Group",
        "badge": "Why us?",
        "title": "A Community<br/>of Builders",
        "expertise": "Shared Expertise",
        "expertise_desc": "Benefit from the lessons learned by our senior founders.",
        "speed": "Speed of Execution",
        "speed_desc": "Go from prototype to market in record time.",
        "network": "Pan-African Network",
        "network_desc": "A springboard to the continent's strategic markets."
    },

    "infrastructure": {
        "badge": "Infrastructure & Resources",
        "title": "The InnovLab Space",
        "description": "Access to our infrastructure is designed not as a rental, but as a strategic resource made exclusively available to incubated projects to maximize their productivity.",
        "coworking": "Collaborative<br/>Coworking Spaces",
        "coworking_desc": "Open and modular workspaces, designed to encourage exchanges, skill sharing, and spontaneous collaboration between project leaders.",
        "open_space": "Offices<br/>(Open-Space)",
        "open_space_desc": "Dedicated work floors for project teams in the development phase, promoting total immersion in the collective dynamic, without barriers.",
        "meeting_rooms": "Meeting &<br/>Brainstorming Rooms",
        "meeting_rooms_desc": "Spaces equipped with presentation technologies made available to incubatees for their strategic work sessions and investor meetings.",
        "btn_visit": "Schedule a visit to the space"
    },

    "sis": {
        "badge": "Technological Subsidiary",
        "title": "Shabaka Intelligence Systems (SIS)",
        "description": "Shabaka InnovLab owns and pilots its own cutting-edge technological structure. Majority-owned by the incubator, SIS is a Simplified Joint Stock Company (SAS) that acts as the group's R&D engine.",
        "sovereignty": "Digital<br/>Sovereignty",
        "sovereignty_desc": "Creation of AI solutions adapted to the specificities of the Moroccan and African markets.",
        "hardware": "Hardware &<br/>Software",
        "hardware_desc": "Research and development of proprietary hardware and advanced software.",
        "integration": "Business<br/>Integration",
        "integration_desc": "Deployment of AI in key sectors (real estate, energy, health, legal)."
    },

    "solutions": {
        "badge": "Advanced Solutions",
        "title": "Our Corporate<br/>Centers of Excellence",
        "description": "Robust and modular software infrastructures, ready to be deployed within your existing architectures.",
        "ai": "Synthetic<br/>Intelligence",
        "ai_desc": "Generative and predictive AI engines adapted to the specificities of your business sector.",
        "cyber": "Cyber<br/>Fortress",
        "cyber_desc": "Zero-Trust architectures and proactive protection of African strategic data.",
        "networks": "Connected<br/>Networks",
        "networks_desc": "IoT ecosystems and unified APIs for total interoperability of your services.",
        "tailored": "Tailored<br/>Tech",
        "tailored_desc": "Custom development of critical software building blocks for your businesses.",
        "expertise_label": "Expertise",
        "btn_consultation": "Request a technical consultation"
    },

    "external_services": {
        "badge": "Open to external companies",
        "title": "Your Digital Transformation<br/>Partner",
        "description": "Beyond incubation, Shabaka InnovLab's striking force is at your disposal. Whether you are an SME or a large account, we put our ecosystem of experts at the service of your technological projects.",
        "btn_launch": "Launch a project",
        "btn_catalog": "View the full catalog",
        "dev_studio": "Web & Mobile Dev Studio",
        "dev_studio_desc": "Custom development of platforms (Web, Mobile, E-commerce) and software engineering for robust and scalable architectures.",
        "ai_cyber": "AI & Cybersecurity Expertise",
        "ai_cyber_desc": "Process automation, integration of AI solutions, and absolute protection of your strategic data.",
        "academy": "Consulting & Shabaka Academy",
        "academy_desc": "Strategic support (marketing, management), and certifying training in new technologies for your teams."
    },

    "portfolio_section": {
        "badge": "Strategic Portfolio",
        "title": "Our Sector Fortresses",
        "description": "Proprietary vertical solutions designed to dominate specific markets.",
        "proptech": "PropTech",
        "proptech_desc": "Revolutionizing real estate management and construction.",
        "legaltech": "LegalTech",
        "legaltech_desc": "Securing legal arguments through AI.",
        "healthtech": "HealthTech",
        "healthtech_desc": "Logistics optimization and diagnostic assistance.",
        "media": "Media & Retail",
        "media_desc": "Digital agility and strategic AI monitoring.",
        "flagship": "Flagship Product",
        "btn_start": "Start a Project",
        "btn_explore": "Explore the Fortresses"
    },

    "testimonials": {
        "title": "Echoes of the Ecosystem",
        "description": "They are building tomorrow's Africa with Shabaka InnovLab.",
        "label_testimonial": "Testimonial",
        "label_featured": "Featured"
    },

    "contact_page": {
        "title": "Contact",
        "subtitle": "Contact our team",
        "description": "Ready to turn your vision into reality? Our team is at your disposal to discuss your projects and ambitions.",
        "contact_info": "Contact Information",
        "email_us": "Email Us",
        "call_us": "Call Us",
        "visit_us": "Visit Us",
        "form_title": "Send us a message",
        "form_desc": "Fill out the form below and we will get back to you as soon as possible.",
        "label_name": "Full Name",
        "label_email": "Email Address",
        "label_phone": "Phone",
        "label_subject": "Subject of your message",
        "label_message": "Your message",
        "placeholder_name": "John Doe",
        "placeholder_email": "john@example.com",
        "placeholder_phone": "+212 600 000 000",
        "placeholder_subject": "How can we help you?",
        "placeholder_message": "Detail your project or request here...",
        "btn_submit": "Send Message"
    }
}

# Update existing files
with open("lang/fr.json", "r") as f:
    fr_data = json.load(f)

with open("lang/en.json", "r") as f:
    en_data = json.load(f)

fr_data.update(translations)
en_data.update(en_translations)

with open("lang/fr.json", "w") as f:
    json.dump(fr_data, f, indent=4, ensure_ascii=False)

with open("lang/en.json", "w") as f:
    json.dump(en_data, f, indent=4, ensure_ascii=False)
