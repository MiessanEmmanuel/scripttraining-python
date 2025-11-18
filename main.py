import time
from utils.gemini_models import model

nombre_de_ligne_a_generer = 100

system_instruction_precis=f"""
Génère un fichier CSV contenant exactement **{nombre_de_ligne_a_generer}** lignes de données aléatoires représentant des personnes fictives.

Respecte strictement ce format CSV et n’ajoute aucun commentaire, explication ou texte en dehors du CSV :

Nom,Prénom,Projet,Spécialité,Hobby,Nombre d'années d'expérience,Défaut,Qualité,Couleur préférée,Plat préféré,Boisson préférée,Langage préféré

Les données doivent être réalistes et variées :
- Les noms et prénoms doivent être plausibles et mélangés (français, africains, internationaux).
- “Projet” doit être un nom de projet fictif ou inspiré de projets ODC (ex : AgriTech+, SafeCity, EduBoost, FinTrack, etc.).
- “Spécialité” : domaines comme Data, Dev Web, DevOps, IA, Cybersécurité, Mobile, Cloud, etc.
- “Hobby” : une activité réaliste (lecture, foot, gaming, coding, danse, voyage…).
- “Nombre d'années d'expérience” : un nombre entre 0 et 15.
- “Défaut” et “Qualité” : des traits humains crédibles.
- “Couleur préférée” : une couleur simple.
- “Plat préféré” et “Boisson préférée” : choix variés, réalistes.
- “Langage préféré” : un langage informatique réel (Python, JavaScript, PHP, Java, Go, Rust, C#, etc.).

Renvoie juste les donnéesans les en-têtes 
Ne renvoie que le CSV final sans les en-têtes, rien d’autre.

"""
print(system_instruction_precis)
n=0
while n < 3:
    response = model.generate_content([
    system_instruction_precis
        ])


    brut = response.text

        # Retirer les balises Markdown s'il y en a
    if brut.startswith("```csv"):
        brut = brut.replace("```csv", "").strip()
    if brut.endswith("```"):
        brut = brut[:-3].strip()
    with open("output_donnee_jeco.csv", "a", encoding="utf-8") as f:
        f.write("\n" + brut)
    n=n+1

    # Wait 7 seconds between requests to respect free tier rate limit (10 requests/minute)
    if n < 3:
        print(f"Waiting 7 seconds before next request... ({n}/3 completed)")
        time.sleep(7)

#source .venv/bin/activate 
#python -m venv .venv           