#Juste // for simple regex for clean email//of list csv
import pandas as pd
import re

# -------- CONFIG --------
csv_file_path = ""  #+Define path# fichier CSV after extractor email
output_csv_path = ""  # CSV nettoyé#

# -------- CHARGER CSV --------
df = pd.read_csv(csv_file_path)

# Vérifier la colonne email
if 'email' not in df.columns:
    raise ValueError("Le CSV doit contenir une colonne 'email'")

# -------- REGEX POUR EMAIL VALIDE --------
#Can add more with re
email_regex = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
)

# Filtrer les emails valides
df_clean = df[df['email'].apply(lambda x: bool(email_regex.match(str(x))))]

# Sauvegarder le CSV nettoyé
df_clean.to_csv(output_csv_path, index=False)
print(f"CSV nettoyé enregistré dans {output_csv_path}, {len(df) - len(df_clean)} lignes supprimées")
