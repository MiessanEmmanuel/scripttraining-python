import pandas as pd
import glob

# Récupère tous les CSV du dossier
fichiers = glob.glob("*.csv")

# Lit et fusionne tous les fichiers
df = pd.concat([pd.read_csv(f) for f in fichiers], ignore_index=True)

# Supprime les doublons
df = df.drop_duplicates()

# Sauvegarde dans un nouveau fichier
df.to_csv("fusion_finale.csv", index=False)

print("Fusion terminée !")
print("Nombre total de lignes :", len(df))
