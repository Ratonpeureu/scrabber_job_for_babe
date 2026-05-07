scrabber_job_for_babe
Simple outil pour deposer à des offres d'emploi sans y passe 2jours.
Actuellement seule le site https://emploidakar.com est prise en compte
###########################
Configurer avec vos propre donnes// 

# ETAPE _1
executer Les scrabe_all_of.py//
il va faire la pagination sur cette addresse :
///
URL = "https://www.emploidakar.com/jm-ajax/get_listings/"
et creer un fichier csv / 
///
Vous devrez definir//
Creer un env 
sur Linux 
python3 -m venv venv
source venv/bin/activate
###################################"
installation de Docker Necessaire
INSTALLER REQUIREMENTS
pip install -r requirements.txt

filename = "" #Define path output of brute csv //
avant d'executer
# ETAPE_2
executer extract_email_thread.py
Il simple regex pour extraire toutes les emails du first csv brut et les organise dans un autre csv//plus propre
define ici ###
INPUT_FILE = "" #Your csv file input Brute //
OUTPUT_FILE = "" #sortie /output

# ETAPE_3
Un clean des emails du csv precedement creer//
-------- CONFIG --------
csv_file_path = ""  #+Define path# fichier CSV after extractor email
output_csv_path = ""  # CSV nettoyé

executer 
clean_csv.py
///
# ETAPE_4
configurer le fichier d'envoi des email 
 -------- CONFIG --------
gmail_user = "..." #Define here your email ///you can use you real email //comme ca le recreture pourra vous repondre redirecement sur votre address
mot de passe Gmail 
gmail_password = "..."  #Access code from google AP// Code access google de votre addresse mail //
you can access from google compte manager //application
#Tuto ==https://support.google.com/accounts/answer/6164209?hl=fr
#Define  you resume /

cv_file_path = "..."#CvPath
csv_file_path = "..."  # fichier CSV contenant les emails et titres propres
//
# ETAPE_5
Configurer Dockerfile avec les bon path //

COPY CV_Awa_Ndiaye_Ba_.pdf /data/CV_Awa_Ndiaye_Ba_.pdf
COPY emploidakar_offres_emails.csv /data/emploidakar_offres_emails.csv
COPY emploidakar_offres_emails.csv /data/emploidakar_offres_emails.csv


# ETAPE_6
docker build .

docker run + name de votre image
# EXEMPLE
docker build -t jobportal .
docker run jobportal


######################## ++++++++++++++ DISCLAMER ++++++++++++++++++++¸¸¸¸¸¸¸¸¸¸¸¸¸¸¸¸¸¸¸¸¸¸¸¸3

Y'A UN SLEEP DANS L'ENVOI //####### EVITEZ DE LE METTRE AU RISQUE DE BAN//
#################### LE SCRAPPE UTILISE PLAYWRIHT #### AU RISQUE DE CONFLICT DE PROXY EVITEZ DE CLONE CE GIT SUR UN VPS
VOTRE PC SUFFIRAI LARGEMENT

################################
