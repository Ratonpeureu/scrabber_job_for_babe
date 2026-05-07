import requests
from bs4 import BeautifulSoup
import csv
import time

URL = "https://www.emploidakar.com/jm-ajax/get_listings/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:144.0) Gecko/20100101 Firefox/144.0",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.emploidakar.com",
    "Referer": "https://www.emploidakar.com/offres-demploi-au-senegal/",
}

BASE_PAYLOAD = {
    "lang": "",
    "search_keywords": "",
    "search_location": "",
    "filter_job_type[]": ["cdd", "cdi", "freelance", "prestation-de-services", "stage", ""],
    "per_page": 17,
    "orderby": "featured",
    "featured_first": "false",
    "order": "DESC",
    "page": 1,
    "show_pagination": "true",
    "form_data": (
        "search_keywords=&search_location=&filter_job_type%5B%5D=cdd"
        "&filter_job_type%5B%5D=cdi&filter_job_type%5B%5D=freelance"
        "&filter_job_type%5B%5D=prestation-de-services&filter_job_type%5B%5D=stage&filter_job_type%5B%5D="
    ),
}

all_jobs = []
session = requests.Session()

print("🔎 Démarrage du scraping des offres EmploiDakar...\n")

for page in range(1, 30):  # adapte si besoin
    print(f" Page {page}...")

    payload = BASE_PAYLOAD.copy()
    payload["page"] = page

    try:
        response = session.post(URL, data=payload, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f" Erreur réseau possible cheeck : {e}")
        break

    try:
        data = response.json()
    except ValueError:
        print(" Réponse non valide (pas JSON) — arrêt.")
        break

    html = data.get("html", "")
    if not html.strip():

        break

    soup = BeautifulSoup(html, "html.parser")
    offers = soup.find_all("li", class_="job_listing")

    if not offers:
        print(" Scrap Termine/Plus d'offres trouvées.")
        break

    for li in offers:
        try:
            title = li.find("h3").get_text(strip=True) if li.find("h3") else "Sans titre"
            a_tag = li.find("a")
            link = a_tag["href"] if a_tag and a_tag.has_attr("href") else "Aucun lien"
            company_tag = li.find("div", class_="company")
            company = company_tag.get_text(strip=True) if company_tag else "Inconnue"
            loc_tag = li.find("div", class_="location")
            location = loc_tag.get_text(strip=True) if loc_tag else "Non précisé"
            time_tag = li.find("time")
            date = time_tag["datetime"] if time_tag and time_tag.has_attr("datetime") else "N/A"

            job = {
                "titre": title,
                "entreprise": company,
                "lieu": location,
                "date": date,
                "lien": link,
            }
            all_jobs.append(job)
            print(f"   {title} | {company}")
        except Exception as e:
            print(f" Erreur parsing offre : {e}")

    time.sleep(1)

print(f"\n✅ {len(all_jobs)} offres récupérées au total.\n")


filename = "emploidakar_offres.csv"
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["titre", "entreprise", "lieu", "date", "lien"])
    writer.writeheader()
    writer.writerows(all_jobs)

print(f" Données enregistrées dans : {filename}")
