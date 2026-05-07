#For Extractor email CSV file//
#with playwrith/risque crabe many False mail///
import csv
import re
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
import random

INPUT_FILE = "" #Your csv file input Brute //
OUTPUT_FILE = "" #sortie /output

# Regex générique pour détecter les adresses e-mail
EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:144.0) Gecko/20100101 Firefox/144.0"
} #can add sythme rotate /pour eviter d'etre flaguer  sur d'autre /mais c'est good

MAX_WORKERS = 10  # nombre de threads simultanés


def extract_email_from_page(url):
    """Doownload une page et tente d’en extraire un email."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code != 200:
            return None

        soup = BeautifulSoup(resp.text, "html.parser")

        # Chercher dans le texte brut
        text = soup.get_text(separator=" ", strip=True)
        emails = re.findall(EMAIL_REGEX, text)
        if emails:
            return emails[0]

        # Chercher dans les liens mailto:
        for a in soup.find_all("a", href=True):
            if "mailto:" in a["href"]:
                return a["href"].replace("mailto:", "").strip()

        return None

    except Exception as e:
        print(f" Erreur sur {url} : {e}")
        return None


def process_offer(row):
    """Traite une ligne du CSV : extrait l'email de l'offre."""
    url = row["lien"]
    print(f" ++++Traitement : {url}")

    email = extract_email_from_page(url)
    row["email"] = email or ""
    sleep(random.uniform(0.5, 1.5))  # délai léger pour ne pas surcharger le site
    return row


def main():
    print("🔍 Lecture du fichier CSV des offres...")
    with open(INPUT_FILE, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        offers = list(reader)

    print(f"++++{len(offers)} offres détectées. Lancement du scraping multithread...")

    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(process_offer, row) for row in offers]

        for future in as_completed(futures):
            results.append(future.result())


    if results:
        fieldnames = list(results[0].keys())
        with open(OUTPUT_FILE, "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

        print(f"++++ Extraction terminée avec succès !")
        print(f"++++ Fichier sauvegardé sous : {OUTPUT_FILE}")
    else:
        print("++++___+++ALERT+++___++++ Aucune donnée extraite.")


if __name__ == "__main__":
    main()
