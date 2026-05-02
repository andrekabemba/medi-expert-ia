from typing import List, Dict

# Base de connaissances optimisée : 5 pathologies courantes avec un ton constructif
DISEASES: List[Dict] = [
    {
        "name": "Rhume Commun",
        "symptoms": ["Nez bouché", "Éternuements", "Écoulement nasal"],
        "gravity": "Légère",
        "description": "Une affection bénigne des voies respiratoires qui se soigne généralement avec du repos.",
        "advice": "Hydratez-vous bien, reposez-vous et utilisez des solutions salines pour le nez."
    },
    {
        "name": "État Grippal",
        "symptoms": ["Fièvre", "Courbatures", "Fatigue", "Maux de tête"],
        "gravity": "Modérée",
        "description": "Une réaction saisonnière classique nécessitant quelques jours de récupération à domicile.",
        "advice": "Repos strict au chaud, paracétamol pour la fièvre et beaucoup de liquides."
    },
    {
        "name": "Allergie Saisonnière",
        "symptoms": ["Éternuements", "Yeux qui piquent", "Nez qui coule"],
        "gravity": "Légère",
        "description": "Une sensibilité au pollen ou à la poussière, très fréquente et facile à gérer.",
        "advice": "Évitez les zones de forte pollinisation et consultez pour un antihistaminique adapté."
    },
    {
        "name": "Angine Légère",
        "symptoms": ["Mal de gorge", "Fièvre", "Difficulté à avaler"],
        "gravity": "Modérée",
        "description": "Une irritation de la gorge qui peut être soulagée rapidement avec un traitement adéquat.",
        "advice": "Buvez des boissons tièdes, du miel, et consultez un médecin pour vérifier l'origine."
    },
    {
        "name": "Fatigue Saisonnière",
        "symptoms": ["Fatigue", "Maux de tête", "Yeux qui piquent"],
        "gravity": "Légère",
        "description": "Souvent liée au manque de sommeil ou au changement de saison.",
        "advice": "Améliorez votre rythme de sommeil et privilégiez une alimentation riche en vitamines."
    }
]

# Extraction automatique des symptômes pour l'interface
ALL_SYMPTOMS = sorted(list(set([s for d in DISEASES for s in d["symptoms"]])))
