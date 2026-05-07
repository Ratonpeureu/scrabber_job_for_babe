import smtplib
import pandas as pd
from email.message import EmailMessage
import time

# -------- CONFIG --------
gmail_user = "..." #Define here your email
# mot de passe Gmail 
gmail_password = "..."  #Access code from google AP

cv_file_path = "..."#CvPath
csv_file_path = "..."  # fichier CSV contenant les emails et titres

# -------- CHARGER CSV --------
df = pd.read_csv(csv_file_path)

# Vérifier les colonnes
if 'email' not in df.columns or 'titre' not in df.columns:
    raise ValueError("Le CSV doit contenir les colonnes 'email' et 'titre'")

# -------- ENVOI DES EMAILS --------
for index, row in df.iterrows():
    destinataire = row['email']
    titre_poste = row['titre']

    msg = EmailMessage()
    msg['Subject'] = f"Candidature spontanée au poste de {titre_poste}"
    msg['From'] = gmail_user
    msg['To'] = destinataire
    msg.set_content(f"Bonjour,\n\nVeuillez trouver ci-joint mon CV pour le poste de {titre_poste}.\n\nCordialement,\nAwa Ndiaye Ba")

    # Ajouter le CV en pièce jointe
    with open(cv_file_path, 'rb') as f:
        file_data = f.read()
        file_name = cv_file_path.split("/")[-1]
    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

    # Envoi de l'email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(gmail_user, gmail_password)
            smtp.send_message(msg)
        print(f"Email envoyé à {destinataire} pour le poste {titre_poste}")
    except Exception as e:
        print(f"Erreur en envoyant à {destinataire}: {e}")
    time.sleep(5)  # pause 5s Sinon risque de spam

